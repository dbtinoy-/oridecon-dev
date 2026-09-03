"""Oridecon Events - Event Sourcing and CQRS for Python.

This package provides a complete Event Sourcing and CQRS implementation
for building scalable, event-driven applications.

Core Features:
    - **Event Sourcing**: Store all changes as immutable events
    - **CQRS**: Separate read and write models for scalability
    - **Aggregate Pattern**: DDD building blocks for domain modeling
    - **Event Store**: Multiple backends (PostgreSQL, MongoDB, In-Memory)
    - **Sagas**: Long-running business processes
    - **Projections**: Build read models from events
    - **Streaming**: Real-time event streaming with WebSocket support
    - **Middleware**: Extensible middleware pipeline

Basic Usage:
    ```python
    from oridecon.contracts.domain import DomainEvent
    from oridecon.events import (
        Command, Query, Event,
        CommandBusImpl, QueryBusImpl, EventBusImpl,
        AggregateRoot, InMemoryEventStore,
    )

    # Define events
    class UserCreated(DomainEvent):
        user_id: UUID
        name: str
        email: str
    ```

Module Structure:
    - messages: Command, Query, Event base classes
    - buses: CommandBusImpl, QueryBusImpl, EventBusImpl
    - stores: Event storage backends
    - aggregates: AggregateRoot, Entity, ValueObject
    - repository: Event sourcing repository
    - handlers: Handler registration and discovery
    - middleware: Middleware pipeline components
    - projections: Read model management
    - streaming: Event streaming and WebSocket
    - adapters: Message broker adapters (RabbitMQ, Kafka, Azure)
    - schema: Schema registry and evolution
"""

from __future__ import annotations

import importlib.metadata
import sys
from typing import TYPE_CHECKING, Any

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from oridecon.events.constants import __version__ as __version__

# Lazy loading to avoid circular imports

if TYPE_CHECKING:
    from oridecon.contracts.data import ReadOnlyRepositoryProtocol
    from oridecon.contracts.domain import DomainEvent
    from oridecon.contracts.events import (
        AggregateFactoryProtocol,
        CommandBusProtocol,
        CommandHandlerProtocol,
        DomainEventPublisherProtocol,
        EventBusProtocol,
        EventHandlerProtocol,
        EventStoreProtocol,
        MultiEventHandlerProtocol,
        ProjectionProtocol,
        QueryBusProtocol,
        QueryHandlerProtocol,
        SnapshotStoreProtocol,
    )
    from oridecon.contracts.workflow import (
        SagaManagerProtocol,
        SagaProtocol,
    )
    from oridecon.events.aggregates.aggregate import AggregateRoot
    from oridecon.events.aggregates.entity import Entity
    from oridecon.events.aggregates.value_object import ValueObject
    from oridecon.events.buses.command import CommandBusImpl
    from oridecon.events.buses.event import (
        DispatchResult,
        EventBusImpl,
    )
    from oridecon.events.buses.query import QueryBusImpl
    from oridecon.events.config import (
        CommandBusConfig,
        EventBusConfig,
        EventsConfig,
        InMemoryEventStoreConfig,
        MongoDBEventStoreConfig,
        PostgresEventStoreConfig,
        QueryBusConfig,
        SnapshotConfig,
    )
    from oridecon.events.decorators.handlers import (
        command_handler,
        event_handler,
        query_handler,
    )
    from oridecon.events.di import EventsProvider
    from oridecon.events.exceptions import (
        AggregateNotFoundError,
        ConcurrencyError,
        EventError,
        EventLoadError,
        EventPersistenceError,
        EventStoreConnectionError,
        EventStoreError,
        HandlerNotFoundError,
        ProjectionBuildError,
        ProjectionNotFoundError,
        SchemaError,
        SecurityError,
        StreamingError,
        StreamNotFoundError,
        WebhookDeliveryError,
    )
    from oridecon.events.handlers.registry import (
        HandlerRegistry,
    )
    from oridecon.events.messages.base import (
        Message,
        MessageMetadata,
    )
    from oridecon.events.messages.command import (
        Command,
        IdempotentCommand,
    )
    from oridecon.events.messages.event import (
        Event,
        IntegrationEvent,
    )
    from oridecon.events.messages.query import (
        PagedResult,
        PaginatedQuery,
        Query,
    )
    from oridecon.events.middleware.base import (
        AbstractMiddleware,
        NextHandler,
    )
    from oridecon.events.protocols import (
        EventFilterProtocol,
        EventSerializerProtocol,
    )
    from oridecon.events.repository.base import (
        AbstractReadOnlyRepository,
        AbstractRepository,
    )
    from oridecon.events.repository.event_sourcing import EventSourcingRepository
    from oridecon.events.stores import (
        HAS_MONGODB,
        HAS_POSTGRES,
        HAS_SQLITE,
        PostgresEventStore,
        PostgresSnapshotStore,
    )
    from oridecon.events.stores.base import (
        AbstractEventStore,
        AbstractSnapshotStore,
    )
    from oridecon.events.stores.memory import (
        InMemoryEventStore,
        InMemorySnapshotStore,
    )
    from oridecon.events.stores.redis import RedisEventStore
    from oridecon.events.stores.snapshot import SnapshotManager
    from oridecon.events.types import (
        AggregateStatus,
        Checkpoint,
        CommandResult,
        EventEnvelope,
        EventStoreBackend,
        HandlerInfo,
        MessageType,
        MiddlewareInfo,
        ProjectionState,
        QueryResult,
        Snapshot,
        SnapshotStrategy,
        StreamInfo,
        StreamPosition,
    )
    from oridecon.events.version_skew import (
        KnownEventSetRegistry,
        VersionAwareSubscription,
        known_events,
    )
    from oridecon.events.webhooks.dispatcher import (
        WebhookDispatcher,
        WebhookEndpoint,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # Module
    "EventsModule": ("oridecon.events.module", "EventsModule"),
    # Buses (concrete implementations — primary names for test/runtime use)
    "CommandBusProtocol": ("oridecon.contracts.events", "CommandBusProtocol"),
    "CommandBusImpl": ("oridecon.events.buses.command", "CommandBusImpl"),
    "CommandBus": ("oridecon.contracts", "CommandBusProtocol"),
    "EventBusProtocol": ("oridecon.contracts.events", "EventBusProtocol"),
    "EventBusImpl": ("oridecon.events.buses.event", "EventBusImpl"),
    "EventBus": ("oridecon.contracts", "EventBusProtocol"),
    "QueryBusProtocol": ("oridecon.contracts.events", "QueryBusProtocol"),
    "QueryBusImpl": ("oridecon.events.buses.query", "QueryBusImpl"),
    "QueryBus": ("oridecon.contracts", "QueryBusProtocol"),
    "command_handler": ("oridecon.events.decorators.handlers", "command_handler"),
    "event_handler": ("oridecon.events.decorators.handlers", "event_handler"),
    "query_handler": ("oridecon.events.decorators.handlers", "query_handler"),
    "NextHandler": ("oridecon.events.middleware.base", "NextHandler"),
    "AbstractMiddleware": ("oridecon.events.middleware.base", "AbstractMiddleware"),
    # Config
    "CommandBusConfig": ("oridecon.events.config", "CommandBusConfig"),
    "EventBusConfig": ("oridecon.events.config", "EventBusConfig"),
    "EventsConfig": ("oridecon.events.config", "EventsConfig"),
    "InMemoryEventStoreConfig": ("oridecon.events.config", "InMemoryEventStoreConfig"),
    "MongoDBEventStoreConfig": ("oridecon.events.config", "MongoDBEventStoreConfig"),
    "PostgresEventStoreConfig": ("oridecon.events.config", "PostgresEventStoreConfig"),
    "PostgresEventStore": ("oridecon.events.stores", "PostgresEventStore"),
    "PostgresSnapshotStore": ("oridecon.events.stores", "PostgresSnapshotStore"),
    "RedisEventStore": ("oridecon.events.stores.redis", "RedisEventStore"),
    "QueryBusConfig": ("oridecon.events.config", "QueryBusConfig"),
    "SnapshotConfig": ("oridecon.events.config", "SnapshotConfig"),
    # Exceptions
    "AggregateNotFoundError": ("oridecon.events.exceptions", "AggregateNotFoundError"),
    "CommandExecutionError": ("oridecon.events.exceptions", "CommandExecutionError"),
    "ConcurrencyError": ("oridecon.events.exceptions", "ConcurrencyError"),
    "DuplicateHandlerError": ("oridecon.events.exceptions", "DuplicateHandlerError"),
    "EventError": ("oridecon.events.exceptions", "EventError"),
    "EventLoadError": ("oridecon.events.exceptions", "EventLoadError"),
    "EventPersistenceError": ("oridecon.events.exceptions", "EventPersistenceError"),
    "EventStoreConnectionError": (
        "oridecon.events.exceptions",
        "EventStoreConnectionError",
    ),
    "EventStoreError": ("oridecon.events.exceptions", "EventStoreError"),
    "HandlerNotFoundError": ("oridecon.events.exceptions", "HandlerNotFoundError"),
    "ProjectionBuildError": ("oridecon.events.exceptions", "ProjectionBuildError"),
    "ProjectionNotFoundError": (
        "oridecon.events.exceptions",
        "ProjectionNotFoundError",
    ),
    "QueryExecutionError": ("oridecon.events.exceptions", "QueryExecutionError"),
    "SchemaError": ("oridecon.events.exceptions", "SchemaError"),
    "SecurityError": ("oridecon.events.exceptions", "SecurityError"),
    "StreamingError": ("oridecon.events.exceptions", "StreamingError"),
    "StreamNotFoundError": ("oridecon.events.exceptions", "StreamNotFoundError"),
    "WebhookDeliveryError": ("oridecon.events.exceptions", "WebhookDeliveryError"),
    # Webhooks
    "WebhookDispatcher": ("oridecon.events.webhooks.dispatcher", "WebhookDispatcher"),
    "WebhookEndpoint": ("oridecon.events.webhooks.dispatcher", "WebhookEndpoint"),
    # Messages
    "Command": ("oridecon.events.messages.command", "Command"),
    "Event": ("oridecon.events.messages.event", "Event"),
    # Domain event base from contracts for convenience
    "DomainEvent": ("oridecon.contracts.domain", "DomainEvent"),
    "IdempotentCommand": ("oridecon.events.messages.command", "IdempotentCommand"),
    "IntegrationEvent": ("oridecon.events.messages.event", "IntegrationEvent"),
    "Message": ("oridecon.events.messages.base", "Message"),
    "MessageMetadata": ("oridecon.events.messages.base", "MessageMetadata"),
    "PagedResult": ("oridecon.events.messages.query", "PagedResult"),
    "PaginatedQuery": ("oridecon.events.messages.query", "PaginatedQuery"),
    "Query": ("oridecon.events.messages.query", "Query"),
    # Stores
    "HAS_MONGODB": ("oridecon.events.stores", "HAS_MONGODB"),
    "HAS_POSTGRES": ("oridecon.events.stores", "HAS_POSTGRES"),
    "HAS_SQLITE": ("oridecon.events.stores", "HAS_SQLITE"),
    "AbstractEventStore": ("oridecon.events.stores.base", "AbstractEventStore"),
    "InMemoryEventStore": ("oridecon.events.stores.memory", "InMemoryEventStore"),
    "InMemorySnapshotStore": ("oridecon.events.stores.memory", "InMemorySnapshotStore"),
    "SnapshotManager": ("oridecon.events.stores.snapshot", "SnapshotManager"),
    "AbstractSnapshotStore": ("oridecon.events.stores.base", "AbstractSnapshotStore"),
    # DTOs
    "Checkpoint": ("oridecon.events.types", "Checkpoint"),
    "EventEnvelope": ("oridecon.events.types", "EventEnvelope"),
    "Snapshot": ("oridecon.events.types", "Snapshot"),
    "StreamInfo": ("oridecon.events.types", "StreamInfo"),
    # Enums
    "AggregateStatus": ("oridecon.events.types", "AggregateStatus"),
    "EventStoreBackend": ("oridecon.events.types", "EventStoreBackend"),
    "MessageType": ("oridecon.events.types", "MessageType"),
    "ProjectionState": ("oridecon.events.types", "ProjectionState"),
    "SnapshotStrategy": ("oridecon.events.types", "SnapshotStrategy"),
    "StreamPosition": ("oridecon.events.types", "StreamPosition"),
    # Results
    "CommandResult": ("oridecon.events.types", "CommandResult"),
    "DispatchResult": ("oridecon.events.buses.event", "DispatchResult"),
    "HandlerInfo": ("oridecon.events.types", "HandlerInfo"),
    "MiddlewareInfo": ("oridecon.events.types", "MiddlewareInfo"),
    "QueryResult": ("oridecon.events.types", "QueryResult"),
    # Aggregates
    "AggregateRoot": ("oridecon.events.aggregates.aggregate", "AggregateRoot"),
    "Entity": ("oridecon.events.aggregates.entity", "Entity"),
    "ValueObject": ("oridecon.events.aggregates.value_object", "ValueObject"),
    # Handlers
    "CommandHandlerProtocol": (
        "oridecon.events.handlers.registry",
        "CommandHandlerProtocol",
    ),
    "EventHandlerProtocol": (
        "oridecon.events.handlers.registry",
        "EventHandlerProtocol",
    ),
    "HandlerRegistry": ("oridecon.events.handlers.registry", "HandlerRegistry"),
    "QueryHandlerProtocol": (
        "oridecon.events.handlers.registry",
        "QueryHandlerProtocol",
    ),
    "clear_handler_registry": (
        "oridecon.events.handlers.registry",
        "clear_handler_registry",
    ),
    # RepositoryProtocol
    "EventSourcingRepository": (
        "oridecon.events.repository.event_sourcing",
        "EventSourcingRepository",
    ),
    "RepositoryProtocol": ("oridecon.contracts.data", "RepositoryProtocol"),
    "AbstractRepository": ("oridecon.events.repository.base", "AbstractRepository"),
    "AbstractReadOnlyRepository": (
        "oridecon.events.repository.base",
        "AbstractReadOnlyRepository",
    ),
    # Provider
    "EventsProvider": ("oridecon.events.di", "EventsProvider"),
    # Version skew
    "VersionAwareSubscription": (
        "oridecon.events.version_skew.subscription",
        "VersionAwareSubscription",
    ),
    "KnownEventSetRegistry": (
        "oridecon.events.version_skew.registry",
        "KnownEventSetRegistry",
    ),
    "known_events": (
        "oridecon.events.version_skew.decorator",
        "known_events",
    ),
    # Contracts
    "AggregateFactoryProtocol": (
        "oridecon.contracts.events",
        "AggregateFactoryProtocol",
    ),
    "DomainEventPublisherProtocol": (
        "oridecon.contracts.events",
        "DomainEventPublisherProtocol",
    ),
    "EventStoreProtocol": ("oridecon.contracts.events", "EventStoreProtocol"),
    "MultiEventHandlerProtocol": (
        "oridecon.contracts.events",
        "MultiEventHandlerProtocol",
    ),
    "ProjectionProtocol": ("oridecon.contracts.events", "ProjectionProtocol"),
    "ReadOnlyRepositoryProtocol": (
        "oridecon.contracts.data",
        "ReadOnlyRepositoryProtocol",
    ),
    "SagaProtocol": ("oridecon.contracts.workflow", "SagaProtocol"),
    "SagaManagerProtocol": ("oridecon.contracts.workflow", "SagaManagerProtocol"),
    "SnapshotStoreProtocol": ("oridecon.contracts.events", "SnapshotStoreProtocol"),
    # Optional stores (sqlite, postgres, mongodb — available if extras installed)
    "SqliteConfig": ("oridecon.events.stores.sqlite", "SqliteConfig"),
    "SqliteEventStore": ("oridecon.events.stores.sqlite", "SqliteEventStore"),
    "SqliteSnapshotStore": ("oridecon.events.stores.sqlite", "SqliteSnapshotStore"),
    "MongoDBConfig": ("oridecon.events.stores.mongodb", "MongoDBConfig"),
    "MongoDBEventStore": ("oridecon.events.stores.mongodb", "MongoDBEventStore"),
    "MongoDBSnapshotStore": ("oridecon.events.stores.mongodb", "MongoDBSnapshotStore"),
    # Internal protocols
    "EventSerializerProtocol": ("oridecon.events.protocols", "EventSerializerProtocol"),
    "EventFilterProtocol": ("oridecon.events.protocols", "EventFilterProtocol"),
    # Events (operational meta-events)
    "EventPublishedEvent": ("oridecon.events.events", "EventPublishedEvent"),
    "ProjectionUpdatedEvent": ("oridecon.events.events", "ProjectionUpdatedEvent"),
    # Hooks
    "EventHandledHook": ("oridecon.events.hooks", "EventHandledHook"),
    "EventPublishedHook": ("oridecon.events.hooks", "EventPublishedHook"),
    "EventStoredHook": ("oridecon.events.hooks", "EventStoredHook"),
    # Reactive bridges
    "from_bus": ("oridecon.events.reactive", "from_bus"),
    "from_store": ("oridecon.events.reactive", "from_store"),
    "retry_with_resilience": ("oridecon.events.reactive", "retry_with_resilience"),
}


def __getattr__(name: str) -> Any:
    """Lazy load attributes to avoid circular imports."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """List available attributes for IDE support."""
    return list(__all__) + list(_LAZY_IMPORTS.keys())


__all__ = list(_LAZY_IMPORTS)
