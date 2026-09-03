"""oridecon-notification protocol re-exports."""

from __future__ import annotations

from oridecon.contracts.mailer.protocols import MailerProtocol
from oridecon.contracts.notification.inbox import InboxStoreProtocol
from oridecon.contracts.notification.protocols import (
    PushChannelProtocol,
    SMSChannelProtocol,
)

__all__ = [
    "InboxStoreProtocol",
    "MailerProtocol",
    "PushChannelProtocol",
    "SMSChannelProtocol",
]
