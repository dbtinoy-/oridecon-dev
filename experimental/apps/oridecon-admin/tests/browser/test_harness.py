"""Verify the browser server harness independently of a browser binary.

The server fixture is the part most likely to rot silently. These tests drive
it over HTTP and verify that it binds unique ephemeral ports and tears down.
"""

from __future__ import annotations

import socket
import threading
import time
from typing import Any

import httpx
import pytest
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route

from tests.browser.conftest import _browser_unavailable


class _BrowserConfig:
    def __init__(self, *, gate: bool) -> None:
        self.gate = gate

    def getoption(self, name: str, *, default: bool = False) -> bool:
        if name == "--browser-gate":
            return self.gate
        return default


def _echo_app(message: str) -> Starlette:
    async def index(request: Any) -> PlainTextResponse:
        return PlainTextResponse(message)

    return Starlette(routes=[Route("/", index)])


class TestBrowserAvailabilityPolicy:
    def test_local_mode_skips_missing_browser(self) -> None:
        with pytest.raises(pytest.skip.Exception, match="missing browser"):
            _browser_unavailable(_BrowserConfig(gate=False), "missing browser")  # type: ignore[arg-type]

    def test_gate_mode_fails_for_missing_browser(self) -> None:
        with pytest.raises(pytest.fail.Exception, match="missing browser"):
            _browser_unavailable(_BrowserConfig(gate=True), "missing browser")  # type: ignore[arg-type]


class TestLiveServer:
    """The fixture owns the full server lifecycle."""

    def test_serves_the_supplied_app(self, live_server: Any) -> None:
        base = live_server(_echo_app("hello from the harness"))

        with httpx.Client(base_url=base, timeout=10) as client:
            response = client.get("/")

        assert response.text == "hello from the harness"

    def test_binds_an_ephemeral_port(self, live_server: Any) -> None:
        """Hardcoded ports collide under parallel runs; port 0 does not."""
        base = live_server(_echo_app("x"))

        port = int(base.rsplit(":", 1)[1])

        assert port > 1024

    def test_two_apps_get_distinct_ports(self, live_server: Any) -> None:
        first = live_server(_echo_app("first"))
        second = live_server(_echo_app("second"))

        assert first != second
        with httpx.Client(base_url=second, timeout=10) as client:
            assert client.get("/").text == "second"


def test_server_is_torn_down() -> None:
    """A stopped server must release its listener and thread."""
    uvicorn = pytest.importorskip(
        "uvicorn", reason="uvicorn is required to serve browser tests"
    )

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        probe.bind(("127.0.0.1", 0))
        port = int(probe.getsockname()[1])

    config = uvicorn.Config(
        _echo_app("bye"), host="127.0.0.1", port=port, log_level="warning"
    )
    server = uvicorn.Server(config)
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()

    deadline = time.monotonic() + 30
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=1):
                break
        except OSError:
            time.sleep(0.05)

    server.should_exit = True
    thread.join(timeout=10)

    assert not thread.is_alive()
