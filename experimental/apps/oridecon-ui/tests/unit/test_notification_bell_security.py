"""Markup + runtime contracts for NotificationBell after the CSP v2 migration.

The Alpine controller no longer ships as a per-instance inline ``<script>``;
it lives once in the generated bundle ``static/js/admin-shell.js``
(source of truth: ``dev/generators/admin_shell_assets.py``) and is bound
statically as ``notificationBell``. Per-instance configuration arrives via
``data-*`` attributes, so the markup contract is attribute-level and the
runtime contract is asserted against the generated asset.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from oridecon.ui import Element
from oridecon.ui.organisms.notification_bell import NotificationBell

_SHELL_JS = (
    Path(__file__).parents[3]
    / "oridecon-admin"
    / "src"
    / "oridecon"
    / "admin"
    / "static"
    / "js"
    / "admin-shell.js"
)


def _shell_js() -> str:
    return _SHELL_JS.read_text(encoding="utf-8")


class TestNotificationBellTrust:
    def test_markup_is_script_free_and_binds_static_controller(self) -> None:
        output = str(NotificationBell())

        assert 'x-data="notificationBell"' in output
        assert "<script" not in output
        assert "onclick=" not in output

    @pytest.mark.parametrize(
        ("argument", "attribute", "marker_in_asset"),
        [
            ("sse_url", "data-sse-url", "new EventSource(config.sseUrl)"),
            ("inbox_api_url", "data-inbox-api-url", "fetch(config.inboxApiUrl"),
            (
                "mark_read_url",
                "data-mark-read-url",
                "config.markReadUrl.replace(",
            ),
            ("mark_all_read_url", "data-mark-all-read-url", "fetch(config.markAllReadUrl, {"),
        ],
    )
    def test_configured_urls_are_escaped_data_attributes(
        self,
        argument: str,
        attribute: str,
        marker_in_asset: str,
    ) -> None:
        payload = '"><img src=x onerror=window.pwned=true>'
        output = str(NotificationBell(**{argument: payload}))

        assert attribute in output
        # The payload is inert attribute text: no element can be opened and
        # the markup metacharacters are escaped.
        assert "<img" not in output
        assert "&lt;img" in output
        assert marker_in_asset in _shell_js()

    def test_controller_uses_safe_runtime_message_rendering(self) -> None:
        output = str(NotificationBell())

        assert 'x-text="notification.title"' in output
        assert 'x-text="notification.message"' in output
        assert "innerHTML" not in output

    def test_runtime_message_ids_are_encoded_for_path_substitution(self) -> None:
        controller = _shell_js()

        assert "encodeURIComponent(String(id))" in controller


class TestNotificationBellIdentity:
    def test_sibling_bells_receive_unique_ids_and_share_the_controller(self) -> None:
        page = Element("main", NotificationBell(), NotificationBell())

        output = str(page)
        root_ids = re.findall(
            r'<div id="(oridecon-notification-bell-root-[^"]+)" x-data=', output
        )
        controllers = re.findall(r'x-data="([^"]+)"', output)
        all_ids = re.findall(r' id="([^"]+)"', output)

        assert root_ids == [
            "oridecon-notification-bell-root-1",
            "oridecon-notification-bell-root-2",
        ]
        # One static Alpine name; the ids remain unique per instance.
        assert controllers == ["notificationBell", "notificationBell"]
        assert len(all_ids) == len(set(all_ids)) == 8

    def test_explicit_key_is_stable_across_partial_renders(self) -> None:
        first = str(NotificationBell(notification_key="topbar"))
        second = str(NotificationBell(notification_key="topbar"))

        assert 'id="oridecon-notification-bell-root-topbar"' in first
        assert first == second

    def test_duplicate_keys_fail_in_one_render_tree(self) -> None:
        page = Element(
            "main",
            NotificationBell(notification_key="topbar"),
            NotificationBell(notification_key="topbar"),
        )

        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            str(page)

    def test_trigger_panel_and_heading_are_linked(self) -> None:
        output = str(NotificationBell())
        trigger_id = re.search(r'<button[^>]* id="([^"]+)"', output)
        panel_id = re.search(r'<div[^>]* id="([^"]+)" role="dialog"', output)
        heading_id = re.search(r'<h3[^>]* id="([^"]+)"', output)

        assert trigger_id is not None
        assert panel_id is not None
        assert heading_id is not None
        assert f'aria-controls="{panel_id.group(1)}"' in output
        assert f'aria-labelledby="{heading_id.group(1)}"' in output


class TestNotificationBellExperience:
    def test_notification_rows_and_header_actions_are_buttons(self) -> None:
        output = str(NotificationBell())

        assert (
            '<button type="button" x-on:click="markAsRead(notification.id)"'
            in output
        )
        assert '<button type="button" x-on:click="markAllRead()"' in output

    def test_status_error_and_optimistic_rollback_states_are_rendered(self) -> None:
        output = str(NotificationBell())
        controller = _shell_js()

        assert "Loading notifications…" in output
        assert "Notifications could not be loaded." in controller
        assert ">Retry</button>" in output
        assert 'x-on:click="loadInbox()"' in output
        assert "mutationError" in controller
        assert "previousUnreadCount" in controller
        assert "notification.read = false" in controller

    def test_controller_registers_before_or_after_alpine_startup(self) -> None:
        controller = _shell_js()

        assert "if (window.Alpine) register();" in controller
        assert "{ once: true }" in controller
        assert "MutationObserver" not in controller

    def test_escape_restores_focus_to_the_trigger(self) -> None:
        output = str(NotificationBell())

        assert "x-on:keydown.escape.window=" in output
        assert "$refs.trigger.focus()" in output

    def test_max_display_is_clamped_to_a_usable_minimum(self) -> None:
        output = str(NotificationBell(max_display=0))
        controller = _shell_js()

        assert 'data-max-display="1"' in output
        assert "this.notifications.length > maxDisplay" in controller
        assert "Number(data.maxDisplay) > 0" in controller

    def test_root_props_are_preserved_but_controller_wiring_is_protected(self) -> None:
        output = str(
            NotificationBell(
                id="alerts",
                class_="custom-bell",
                data_testid="alerts",
                x_data="untrustedController",
                data_csrf_token="wrong",
                csrf_token="correct",
            )
        )

        assert 'id="alerts"' in output
        assert 'class="relative custom-bell"' in output
        assert 'data-testid="alerts"' in output
        assert 'x-data="untrustedController"' not in output
        assert 'data-csrf-token="correct"' in output
        assert output.count("data-csrf-token=") == 1
        assert " notification-key=" not in output
