"""Server-Sent Events support for Oridecon Web."""

from __future__ import annotations

from oridecon.web.sse.backpressure import (
    SSEBackpressureHandler,
    SSEConnectionEvents,
    SSEResponse,
    SSERetryTracker,
)
from oridecon.web.sse.decorators import sse_endpoint
from oridecon.web.sse.handler import AbstractSSEHandler
from oridecon.web.sse.heartbeat import SSEHeartbeatScheduler, get_heartbeat_scheduler
from oridecon.web.transport.sse import EventSourceResponse, ServerSentEvent

__all__ = [
    "AbstractSSEHandler",
    "EventSourceResponse",
    "SSEBackpressureHandler",
    "SSEConnectionEvents",
    "SSEHeartbeatScheduler",
    "SSEResponse",
    "SSERetryTracker",
    "ServerSentEvent",
    "get_heartbeat_scheduler",
    "sse_endpoint",
]
