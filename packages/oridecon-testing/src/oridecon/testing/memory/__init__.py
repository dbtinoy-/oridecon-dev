"""In-memory implementations for Oridecon Framework testing.

Provides in-memory implementations of core framework contracts for use in
unit tests, integration tests, and local development. These implementations
are lightweight, fast, and require no external infrastructure.

Exports:
    InMemoryRepository: Generic in-memory data repository.
    InMemoryEventBus: Single-process event dispatch.
    InMemoryCommandBus, InMemoryQueryBus: CQRS buses.
    InMemoryUnitOfWork: Entity tracking and event collection.
    InMemoryAuditLogger: In-memory audit logging.
    InMemoryDistributedLock: Cross-coroutine distributed lock.
    InMemoryAsyncLock: In-process asyncio mutual-exclusion lock.
    InMemoryOutbox, OutboxRelay, OutboxEntry, OutboxStatus: Outbox pattern.
    CommandBusError, CommandHandlerNotFoundError, DuplicateHandlerError,
    QueryBusError, QueryDuplicateHandlerError, QueryHandlerNotFoundError: Errors.
    MemoryProvider: DI provider for in-memory implementations.
    MemoryConfig: Configuration model.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oridecon.testing.memory.audit import InMemoryAuditLogger
    from oridecon.testing.memory.blob_store import FileInfo, InMemoryBlobStore
    from oridecon.testing.memory.cache import InMemoryCacheBackend
    from oridecon.testing.memory.cqrs import (
        InMemoryCommandBus,
        InMemoryQueryBus,
    )
    from oridecon.testing.memory.event_bus import InMemoryEventBus
    from oridecon.testing.memory.exceptions import (
        CommandBusError,
        CommandError,
        CommandHandlerNotFoundError,
        DuplicateHandlerError,
        QueryBusError,
        QueryDuplicateHandlerError,
        QueryHandlerNotFoundError,
    )
    from oridecon.testing.memory.lock import (
        InMemoryAsyncLock,
        InMemoryDistributedLock,
        InMemoryLockStore,
    )
    from oridecon.testing.memory.outbox import (
        InMemoryOutbox,
        OutboxEntry,
        OutboxRelay,
        OutboxStatus,
    )
    from oridecon.testing.memory.repository import InMemoryRepository
    from oridecon.testing.memory.uow import InMemoryUnitOfWork

_LAZY_IMPORTS: dict[str, str] = {
    "InMemoryBlobStore": "oridecon.testing.memory.blob_store",
    "FileInfo": "oridecon.testing.memory.blob_store",
    "InMemoryCacheBackend": "oridecon.testing.memory.cache",
    "InMemoryAuditLogger": "oridecon.testing.memory.audit",
    "CommandBusError": "oridecon.testing.memory.exceptions",
    "CommandError": "oridecon.testing.memory.exceptions",
    "CommandHandlerNotFoundError": "oridecon.testing.memory.exceptions",
    "DuplicateHandlerError": "oridecon.testing.memory.exceptions",
    "InMemoryCommandBus": "oridecon.testing.memory.cqrs",
    "InMemoryQueryBus": "oridecon.testing.memory.cqrs",
    "QueryBusError": "oridecon.testing.memory.exceptions",
    "QueryDuplicateHandlerError": "oridecon.testing.memory.exceptions",
    "QueryHandlerNotFoundError": "oridecon.testing.memory.exceptions",
    "InMemoryEventBus": "oridecon.testing.memory.event_bus",
    "InMemoryAsyncLock": "oridecon.testing.memory.lock",
    "InMemoryDistributedLock": "oridecon.testing.memory.lock",
    "InMemoryLockStore": "oridecon.testing.memory.lock",
    "InMemoryOutbox": "oridecon.testing.memory.outbox",
    "OutboxEntry": "oridecon.testing.memory.outbox",
    "OutboxRelay": "oridecon.testing.memory.outbox",
    "OutboxStatus": "oridecon.testing.memory.outbox",
    "InMemoryRepository": "oridecon.testing.memory.repository",
    "InMemoryUnitOfWork": "oridecon.testing.memory.uow",
    "MemoryConfig": "oridecon.testing.memory.config.models",
    "MemoryBackendError": "oridecon.testing.memory.exceptions",
    "MemoryProvider": "oridecon.testing.memory.di.provider",
    "DEFAULT_AUDIT_CAPACITY": "oridecon.testing.memory.constants",
    "DEFAULT_EVENT_BUS_CAPACITY": "oridecon.testing.memory.constants",
    "DEFAULT_OUTBOX_CAPACITY": "oridecon.testing.memory.constants",
    "DEFAULT_REPOSITORY_CAPACITY": "oridecon.testing.memory.constants",
}


def __getattr__(name: str) -> object:
    """Lazily import and return a public attribute by name."""
    if name in _LAZY_IMPORTS:
        import importlib

        module = importlib.import_module(_LAZY_IMPORTS[name])
        value = getattr(module, name)
        globals()[name] = value
        return value
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)


def __dir__() -> list[str]:
    """Return list of public API names."""
    return list(_LAZY_IMPORTS.keys())


__all__ = list(_LAZY_IMPORTS.keys())
