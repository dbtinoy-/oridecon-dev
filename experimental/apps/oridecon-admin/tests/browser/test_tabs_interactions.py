"""Real-browser keyboard and state checks for the shared Tabs primitive."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from starlette.applications import Starlette
from starlette.responses import FileResponse, HTMLResponse
from starlette.routing import Route

from oridecon.ui.molecules.tabs import TabPanel, Tabs

pytestmark = pytest.mark.browser

_ALPINE_FILE = (
    Path(__file__).resolve().parents[2] / "src/oridecon/admin/static/js/alpine.min.js"
)


def _app() -> Starlette:
    tabs = Tabs(
        [("Profile", "profile"), ("Security", "security"), ("Audit", "audit")],
        tabs_id="browser-tabs",
        children=[
            TabPanel("profile", "Profile panel"),
            TabPanel("security", "Security panel"),
            TabPanel("audit", "Audit panel"),
        ],
    )

    async def index(request: Any) -> HTMLResponse:
        return HTMLResponse(
            "<!doctype html><html><head>"
            '<script defer src="/static/alpine.min.js"></script>'
            "</head><body>"
            f"{tabs}"
            "</body></html>"
        )

    async def alpine(request: Any) -> FileResponse:
        return FileResponse(_ALPINE_FILE, media_type="application/javascript")

    return Starlette(
        routes=[
            Route("/", index),
            Route("/static/alpine.min.js", alpine),
        ]
    )


@pytest.fixture
def tabs_page(live_server: Any, page: Any) -> Any:
    page.goto(live_server(_app()), wait_until="load")
    page.wait_for_function(
        "() => document.querySelector('#browser-tabs')._x_dataStack !== undefined"
    )
    return page


def test_arrow_keys_move_focus_and_activate(tabs_page: Any) -> None:
    first = tabs_page.locator("#browser-tabs-tab-0")
    first.focus()
    first.press("ArrowRight")

    tabs_page.wait_for_function(
        "() => document.activeElement.id === 'browser-tabs-tab-1'"
    )
    assert (
        tabs_page.locator("#browser-tabs-tab-1").get_attribute("aria-selected")
        == "true"
    )
    assert tabs_page.locator("#browser-tabs-panel-1").is_visible()
    assert tabs_page.locator("#browser-tabs-panel-0").is_hidden()


def test_arrow_keys_wrap(tabs_page: Any) -> None:
    first = tabs_page.locator("#browser-tabs-tab-0")
    first.focus()
    first.press("ArrowLeft")

    tabs_page.wait_for_function(
        "() => document.activeElement.id === 'browser-tabs-tab-2'"
    )
    assert tabs_page.locator("#browser-tabs-tab-2").get_attribute("tabindex") == "0"


def test_home_and_end_move_to_boundaries(tabs_page: Any) -> None:
    middle = tabs_page.locator("#browser-tabs-tab-1")
    middle.focus()
    middle.press("End")
    tabs_page.wait_for_function(
        "() => document.activeElement.id === 'browser-tabs-tab-2'"
    )

    tabs_page.locator("#browser-tabs-tab-2").press("Home")
    tabs_page.wait_for_function(
        "() => document.activeElement.id === 'browser-tabs-tab-0'"
    )
    assert tabs_page.locator("#browser-tabs-panel-0").is_visible()
