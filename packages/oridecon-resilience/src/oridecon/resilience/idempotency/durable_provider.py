"""DI provider for the Redis-backed (durable) idempotency store.

Overrides the IdempotencyStoreProtocol binding with a RedisIdempotencyStore,
enabling distributed deduplication across multiple application instances.
Depends on the core 'idempotency' provider being registered first.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.app.exceptions import AppStartupError
from oridecon.contracts.core.idempotency import IdempotencyStoreProtocol
from oridecon.contracts.infra.cache import CacheBackendProtocol
from oridecon.di.provider import Provider, ProviderPriority
from oridecon.logging import get_logger
from oridecon.resilience.idempotency.redis import RedisIdempotencyStore

if TYPE_CHECKING:
    from oridecon.contracts.core.di import (
        ContainerRegistrarProtocol,
        ContainerResolverProtocol,
    )

logger = get_logger(__name__)


class DurableIdempotencyProvider(Provider):
    """DI provider that replaces the in-memory store with a Redis-backed store.

    Registers RedisIdempotencyStore as the IdempotencyStoreProtocol factory,
    requiring a CacheBackendProtocol to be resolvable from the container.

    This provider declares a dependency on 'idempotency' so the core provider
    runs first.
    """

    name = "durable_idempotency"
    priority = ProviderPriority.INFRASTRUCTURE
    dependencies: tuple[str, ...] = ("idempotency",)

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        """Override IdempotencyStoreProtocol with a RedisIdempotencyStore factory.

        Args:
            container: The DI container registrar.
        """
        container.singleton(IdempotencyStoreProtocol, factory=RedisIdempotencyStore)
        logger.debug("durable_idempotency.provider.registered")

    async def boot(self, container: ContainerResolverProtocol) -> None:
        """Verify that CacheBackendProtocol is available in the container.

        Args:
            container: The DI container resolver.

        Raises:
            AppStartupError: When CacheBackendProtocol cannot be resolved.
        """
        try:
            await container.resolve(CacheBackendProtocol)
        except Exception as exc:
            raise AppStartupError(
                "DurableIdempotencyProvider requires CacheBackendProtocol to be "
                "registered in the container."
            ) from exc
        logger.debug("durable_idempotency.provider.booted")

    async def shutdown(self) -> None:
        """No-op shutdown for the Redis-backed provider."""


__all__ = ["DurableIdempotencyProvider"]
