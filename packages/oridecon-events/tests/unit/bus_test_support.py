"""Shared helpers for bus test modules."""

from unittest.mock import AsyncMock, Mock, patch
from uuid import uuid4

import pytest

from oridecon.contracts.domain import DomainEvent
from oridecon.events.buses import (
    CommandBusImpl,
    EventBusImpl,
    QueryBusImpl,
)
from oridecon.events.buses.base import Bus, HandlerNotFoundError
from oridecon.events.buses.command import CommandExecutionError
from oridecon.events.buses.event import EventHandlerError
from oridecon.events.buses.query import QueryExecutionError
from oridecon.events.decorators import (
    command_handler,
    event_handler,
    query_handler,
)
from oridecon.events.hooks import EventHandledHook, EventPublishedHook
from oridecon.events.messages import Command, Event, Query
from oridecon.hooks import HookRegistry

# Ensure helper `make_domain_event` is available in varied test invocation contexts
try:
    from oridecon.events.tests.unit.conftest import make_domain_event
except ImportError:
    try:
        from tests.conftest import make_domain_event
    except ImportError:

        def make_domain_event(**kwargs):
            from uuid import uuid4

            from oridecon.contracts.domain import DomainEvent

            data = {
                "aggregate_id": kwargs.get("aggregate_id", uuid4()),
                "aggregate_type": kwargs.get("aggregate_type", "TestAggregate"),
                "event_type": kwargs.get("event_type", None),
                "sequence_number": kwargs.get("sequence_number", kwargs.get("version", 0)),
                "actor_id": kwargs.get("actor_id", None),
            }
            data.update(kwargs)
            if "version" in data:
                del data["version"]
            return DomainEvent(**data)



