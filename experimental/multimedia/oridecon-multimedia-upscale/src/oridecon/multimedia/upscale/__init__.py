"""Image and video super-resolution subsystem for the Oridecon multimedia package family."""

from __future__ import annotations

from oridecon.multimedia.upscale.config import UpscaleConfig
from oridecon.multimedia.upscale.di import UpscaleGenerationProvider
from oridecon.multimedia.upscale.module import UpscaleModule
from oridecon.multimedia.upscale.providers import (
    HatUpscaleProvider,
    RealEsrganUpscaleProvider,
)
from oridecon.multimedia.upscale.tasks import UpscaleTask
from oridecon.multimedia.upscale.video_upscale_service import VideoUpscaleService

__all__ = [
    "HatUpscaleProvider",
    "RealEsrganUpscaleProvider",
    "UpscaleConfig",
    "UpscaleGenerationProvider",
    "UpscaleModule",
    "UpscaleTask",
    "VideoUpscaleService",
]
