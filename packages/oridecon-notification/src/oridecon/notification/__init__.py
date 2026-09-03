"""oridecon-notification — SMS, push, email, and user inbox with Named DI multi-backend support."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.contracts.notification.errors import NotificationError
from oridecon.contracts.notification.inbox import InboxMessage, InboxStoreProtocol
from oridecon.contracts.notification.protocols import (
    PushChannelProtocol,
    SMSChannelProtocol,
)
from oridecon.contracts.notification.types import PushMessage, SMSMessage
from oridecon.notification.backends.push import WebPushChannel
from oridecon.notification.config import (
    APNsDriverConfig,
    FCMDriverConfig,
    InboxConfig,
    MailerConfig,
    NamedMailerConfig,
    NamedPushConfig,
    NamedSMSConfig,
    NotificationConfig,
    SendGridDriverConfig,
    SMTPDriverConfig,
    TwilioDriverConfig,
    WebPushDriverConfig,
)
from oridecon.notification.constants import __version__
from oridecon.notification.events import (
    EmailBouncedEvent,
    EmailSentEvent,
    InboxMessageCreatedEvent,
    InboxMessageReadEvent,
    NotificationFailedEvent,
    NotificationSentEvent,
)
from oridecon.notification.exceptions import (
    APNsNotificationError,
    FCMNotificationError,
    InboxError,
    InboxMessageNotFoundError,
    InboxPermissionError,
    SendGridMailerError,
    SMTPMailerError,
    TwilioNotificationError,
    WebPushNotificationError,
)
from oridecon.notification.hooks import (
    NotificationFailedHook,
    NotificationSentHook,
)
from oridecon.notification.inbox.database import DatabaseInboxStore
from oridecon.notification.inbox.memory import InMemoryInboxStore
from oridecon.notification.inbox.service import InboxService
from oridecon.notification.mailer.mailable import Mailable
from oridecon.notification.mailer.retrying_mailer import RetryingMailer
from oridecon.notification.mailer.sendgrid_mailer import SendGridMailer
from oridecon.notification.mailer.smtp_mailer import SMTPMailer
from oridecon.notification.module import NotificationModule
from oridecon.notification.protocols import (
    InboxStoreProtocol,
    MailerProtocol,
    PushChannelProtocol,
    SMSChannelProtocol,
)

__all__ = [
    "APNsDriverConfig",
    "APNsNotificationError",
    "DatabaseInboxStore",
    "EmailBouncedEvent",
    "EmailSentEvent",
    "FCMDriverConfig",
    "FCMNotificationError",
    "InMemoryInboxStore",
    "InboxConfig",
    "InboxError",
    "InboxMessage",
    "InboxMessageCreatedEvent",
    "InboxMessageNotFoundError",
    "InboxMessageReadEvent",
    "InboxPermissionError",
    "InboxService",
    "InboxStoreProtocol",
    "Mailable",
    "MailerConfig",
    "MailerProtocol",
    "NamedMailerConfig",
    "NamedPushConfig",
    "NamedSMSConfig",
    "NotificationConfig",
    "NotificationError",
    "NotificationFailedEvent",
    "NotificationFailedHook",
    "NotificationModule",
    "NotificationSentEvent",
    "NotificationSentHook",
    "PushChannelProtocol",
    "PushMessage",
    "RetryingMailer",
    "SMSChannelProtocol",
    "SMSMessage",
    "SMTPDriverConfig",
    "SMTPMailer",
    "SMTPMailerError",
    "SendGridMailer",
    "SendGridMailerError",
    "TwilioDriverConfig",
    "TwilioNotificationError",
    "WebPushChannel",
    "WebPushDriverConfig",
    "WebPushNotificationError",
    "__version__",
]
