"""Video frame-rate interpolation subsystem for the Oridecon multimedia package family."""

from __future__ import annotations

from oridecon.multimedia.interpolate.config import InterpolationConfig
from oridecon.multimedia.interpolate.di import InterpolationGenerationProvider
from oridecon.multimedia.interpolate.module import InterpolationModule
from oridecon.multimedia.interpolate.providers import RifeInterpolationProvider
from oridecon.multimedia.interpolate.tasks import InterpolationTask
from oridecon.multimedia.interpolate.video_interpolation_service import (
    VideoInterpolationService,
)

__all__ = [
    "InterpolationConfig",
    "InterpolationGenerationProvider",
    "InterpolationModule",
    "InterpolationTask",
    "RifeInterpolationProvider",
    "VideoInterpolationService",
]
