"""Distributed locking utilities for Oridecon cache.

Provides distributed locks with automatic TTL renewal.
"""

from __future__ import annotations

from oridecon.cache.locks.distributed import (
    DistributedLockInfo,
    DistributedLockProtocol,
)
from oridecon.cache.locks.manager import LockManager

__all__ = [
    "DistributedLockInfo",
    "DistributedLockProtocol",
    "LockManager",
]
