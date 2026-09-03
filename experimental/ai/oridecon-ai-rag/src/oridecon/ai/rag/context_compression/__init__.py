"""Context compression strategies for RAG systems.

This module provides various compression techniques to reduce token usage
while maintaining semantic content and relevance:

- Extractive compression: Select most relevant sentences
- Abstractive compression: LLM-based summarization
- Reranking-based compression: Rerank and filter by relevance
- Token-based compression: Truncate to token limits
- Semantic deduplication: Remove redundant information

Examples:
    >>> from oridecon.ai.rag.context_compression import (
    ...     ExtractiveSummaryCompressor,
    ...     AbstractiveCompressor,
    ...     TokenLimitCompressor,
    ... )
    >>>
    >>> # Extractive compression
    >>> compressor = ExtractiveSummaryCompressor(max_sentences=3)
    >>> compressed = await compressor.compress(context, query="What is AI?")
    >>>
    >>> # Abstractive compression with LLM
    >>> compressor = AbstractiveCompressor(llm_client=llm, max_tokens=100)
    >>> compressed = await compressor.compress(context, query="Explain ML")
    >>>
    >>> # Token limit compression
    >>> compressor = TokenLimitCompressor(max_tokens=500)
    >>> compressed = await compressor.compress(context)

"""

from __future__ import annotations

from oridecon.ai.rag.context_compression.abstractive import AbstractiveCompressor
from oridecon.ai.rag.context_compression.base import AbstractCompressor
from oridecon.ai.rag.context_compression.compress import compress_context
from oridecon.ai.rag.context_compression.extractive import ExtractiveSummaryCompressor
from oridecon.ai.rag.context_compression.hybrid import HybridCompressor
from oridecon.ai.rag.context_compression.semantic_dedup import (
    SemanticDeduplicationCompressor,
)
from oridecon.ai.rag.context_compression.token_limit import TokenLimitCompressor
from oridecon.ai.rag.context_compression.types import (
    CompressionResult,
    CompressionStrategy,
)

__all__ = [
    "AbstractCompressor",
    "AbstractiveCompressor",
    "CompressionResult",
    "CompressionStrategy",
    "ExtractiveSummaryCompressor",
    "HybridCompressor",
    "SemanticDeduplicationCompressor",
    "TokenLimitCompressor",
    "compress_context",
]
