"""One response-wide UI render scope per admin request.

Every complete admin response — full document, page frame, or component
fragment — must receive exactly one root :class:`RenderScope` so DOM IDs,
zone identities, and once-per-response claims are unique across all
components rendered for that request. Standalone ``render_to_string`` calls
create their own throwaway scope, which silently reuses IDs when a controller
renders several components before composing the response.

This middleware is a pure-ASGI wrapper around the admin sub-app: it installs
a fresh ``RenderContext`` for the request task and restores the previous value
after the response is produced. Rendering happens synchronously inside the
ASGI call, so the context is active for every render path in the request.
"""

from __future__ import annotations

from starlette.types import ASGIApp, Receive, Scope, Send

from oridecon.ui import RenderContext, RenderScope, render_context


class AdminRenderScopeMiddleware:
    """Install the response-local UI render context for one admin request."""

    def __init__(self, app: ASGIApp) -> None:
        self._app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self._app(scope, receive, send)
            return

        with render_context(RenderContext(scope=RenderScope())):
            await self._app(scope, receive, send)


__all__ = ["AdminRenderScopeMiddleware"]
