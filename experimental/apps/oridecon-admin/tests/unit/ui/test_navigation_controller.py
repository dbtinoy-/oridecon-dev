"""Navigation-ownership contract (slice 4: one navigation controller).

The admin shell must have exactly one client-side navigation owner. Plain
link clicks and command-palette commands route through
``window.OrideconNavigator``, and the server declares the swap target and
title on the response so the owner can apply the lifecycle (abort stale
widget loads, title, scroll reset, focus/announcement, auth expiry,
history) without duplicating it in every component.

Since the CSP v2 migration the shell scripts ship as the generated static
asset ``static/js/admin-shell.js`` (source of truth:
``dev/generators/admin_shell_assets.py``), so the contracts are asserted
against that file rather than ``render_to_string`` of inline script markup.
"""

from __future__ import annotations

from pathlib import Path

from oridecon.admin.ui.organisms.command_palette import CommandPalette
from oridecon.ui import render_to_string

_SHELL_JS = (
    Path(__file__).parents[3]
    / "src"
    / "oridecon"
    / "admin"
    / "static"
    / "js"
    / "admin-shell.js"
)


def _shell_js() -> str:
    return _SHELL_JS.read_text(encoding="utf-8")


class TestNavigatorScript:
    """The shell ships exactly one navigation controller."""

    def test_single_owner_registered(self) -> None:
        html = _shell_js()

        assert "window.OrideconNavigator = navigator" in html
        assert "window.__orideconAdminNavigatorInit" in html

    def test_routes_through_main_content_swap(self) -> None:
        html = _shell_js()

        assert "target: MAIN_CONTENT_SELECTOR" in html
        assert "swap: 'innerHTML'" in html

    def test_lifecycle_handlers_present(self) -> None:
        html = _shell_js()

        # Abort stale widget loads owned by the page being left.
        assert ".widget-body[hx-get]" in html
        assert "htmx:abort" in html
        # Title from the server contract.
        assert "X-Admin-Title" in html
        # Scroll reset + focus + announcement.
        assert "SCROLL_SELECTOR" in html
        assert "main.focus" in html
        assert "oridecon:nav:complete" in html
        # Auth expiry redirect.
        assert "onResponseError" in html
        assert "window.location.assign(loginUrl)" in html
        # History is owned here, not in the palette.
        assert "onPopState" in html

    def test_link_interception_uses_navigator(self) -> None:
        html = _shell_js()

        assert "navigator.navigate(url.href)" in html
        assert "window.scrollTo(0, 0)" not in html.split("navigator = {")[0]


class TestShellScriptsDelegation:
    """The legacy body-swap hook must no longer own navigation."""

    def test_search_overlay_no_longer_issues_body_swap(self) -> None:
        html = _shell_js()
        # Scope to the search-overlay section; the navigator legitimately
        # scrolls to the top after a content swap.
        search_section = html.split("Search overlay + settings panel nav sync")[1]
        search_section = search_section.split("Navigation controller")[0]

        assert "SPA navigation is owned by window.OrideconNavigator" in search_section
        assert "target: 'body'" not in search_section
        assert "window.scrollTo(0, 0);" not in search_section

    def test_settings_panel_history_sync_remains(self) -> None:
        html = _shell_js()

        assert "syncSettingsPanelNavigation" in html
        assert "htmx:pushedIntoHistory" in html
        assert "window.addEventListener('popstate'" in html


class TestCommandPaletteDelegation:
    """Palette commands must not own a second navigation path."""

    def test_rendered_controller_has_no_direct_history_push(self) -> None:
        palette = CommandPalette(
            commands=[
                {"label": "Users", "href": "/admin/users", "icon": "users"},
            ],
            command_palette_key="test",
        )
        html = render_to_string(palette)

        assert "window.OrideconNavigator.navigate(destination)" in _shell_js()
        # The palette markup carries only a non-executable JSON data island;
        # the controller is a static asset, so no inline executable script.
        assert "type=\"application/json\"" in html
        assert "<script>" not in html
        assert "window.history.pushState" not in html
        primary = _shell_js().index("if (window.OrideconNavigator)")
        fallback = _shell_js().index("htmx.ajax('GET', destination")
        assert primary < fallback
        assert _shell_js().count("htmx.ajax('GET', destination") == 1

    def test_palette_keeps_safe_navigation_check(self) -> None:
        html = render_to_string(
            CommandPalette(
                commands=[{"label": "X", "href": "https://evil.example"}],
                command_palette_key="test2",
            )
        )

        assert "safeNavigationUrl" in _shell_js()
        assert "application/json" in html
