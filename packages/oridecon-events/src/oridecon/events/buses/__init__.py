"""Buses module for Event Sourcing and CQRS.

This module provides the message bus implementations:
- CommandBusImpl: For dispatching commands (single handler)
- QueryBusImpl: For dispatching queries (single handler)
- EventBusImpl: For publishing events (multiple handlers)
"""

from __future__ import annotations

from oridecon.events.buses.base import Bus, MiddlewareFunc
from oridecon.events.buses.command import CommandBusImpl
from oridecon.events.buses.event import EventBusImpl
from oridecon.events.buses.query import QueryBusImpl

__all__ = [
    "Bus",
    "CommandBusImpl",
    "EventBusImpl",
    "MiddlewareFunc",
    "QueryBusImpl",
]
