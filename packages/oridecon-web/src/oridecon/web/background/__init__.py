"""Background tasks for fire-and-forget operations."""

from __future__ import annotations

from oridecon.web.background.decorator import background
from oridecon.web.background.tasks import (
    BackgroundTasks,
    BackgroundTaskScope,
    StarletteBackgroundTaskRunner,
)

__all__ = [
    "BackgroundTaskScope",
    "BackgroundTasks",
    "StarletteBackgroundTaskRunner",
    "background",
]
