"""Cache protocols."""

from __future__ import annotations

from oridecon.contracts.core.serialization import AsyncStringSerializerProtocol
from oridecon.contracts.infra.cache.exceptions import (
    CacheError,
    CacheKeyNotFoundError,
    CacheWriteError,
)
from oridecon.contracts.infra.cache.protocols import (
    CacheBackendProtocol,
    CacheHealthCheckerProtocol,
    CacheKeyBuilderProtocol,
    CacheProtectionStrategyProtocol,
    CacheProviderProtocol,
)

__all__ = [
    "AsyncStringSerializerProtocol",
    "CacheBackendProtocol",
    "CacheError",
    "CacheHealthCheckerProtocol",
    "CacheKeyBuilderProtocol",
    "CacheKeyNotFoundError",
    "CacheProtectionStrategyProtocol",
    "CacheProviderProtocol",
    "CacheWriteError",
]
