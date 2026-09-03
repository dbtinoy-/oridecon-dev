"""InboxProvider — DI provider for the user inbox subsystem."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.contracts.core import HealthCheckResult, HealthStatus, ProviderPriority
from oridecon.contracts.notification.inbox import InboxStoreProtocol
from oridecon.di.provider import Provider
from oridecon.logging import get_logger
from oridecon.notification.config import InboxConfig

if TYPE_CHECKING:
    from oridecon.contracts.core.di import (
        ContainerRegistrarProtocol,
        ContainerResolverProtocol,
    )

logger = get_logger(__name__)


class InboxProvider(Provider):
    """Register the inbox store and service into the DI container.

    Honors :class:`~oridecon.notification.config.InboxConfig.store_backend`:

    - ``database`` — :class:`~oridecon.notification.inbox.database.DatabaseInboxStore`
      backed by :class:`~oridecon.contracts.data.sql.database.DatabaseProviderProtocol`
      (resolved lazily at first use).
    - ``memory`` — :class:`~oridecon.notification.inbox.memory.InMemoryInboxStore`.

    Also registers :class:`~oridecon.notification.inbox.service.InboxService`
    for constructor injection.

    Args:
        config: Inbox configuration. When ``None`` the default
            :class:`InboxConfig` (``store_backend="database"``) is used.
    """

    name = "inbox"
    priority = ProviderPriority.INFRASTRUCTURE

    def __init__(self, config: InboxConfig | None = None) -> None:
        super().__init__()
        self._config = config or InboxConfig()
        self._store: InboxStoreProtocol | None = None

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        """Bind inbox store and service into the container.

        Args:
            container: DI registrar received from the framework.
        """
        from oridecon.notification.inbox.service import InboxService

        backend = self._config.store_backend
        if backend == "database":
            from oridecon.contracts.data.sql.database import (
                DatabaseProviderProtocol,
            )
            from oridecon.notification.inbox.database import DatabaseInboxStore

            async def _database_store_factory(
                resolver: ContainerResolverProtocol,
            ) -> DatabaseInboxStore:
                db = await resolver.resolve(DatabaseProviderProtocol)
                return DatabaseInboxStore(db=db)

            container.singleton(
                InboxStoreProtocol,
                factory=_database_store_factory,
            )
        else:
            from oridecon.notification.inbox.memory import InMemoryInboxStore

            container.singleton(InboxStoreProtocol, InMemoryInboxStore)

        container.singleton(InboxService, InboxService)
        logger.info("inbox_registered", backend=backend)

    async def boot(self, container: ContainerResolverProtocol) -> None:
        """Resolve the inbox store for health checking.

        Args:
            container: DI resolver used to obtain the registered store.
        """
        from oridecon.notification.inbox.service import InboxService

        self._store = await container.resolve(InboxStoreProtocol)
        await container.resolve(InboxService)
        logger.info("inbox_booted", backend=self._config.store_backend)

    async def shutdown(self) -> None:
        """Release store reference on shutdown."""
        self._store = None

    async def health_check(self, timeout: float = 5.0) -> HealthCheckResult:
        """Delegate health check to the registered inbox store.

        Returns degraded status before :meth:`boot` has been called.

        Args:
            timeout: Max seconds to wait for the store health probe.

        Returns:
            :class:`~oridecon.contracts.core.HealthCheckResult`.
        """
        if self._store is None:
            return HealthCheckResult(
                component="inbox",
                status=HealthStatus.DEGRADED,
                message="inbox store not initialized",
            )

        store_result = await self._store.health_check(timeout=timeout)
        return HealthCheckResult(
            component="inbox",
            status=store_result.status,
            message=store_result.message,
            details=store_result.details,
            error=store_result.error,
            duration_ms=store_result.duration_ms,
        )


__all__ = ["InboxProvider"]
