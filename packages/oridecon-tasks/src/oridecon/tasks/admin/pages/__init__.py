"""Management pages for oridecon-tasks admin."""

from __future__ import annotations

from oridecon.tasks.admin.pages.active import TasksActivePage
from oridecon.tasks.admin.pages.failed import TasksFailedPage
from oridecon.tasks.admin.pages.history import TasksHistoryPage
from oridecon.tasks.admin.pages.overview import TasksOverviewPage

__all__ = [
    "TasksActivePage",
    "TasksFailedPage",
    "TasksHistoryPage",
    "TasksOverviewPage",
]
