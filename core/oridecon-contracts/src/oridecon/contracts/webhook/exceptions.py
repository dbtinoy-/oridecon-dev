"""Webhook domain exception hierarchy."""

from __future__ import annotations

from oridecon.contracts.exceptions.domain import DomainError


class WebhookError(DomainError):
    """Base exception for webhook domain operations."""

    _code = "ORI_ERR_WEBHOOK_001"


__all__ = ["WebhookError"]
