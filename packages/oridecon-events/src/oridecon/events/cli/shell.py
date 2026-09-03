"""CLI shell context factories for oridecon-events."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.contracts.events import EventBusProtocol

if TYPE_CHECKING:
    from oridecon.contracts.core.di import ContainerResolverProtocol


async def provide_event_bus(container: ContainerResolverProtocol) -> EventBusProtocol:
    """Provide event bus for interactive shell use.

    Args:
        container: Booted DI container.

    Returns:
        The resolved EventBus instance.
    """
    bus: EventBusProtocol = await container.resolve(EventBusProtocol)
    return bus
