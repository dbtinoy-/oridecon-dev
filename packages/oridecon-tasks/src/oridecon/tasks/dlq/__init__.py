"""Dead letter queue management for failed tasks."""

from __future__ import annotations

from oridecon.tasks.dlq.backend import (
    DLQBackend,
    InMemoryDLQBackend,
    StateStoreDLQBackend,
)
from oridecon.tasks.dlq.core import DeadLetterQueue, FailureRecord
from oridecon.tasks.dlq.persistent import PersistentDeadLetterQueue
from oridecon.tasks.dlq.redis_dlq import RedisDLQBackend

__all__ = [
    "DLQBackend",
    "DeadLetterQueue",
    "FailureRecord",
    "InMemoryDLQBackend",
    "PersistentDeadLetterQueue",
    "RedisDLQBackend",
    "StateStoreDLQBackend",
]
