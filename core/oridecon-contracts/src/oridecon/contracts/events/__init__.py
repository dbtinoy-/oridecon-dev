"""Event sourcing protocols (CQRS/ES)."""

from __future__ import annotations

from oridecon.contracts.events.messages import (
    Command,
    IdempotentCommand,
    Message,
    MessageMetadata,
    MessageSerializerProtocol,
)
from oridecon.contracts.events.outbox import (
    OutboxBackendProtocol,
    OutboxEntryProtocol,
    OutboxRelayProtocol,
    OutboxStatus,
)
from oridecon.contracts.events.protocols import (
    AggregateFactoryProtocol,
    CommandBusProtocol,
    CommandHandlerProtocol,
    DomainEventPublisherProtocol,
    EventBusDiagnosticsProtocol,
    EventBusProtocol,
    EventHandlerProtocol,
    EventMiddlewareProtocol,
    EventReplayProtocol,
    EventSourcedReadRepositoryProtocol,
    EventSourcedRepositoryProtocol,
    EventStoreProtocol,
    IntegrationEventProtocol,
    MultiEventHandlerProtocol,
    ProjectionProtocol,
    PubSubProtocol,
    QueryBusProtocol,
    QueryHandlerProtocol,
    SnapshotStoreProtocol,
    WebhookSignatureVerifierProtocol,
)
from oridecon.contracts.events.version_skew import (
    EventSchemaVersionSkew,
    EventTypeVersion,
    UnknownEventTypeReceived,
)

__all__ = [
    "AggregateFactoryProtocol",
    "Command",
    "CommandBusProtocol",
    "CommandHandlerProtocol",
    "DomainEventPublisherProtocol",
    "EventBusDiagnosticsProtocol",
    "EventBusProtocol",
    "EventHandlerProtocol",
    "EventMiddlewareProtocol",
    "EventReplayProtocol",
    "EventSchemaVersionSkew",
    "EventSourcedReadRepositoryProtocol",
    "EventSourcedRepositoryProtocol",
    "EventStoreProtocol",
    "EventTypeVersion",
    "IdempotentCommand",
    "IntegrationEventProtocol",
    "Message",
    "MessageMetadata",
    "MessageSerializerProtocol",
    "MultiEventHandlerProtocol",
    "OutboxBackendProtocol",
    "OutboxEntryProtocol",
    "OutboxRelayProtocol",
    "OutboxStatus",
    "ProjectionProtocol",
    "PubSubProtocol",
    "QueryBusProtocol",
    "QueryHandlerProtocol",
    "SnapshotStoreProtocol",
    "UnknownEventTypeReceived",
    "WebhookSignatureVerifierProtocol",
]
