"""Event sourcing protocol class definitions (CQRS/ES).

Protocols for event buses, command buses, event stores,
and related patterns.
"""

from __future__ import annotations

from oridecon.contracts.events.protocols.cqrs import (
    CommandBusProtocol as CommandBusProtocol,
)
from oridecon.contracts.events.protocols.cqrs import (
    CommandHandlerProtocol as CommandHandlerProtocol,
)
from oridecon.contracts.events.protocols.cqrs import (
    QueryBusProtocol as QueryBusProtocol,
)
from oridecon.contracts.events.protocols.cqrs import (
    QueryHandlerProtocol as QueryHandlerProtocol,
)
from oridecon.contracts.events.protocols.domain import (
    DomainEventPublisherProtocol as DomainEventPublisherProtocol,
)
from oridecon.contracts.events.protocols.domain import (
    EventBusDiagnosticsProtocol as EventBusDiagnosticsProtocol,
)
from oridecon.contracts.events.protocols.domain import (
    EventBusProtocol as EventBusProtocol,
)
from oridecon.contracts.events.protocols.domain import (
    EventHandlerProtocol as EventHandlerProtocol,
)
from oridecon.contracts.events.protocols.domain import (
    EventMiddlewareProtocol as EventMiddlewareProtocol,
)
from oridecon.contracts.events.protocols.domain import (
    MultiEventHandlerProtocol as MultiEventHandlerProtocol,
)
from oridecon.contracts.events.protocols.projection import (
    IntegrationEventProtocol as IntegrationEventProtocol,
)
from oridecon.contracts.events.protocols.projection import (
    ProjectionProtocol as ProjectionProtocol,
)
from oridecon.contracts.events.protocols.projection import (
    PubSubProtocol as PubSubProtocol,
)
from oridecon.contracts.events.protocols.projection import (
    WebhookSignatureVerifierProtocol as WebhookSignatureVerifierProtocol,
)
from oridecon.contracts.events.protocols.store import (
    AggregateFactoryProtocol as AggregateFactoryProtocol,
)
from oridecon.contracts.events.protocols.store import (
    EventReplayProtocol as EventReplayProtocol,
)
from oridecon.contracts.events.protocols.store import (
    EventSourcedReadRepositoryProtocol as EventSourcedReadRepositoryProtocol,
)
from oridecon.contracts.events.protocols.store import (
    EventSourcedRepositoryProtocol as EventSourcedRepositoryProtocol,
)
from oridecon.contracts.events.protocols.store import (
    EventStoreProtocol as EventStoreProtocol,
)
from oridecon.contracts.events.protocols.store import (
    SnapshotStoreProtocol as SnapshotStoreProtocol,
)

__all__ = [
    "AggregateFactoryProtocol",
    "CommandBusProtocol",
    "CommandHandlerProtocol",
    "DomainEventPublisherProtocol",
    "EventBusDiagnosticsProtocol",
    "EventBusProtocol",
    "EventHandlerProtocol",
    "EventMiddlewareProtocol",
    "EventReplayProtocol",
    "EventSourcedReadRepositoryProtocol",
    "EventSourcedRepositoryProtocol",
    "EventStoreProtocol",
    "IntegrationEventProtocol",
    "MultiEventHandlerProtocol",
    "ProjectionProtocol",
    "PubSubProtocol",
    "QueryBusProtocol",
    "QueryHandlerProtocol",
    "SnapshotStoreProtocol",
    "WebhookSignatureVerifierProtocol",
]
