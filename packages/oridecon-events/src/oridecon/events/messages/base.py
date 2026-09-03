"""Base message classes for Event Sourcing and CQRS.

Re-exports :class:`~oridecon.contracts.events.messages.Message` and
:class:`~oridecon.contracts.events.messages.MessageMetadata` from
``oridecon.contracts`` so that event-sourcing code has a single, stable
import path within the events package.
"""

from __future__ import annotations

from oridecon.contracts.events.messages import Message, MessageMetadata

__all__ = ["Message", "MessageMetadata"]
