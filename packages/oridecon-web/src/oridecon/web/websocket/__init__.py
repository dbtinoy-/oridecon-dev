"""WebSocket Module.

Provides base classes and decorators for building WebSocket handlers
and gateways.

Low-level handler example::

    from oridecon.web.websocket import AbstractWebSocketHandler, websocket_handler

    @websocket_handler("/ws/chat/{room}")
    class ChatHandler(AbstractWebSocketHandler):
        async def on_connect(self, websocket):
            await websocket.accept()
        async def on_message(self, websocket, message):
            await self.broadcast(message)
        async def on_disconnect(self, websocket):
            pass

High-level gateway example::

    from oridecon.web.websocket import WebSocketGateway, subscribe_message, websocket_gateway

    @websocket_gateway("/ws/chat")
    class ChatGateway(WebSocketGateway):
        @subscribe_message("chat.send")
        async def handle_send(self, ws, payload):
            await self.broadcast(payload)
"""

from __future__ import annotations

from oridecon.web.transport.websocket_guards import (
    GuardedWebSocket,
    execute_websocket_guards,
)
from oridecon.web.transport.websockets import WebSocket
from oridecon.web.websocket.connection_id import ConnectionIDManager
from oridecon.web.websocket.decorators import websocket_handler
from oridecon.web.websocket.gateway import (
    WebSocketGateway,
    on_connect,
    on_disconnect,
    on_error,
    subscribe_message,
    websocket_gateway,
)
from oridecon.web.websocket.handler import AbstractWebSocketHandler
from oridecon.web.websocket.rate_limiter import WebSocketRateLimiter

__all__ = [
    "AbstractWebSocketHandler",
    "ConnectionIDManager",
    "GuardedWebSocket",
    "WebSocket",
    "WebSocketGateway",
    "WebSocketRateLimiter",
    "execute_websocket_guards",
    "on_connect",
    "on_disconnect",
    "on_error",
    "subscribe_message",
    "websocket_gateway",
    "websocket_handler",
]
