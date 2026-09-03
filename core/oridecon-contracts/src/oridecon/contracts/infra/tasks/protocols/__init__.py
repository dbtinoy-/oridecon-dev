"""Task and job queue protocol class definitions."""

from __future__ import annotations

from oridecon.contracts.infra.tasks.protocols.idempotency import (
    IdempotencyManagerProtocol as IdempotencyManagerProtocol,
)
from oridecon.contracts.infra.tasks.protocols.idempotency import (
    IdempotentTaskManagerProtocol as IdempotentTaskManagerProtocol,
)
from oridecon.contracts.infra.tasks.protocols.queue import DLQProtocol as DLQProtocol
from oridecon.contracts.infra.tasks.protocols.queue import JobProtocol as JobProtocol
from oridecon.contracts.infra.tasks.protocols.queue import (
    JobTemplateProtocol as JobTemplateProtocol,
)
from oridecon.contracts.infra.tasks.protocols.queue import (
    TaskExecutorProtocol as TaskExecutorProtocol,
)
from oridecon.contracts.infra.tasks.protocols.queue import (
    TaskManagerProtocol as TaskManagerProtocol,
)
from oridecon.contracts.infra.tasks.protocols.queue import (
    TaskProviderProtocol as TaskProviderProtocol,
)
from oridecon.contracts.infra.tasks.protocols.queue import (
    TaskQueueProtocol as TaskQueueProtocol,
)
from oridecon.contracts.infra.tasks.protocols.queue import (
    TaskWorkerProtocol as TaskWorkerProtocol,
)

__all__ = [
    "DLQProtocol",
    "IdempotencyManagerProtocol",
    "IdempotentTaskManagerProtocol",
    "JobProtocol",
    "JobTemplateProtocol",
    "TaskExecutorProtocol",
    "TaskProviderProtocol",
    "TaskQueueProtocol",
    "TaskWorkerProtocol",
]
