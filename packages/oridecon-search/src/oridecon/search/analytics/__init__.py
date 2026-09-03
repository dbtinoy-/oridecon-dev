"""Search analytics module."""

from __future__ import annotations

from oridecon.search.analytics.recorder import (
    InMemorySearchAnalyticsRecorder,
    SearchAnalyticsRecorder,
    SearchEvent,
)

__all__ = [
    "InMemorySearchAnalyticsRecorder",
    "SearchAnalyticsRecorder",
    "SearchEvent",
]
