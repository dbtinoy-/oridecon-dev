"""Server- and client-side Server-Sent Events support."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncGenerator
from enum import Enum
from typing import Any

from starlette.responses import StreamingResponse

from oridecon.serialization import dumps_str
from oridecon.ui.core.base import Component, Element
from oridecon.ui.core.js import js_string
from oridecon.ui.core.render_context import get_render_scope
from oridecon.ui.core.trusted_html import trusted_html

__all__ = [
    "SSEEventType",
    "SSEMessage",
    "SSEStream",
    "SSE",
]


class SSEEventType(str, Enum):
    """Well-known SSE event type names."""

    MESSAGE = "message"
    UPDATE = "update"
    ERROR = "error"
    PING = "ping"
    CLOSE = "close"
    CONNECT = "connect"
    DISCONNECT = "disconnect"


def _single_line_field(value: str, *, field: str) -> str:
    """Validate an SSE field that cannot safely contain a line boundary."""
    if "\r" in value or "\n" in value:
        raise ValueError(f"SSE {field} must not contain CR or LF")
    if "\x00" in value:
        raise ValueError(f"SSE {field} must not contain NUL")
    return value


class SSEMessage:
    """Format one standards-compliant SSE message."""

    def __init__(
        self,
        data: Any,
        event: str | None = None,
        event_id: str | None = None,
        retry: int | None = None,
    ) -> None:
        if event is not None:
            event = _single_line_field(str(event), field="event")
        if event_id is not None:
            event_id = _single_line_field(str(event_id), field="id")
        if retry is not None and retry < 0:
            raise ValueError("SSE retry must be zero or greater")

        self.data = data
        self.event = event
        self.id = event_id
        self.retry = retry

    def __str__(self) -> str:
        lines: list[str] = []
        if self.id:
            lines.append(f"id: {self.id}")
        if self.event:
            lines.append(f"event: {self.event}")
        if self.retry is not None:
            lines.append(f"retry: {self.retry}")

        data = self.data if isinstance(self.data, str) else dumps_str(self.data)
        # CR is also an SSE line boundary. Normalize it before prefixing every
        # line so payload text can never introduce a protocol control field.
        normalized_data = data.replace("\r\n", "\n").replace("\r", "\n")
        for line in normalized_data.split("\n"):
            lines.append(f"data: {line}")

        return "\n".join(lines) + "\n\n"


class SSEStream(StreamingResponse):
    """Stream :class:`SSEMessage` instances with proxy-safe headers."""

    def __init__(self, generator: AsyncGenerator[SSEMessage, None], **kwargs: Any):
        async def event_generator() -> Any:
            try:
                async for message in generator:
                    yield str(message)
            except asyncio.CancelledError:
                pass

        super().__init__(event_generator(), media_type="text/event-stream", **kwargs)
        self.headers["Cache-Control"] = "no-cache"
        self.headers["Connection"] = "keep-alive"
        self.headers["X-Accel-Buffering"] = "no"


class SSE(Component):
    """Render an HTMX SSE region with scoped exponential-backoff handling.

    Args:
        url: SSE endpoint URL (``sse-connect`` attribute).
        target: CSS selector or ``"this"`` for the HTMX swap target.
        event_type: SSE event name to swap on.
        retry_ms: Initial reconnect delay, clamped to at least 100 ms.
        sse_key: Optional stable identity for full/partial render parity.
        **props: Additional attributes for the root region. Core SSE attributes
            cannot be overridden.
    """

    def __init__(
        self,
        url: str,
        target: str = "this",
        event_type: str = SSEEventType.MESSAGE,
        retry_ms: int = 3000,
        sse_key: str | None = None,
        **props: Any,
    ) -> None:
        super().__init__(**props)
        self.url = url
        self.target = target
        normalized_event_type = (
            event_type.value if isinstance(event_type, SSEEventType) else event_type
        )
        self.event_type = _single_line_field(normalized_event_type, field="event type")
        self.retry_ms = max(100, int(retry_ms))
        self.sse_key = sse_key

    def _reconnect_script(self, component_id: str) -> str:
        return f"""
(() => {{
    const element = document.getElementById({js_string(component_id)});
    if (!element || element.dataset.sseReconnectBound === 'true') return;
    element.dataset.sseReconnectBound = 'true';
    const initialRetry = {self.retry_ms};
    const maxRetry = 30000;
    let attempts = 0;

    element.addEventListener('htmx:sseError', (event) => {{
        const source = event.detail?.elt || event.target;
        if (source !== element && !element.contains(source)) return;
        const delay = Math.min(initialRetry * Math.pow(2, attempts), maxRetry);
        attempts += 1;
        window.setTimeout(() => {{
            if (element.isConnected && typeof htmx !== 'undefined') {{
                htmx.process(element);
            }}
        }}, delay);
    }});
    element.addEventListener('htmx:sseOpen', () => {{
        attempts = 0;
    }});
}})();
"""

    def render(self) -> Element:
        root_props = dict(self.props)
        explicit_id = root_props.pop("id", root_props.pop("id_", None))
        for protected_name in (
            "hx-ext",
            "hx_ext",
            "sse-connect",
            "sse_connect",
            "sse-swap",
            "sse_swap",
            "hx-target",
            "hx_target",
        ):
            root_props.pop(protected_name, None)

        scope = get_render_scope().child("sse")
        if explicit_id is None:
            component_id = scope.id("region", key=self.sse_key)
        else:
            component_id = str(explicit_id)
            # Reserve an identity as well as honoring the caller-facing ID, so
            # duplicate explicit IDs in one render response fail loudly.
            scope.id("explicit-region", key=component_id)

        root_props.update(
            {
                "id": component_id,
                "hx-ext": "sse",
                "sse-connect": self.url,
                "sse-swap": self.event_type,
                "hx-target": self.target,
            }
        )
        root_props.setdefault("role", "status")
        if "aria-live" not in root_props and "aria_live" not in root_props:
            root_props["aria-live"] = "polite"

        script = Element(
            "script",
            trusted_html(
                self._reconnect_script(component_id),
                source="generated SSE reconnect controller",
            ),
        )
        return Element("div", *self.children, script, **root_props)
