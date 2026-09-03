"""Test-friendly aliases for in-memory fakes from oridecon.testing.memory.

Re-exports all ``InMemory*`` implementations under shorter ``Fake*`` names
that read naturally in test code.

Example::

    from oridecon.testing.testkit.fakes import FakeEventBus, FakeRepository

    event_bus = FakeEventBus()
    repo: FakeRepository[User] = FakeRepository()
"""

from __future__ import annotations

from oridecon.testing.memory.audit import InMemoryAuditLogger as FakeAuditLogger
from oridecon.testing.memory.cqrs import InMemoryCommandBus as FakeCommandBus
from oridecon.testing.memory.cqrs import InMemoryQueryBus as FakeQueryBus
from oridecon.testing.memory.event_bus import InMemoryEventBus as FakeEventBus
from oridecon.testing.memory.lock import InMemoryDistributedLock as FakeLock
from oridecon.testing.memory.outbox import InMemoryOutbox as FakeOutbox
from oridecon.testing.memory.repository import InMemoryRepository as FakeRepository
from oridecon.testing.memory.uow import InMemoryUnitOfWork as FakeUoW

__all__ = [
    "FakeAuditLogger",
    "FakeCommandBus",
    "FakeEventBus",
    "FakeLock",
    "FakeOutbox",
    "FakeQueryBus",
    "FakeRepository",
    "FakeUoW",
]
