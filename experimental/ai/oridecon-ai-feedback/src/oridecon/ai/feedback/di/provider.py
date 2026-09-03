"""Feedback DI provider."""

from __future__ import annotations

import inspect
from typing import TYPE_CHECKING

from oridecon.ai.feedback.config import FeedbackConfig
from oridecon.ai.feedback.processors.processor_registry import FeedbackProcessorRegistry
from oridecon.ai.feedback.services.collector import FeedbackCollector
from oridecon.ai.feedback.services.feedback_service import FeedbackService
from oridecon.contracts.ai.feedback import FeedbackProtocol
from oridecon.contracts.core.health import HealthCheckResult, HealthStatus
from oridecon.contracts.core.provider import ProviderPriority
from oridecon.di.provider import Provider
from oridecon.logging import (
    get_logger,
)

if TYPE_CHECKING:
    from oridecon.ai.feedback.storage.protocols import FeedbackStoreProtocol
    from oridecon.contracts.core.di import (
        ContainerRegistrarProtocol,
        ContainerResolverProtocol,
    )

logger = get_logger(__name__)


class FeedbackProvider(Provider):
    """Provider for AI Feedback.

    Registers :class:`~oridecon.ai.feedback.collector.FeedbackCollector` and
    :class:`~oridecon.ai.feedback.processor_registry.FeedbackProcessorRegistry`.
    Wires a durable storage backend (DB-backed, optionally cached) into the
    collector during :meth:`boot`.
    """

    name = "feedback"
    priority = ProviderPriority.DOMAIN
    config_key: str | None = "ai_feedback"
    config_model: type | None = FeedbackConfig

    def __init__(self, config: FeedbackConfig | dict | None = None) -> None:
        super().__init__()
        if isinstance(config, dict):
            config = FeedbackConfig(**config)
        self._requested_config = config
        self._config = config or FeedbackConfig()

    @classmethod
    def from_config(cls, config: FeedbackConfig, **context: object) -> FeedbackProvider:
        """Factory method for DI container setup."""
        del context
        return cls(config)

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        """Register the feedback services."""
        self._config = self._requested_config or (
            self.config
            if isinstance(getattr(self, "config", None), FeedbackConfig)
            else self._config
        )
        container.singleton(FeedbackConfig, self._config)

        if not self._config.enabled:
            logger.info("feedback_disabled", reason="FeedbackConfig.enabled=False")
            return

        container.singleton(FeedbackProcessorRegistry)
        container.singleton(FeedbackCollector)
        container.singleton(FeedbackProtocol, FeedbackService)

        logger.info("feedback_registered")

    async def boot(self, container: ContainerResolverProtocol) -> None:
        """Wire a durable storage backend into :class:`FeedbackCollector`."""
        if not self._config.enabled:
            return

        from oridecon.ai.feedback.storage.cache import CachedFeedbackStore
        from oridecon.ai.feedback.storage.database import DatabaseFeedbackStore
        from oridecon.contracts.data import DatabaseProviderProtocol
        from oridecon.contracts.infra.cache import CacheBackendProtocol

        db_provider = await container.resolve_optional(DatabaseProviderProtocol)
        if db_provider is None:
            logger.debug(
                "feedback_store_not_wired",
                reason="DatabaseProviderProtocol unavailable",
            )
            return

        store: FeedbackStoreProtocol = DatabaseFeedbackStore(db_provider)  # type: ignore[assignment]

        cache_backend = await container.resolve_optional(CacheBackendProtocol)
        if cache_backend is not None:
            store = CachedFeedbackStore(store, cache_backend)
            logger.info("feedback_cached_store_wired")
        else:
            logger.info("feedback_database_store_wired")

        collector_resolved = container.resolve(FeedbackCollector)
        if inspect.isawaitable(collector_resolved):
            collector = await collector_resolved
        else:
            collector = collector_resolved
        collector.storage = store

        service_resolved = container.resolve(FeedbackProtocol)
        if inspect.isawaitable(service_resolved):
            service = await service_resolved
        else:
            service = service_resolved
        service._store = store

    async def shutdown(self) -> None:
        """Shutdown phase."""
        logger.debug("feedback_shutdown")

    async def health_check(self, timeout: float = 5.0) -> HealthCheckResult:
        """Health check — always healthy (in-process domain provider).

        No external backend to ping.

        Args:
            timeout: Ignored for in-process providers.

        Returns:
            Always HEALTHY — no external backend to ping.
        """
        return HealthCheckResult(
            component=self.name,
            status=HealthStatus.HEALTHY,
            details={"status": "operational"},
        )


__all__ = ["FeedbackProvider"]
