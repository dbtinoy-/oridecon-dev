"""Testing clients and test beds for oridecon-tasks."""

from __future__ import annotations

from oridecon.testing.clients.tasks.bed import TaskTestBed
from oridecon.testing.clients.tasks.client import TaskTestClient
from oridecon.testing.clients.tasks.data import TaskTestData
from oridecon.testing.clients.tasks.mocks import (
    MockTaskExecutor,
    MockTaskQueue,
    MockTaskResult,
    MockTasksProvider,
)

__all__ = [
    "MockTaskExecutor",
    "MockTaskQueue",
    "MockTaskResult",
    "MockTasksProvider",
    "TaskTestBed",
    "TaskTestClient",
    "TaskTestData",
]
