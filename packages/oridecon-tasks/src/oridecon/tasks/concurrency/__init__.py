"""Concurrency utilities for task processing.

This module provides concurrency controls for task execution:
- Distributed locking for task deduplication
- Rate limiting for throughput control
"""

from __future__ import annotations

from oridecon.tasks.concurrency.compute import (
    Compute,
    ComputePool,
    PoolMetrics,
    ProcessStats,
)
from oridecon.tasks.concurrency.locking import (
    InMemoryLock as DistributedLockProtocol,
)
from oridecon.tasks.concurrency.locking import (
    UniqueTask,
    distributed_lock,
)
from oridecon.tasks.concurrency.rate_limit import (
    GlobalRateLimiter,
    QueueRateLimiter,
)

__all__ = [
    # Compute
    "Compute",
    "ComputePool",
    # Locking
    "DistributedLockProtocol",
    "GlobalRateLimiter",
    "PoolMetrics",
    "ProcessStats",
    "QueueRateLimiter",
    "UniqueTask",
    "distributed_lock",
]
