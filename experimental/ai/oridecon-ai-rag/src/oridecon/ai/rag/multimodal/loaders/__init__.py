"""Loaders for multi-modal documents."""

from __future__ import annotations

from oridecon.ai.rag.multimodal.loaders.audio import AudioLoader
from oridecon.ai.rag.multimodal.loaders.image import ImageLoader
from oridecon.ai.rag.multimodal.loaders.video import VideoLoader

__all__ = [
    "AudioLoader",
    "ImageLoader",
    "VideoLoader",
]
