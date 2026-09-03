"""
Cache backends for Oridecon Framework.

This package contains backend implementations that wrap infrastructure
drivers, ensuring DRY compliance and consistency.

Note: Database-backed state, secret, and lock stores (previously
``DatabaseBridgeStateStore``, ``DatabaseBridgeSecretStore``, and
``DatabaseBridgeLockStore``) have been moved to ``oridecon-sql`` as
``DatabaseStateStore``, ``DatabaseSecretStore``, and ``DatabaseLockStore``.
Import them from ``oridecon.sql.stores`` instead.
"""

from __future__ import annotations

from oridecon.cache.backends.hash import _compute_hash
from oridecon.cache.backends.memcached.backend import MemcachedCacheBackend
from oridecon.cache.backends.memory.backend import MemoryCacheBackend
from oridecon.cache.backends.redis.backend import RedisCacheBackend

__all__ = [
    "MemcachedCacheBackend",
    "MemoryCacheBackend",
    "RedisCacheBackend",
    "_compute_hash",
]
