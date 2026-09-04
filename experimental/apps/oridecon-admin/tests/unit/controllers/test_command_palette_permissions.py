"""Tests for command palette permission filtering (audit F1/F2)."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, call

import pytest
from starlette.datastructures import QueryParams
from starlette.requests import Request

from oridecon.admin.controllers.command_palette import CommandPaletteController
from oridecon.admin.services.search_service import SearchService
from oridecon.serialization import loads_str


class PermissionsUsersResource:
    """Searchable resource the fixture authorizer admits."""

    name = "users"
    label = "Users"
    search_fields = ["name"]

    @classmethod
    async def search(cls, query: str, *, limit: int = 5) -> list[dict]:
        return [{"id": 1, "title": "Alice", "subtitle": "alice@example.com"}]


class PermissionsPostsResource:
    """Searchable resource the fixture authorizer denies."""

    name = "posts"
    label = "Posts"
    search_fields = ["title"]

    @classmethod
    async def search(cls, query: str, *, limit: int = 5) -> list[dict]:
        return [{"id": 10, "title": "Hello World"}]


def _manager() -> MagicMock:
    manager = MagicMock()
    manager.get_all_resources = MagicMock(
        return_value=[PermissionsUsersResource, PermissionsPostsResource]
    )
    return manager


class TestCommandPalettePermissions:
    """Palette JSON must never disclose denied-resource records."""

    @pytest.fixture
    def authorizer(self) -> AsyncMock:
        authorizer = AsyncMock()
        authorizer.can_view.side_effect = lambda _user, name: {
            "users": True,
            "posts": False,
        }.get(name, False)
        return authorizer

    @pytest.fixture
    def service(self, authorizer: AsyncMock) -> SearchService:
        return SearchService(resource_manager=_manager(), authorizer=authorizer)

    @pytest.fixture
    def controller(self, service: SearchService) -> CommandPaletteController:
        return CommandPaletteController(search_service=service)

    def _request(self, query: str) -> MagicMock:
        request = MagicMock(spec=Request)
        request.query_params = QueryParams(q=query)
        request.state.user = {"id": "u1"}
        return request

    async def test_denied_resource_absent_from_json(
        self, controller: CommandPaletteController, authorizer: AsyncMock
    ) -> None:
        response = await controller.search(self._request("alice"))
        commands = loads_str(response.body.decode())
        labels = [c["label"] for c in commands]
        assert "Users: Alice" in labels
        assert "Posts: Hello World" not in labels
        assert all(c.get("href") != "/admin/posts/10" for c in commands)
        assert authorizer.can_view.await_args_list == [
            call({"id": "u1"}, "users"),
            call({"id": "u1"}, "posts"),
        ]

    async def test_missing_principal_cannot_receive_dynamic_results(
        self, controller: CommandPaletteController, authorizer: AsyncMock
    ) -> None:
        request = self._request("alice")
        request.state.user = None

        response = await controller.search(request)

        assert loads_str(response.body.decode()) == []
        authorizer.can_view.assert_not_awaited()

    async def test_all_denied_does_not_restore_privileged_static_commands(
        self,
    ) -> None:
        authorizer = AsyncMock()
        authorizer.can_view.side_effect = lambda *_args: False
        controller = CommandPaletteController(
            search_service=SearchService(
                resource_manager=_manager(),
                authorizer=authorizer,
            )
        )

        response = await controller.search(self._request("users"))
        commands = loads_str(response.body.decode())
        labels = [c["label"] for c in commands]

        assert "Manage Users" not in labels
        assert "Users: Alice" not in labels
        assert "Posts: Hello World" not in labels
        assert commands == []

    async def test_unrestricted_static_commands_remain_for_restricted_user(
        self, controller: CommandPaletteController
    ) -> None:
        response = await controller.search(self._request(""))
        commands = loads_str(response.body.decode())
        labels = [c["label"] for c in commands]

        assert "Go to Dashboard" in labels
        assert "Toggle Dark Mode" in labels
        assert "Manage Users" in labels
        assert "Settings" not in labels

    async def test_short_queries_filter_matching_privileged_commands(
        self, controller: CommandPaletteController, authorizer: AsyncMock
    ) -> None:
        response = await controller.search(self._request("s"))
        commands = loads_str(response.body.decode())
        labels = [c["label"] for c in commands]

        assert "Manage Users" in labels
        assert "Settings" not in labels
        assert call({"id": "u1"}, "settings") in authorizer.can_view.await_args_list
