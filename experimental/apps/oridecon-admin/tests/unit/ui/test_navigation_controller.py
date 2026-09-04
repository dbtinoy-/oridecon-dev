"""Navigation-ownership contract (slice 4: one navigation controller).

The admin shell must have exactly one client-side navigation owner. Plain
link clicks and command-palette commands route through
``window.OrideconNavigator``, and the server declares the swap target and
title on the response so the owner can apply the lifecycle (abort stale
widget loads, title, scroll reset, focus/announcement, auth expiry,
history) without duplicating it in every component.
"""

from __future__ import annotations

from oridecon.admin.ui.organisms.command_palette import CommandPalette
from oridecon.admin.ui.templates.shell_scripts import (
    admin_navigator_script,
    search_overlay_markup,
)
from oridecon.ui import render_to_string


class TestNavigatorScript:
    """The shell ships exactly one navigation controller."""

    def test_single_owner_registered(self) -> None:
        html = render_to_string(admin_navigator_script())

        assert "window.OrideconNavigator = navigator" in html
        assert "window.__orideconAdminNavigatorInit" in html

    def test_routes_through_main_content_swap(self) -> None:
        html = render_to_string(admin_navigator_script())

        assert "target: MAIN_CONTENT_SELECTOR" in html
        assert "swap: 'innerHTML'" in html

    def test_lifecycle_handlers_present(self) -> None:
        html = render_to_string(admin_navigator_script())

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
        html = render_to_string(admin_navigator_script())

        assert "navigator.navigate(url.href)" in html
        assert "window.scrollTo(0, 0)" not in html.split("navigator = {")[0]


class TestShellScriptsDelegation:
    """The legacy body-swap hook must no longer own navigation."""

    def test_search_overlay_no_longer_issues_body_swap(self) -> None:
        html = render_to_string(search_overlay_markup())

        assert "SPA navigation is owned by window.OrideconNavigator" in html
        assert "target: 'body'" not in html
        assert "window.scrollTo(0, 0);" not in html

    def test_settings_panel_history_sync_remains(self) -> None:
        html = render_to_string(search_overlay_markup())

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

        assert "window.OrideconNavigator.navigate(destination)" in html
        # No second history owner. The htmx.ajax fallback is allowed only as
        # the no-navigator escape hatch, never as the primary path.
        assert "window.history.pushState" not in html
        primary = html.index("if (window.OrideconNavigator)")
        fallback = html.index("htmx.ajax('GET', destination")
        assert primary < fallback
        assert html.count("htmx.ajax('GET', destination") == 1

    def test_palette_keeps_safe_navigation_check(self) -> None:
        html = render_to_string(
            CommandPalette(
                commands=[{"label": "X", "href": "https://evil.example"}],
                command_palette_key="test2",
            )
        )

        assert "safeNavigationUrl" in html
