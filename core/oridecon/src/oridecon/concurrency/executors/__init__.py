"""Task execution primitives: dispatcher, parallel execution, task manager."""

from __future__ import annotations

from oridecon.concurrency.executors.dispatcher import DispatcherImpl
from oridecon.concurrency.executors.task_manager import TaskManager

__all__ = ["DispatcherImpl", "TaskManager"]
