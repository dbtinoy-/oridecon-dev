"""Admin contributor subpackage for oridecon-notification."""

from __future__ import annotations

from oridecon.notification.admin.contributor import NotificationAdminContributor
from oridecon.notification.admin.handlers.inbox import InboxHandlers
from oridecon.notification.admin.pages.inbox import NotificationsInboxPage

__all__ = [
    "InboxHandlers",
    "NotificationAdminContributor",
    "NotificationsInboxPage",
]
