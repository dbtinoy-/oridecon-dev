"""Video generation module for dependency injection."""

from __future__ import annotations

from oridecon.contracts.multimedia.protocols import VideoProcessor, VideoProvider
from oridecon.di.module import DynamicModule, Module, module
from oridecon.multimedia.video.config import VideoConfig
from oridecon.multimedia.video.tasks import VideoGenerationTask, VideoProcessingTask


@module()
class VideoModule(Module):
    """Video generation integration."""

    @classmethod
    def configure(cls, config: VideoConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.video.di.provider import VideoGenerationProvider

        return DynamicModule(
            module=cls,
            providers=[VideoGenerationProvider(config=config)],
            exports=[
                VideoProcessor,
                VideoProvider,
                VideoGenerationTask,
                VideoProcessingTask,
            ],
        )

    @classmethod
    def stub(cls, config: VideoConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.video.di.provider import VideoGenerationProvider

        return DynamicModule(
            module=cls,
            providers=[
                VideoGenerationProvider(
                    config=config or VideoConfig(backend="local-http")
                )
            ],
            exports=[
                VideoProcessor,
                VideoProvider,
                VideoGenerationTask,
                VideoProcessingTask,
            ],
        )


__all__ = ["VideoModule"]
