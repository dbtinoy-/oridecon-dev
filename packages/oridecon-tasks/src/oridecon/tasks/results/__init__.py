"""Task result store for persisting and querying results."""

from __future__ import annotations

from oridecon.tasks.results.cache_backend import CacheBackendResultStore
from oridecon.tasks.results.core import (
    InMemoryResultStore,
    ResultStore,
)

__all__ = [
    "CacheBackendResultStore",
    "InMemoryResultStore",
    "ResultStore",
]
