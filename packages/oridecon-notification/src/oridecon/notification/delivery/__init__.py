"""Notification delivery retry queue module."""

from __future__ import annotations

from oridecon.notification.delivery.exceptions import PermanentDeliveryFailure
from oridecon.notification.delivery.retry import RetryingMailer

__all__ = ["PermanentDeliveryFailure", "RetryingMailer"]
