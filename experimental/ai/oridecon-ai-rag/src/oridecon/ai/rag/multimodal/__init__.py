"""Multi-modal RAG support.

This module provides support for handling multiple modalities in RAG:
- Images: JPEG, PNG, GIF, etc.
- Audio: MP3, WAV, FLAC, etc.
- Video: MP4, AVI, MOV, etc.
- Cross-modal retrieval: text→image, image→text, etc.
"""

from __future__ import annotations

from oridecon.ai.rag.multimodal.embeddings import (
    CLIPEmbedding,
    MultiModalEmbedder,
)
from oridecon.ai.rag.multimodal.loaders import (
    AudioLoader,
    ImageLoader,
    VideoLoader,
)
from oridecon.ai.rag.multimodal.retrieval import CrossModalRetriever
from oridecon.ai.rag.multimodal.types import (
    AudioDocument,
    AudioFormat,
    AudioMetadata,
    ImageDocument,
    ImageFormat,
    ImageMetadata,
    Modality,
    MultiModalDocument,
    MultiModalEmbedding,
    VideoDocument,
    VideoFormat,
    VideoMetadata,
)

__all__ = [
    "AudioDocument",
    "AudioFormat",
    "AudioLoader",
    "AudioMetadata",
    # Embeddings
    "CLIPEmbedding",
    # Retrieval
    "CrossModalRetriever",
    # Documents
    "ImageDocument",
    # Enums
    "ImageFormat",
    # Loaders
    "ImageLoader",
    # Metadata
    "ImageMetadata",
    "Modality",
    "MultiModalDocument",
    "MultiModalEmbedder",
    "MultiModalEmbedding",
    "VideoDocument",
    "VideoFormat",
    "VideoLoader",
    "VideoMetadata",
]
