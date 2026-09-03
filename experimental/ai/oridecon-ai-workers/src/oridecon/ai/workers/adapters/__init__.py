"""Task queue and pipeline adapters for optional integrations.

Bridges oridecon-intelligence workers with external task queues, the RAG
pipeline, and document loader registries.
"""

from __future__ import annotations

from oridecon.ai.workers.adapters.loader_worker import LoaderWorkerBridge
from oridecon.ai.workers.adapters.rag_adapter import (
    IngestionError,
    IngestionReport,
    RAGIngestionAdapter,
)
from oridecon.ai.workers.adapters.tasks_adapter import (
    HAS_ORI_TASKS,
    OrideconTasksAdapter,
)

__all__ = [
    "HAS_ORI_TASKS",
    "IngestionError",
    "IngestionReport",
    "OrideconTasksAdapter",
    "LoaderWorkerBridge",
    "RAGIngestionAdapter",
]
