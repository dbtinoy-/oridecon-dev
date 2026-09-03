"""
Document preprocessing modules.

This package provides modular document preprocessing capabilities
including OCR, table extraction, and metadata enrichment.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.ai.rag.exceptions import PreprocessingError
from oridecon.ai.rag.preprocessing.base import AbstractPreprocessor
from oridecon.ai.rag.preprocessing.document import PreprocessedDocument
from oridecon.ai.rag.preprocessing.enricher import MetadataEnricher
from oridecon.ai.rag.preprocessing.ocr import OCRPreprocessor
from oridecon.ai.rag.preprocessing.pipeline import PreprocessingPipeline
from oridecon.ai.rag.preprocessing.tables import TableExtractor
from oridecon.ai.rag.preprocessing.types import (
    DocumentMetadata,
    DocumentType,
    ExtractedImage,
    ExtractedTable,
    TableFormat,
)

__all__ = [
    "AbstractPreprocessor",
    "DocumentMetadata",
    "DocumentType",
    "ExtractedImage",
    "ExtractedTable",
    "MetadataEnricher",
    "OCRPreprocessor",
    "PreprocessedDocument",
    "PreprocessingError",
    "PreprocessingPipeline",
    "TableExtractor",
    "TableFormat",
]
