"""Document chunking strategies for RAG pipelines.

This module provides various chunking strategies to split documents into
smaller pieces suitable for embedding and retrieval.

Example:
    >>> from oridecon.ai.rag.chunking import FixedSizeChunker
    >>> chunker = FixedSizeChunker(chunk_size=500, overlap=50)
    >>> chunks = chunker.chunk("Long document text...")
"""

from __future__ import annotations

from oridecon.ai.rag.chunking.base import AbstractChunker
from oridecon.ai.rag.chunking.factory import create_chunker
from oridecon.ai.rag.chunking.strategies.custom import CustomChunker
from oridecon.ai.rag.chunking.strategies.fixed_size import FixedSizeChunker
from oridecon.ai.rag.chunking.strategies.recursive import RecursiveChunker
from oridecon.ai.rag.chunking.strategies.semantic import SemanticChunker
from oridecon.ai.rag.chunking.strategies.sliding_window import SlidingWindowChunker
from oridecon.ai.rag.chunking.strategies.token import TokenChunker
from oridecon.ai.rag.chunking.strategy_registry import ChunkingStrategyRegistry
from oridecon.ai.rag.chunking.types import Chunk, ChunkingConfig, ChunkingStrategy

__all__ = [
    "AbstractChunker",
    "Chunk",
    "ChunkingConfig",
    "ChunkingStrategy",
    "ChunkingStrategyRegistry",
    "CustomChunker",
    "FixedSizeChunker",
    "RecursiveChunker",
    "SemanticChunker",
    "SlidingWindowChunker",
    "TokenChunker",
    "create_chunker",
]
