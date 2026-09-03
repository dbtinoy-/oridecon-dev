# oridecon-contracts/src/oridecon/contracts/mailer/__init__.py
"""Mailer protocols, types, and errors."""

from __future__ import annotations

from oridecon.contracts.mailer.errors import MailerError
from oridecon.contracts.mailer.protocols import MailerProtocol
from oridecon.contracts.mailer.types import (
    Attachment,
    DeliveryState,
    EmailMessage,
    MessageAddress,
    MessageDeliveryReceipt,
    MessagePriority,
    MessageStatus,
)

__all__ = [
    "Attachment",
    "DeliveryState",
    "EmailMessage",
    "MailerError",
    "MailerProtocol",
    "MessageAddress",
    "MessageDeliveryReceipt",
    "MessagePriority",
    "MessageStatus",
]
