"""OpenAI-compatible embedding client for oridecon-vector."""

from __future__ import annotations

from oridecon.vector.embedding.cache import EmbeddingCache, InMemoryEmbeddingCache
from oridecon.vector.embedding.client import OpenAICompatibleEmbeddingClient
from oridecon.vector.embedding.config import EmbeddingClientConfig

__all__ = [
    "EmbeddingCache",
    "EmbeddingClientConfig",
    "InMemoryEmbeddingCache",
    "OpenAICompatibleEmbeddingClient",
]
