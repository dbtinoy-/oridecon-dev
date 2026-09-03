"""
Batch embedding worker for efficient embedding generation.

Handles batch processing of embeddings with:
- Queue-based job management
- Batch optimization (minimize API calls)
- Progress tracking and resumability
- Automatic retry on failures
- Integration with embedding cache
"""

from __future__ import annotations

from oridecon.ai.workers.batch_embedding.cache import EmbeddingCache
from oridecon.ai.workers.batch_embedding.progress import ProgressTracker
from oridecon.ai.workers.batch_embedding.protocols import EmbeddingProvider
from oridecon.ai.workers.batch_embedding.types import (
    BatchEmbeddingJob,
    BatchEmbeddingProgress,
    BatchEmbeddingResult,
    EmbeddingStatus,
)
from oridecon.ai.workers.batch_embedding.worker import BatchEmbeddingWorker

__all__ = [
    "BatchEmbeddingJob",
    "BatchEmbeddingProgress",
    "BatchEmbeddingResult",
    "BatchEmbeddingWorker",
    "EmbeddingCache",
    "EmbeddingProvider",
    "EmbeddingStatus",
    "ProgressTracker",
]
