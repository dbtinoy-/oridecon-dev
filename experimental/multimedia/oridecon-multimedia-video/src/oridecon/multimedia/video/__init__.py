"""Video generation subsystem for the Oridecon multimedia package family."""

from __future__ import annotations

from oridecon.multimedia.video.config import VideoConfig, VideoProcessingConfig
from oridecon.multimedia.video.di import VideoGenerationProvider
from oridecon.multimedia.video.exceptions import (
    VideoGenerationAuthenticationError,
    VideoGenerationError,
    VideoTimeoutError,
)
from oridecon.multimedia.video.module import VideoModule
from oridecon.multimedia.video.processing import FFmpegVideoProcessor
from oridecon.multimedia.video.providers import (
    CogVideoXVideoProvider,
    ComfyUiVideoProvider,
    LocalHttpVideoProvider,
    OpenAIVideoProvider,
    RunwayVideoProvider,
    SVDVideoProvider,
    Wan22VideoProvider,
)
from oridecon.multimedia.video.tasks import VideoGenerationTask, VideoProcessingTask

__all__ = [
    "CogVideoXVideoProvider",
    "ComfyUiVideoProvider",
    "FFmpegVideoProcessor",
    "LocalHttpVideoProvider",
    "OpenAIVideoProvider",
    "RunwayVideoProvider",
    "SVDVideoProvider",
    "VideoConfig",
    "VideoGenerationAuthenticationError",
    "VideoGenerationError",
    "VideoGenerationProvider",
    "VideoGenerationTask",
    "VideoModule",
    "VideoProcessingConfig",
    "VideoProcessingTask",
    "VideoTimeoutError",
    "Wan22VideoProvider",
]
