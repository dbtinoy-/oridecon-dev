"""Image generation backend providers."""

from __future__ import annotations

from oridecon.multimedia.image.providers.comfyui import ComfyUiImageProvider
from oridecon.multimedia.image.providers.local_http import LocalHttpImageProvider
from oridecon.multimedia.image.providers.openai import OpenAIImageProvider
from oridecon.multimedia.image.providers.stability import StabilityImageProvider

__all__ = [
    "ComfyUiImageProvider",
    "LocalHttpImageProvider",
    "OpenAIImageProvider",
    "StabilityImageProvider",
]
