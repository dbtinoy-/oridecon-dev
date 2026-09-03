"""Notification configuration facade.

Re-exports every public name so that
``from oridecon.notification.config import X`` continues to work unchanged.
"""

from oridecon.notification.config.inbox import InboxConfig as InboxConfig
from oridecon.notification.config.mailer import (
    MailerConfig as MailerConfig,
)
from oridecon.notification.config.mailer import (
    NamedMailerConfig as NamedMailerConfig,
)
from oridecon.notification.config.mailer import (
    SendGridDriverConfig as SendGridDriverConfig,
)
from oridecon.notification.config.mailer import (
    SMTPDriverConfig as SMTPDriverConfig,
)
from oridecon.notification.config.push import (
    APNsDriverConfig as APNsDriverConfig,
)
from oridecon.notification.config.push import (
    FCMDriverConfig as FCMDriverConfig,
)
from oridecon.notification.config.push import (
    NamedPushConfig as NamedPushConfig,
)
from oridecon.notification.config.push import (
    WebPushDriverConfig as WebPushDriverConfig,
)
from oridecon.notification.config.sms import (
    NamedSMSConfig as NamedSMSConfig,
)
from oridecon.notification.config.sms import (
    TwilioDriverConfig as TwilioDriverConfig,
)
from oridecon.notification.config.top_level import (
    NotificationConfig as NotificationConfig,
)

__all__ = [
    "APNsDriverConfig",
    "FCMDriverConfig",
    "InboxConfig",
    "MailerConfig",
    "NamedMailerConfig",
    "NamedPushConfig",
    "NamedSMSConfig",
    "NotificationConfig",
    "SMTPDriverConfig",
    "SendGridDriverConfig",
    "TwilioDriverConfig",
    "WebPushDriverConfig",
]
