"""Server-side navigation contract for main-content partials (slice 4).

When an HTMX request targets ``main-content``, the admin controller must
return only the fragment and declare the navigation contract the client
controller applies: the swap target and the document title.
"""

from __future__ import annotations

import asyncio
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock

from starlette.responses import HTMLResponse

from oridecon.admin.controllers.base import AdminController


def _request() -> MagicMock:
    request = MagicMock()
    request.state = SimpleNamespace(container=MagicMock(), user=None, tenant_id=None)
    request.session = {}
    request.headers = {"HX-Request": "true", "HX-Target": "main-content"}
    request.cookies = {}
    request.app.state = SimpleNamespace(
        nav_builder=None,
        assembler_nav_items=[],
        assembler_groups=None,
        cluster_registry=None,
    )
    # Force theme/tenant/CSRF hooks to be best-effort no-ops.
    request.state.container.resolve = AsyncMock(side_effect=RuntimeError("no di"))
    return request


def _controller() -> AdminController:
    renderer = MagicMock()
    renderer.render_partial.return_value = HTMLResponse("<h1>Users</h1>")
    renderer.render_page.return_value = HTMLResponse("<html>full</html>")
    return AdminController(renderer=renderer)


def test_main_content_htmx_gets_fragment_with_contract_headers() -> None:
    controller = _controller()
    response = asyncio.run(
        controller.render_admin(
            _request(),
            content="<h1>Users</h1>",
            title="Users | Admin",
        )
    )

    assert response.body == b"<h1>Users</h1>"
    assert response.headers["hx-target"] == "#main-content"
    assert response.headers["x-admin-title"] == "Users | Admin"
    controller.renderer.render_partial.assert_called_once()
    controller.renderer.render_page.assert_not_called()


def test_plain_htmx_target_keeps_full_page() -> None:
    request = _request()
    request.headers = {"HX-Request": "true", "HX-Target": "search-results"}
    controller = _controller()

    response = asyncio.run(
        controller.render_admin(request, content="<h1>Users</h1>", title="Users")
    )

    assert response.body == b"<html>full</html>"
    controller.renderer.render_partial.assert_not_called()


def test_title_omitted_header_not_set() -> None:
    controller = _controller()
    response = asyncio.run(
        controller.render_admin(_request(), content="<h1>Users</h1>", title="")
    )

    assert response.headers["hx-target"] == "#main-content"
    assert "x-admin-title" not in response.headers
