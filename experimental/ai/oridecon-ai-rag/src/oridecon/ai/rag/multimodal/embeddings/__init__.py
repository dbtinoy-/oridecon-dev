"""Embeddings for multi-modal documents."""

from __future__ import annotations

from oridecon.ai.rag.multimodal.embeddings.clip import CLIPEmbedding
from oridecon.ai.rag.multimodal.embeddings.multimodal import (
    MultiModalEmbedder,
)

__all__ = [
    "CLIPEmbedding",
    "MultiModalEmbedder",
]
