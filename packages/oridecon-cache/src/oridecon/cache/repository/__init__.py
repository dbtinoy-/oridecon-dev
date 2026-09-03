"""
RepositoryProtocol pattern implementations for Oridecon Cache.

This package provides repository patterns that offer domain-specific
caching abstractions on top of the core cache service.
"""

from __future__ import annotations

from oridecon.cache.repository.base import (
    CacheRepository,
    EntityRepository,
    QueryRepository,
)
from oridecon.cache.repository.collections import (
    CollectionRepository,
    ConfigurationRepository,
)

__all__ = [
    "CacheRepository",
    "CollectionRepository",
    "ConfigurationRepository",
    "EntityRepository",
    "QueryRepository",
]
