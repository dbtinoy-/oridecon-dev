"""Type definitions for the memory subsystem.

Re-exports ``OutboxStatus`` and ``OutboxEntry`` from their canonical
home in ``oridecon.memory.outbox`` for convenient top-level access.
"""

from __future__ import annotations

from oridecon.testing.memory.outbox import OutboxEntry as OutboxEntry
from oridecon.testing.memory.outbox import OutboxStatus as OutboxStatus

__all__ = [
    "OutboxEntry",
    "OutboxStatus",
]
