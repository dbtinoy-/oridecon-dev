"""
Oridecon Cache - Multi-backend caching system for Oridecon Framework.

This package provides a unified caching API across multiple backends including
in-memory, Redis, and Memcached. It follows the Oridecon Framework's provider
pattern for clean integration and extensibility.

Exports:
    CacheService: Main cache service for DI injection
    CacheProvider: Provider for framework integration
    CacheConfig: Configuration model
    CacheBackendProtocol: Protocol for backend implementations
    BackendType: Enum of supported backends
    CacheError: Base exception for cache errors
"""

from __future__ import annotations

import importlib.metadata

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from typing import TYPE_CHECKING, Any

from oridecon.cache.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.cache.backends.memcached.backend import MemcachedCacheBackend
    from oridecon.cache.backends.memory.backend import MemoryCacheBackend
    from oridecon.cache.backends.redis.backend import RedisCacheBackend
    from oridecon.cache.config import (
        CacheBackendConfig,
        CacheConfig,
        CacheOperationConfig,
        CacheServiceConfig,
        EnvironmentConfigLoader,
        MemcachedBackendConfig,
        MemoryBackendConfig,
        RedisBackendConfig,
    )
    from oridecon.cache.decorators import cacheable
    from oridecon.cache.di.provider import CacheProvider
    from oridecon.cache.exceptions import (
        CacheBackendError,
        CacheCapacityError,
        CacheConfigurationError,
        CacheConnectionError,
        CacheError,
        CacheInvalidationError,
        CacheKeyError,
        CacheSerializationError,
        CacheStampedeError,
        CacheTimeoutError,
    )
    from oridecon.cache.serialization.compression import CompressingSerializer
    from oridecon.cache.serialization.json import JSONSerializer
    from oridecon.cache.serialization.type_registry import (
        DEFAULT_REGISTRY,
        TypeRegistry,
    )
    from oridecon.cache.service.core import CacheService
    from oridecon.cache.service.decorators import (
        CacheDecorator,
        cache,
        conditional_cache,
        invalidate_cache,
        remember,
    )
    from oridecon.cache.service.request_cache import (
        cache_in_request,
        clear_request_cache,
        get_request_cache,
    )
    from oridecon.cache.stores import RedisLockStore, RedisSecretStore, RedisStateStore
    from oridecon.cache.stores.redis_state import RedisDriver
    from oridecon.cache.types import (
        BackendType,
        CacheEntry,
        CacheHealthResult,
        CacheItem,
        CacheMetrics,
        CacheResult,
        CacheStats,
        CacheStatus,
        CacheStatusHandler,
        DistributedLockInfo,
        TaggedCacheKey,
    )
    from oridecon.contracts.core import HealthStatus
    from oridecon.contracts.infra.cache import (
        AsyncStringSerializerProtocol,
        CacheBackendProtocol,
        CacheHealthCheckerProtocol,
        CacheKeyBuilderProtocol,
        CacheProtectionStrategyProtocol,
    )

_LAZY_IMPORTS = {
    "AutoRenewingLock": "oridecon.cache.locks.auto_renewing",
    "BackendType": "oridecon.cache.types",
    "cacheable": "oridecon.cache.decorators",
    "cache_in_request": "oridecon.cache.service.request_cache",
    "clear_request_cache": "oridecon.cache.service.request_cache",
    "get_request_cache": "oridecon.cache.service.request_cache",
    "CacheBackendProtocol": "oridecon.contracts.cache",
    "CacheBackendConfig": "oridecon.cache.config",
    "CacheBackendError": "oridecon.cache.exceptions",
    "CacheCapacityError": "oridecon.cache.exceptions",
    "CacheConfig": "oridecon.cache.config",
    "CacheConfigurationError": "oridecon.cache.exceptions",
    "CacheConnectionError": "oridecon.cache.exceptions",
    "CacheDecorator": "oridecon.cache.service.decorators",
    "CacheEntry": "oridecon.cache.types",
    "CacheError": "oridecon.cache.exceptions",
    "CacheHealthCheckerProtocol": "oridecon.contracts.cache",
    "CacheHealthResult": "oridecon.cache.types",
    "CacheInvalidationError": "oridecon.cache.exceptions",
    "CacheItem": "oridecon.cache.types",
    "CacheKeyBuilderProtocol": "oridecon.contracts.cache",
    "CacheKeyError": "oridecon.cache.exceptions",
    "CacheMetrics": "oridecon.cache.types",
    "CacheModule": "oridecon.cache.module",
    "CacheOperationConfig": "oridecon.cache.config",
    "CacheProtectionStrategyProtocol": "oridecon.contracts.cache",
    "CacheProvider": "oridecon.cache.di.provider",
    "CacheResult": "oridecon.cache.types",
    "CacheSerializationError": "oridecon.cache.exceptions",
    "CacheService": "oridecon.cache.service.core",
    "CacheServiceConfig": "oridecon.cache.config",
    "CacheStampedeError": "oridecon.cache.exceptions",
    "CacheStats": "oridecon.cache.types",
    "CacheStatus": "oridecon.cache.types",
    "CacheStatusHandler": "oridecon.cache.types",
    "CacheTimeoutError": "oridecon.cache.exceptions",
    "DistributedLockInfo": "oridecon.cache.types",
    "CompressingSerializer": "oridecon.cache.serialization.compression",
    "CostAwareCacheDecision": "oridecon.cache.semantic.cost_decision",
    "DEFAULT_REGISTRY": "oridecon.cache.serialization.type_registry",
    "EnvironmentConfigLoader": "oridecon.cache.config",
    "FaissVectorIndex": "oridecon.cache.semantic.vector_index",
    "HealthStatus": "oridecon.contracts.core",
    "JSONSerializer": "oridecon.cache.serialization.json",
    "MemcachedBackendConfig": "oridecon.cache.config",
    "MemcachedCacheBackend": "oridecon.cache.backends.memcached.backend",
    "MemoryBackendConfig": "oridecon.cache.config",
    "MemoryCacheBackend": "oridecon.cache.backends.memory.backend",
    "RedisBackendConfig": "oridecon.cache.config",
    "RedisCacheBackend": "oridecon.cache.backends.redis.backend",
    "AsyncStringSerializerProtocol": "oridecon.contracts.cache",
    "SemanticCacheStore": "oridecon.cache.semantic.store",
    "TaggedCacheKey": "oridecon.cache.types",
    "TypeRegistry": "oridecon.cache.serialization.type_registry",
    "cache": "oridecon.cache.service.decorators",
    "conditional_cache": "oridecon.cache.service.decorators",
    "invalidate_cache": "oridecon.cache.service.decorators",
    "remember": "oridecon.cache.service.decorators",
    "RedisDriver": "oridecon.cache.stores.redis_state",
    "RedisLockStore": "oridecon.cache.stores.redis_lock",
    "RedisSecretStore": "oridecon.cache.stores.redis_secrets",
    "RedisStateStore": "oridecon.cache.stores.redis_state",
    # Hooks
    "CacheConnectedHook": "oridecon.cache.hooks",
    "CacheDisconnectedHook": "oridecon.cache.hooks",
    "CacheEntryEvictedHook": "oridecon.cache.hooks",
    # Events
    "CacheHitEvent": "oridecon.cache.events",
    "CacheMissEvent": "oridecon.cache.events",
    "CacheEvictedEvent": "oridecon.cache.events",
    "CacheConnectedEvent": "oridecon.cache.events",
}


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib

        module_path = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> Any:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = list(_LAZY_IMPORTS.keys())
