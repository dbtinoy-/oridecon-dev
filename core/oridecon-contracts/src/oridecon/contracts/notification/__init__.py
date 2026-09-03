# oridecon-contracts/src/oridecon/contracts/notification/__init__.py
"""Notification protocols, types, and errors."""

from __future__ import annotations

from oridecon.contracts.notification.delivery import (
    DeliveryStatus,
    DeliveryStoreProtocol,
)
from oridecon.contracts.notification.errors import NotificationError
from oridecon.contracts.notification.inbox import InboxMessage, InboxStoreProtocol
from oridecon.contracts.notification.protocols import (
    PushChannelProtocol,
    SMSChannelProtocol,
)
from oridecon.contracts.notification.types import PushMessage, SMSMessage
from oridecon.contracts.notification.web_push import WebPushKeys, WebPushSubscription

__all__ = [
    "DeliveryStatus",
    "DeliveryStoreProtocol",
    "InboxMessage",
    "InboxStoreProtocol",
    "NotificationError",
    "PushChannelProtocol",
    "PushMessage",
    "SMSChannelProtocol",
    "SMSMessage",
    "WebPushKeys",
    "WebPushSubscription",
]
