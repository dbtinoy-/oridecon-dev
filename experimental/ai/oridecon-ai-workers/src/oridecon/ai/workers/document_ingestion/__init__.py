"""
Document ingestion package.

Provides comprehensive document ingestion functionality for the Oridecon AI framework.
"""

from __future__ import annotations

from oridecon.ai.workers.document_ingestion.parser import (
    DocumentParser,
    UniversalDocumentParser,
)
from oridecon.ai.workers.document_ingestion.processor import DocumentProcessor
from oridecon.ai.workers.document_ingestion.progress import ProgressTracker
from oridecon.ai.workers.document_ingestion.types import (
    Document,
    DocumentIngestionJob,
    IngestionProgress,
    IngestionResult,
    IngestionStatus,
)
from oridecon.ai.workers.document_ingestion.worker import DocumentIngestionWorker

__all__ = [
    "Document",
    "DocumentIngestionJob",
    "DocumentIngestionWorker",
    "DocumentParser",
    "DocumentProcessor",
    "IngestionProgress",
    "IngestionResult",
    "IngestionStatus",
    "ProgressTracker",
    "UniversalDocumentParser",
]
