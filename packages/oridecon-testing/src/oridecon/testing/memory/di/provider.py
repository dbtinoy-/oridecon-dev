from __future__ import annotations

from oridecon.contracts.core.di import (
    ContainerRegistrarProtocol,
    ContainerResolverProtocol,
)
from oridecon.contracts.events import (
    CommandBusProtocol as CommandBusProtocol,
)
from oridecon.contracts.events import (
    DomainEventPublisherProtocol as DomainEventPublisherProtocol,
)
from oridecon.contracts.events import (
    EventBusProtocol as EventBusProtocol,
)
from oridecon.contracts.events import (
    QueryBusProtocol as QueryBusProtocol,
)
from oridecon.di.provider import Provider, ProviderPriority
from oridecon.testing.memory.cqrs import InMemoryCommandBus, InMemoryQueryBus
from oridecon.testing.memory.event_bus import InMemoryEventBus


class MemoryProvider(Provider):
    """Registers all in-memory bus implementations as singletons."""

    name = "memory"
    priority = ProviderPriority.INFRASTRUCTURE

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        """Register InMemoryEventBus, InMemoryCommandBus, InMemoryQueryBus, and AuditLogger."""
        from oridecon.contracts.audit import AuditLoggerProtocol
        from oridecon.testing.memory.audit import InMemoryAuditLogger

        event_bus = InMemoryEventBus()
        container.singleton(EventBusProtocol, instance=event_bus)
        container.singleton(DomainEventPublisherProtocol, instance=event_bus)

        container.singleton(CommandBusProtocol, instance=InMemoryCommandBus())
        container.singleton(QueryBusProtocol, instance=InMemoryQueryBus())
        container.singleton(AuditLoggerProtocol, instance=InMemoryAuditLogger())

    async def boot(self, container: ContainerResolverProtocol) -> None:
        """No boot-time work required for the event bus module."""

    async def shutdown(self) -> None:
        """No resources to release for the event bus module."""


__all__ = ["MemoryProvider"]
