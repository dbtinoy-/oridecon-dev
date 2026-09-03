"""Worker pool and execution management

This module provides worker management for task processing,
including health monitoring and statistics.
"""

from __future__ import annotations

from oridecon.tasks.execution.health import TaskHealth
from oridecon.tasks.execution.metrics import TaskMetricsCollector
from oridecon.tasks.execution.pool import WorkerPool
from oridecon.tasks.execution.registry import HandlerRegistry
from oridecon.tasks.execution.worker import (
    TaskWorker,
    TaskWorkerServices,
    WorkerJobStats,
)

__all__ = [
    "HandlerRegistry",
    # Metrics
    "TaskHealth",
    "TaskMetricsCollector",
    "TaskWorker",
    "TaskWorkerServices",
    "WorkerJobStats",
    "WorkerPool",
]
