"""Self-contained browser-test infrastructure for the admin UI.

The harness owns a real ASGI server on a pre-bound ephemeral socket and a
fresh Playwright context for each test. Browser tests remain opt-in for local
unit-test runs, while ``--browser-gate`` turns missing runtime dependencies
into failures so CI cannot report a green browser job that only skipped.
"""

from __future__ import annotations

from collections.abc import Iterator
import socket
import threading
import time
from typing import Any, NoReturn

import pytest

_STARTUP_TIMEOUT_S = 30.0
_POLL_INTERVAL_S = 0.05
_BROWSER_INSTALL = "uv run playwright install chromium"


def pytest_addoption(parser: pytest.Parser) -> None:
    """Register local opt-in and required-gate browser modes."""
    parser.addoption(
        "--run-browser",
        action="store_true",
        default=False,
        help="Run Playwright browser tests (requires installed browsers)",
    )
    parser.addoption(
        "--browser-gate",
        action="store_true",
        default=False,
        help="Run browser tests and fail, rather than skip, if tooling is missing",
    )


def pytest_configure(config: pytest.Config) -> None:
    """Declare the marker so strict-marker runs do not error."""
    config.addinivalue_line(
        "markers", "browser: browser test (skipped unless explicitly enabled)"
    )


def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    """Skip browser-marked tests unless local or gate mode is enabled."""
    if config.getoption("--run-browser", default=False) or config.getoption(
        "--browser-gate", default=False
    ):
        return

    skip = pytest.mark.skip(
        reason="Browser tests skipped: pass --run-browser (or --browser-gate in CI)"
    )
    for item in items:
        if item.get_closest_marker("browser"):
            item.add_marker(skip)


def _browser_unavailable(config: pytest.Config, reason: str) -> NoReturn:
    """Report unavailable browser tooling according to the selected mode."""
    if config.getoption("--browser-gate", default=False):
        pytest.fail(reason, pytrace=False)
    pytest.skip(reason)


def _bind_ephemeral_socket(host: str) -> socket.socket:
    """Reserve a listener so no process can steal the selected port."""
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind((host, 0))
    listener.listen(socket.SOMAXCONN)
    return listener


def _wait_until_started(server: Any, thread: threading.Thread) -> None:
    """Wait for Uvicorn lifespan startup without probing an unready socket."""
    deadline = time.monotonic() + _STARTUP_TIMEOUT_S
    while time.monotonic() < deadline:
        if server.started:
            return
        if not thread.is_alive():
            pytest.fail("Browser test server exited before startup", pytrace=False)
        time.sleep(_POLL_INTERVAL_S)
    pytest.fail("Browser test server did not finish startup", pytrace=False)


@pytest.fixture(scope="session")
def browser_type(pytestconfig: pytest.Config) -> Iterator[Any]:
    """Launch headless Chromium, failing hard when required by the CI gate."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        _browser_unavailable(
            pytestconfig,
            "Playwright is not installed; sync the tooling and QA dependency groups",
        )

    with sync_playwright() as api:
        try:
            browser = api.chromium.launch(headless=True)
        except Exception as exc:  # noqa: BLE001 - dependency errors vary by platform
            _browser_unavailable(
                pytestconfig,
                "Chromium is not available. Run "
                f"'{_BROWSER_INSTALL}'. Underlying error: {type(exc).__name__}",
            )
        try:
            yield browser
        finally:
            browser.close()


@pytest.fixture
def page(browser_type: Any) -> Iterator[Any]:
    """Return a page in a fresh context so tests never share browser state."""
    context = browser_type.new_context()
    page = context.new_page()
    try:
        yield page
    finally:
        context.close()


@pytest.fixture
def live_server() -> Iterator[Any]:
    """Yield an ASGI server factory with race-free ephemeral ports."""
    try:
        import uvicorn
    except ImportError:
        pytest.fail("uvicorn is required to serve browser tests", pytrace=False)

    servers: list[Any] = []
    threads: list[threading.Thread] = []
    listeners: list[socket.socket] = []

    def _start(app: Any, host: str = "127.0.0.1") -> str:
        listener = _bind_ephemeral_socket(host)
        port = int(listener.getsockname()[1])
        config = uvicorn.Config(
            app, host=host, port=port, log_level="warning", lifespan="on"
        )
        server = uvicorn.Server(config)
        thread = threading.Thread(
            target=server.run,
            kwargs={"sockets": [listener]},
            daemon=True,
        )

        servers.append(server)
        threads.append(thread)
        listeners.append(listener)
        thread.start()
        _wait_until_started(server, thread)
        return f"http://{host}:{port}"

    try:
        yield _start
    finally:
        for server in servers:
            server.should_exit = True
        for thread in threads:
            thread.join(timeout=10.0)
        for listener in listeners:
            listener.close()
        leaked = [thread.name for thread in threads if thread.is_alive()]
        if leaked:
            pytest.fail(
                f"Browser test server threads did not stop: {', '.join(leaked)}",
                pytrace=False,
            )
