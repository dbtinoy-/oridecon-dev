from __future__ import annotations

import pytest

from oridecon.contracts.web.sse import ReactiveSseBridgeProtocol
from oridecon.di.container import Container
from oridecon.web.di import provider_sections
from oridecon.web.di.provider import WebProvider
from oridecon.web.transport.reactive import sse_from_stream


@pytest.mark.asyncio
async def test_reactive_sse_bridge_resolves_to_bridge_callable() -> None:
    """The DI registration must not eagerly consume a stream argument."""
    container = Container()
    provider_sections.register_transport_services(WebProvider(), container)

    bridge = await container.resolve(ReactiveSseBridgeProtocol)

    assert bridge is sse_from_stream
