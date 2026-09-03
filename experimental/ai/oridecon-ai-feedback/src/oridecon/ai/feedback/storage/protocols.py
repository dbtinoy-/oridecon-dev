"""Storage protocols for AI Feedback - re-exported from contracts.

This module re-exports FeedbackStoreProtocol and FeedbackSummary
from oridecon.contracts.ai.feedback for convenience. Use those
imports directly for new code.
"""

from __future__ import annotations

# Re-export from contracts where storage protocols are centralized
from oridecon.contracts.ai.feedback import FeedbackStoreProtocol, FeedbackSummary

__all__ = ["FeedbackStoreProtocol", "FeedbackSummary"]
