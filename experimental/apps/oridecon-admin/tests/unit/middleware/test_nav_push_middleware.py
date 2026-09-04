"""Regression tests for body-navigation history middleware."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any
from unittest.mock import AsyncMock

import pytest

from oridecon.admin.middleware.nav_push import AdminNavPushMiddleware

ResponseHeaders = list[tuple[bytes, bytes]]


def _scope(
    *,
    method: str = "GET",
    path: str = "/users",
    root_path: str = "/admin",
    raw_path: bytes | None = b"/admin/users",
    query_string: bytes = b"",
    target: bytes | None = b"body",
) -> dict[str, Any]:
    headers: ResponseHeaders = [(b"hx-request", b"true")]
    if target is not None:
        headers.append((b"hx-target", target))
    scope: dict[str, Any] = {
        "type": "http",
        "method": method,
        "path": path,
        "root_path": root_path,
        "query_string": query_string,
        "headers": headers,
    }
    if raw_path is not None:
        scope["raw_path"] = raw_path
    return scope


async def _invoke(
    scope: dict[str, Any],
    *,
    status: int = 200,
    response_headers: ResponseHeaders | None = None,
) -> list[dict[str, Any]]:
    headers = (
        response_headers
        if response_headers is not None
        else [(b"content-type", b"text/html; charset=utf-8")]
    )

    async def app(
        app_scope: dict[str, Any],
        receive: Callable[..., Any],
        send: Callable[[dict[str, Any]], Any],
    ) -> None:
        await send(
            {
                "type": "http.response.start",
                "status": status,
                "headers": list(headers),
            }
        )
        await send({"type": "http.response.body", "body": b""})

    messages: list[dict[str, Any]] = []

    async def send(message: dict[str, Any]) -> None:
        messages.append(message)

    await AdminNavPushMiddleware(app)(scope, AsyncMock(), send)
    return messages


def _history_headers(messages: list[dict[str, Any]]) -> list[bytes]:
    start = messages[0]
    return [value for name, value in start["headers"] if name.lower() == b"hx-push-url"]


class TestAdminNavPushMiddleware:
    """History URLs must preserve exact request state without duplicate headers."""

    async def test_raw_path_keeps_query_string(self) -> None:
        messages = await _invoke(_scope(query_string=b"page=2&sort_by=name%20asc"))

        assert _history_headers(messages) == [b"/admin/users?page=2&sort_by=name%20asc"]

    async def test_fallback_combines_root_path_path_and_query(self) -> None:
        messages = await _invoke(
            _scope(
                path="/users",
                root_path="/ops/console",
                raw_path=None,
                query_string=b"filter=active",
            )
        )

        assert _history_headers(messages) == [b"/ops/console/users?filter=active"]

    async def test_encoded_raw_path_is_preserved(self) -> None:
        messages = await _invoke(
            _scope(
                raw_path=b"/admin/users/caf%C3%A9",
                query_string=b"return_to=%2Fadmin%2F",
            )
        )

        assert _history_headers(messages) == [
            b"/admin/users/caf%C3%A9?return_to=%2Fadmin%2F"
        ]

    async def test_existing_header_is_replaced_case_insensitively(self) -> None:
        messages = await _invoke(
            _scope(query_string=b"page=3"),
            response_headers=[
                (b"content-type", b"text/html"),
                (b"HX-Push-Url", b"/stale"),
                (b"hx-push-url", b"/also-stale"),
                (b"set-cookie", b"a=1"),
                (b"set-cookie", b"b=2"),
            ],
        )

        assert _history_headers(messages) == [b"/admin/users?page=3"]
        assert [
            value
            for name, value in messages[0]["headers"]
            if name.lower() == b"set-cookie"
        ] == [b"a=1", b"b=2"]

    @pytest.mark.parametrize(
        ("scope", "status", "headers"),
        [
            (_scope(method="POST"), 200, [(b"content-type", b"text/html")]),
            (_scope(), 302, [(b"content-type", b"text/html")]),
            (_scope(), 200, [(b"content-type", b"application/json")]),
        ],
    )
    async def test_ineligible_response_has_no_history_header(
        self,
        scope: dict[str, Any],
        status: int,
        headers: ResponseHeaders,
    ) -> None:
        messages = await _invoke(scope, status=status, response_headers=headers)

        assert _history_headers(messages) == []

    @pytest.mark.parametrize("target", [b"main-content", b"#main-content"])
    async def test_main_content_target_gets_navigation_contract(
        self, target: bytes
    ) -> None:
        """The client navigator receives push URL + declared swap target."""
        messages = await _invoke(_scope(target=target))

        assert _history_headers(messages) == [b"/admin/users"]
        start = messages[0]
        headers = {name: value for name, value in start["headers"]}
        assert headers[b"hx-target"] == b"#main-content"

    async def test_main_content_contract_preserves_unrelated_headers(self) -> None:
        messages = await _invoke(
            _scope(target=b"main-content"),
            response_headers=[
                (b"content-type", b"text/html"),
                (b"x-admin-title", b"Users"),
                (b"set-cookie", b"a=1"),
                (b"set-cookie", b"b=2"),
            ],
        )

        start = messages[0]
        headers = {name: value for name, value in start["headers"]}
        assert headers[b"hx-push-url"] == b"/admin/users"
        assert headers[b"hx-target"] == b"#main-content"
        assert headers[b"x-admin-title"] == b"Users"
        assert [
            value
            for name, value in start["headers"]
            if name.lower() == b"set-cookie"
        ] == [b"a=1", b"b=2"]
