"""Concrete feature-flag backend implementations.

Backends:
    AbstractFlagProvider: Rich abstract base class with full evaluation logic.
    LocalProvider: In-memory, code-defined flag store.
    EnvProvider: Reads flags from environment variables.
    ChainedProvider: Layered lookup across multiple providers.
    MemoryProvider: Lightweight test double with override support.
    CacheBackendFlagProvider: Cache-backed provider (Redis, Memcached, etc.).
"""

from __future__ import annotations

from oridecon.features.backends.base import AbstractFlagProvider
from oridecon.features.backends.cache import CacheBackendFlagProvider
from oridecon.features.backends.chained import ChainedProvider
from oridecon.features.backends.env import EnvProvider
from oridecon.features.backends.local import LocalProvider
from oridecon.features.backends.testing import MemoryProvider

__all__ = [
    "AbstractFlagProvider",
    "CacheBackendFlagProvider",
    "ChainedProvider",
    "EnvProvider",
    "LocalProvider",
    "MemoryProvider",
]
