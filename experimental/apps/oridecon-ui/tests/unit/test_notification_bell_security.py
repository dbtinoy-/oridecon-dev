"""Trust, identity, and accessibility contracts for NotificationBell."""

from __future__ import annotations

import re

import pytest

from oridecon.ui import Element
from oridecon.ui.core.trusted_html import TrustedHTML
from oridecon.ui.organisms.notification_bell import NotificationBell


class TestNotificationBellTrust:
    def test_generated_controller_has_specific_provenance(self) -> None:
        root = NotificationBell().render()
        script = root.children[-1]

        assert isinstance(script, Element)
        assert script.tag == "script"
        assert isinstance(script.children[0], TrustedHTML)
        assert script.children[0].source == (
            "generated NotificationBell Alpine controller"
        )

    @pytest.mark.parametrize(
        ("argument", "marker"),
        [
            ("sse_url", "new EventSource("),
            ("inbox_api_url", "await fetch("),
            ("mark_read_url", "const url = "),
            ("mark_all_read_url", "await fetch("),
        ],
    )
    def test_configured_urls_cannot_close_the_script(
        self,
        argument: str,
        marker: str,
    ) -> None:
        payload = "</script><img src=x onerror=window.pwned=true>"

        output = str(NotificationBell(**{argument: payload}))
        script_body = output.split("<script>", 1)[1].split("</script>", 1)[0]

        assert marker in script_body
        assert "<img" not in script_body
        assert "\\u003c/script\\u003e" in script_body

    def test_controller_uses_safe_runtime_message_rendering(self) -> None:
        output = str(NotificationBell())

        assert 'x-text="notification.title"' in output
        assert 'x-text="notification.message"' in output
        assert "innerHTML" not in output

    def test_runtime_message_ids_are_encoded_for_path_substitution(self) -> None:
        output = str(NotificationBell())

        assert "encodeURIComponent(String(id))" in output


class TestNotificationBellIdentity:
    def test_sibling_bells_receive_unique_ids_and_controllers(self) -> None:
        page = Element("main", NotificationBell(), NotificationBell())

        output = str(page)
        root_ids = re.findall(
            r'<div id="(oridecon-notification-bell-root-[^"]+)" x-data=', output
        )
        controllers = re.findall(
            r'x-data="(oridecon_notification_bell_root_[^"]+)"', output
        )
        all_ids = re.findall(r' id="([^"]+)"', output)

        assert root_ids == [
            "oridecon-notification-bell-root-1",
            "oridecon-notification-bell-root-2",
        ]
        assert len(controllers) == len(set(controllers)) == 2
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
            '<button type="button" x-on:click="markAsRead(notification.id)"' in output
        )
        assert '<button type="button" x-on:click="markAllRead()"' in output

    def test_status_error_and_optimistic_rollback_states_are_rendered(self) -> None:
        output = str(NotificationBell())

        assert "Loading notifications…" in output
        assert "Notifications could not be loaded." in output
        assert ">Retry</button>" in output
        assert 'x-on:click="loadInbox()"' in output
        assert "mutationError" in output
        assert "previousUnreadCount" in output
        assert "notification.read = false" in output

    def test_controller_registers_before_or_after_alpine_startup(self) -> None:
        output = str(NotificationBell())

        assert "if (window.Alpine) register();" in output
        assert "{ once: true }" in output
        assert "MutationObserver" not in output

    def test_escape_restores_focus_to_the_trigger(self) -> None:
        output = str(NotificationBell())

        assert "x-on:keydown.escape.window=" in output
        assert "$refs.trigger.focus()" in output

    def test_max_display_is_clamped_to_a_usable_minimum(self) -> None:
        output = str(NotificationBell(max_display=0))

        assert "this.notifications.length > 1" in output
        assert ")).slice(0, 1)" in output

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
