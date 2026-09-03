"""Oridecon Tasks - Background Processing and Task Scheduling.

A comprehensive background task processing system for the Oridecon Framework,
providing task scheduling, job queues, worker management, and monitoring capabilities.

This package follows the Root File Pattern for consistent structure:
- protocols.py: TaskQueueProtocol protocol and abstractions
- types.py: Shared type definitions (Priority)
- config.py: Task configuration settings
- exceptions.py: Task-specific exceptions
- provider.py: Framework integration via provider pattern

Subpackages:
- models/: JobProtocol and Task data models
- backends/: Task queue implementations (memory, Redis, RabbitMQ)
- execution/: Worker pool management, task execution, and health monitoring
- scheduling/: Cron-based job scheduling and templates
- concurrency/: Rate limiting and distributed locking
- workflows/: Task chaining, groups, chords, and conditionals
- middleware/: Pre/post execution hooks and middleware
- progress/: Real-time task progress tracking
- dlq/: Dead letter queue management
- results/: Task result store with async wait
- observability/: Dashboard metrics and execution history
"""

from __future__ import annotations

import importlib.metadata
from typing import TYPE_CHECKING, Any

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from oridecon.tasks.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.contracts.infra.tasks import TaskExecutorProtocol, TaskQueueProtocol
    from oridecon.tasks.backends import (
        MemoryTaskQueue,
        RabbitMQTaskQueue,
        RedisTaskQueue,
    )
    from oridecon.tasks.background_task_manager import BackgroundTaskManager
    from oridecon.tasks.concurrency import (
        DistributedLockProtocol,
        GlobalRateLimiter,
        QueueRateLimiter,
        UniqueTask,
        distributed_lock,
    )
    from oridecon.tasks.config import (
        NamedTaskConfig,
        TaskBackendConfig,
        TaskConfig,
        TaskRateLimitConfig,
        TaskSchedulerConfig,
        TaskTimeoutConfig,
        TaskWorkerConfig,
    )
    from oridecon.tasks.decorators import scheduled, task
    from oridecon.tasks.di.factories import (
        create_memory_task_provider,
        create_provider_from_config,
        create_rabbitmq_task_provider,
        create_redis_task_provider,
    )
    from oridecon.tasks.di.provider import TaskProvider
    from oridecon.tasks.dispatch import delay
    from oridecon.tasks.dlq import DeadLetterQueue, FailureRecord
    from oridecon.tasks.exceptions import (
        TaskCancelledError,
        TaskError,
        TaskExecutionError,
        TaskNotFoundError,
        TaskTimeoutError,
        TaskValidationError,
    )
    from oridecon.tasks.execution import (
        HandlerRegistry,
        TaskHealth,
        TaskWorker,
        TaskWorkerServices,
        WorkerJobStats,
        WorkerPool,
    )
    from oridecon.tasks.middleware import (
        LoggingMiddleware,
        MetricsMiddleware,
        TaskExecutionContext,
        TaskMiddleware,
        TaskMiddlewarePipeline,
        TimeoutMiddleware,
    )
    from oridecon.tasks.models import JobProtocol, JobResult, JobStatus
    from oridecon.tasks.observability import ExecutionRecord, TaskDashboard
    from oridecon.tasks.progress import (
        CacheBackendProgressStore,
        InMemoryProgressStore,
        InMemoryProgressTracker,
        ProgressInfo,
        ProgressSnapshot,
        ProgressStatus,
        ProgressStore,
        ProgressTracker,
        ProgressTrackerProtocol,
    )
    from oridecon.tasks.results import (
        CacheBackendResultStore,
        InMemoryResultStore,
        ResultStore,
    )
    from oridecon.tasks.scheduled_worker import OnErrorPolicy, ScheduledWorker
    from oridecon.tasks.scheduling import (
        CronExpression,
        JobTemplateProtocol,
        ScheduledJob,
        TaskScheduler,
    )
    from oridecon.tasks.types import Priority
    from oridecon.tasks.workflows import (
        BranchStep,
        StepResult,
        TaskChain,
        TaskChord,
        TaskGroup,
        TaskStep,
        WorkflowResult,
        WorkflowStatus,
        chain,
    )

_LAZY_SUBMODULES = {
    "concurrency": "oridecon.tasks.concurrency",
    "execution": "oridecon.tasks.execution",
    "scheduling": "oridecon.tasks.scheduling",
    "models": "oridecon.tasks.models",
    "backends": "oridecon.tasks.backends",
    "workflows": "oridecon.tasks.workflows",
    "middleware": "oridecon.tasks.middleware",
    "progress": "oridecon.tasks.progress",
    "dlq": "oridecon.tasks.dlq",
    "results": "oridecon.tasks.results",
    "observability": "oridecon.tasks.observability",
}

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # BackgroundTaskManager + ScheduledWorker (LEX-006 / LEX-005)
    "BackgroundTaskManager": (
        "oridecon.tasks.background_task_manager",
        "BackgroundTaskManager",
    ),
    "ScheduledWorker": ("oridecon.tasks.scheduled_worker", "ScheduledWorker"),
    "OnErrorPolicy": ("oridecon.tasks.scheduled_worker", "OnErrorPolicy"),
    # Module
    "TasksModule": ("oridecon.tasks.module", "TasksModule"),
    "JobProtocol": ("oridecon.tasks.models", "JobProtocol"),
    "JobStatus": ("oridecon.tasks.models", "JobStatus"),
    "JobResult": ("oridecon.tasks.models", "JobResult"),
    "Priority": ("oridecon.tasks.types", "Priority"),
    "TaskError": ("oridecon.tasks.exceptions", "TaskError"),
    "QueueFullError": ("oridecon.tasks.exceptions", "QueueFullError"),
    "TaskNotFoundError": ("oridecon.tasks.exceptions", "TaskNotFoundError"),
    "TaskTimeoutError": ("oridecon.tasks.exceptions", "TaskTimeoutError"),
    "TaskCancelledError": ("oridecon.tasks.exceptions", "TaskCancelledError"),
    "TaskExecutionError": ("oridecon.tasks.exceptions", "TaskExecutionError"),
    "TaskValidationError": ("oridecon.tasks.exceptions", "TaskValidationError"),
    "TaskConfig": ("oridecon.tasks.config", "TaskConfig"),
    "NamedTaskConfig": ("oridecon.tasks.config", "NamedTaskConfig"),
    "TaskBackendConfig": ("oridecon.tasks.config", "TaskBackendConfig"),
    "TaskWorkerConfig": ("oridecon.tasks.config", "TaskWorkerConfig"),
    "TaskSchedulerConfig": ("oridecon.tasks.config", "TaskSchedulerConfig"),
    "TaskRateLimitConfig": ("oridecon.tasks.config", "TaskRateLimitConfig"),
    "TaskTimeoutConfig": ("oridecon.tasks.config", "TaskTimeoutConfig"),
    "TaskQueueProtocol": ("oridecon.contracts.infra.tasks", "TaskQueueProtocol"),
    "TaskExecutorProtocol": ("oridecon.contracts.infra.tasks", "TaskExecutorProtocol"),
    "MemoryTaskQueue": ("oridecon.tasks.backends", "MemoryTaskQueue"),
    "RedisTaskQueue": ("oridecon.tasks.backends", "RedisTaskQueue"),
    "RabbitMQTaskQueue": ("oridecon.tasks.backends", "RabbitMQTaskQueue"),
    "TaskWorker": ("oridecon.tasks.execution", "TaskWorker"),
    "TaskWorkerServices": ("oridecon.tasks.execution", "TaskWorkerServices"),
    "WorkerJobStats": ("oridecon.tasks.execution", "WorkerJobStats"),
    "WorkerPool": ("oridecon.tasks.execution", "WorkerPool"),
    "HandlerRegistry": ("oridecon.tasks.execution", "HandlerRegistry"),
    "TaskHealth": ("oridecon.tasks.execution", "TaskHealth"),
    "TaskScheduler": ("oridecon.tasks.scheduling", "TaskScheduler"),
    "ScheduledJob": ("oridecon.tasks.scheduling", "ScheduledJob"),
    "CronExpression": ("oridecon.tasks.scheduling", "CronExpression"),
    "JobTemplateProtocol": ("oridecon.tasks.scheduling", "JobTemplateProtocol"),
    "TaskProvider": ("oridecon.tasks.di.provider", "TaskProvider"),
    "create_provider_from_config": (
        "oridecon.tasks.di.provider",
        "create_provider_from_config",
    ),
    "create_memory_task_provider": (
        "oridecon.tasks.di.provider",
        "create_memory_task_provider",
    ),
    "create_redis_task_provider": (
        "oridecon.tasks.di.provider",
        "create_redis_task_provider",
    ),
    "create_rabbitmq_task_provider": (
        "oridecon.tasks.di.provider",
        "create_rabbitmq_task_provider",
    ),
    "QueueRateLimiter": ("oridecon.tasks.concurrency", "QueueRateLimiter"),
    "GlobalRateLimiter": ("oridecon.tasks.concurrency", "GlobalRateLimiter"),
    "DistributedLockProtocol": (
        "oridecon.tasks.concurrency",
        "DistributedLockProtocol",
    ),
    "UniqueTask": ("oridecon.tasks.concurrency", "UniqueTask"),
    "distributed_lock": ("oridecon.tasks.concurrency", "distributed_lock"),
    "task": ("oridecon.tasks.decorators", "task"),
    "scheduled": ("oridecon.tasks.decorators", "scheduled"),
    # Dispatch
    "delay": ("oridecon.tasks.dispatch", "delay"),
    # Workflows
    "TaskChain": ("oridecon.tasks.workflows", "TaskChain"),
    "TaskGroup": ("oridecon.tasks.workflows", "TaskGroup"),
    "TaskChord": ("oridecon.tasks.workflows", "TaskChord"),
    "TaskStep": ("oridecon.tasks.workflows", "TaskStep"),
    "BranchStep": ("oridecon.tasks.workflows", "BranchStep"),
    "WorkflowResult": ("oridecon.tasks.workflows", "WorkflowResult"),
    "WorkflowStatus": ("oridecon.tasks.workflows", "WorkflowStatus"),
    "StepResult": ("oridecon.tasks.workflows", "StepResult"),
    "chain": ("oridecon.tasks.workflows", "chain"),
    # Middleware
    "TaskMiddlewarePipeline": (
        "oridecon.tasks.middleware",
        "TaskMiddlewarePipeline",
    ),
    "TaskMiddleware": ("oridecon.tasks.middleware", "TaskMiddleware"),
    "TaskExecutionContext": (
        "oridecon.tasks.middleware",
        "TaskExecutionContext",
    ),
    "LoggingMiddleware": ("oridecon.tasks.middleware", "LoggingMiddleware"),
    "MetricsMiddleware": ("oridecon.tasks.middleware", "MetricsMiddleware"),
    "TimeoutMiddleware": ("oridecon.tasks.middleware", "TimeoutMiddleware"),
    # Progress
    "ProgressTracker": ("oridecon.tasks.progress", "ProgressTracker"),
    "ProgressStore": ("oridecon.tasks.progress", "ProgressStore"),
    "InMemoryProgressStore": ("oridecon.tasks.progress", "InMemoryProgressStore"),
    "InMemoryProgressTracker": ("oridecon.tasks.progress", "InMemoryProgressTracker"),
    "ProgressInfo": ("oridecon.tasks.progress", "ProgressInfo"),
    "ProgressSnapshot": ("oridecon.tasks.progress", "ProgressSnapshot"),
    "ProgressStatus": ("oridecon.tasks.progress", "ProgressStatus"),
    "ProgressTrackerProtocol": ("oridecon.tasks.progress", "ProgressTrackerProtocol"),
    "CacheBackendProgressStore": (
        "oridecon.tasks.progress",
        "CacheBackendProgressStore",
    ),
    # DLQ
    "DeadLetterQueue": ("oridecon.tasks.dlq", "DeadLetterQueue"),
    "FailureRecord": ("oridecon.tasks.dlq", "FailureRecord"),
    # Results
    "ResultStore": ("oridecon.tasks.results", "ResultStore"),
    "InMemoryResultStore": ("oridecon.tasks.results", "InMemoryResultStore"),
    "CacheBackendResultStore": ("oridecon.tasks.results", "CacheBackendResultStore"),
    # Observability
    "TaskDashboard": ("oridecon.tasks.observability", "TaskDashboard"),
    "ExecutionRecord": ("oridecon.tasks.observability", "ExecutionRecord"),
    # Events
    "TaskQueuedEvent": ("oridecon.tasks.events", "TaskQueuedEvent"),
    "TaskCompletedEvent": ("oridecon.tasks.events", "TaskCompletedEvent"),
    "TaskFailedEvent": ("oridecon.tasks.events", "TaskFailedEvent"),
    # Hooks
    "TaskCompletedHook": ("oridecon.tasks.hooks", "TaskCompletedHook"),
    "TaskEnqueuedHook": ("oridecon.tasks.hooks", "TaskEnqueuedHook"),
    "TaskFailedHook": ("oridecon.tasks.hooks", "TaskFailedHook"),
    "TaskStartedHook": ("oridecon.tasks.hooks", "TaskStartedHook"),
}


def __getattr__(name: str) -> Any:
    """Lazy load attributes to avoid circular imports."""
    import importlib

    # Check if it's a lazy class first
    if name in _LAZY_IMPORTS:
        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value

    # Check if it's a submodule request
    if name in _LAZY_SUBMODULES:
        return importlib.import_module(_LAZY_SUBMODULES[name])

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """List available attributes for IDE support."""
    return sorted(
        set(__all__) | set(_LAZY_SUBMODULES.keys()) | set(_LAZY_IMPORTS.keys())
    )


__all__ = list(_LAZY_SUBMODULES.keys()) + list(_LAZY_IMPORTS.keys())
