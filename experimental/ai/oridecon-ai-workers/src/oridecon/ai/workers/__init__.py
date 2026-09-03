"""
Background workers for oridecon-intelligence.

This module provides background processing capabilities for:
- Document ingestion and processing
- Batch embedding generation
- Scheduled maintenance tasks
- Failed task recovery (Dead Letter Queue)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oridecon.ai.workers.batch_embedding import (
        BatchEmbeddingJob,
        BatchEmbeddingProgress,
        BatchEmbeddingResult,
        BatchEmbeddingWorker,
    )
    from oridecon.ai.workers.config import WorkersConfig
    from oridecon.ai.workers.constants import (
        DEFAULT_BASE_BACKOFF,
        DEFAULT_CHECK_INTERVAL,
        DEFAULT_MAX_RETRIES,
        DEFAULT_TASK_TIMEOUT,
        MAX_BACKOFF_SECONDS,
        MAX_HISTORY_SIZE,
    )
    from oridecon.ai.workers.di.provider import WorkersProvider
    from oridecon.ai.workers.dlq.worker import DeadLetterQueueWorker, ErrorClassifier
    from oridecon.ai.workers.document_ingestion import (
        DocumentIngestionJob,
        DocumentIngestionWorker,
        IngestionProgress,
        IngestionResult,
    )
    from oridecon.ai.workers.exceptions import DLQError, MaintenanceError, WorkerError
    from oridecon.ai.workers.hooks import (
        WorkerJobCompletedHook,
        WorkerJobStartedHook,
        WorkerMaintenanceRunHook,
    )
    from oridecon.ai.workers.maintenance.worker import MaintenanceWorker
    from oridecon.ai.workers.module import WorkersModule
    from oridecon.ai.workers.types import (
        DLQAction,
        DLQItem,
        DLQStats,
        FailureCategory,
        MaintenanceResult,
        MaintenanceStatus,
        MaintenanceTask,
        MaintenanceTaskType,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "BatchEmbeddingJob": ("oridecon.ai.workers.batch_embedding", "BatchEmbeddingJob"),
    "BatchEmbeddingProgress": (
        "oridecon.ai.workers.batch_embedding",
        "BatchEmbeddingProgress",
    ),
    "BatchEmbeddingResult": (
        "oridecon.ai.workers.batch_embedding",
        "BatchEmbeddingResult",
    ),
    "BatchEmbeddingWorker": (
        "oridecon.ai.workers.batch_embedding",
        "BatchEmbeddingWorker",
    ),
    "DEFAULT_BASE_BACKOFF": ("oridecon.ai.workers.constants", "DEFAULT_BASE_BACKOFF"),
    "DEFAULT_CHECK_INTERVAL": (
        "oridecon.ai.workers.constants",
        "DEFAULT_CHECK_INTERVAL",
    ),
    "DEFAULT_MAX_RETRIES": ("oridecon.ai.workers.constants", "DEFAULT_MAX_RETRIES"),
    "DEFAULT_TASK_TIMEOUT": ("oridecon.ai.workers.constants", "DEFAULT_TASK_TIMEOUT"),
    "DLQAction": ("oridecon.ai.workers.types", "DLQAction"),
    "DLQError": ("oridecon.ai.workers.exceptions", "DLQError"),
    "DLQItem": ("oridecon.ai.workers.types", "DLQItem"),
    "DLQStats": ("oridecon.ai.workers.types", "DLQStats"),
    "DeadLetterQueueWorker": (
        "oridecon.ai.workers.dlq.worker",
        "DeadLetterQueueWorker",
    ),
    "DocumentIngestionJob": (
        "oridecon.ai.workers.document_ingestion",
        "DocumentIngestionJob",
    ),
    "DocumentIngestionWorker": (
        "oridecon.ai.workers.document_ingestion",
        "DocumentIngestionWorker",
    ),
    "ErrorClassifier": ("oridecon.ai.workers.dlq.worker", "ErrorClassifier"),
    "FailureCategory": ("oridecon.ai.workers.types", "FailureCategory"),
    "IngestionProgress": (
        "oridecon.ai.workers.document_ingestion",
        "IngestionProgress",
    ),
    "IngestionResult": ("oridecon.ai.workers.document_ingestion", "IngestionResult"),
    "MaintenanceError": ("oridecon.ai.workers.exceptions", "MaintenanceError"),
    "MaintenanceResult": ("oridecon.ai.workers.types", "MaintenanceResult"),
    "WorkerJobCompletedHook": (
        "oridecon.ai.workers.hooks",
        "WorkerJobCompletedHook",
    ),
    "WorkerJobStartedHook": (
        "oridecon.ai.workers.hooks",
        "WorkerJobStartedHook",
    ),
    "WorkerMaintenanceRunHook": (
        "oridecon.ai.workers.hooks",
        "WorkerMaintenanceRunHook",
    ),
    "MaintenanceStatus": ("oridecon.ai.workers.types", "MaintenanceStatus"),
    "MaintenanceTask": ("oridecon.ai.workers.types", "MaintenanceTask"),
    "MaintenanceTaskType": ("oridecon.ai.workers.types", "MaintenanceTaskType"),
    "MaintenanceWorker": (
        "oridecon.ai.workers.maintenance.worker",
        "MaintenanceWorker",
    ),
    "MAX_BACKOFF_SECONDS": ("oridecon.ai.workers.constants", "MAX_BACKOFF_SECONDS"),
    "MAX_HISTORY_SIZE": ("oridecon.ai.workers.constants", "MAX_HISTORY_SIZE"),
    "WorkerError": ("oridecon.ai.workers.exceptions", "WorkerError"),
    "WorkersConfig": ("oridecon.ai.workers.config", "WorkersConfig"),
    "WorkersModule": ("oridecon.ai.workers.module", "WorkersModule"),
    "WorkersProvider": ("oridecon.ai.workers.di.provider", "WorkersProvider"),
}

__all__ = list(_LAZY_IMPORTS)


def __getattr__(name: str) -> object:
    """Lazy-load public symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr = _LAZY_IMPORTS[name]
        mod = importlib.import_module(module_path)
        value = getattr(mod, attr)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """Expose lazy-loaded names for tab completion and dir()."""
    return list(_LAZY_IMPORTS)
