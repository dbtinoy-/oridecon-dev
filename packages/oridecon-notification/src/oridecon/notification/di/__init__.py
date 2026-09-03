"""oridecon-notification DI module."""

from __future__ import annotations

from oridecon.notification.di.inbox_provider import InboxProvider
from oridecon.notification.di.mailer_provider import MailerProvider
from oridecon.notification.di.provider import NotificationProvider

__all__ = ["InboxProvider", "MailerProvider", "NotificationProvider"]
