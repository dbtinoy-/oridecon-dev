"""Messages module for Event Sourcing and CQRS.

This module provides the core message types: Command, Query, and Event,
along with metadata handling and message base classes.
"""

from __future__ import annotations

from oridecon.events.messages.base import Message, MessageMetadata
from oridecon.events.messages.command import Command, IdempotentCommand
from oridecon.events.messages.event import (
    Event,
    IntegrationEvent,
)
from oridecon.events.messages.query import PagedResult, PaginatedQuery, Query

__all__ = [
    "Command",
    "Event",
    "IdempotentCommand",
    "IntegrationEvent",
    "Message",
    "MessageMetadata",
    "PagedResult",
    "PaginatedQuery",
    "Query",
]
