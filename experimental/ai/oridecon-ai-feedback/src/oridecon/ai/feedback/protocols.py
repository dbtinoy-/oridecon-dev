"""Protocol re-exports for feedback — convenience surface for consumers."""

from __future__ import annotations

from oridecon.contracts.ai.feedback import FeedbackProtocol as FeedbackProtocol
from oridecon.contracts.ai.feedback import (
    FeedbackStoreProtocol as FeedbackStoreProtocol,
)

__all__ = [
    "FeedbackProtocol",
    "FeedbackStoreProtocol",
]
