"""Outbound webhook delivery for oridecon-events."""

from __future__ import annotations

from oridecon.events.webhooks.dispatcher import WebhookDispatcher, WebhookEndpoint

__all__ = ["WebhookDispatcher", "WebhookEndpoint"]
