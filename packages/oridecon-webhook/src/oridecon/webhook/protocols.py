"""Public protocol surface for ``oridecon.webhook``.

Re-exports the canonical webhook protocols from ``oridecon-contracts`` so
consumers can import from ``oridecon.webhook`` directly.
"""

from __future__ import annotations

from oridecon.contracts.webhook import (
    WebhookDeliveryServiceProtocol,
    WebhookDeliveryStoreProtocol,
    WebhookSubscriptionStoreProtocol,
)

__all__ = [
    "WebhookDeliveryServiceProtocol",
    "WebhookDeliveryStoreProtocol",
    "WebhookSubscriptionStoreProtocol",
]
