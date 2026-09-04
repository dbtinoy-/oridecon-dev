"""Controller for the command palette endpoint."""

from __future__ import annotations

from typing import Any

from starlette.requests import Request
from starlette.responses import JSONResponse

from oridecon.admin.resources.urls import admin_prefix_from_request, mount_admin_url
from oridecon.admin.services.search_service import SearchService
from oridecon.di.decorators import inject
from oridecon.logging import get_logger

logger = get_logger(__name__)

_STATIC_COMMANDS: list[dict[str, Any]] = [
    {"label": "Go to Dashboard", "href": "/admin/", "icon": "home", "shortcut": "G D"},
    {
        "label": "Manage Users",
        "href": "/admin/users",
        "icon": "users",
        "shortcut": "G U",
        "required_resource": "users",
    },
    {
        "label": "Toggle Dark Mode",
        "action": "darkMode = !darkMode",
        "icon": "moon",
        "shortcut": "T D",
    },
    {
        "label": "Settings",
        "href": "/admin/settings",
        "icon": "settings",
        "shortcut": ",",
        "required_resource": "settings",
    },
]

_MIN_QUERY_LENGTH = 2


@inject
class CommandPaletteController:
    """Handles the command palette search endpoint.

    Returns JSON commands that the frontend merges with static commands.
    """

    def __init__(self, search_service: SearchService) -> None:
        self._search_service = search_service

    async def search(self, request: Request) -> JSONResponse:
        """Handle GET /admin/command-palette?q=..."""
        query = (request.query_params.get("q") or "").strip()
        commands: list[dict[str, Any]] = []

        admin_prefix = admin_prefix_from_request(request)
        user = getattr(request.state, "user", None)

        # Filter static commands by query and the same authorizer used for
        # dynamic resources. Navigation visibility is not endpoint security,
        # but the palette must not advertise privileged areas to principals
        # that cannot view them.
        for original in _STATIC_COMMANDS:
            if query and query.lower() not in original["label"].lower():
                continue

            required_resource = original.get("required_resource")
            if required_resource:
                try:
                    if not await self._search_service.can_view_resource(
                        user, required_resource
                    ):
                        continue
                except Exception:  # noqa: BLE001 — command fails closed
                    logger.exception(
                        "Command palette authorization failed for resource=%s",
                        required_resource,
                    )
                    continue

            cmd = {
                key: value
                for key, value in original.items()
                if key != "required_resource"
            }
            if cmd.get("href"):
                cmd["href"] = mount_admin_url(cmd["href"], admin_prefix)
            commands.append(cmd)

        # Dynamic search results from backend
        if len(query) >= _MIN_QUERY_LENGTH:
            try:
                allowed = await self._search_service.allowed_resources_for(user)
                results = await self._search_service.search(
                    query, allowed_resources=allowed
                )
                for r in results.results:
                    commands.append(
                        {
                            "label": f"{r.resource_label}: {r.title}",
                            "href": mount_admin_url(r.url, admin_prefix),
                            "icon": "search",
                            "subtitle": r.subtitle,
                        }
                    )
            except Exception:
                logger.exception("Command palette search failed for query=%s", query)

        return JSONResponse(commands)
