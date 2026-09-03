"""Admin notification services package."""

from __future__ import annotations

from oridecon.admin.services.notifications.models import (
    Notification,
    NotificationChannel,
    NotificationRecipient,
    NotificationResult,
    NotificationType,
)
from oridecon.admin.services.notifications.sender import EmailSender
from oridecon.admin.services.notifications.service import AdminNotificationService
from oridecon.admin.services.notifications.templates import (
    ADMIN_EMAIL_BASE,
    EMAIL_TEMPLATES,
    TemplateRenderer,
)

__all__ = [
    # Templates
    "ADMIN_EMAIL_BASE",
    "EMAIL_TEMPLATES",
    # Service
    "AdminNotificationService",
    "EmailSender",
    "Notification",
    "NotificationChannel",
    "NotificationRecipient",
    "NotificationResult",
    # Models
    "NotificationType",
    "TemplateRenderer",
]
