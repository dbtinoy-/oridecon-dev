"""Shared attribute surface for TaskProvider mixins."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any

from oridecon.contracts.core.di import ContainerRegistrarProtocol
from oridecon.contracts.core.logging import LoggerProtocol
from oridecon.contracts.infra.tasks.protocols import TaskQueueProtocol
from oridecon.tasks.backends.registry import TaskBackendRegistry
from oridecon.tasks.config import TaskConfig
from oridecon.tasks.execution.pool import WorkerPool
from oridecon.tasks.execution.registry import HandlerRegistry
from oridecon.tasks.middleware.core import TaskMiddlewarePipeline
from oridecon.tasks.results.core import ResultStore
from oridecon.tasks.scheduling.scheduler import TaskScheduler

if TYPE_CHECKING:
    from oridecon.contracts.core.identity import IdGeneratorProtocol
    from oridecon.tasks.models.job import JobProtocol


class _TaskAttrsMixin:
    """Attribute contract shared by all TaskProvider mixins."""

    _backend_registry: TaskBackendRegistry
    _background_tasks: set[asyncio.Task[Any]]
    _config: TaskConfig | None
    _container: ContainerRegistrarProtocol
    _id_generator: IdGeneratorProtocol | None
    _middleware_pipeline: TaskMiddlewarePipeline | None
    _queue_services: list[tuple[str, Any]]
    _result_store: ResultStore
    _task_modules: tuple[str, ...]
    _task_packages: tuple[str, ...]
    enable_scheduler: bool
    logger: LoggerProtocol
    name: str
    queue: TaskQueueProtocol
    registry: HandlerRegistry
    scheduler: TaskScheduler | None
    scheduler_task: asyncio.Task[Any] | None
    worker_count: int
    worker_pool: WorkerPool | None

    if TYPE_CHECKING:

        async def _enqueue_job(self, job: JobProtocol) -> None: ...
