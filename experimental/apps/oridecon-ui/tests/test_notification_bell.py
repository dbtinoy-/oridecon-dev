"""Render tests for the NotificationBell Alpine component (CSP v2 layout).

The controller is a static asset (``static/js/admin-shell.js``) bound as
``notificationBell``; markup carries only data-attribute configuration.
"""

from __future__ import annotations

from pathlib import Path

_SHELL_JS = (
    Path(__file__).parents[2]
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


def test_bell_renders_badge_and_alpine_root() -> None:
    """Bell should be an Alpine component with an unread count badge."""
    from oridecon.ui import NotificationBell

    bell = NotificationBell()
    html = str(bell)

    assert 'x-data="notificationBell"' in html
    assert "x-init" in html
    assert "unreadCount &gt; 0" in html
    assert "99+" in html
    assert 'aria-label="Notifications"' in html
    assert "<script" not in html


def test_bell_renders_notification_list_and_empty_state() -> None:
    """Dropdown should iterate notifications and show an empty state."""
    from oridecon.ui import NotificationBell

    html = str(NotificationBell())

    assert "x-for" in html
    assert "notification.title" in html
    assert "notification.message" in html
    assert "notifications.length === 0" in html
    assert "No new notifications" in html


def test_bell_wires_mark_read_handlers() -> None:
    """Bell should render mark-as-read and mark-all-read handlers."""
    from oridecon.ui import NotificationBell

    html = str(NotificationBell())

    assert "markAsRead" in html
    assert "markAllRead" in html
    assert "Mark all read" in html
    assert "unreadCount = Math.max(0, this.unreadCount - 1)" in _shell_js()


def test_bell_connects_to_sse_endpoint() -> None:
    """Config arrives as escaped data attributes; the controller consumes them."""
    from oridecon.ui import NotificationBell

    bell = NotificationBell(sse_url="/custom/events")
    html = str(bell)
    controller = _shell_js()

    assert 'data-sse-url="/custom/events"' in html
    assert "addEventListener('message'" in controller
    assert "addEventListener('notification'" in controller
    assert "addEventListener('toast'" in controller


def test_bell_loads_persisted_inbox() -> None:
    """Bell should fetch the persisted inbox on init."""
    from oridecon.ui import NotificationBell

    html = str(NotificationBell())
    controller = _shell_js()

    assert "loadInbox()" in html
    assert "fetch(config.inboxApiUrl" in controller
    assert "'X-Requested-With': 'fetch'" in controller
    assert "data.unread_count" in controller
    assert "data.notifications" in controller


def test_bell_posts_mark_read_to_inbox_endpoints() -> None:
    """Bell should POST mark-read and mark-all-read to the endpoints."""
    from oridecon.ui import NotificationBell

    bell = NotificationBell(
        mark_read_url="/custom/read/{message_id}",
        mark_all_read_url="/custom/read-all",
    )
    html = str(bell)
    controller = _shell_js()

    assert 'data-mark-read-url="/custom/read/{message_id}"' in html
    assert "encodeURIComponent(String(id))" in controller
    assert "method: 'POST'" in controller
    assert 'data-mark-all-read-url="/custom/read-all"' in html


def test_bell_sends_csrf_for_mutating_requests() -> None:
    """Mark-read requests must carry the page token through the bell root."""
    from oridecon.ui import NotificationBell

    html = str(NotificationBell(csrf_token="csrf-123"))

    assert 'data-csrf-token="csrf-123"' in html
    assert "X-CSRF-Token" in _shell_js()
    assert "this.$el.dataset.csrfToken" in _shell_js()


def test_bell_inbox_footer_only_with_inbox_url() -> None:
    """View-all footer should render only when inbox_url is set."""
    from oridecon.ui import NotificationBell

    with_footer = str(NotificationBell(inbox_url="/admin/notifications"))
    without_footer = str(NotificationBell())

    assert "View all notifications" in with_footer
    assert 'href="/admin/notifications"' in with_footer
    assert "View all notifications" not in without_footer


def test_bell_respects_max_display() -> None:
    """Bell should cap the in-memory notification list at max_display."""
    from oridecon.ui import NotificationBell

    html = str(NotificationBell(max_display=5))

    assert 'data-max-display="5"' in html
    assert "this.notifications.length > maxDisplay" in _shell_js()
