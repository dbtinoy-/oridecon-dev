"""Handler decorator registration tests."""

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

from bus_test_support import make_domain_event


class TestDecorators:
    """Test handler decorators"""

    def test_command_handler_decorator(self):
        """Test command handler decorator"""
        bus = CommandBusImpl()

        @command_handler(Command)
        class TestCommandHandler:
            async def handle(self, cmd):
                return "handled"

        # The decorator should attach handler info
        from oridecon.events.decorators.handlers import get_handler_info
        info = get_handler_info(TestCommandHandler)
        assert info is not None
        assert info.handler_type == "command"
        assert info.message_types == [Command]

    def test_query_handler_decorator(self):
        """Test query handler decorator"""
        bus = QueryBusImpl()

        @query_handler(Query)
        class TestQueryHandler:
            async def handle(self, query):
                return "result"

        from oridecon.events.decorators.handlers import get_handler_info
        info = get_handler_info(TestQueryHandler)
        assert info is not None
        assert info.handler_type == "query"
        assert info.message_types == [Query]

    def test_event_handler_decorator(self):
        """Test event handler decorator"""
        bus = EventBusImpl()

        @event_handler(DomainEvent)
        class TestEventHandler:
            async def handle(self, event):
                pass

        from oridecon.events.decorators.handlers import get_handler_info
        info = get_handler_info(TestEventHandler)
        assert info is not None
        assert info.handler_type == "event"
        assert info.message_types == [DomainEvent]

    def test_event_handler_multiple_events(self):
        """Test event handler decorator with multiple events"""
        from oridecon.events.decorators.handlers import multi_event_handler
        bus = EventBusImpl()

        class OrderEvent(DomainEvent):
            order_id: str = "test"

        class PaymentEvent(DomainEvent):
            payment_id: str = "test"

        @multi_event_handler(OrderEvent, PaymentEvent)
        class TestEventHandler:
            async def handle(self, event):
                pass

        from oridecon.events.decorators.handlers import get_handler_info
        info = get_handler_info(TestEventHandler)
        assert info is not None
        assert info.handler_type == "event"
        assert OrderEvent in info.message_types
        assert PaymentEvent in info.message_types


