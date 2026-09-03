"""Umbrella module for dependency injection."""

from __future__ import annotations

from typing import Any

from oridecon.contracts.multimedia.protocols import (
    BeatAnalysisProvider,
    ImageProvider,
    InterpolationProvider,
    MusicProvider,
    TTSProvider,
    UpscaleProvider,
    VideoProvider,
)
from oridecon.di.module import DynamicModule, Module, module
from oridecon.multimedia.config import MultimediaConfig


@module()
class MultimediaModule(Module):
    """Audio/video/image generation: TTS, music, video, image, upscale,
    interpolate, and beat-analysis subsystems.
    """

    @classmethod
    def configure(cls, config: MultimediaConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.di.provider import MultimediaProvider

        return DynamicModule(
            module=cls,
            providers=[MultimediaProvider(config=config)],
            exports=[
                TTSProvider,
                MusicProvider,
                VideoProvider,
                ImageProvider,
                UpscaleProvider,
                InterpolationProvider,
                BeatAnalysisProvider,
            ],
        )

    @classmethod
    def stub(cls, config: MultimediaConfig | None = None) -> DynamicModule:
        from importlib.metadata import entry_points

        from oridecon.multimedia.beat.module import BeatAnalysisModule
        from oridecon.multimedia.constants import CORE_SUBSYSTEMS
        from oridecon.multimedia.image.module import ImageModule
        from oridecon.multimedia.interpolate.module import InterpolationModule
        from oridecon.multimedia.music.module import AudioMusicModule
        from oridecon.multimedia.tts.module import AudioTTSModule
        from oridecon.multimedia.upscale.module import UpscaleModule
        from oridecon.multimedia.video.module import VideoModule

        effective = config or MultimediaConfig()
        stub_imports: list[Any] = [
            AudioTTSModule.stub(effective.tts),
            AudioMusicModule.stub(effective.music),
            VideoModule.stub(effective.video),
            ImageModule.stub(effective.image),
            UpscaleModule.stub(effective.upscale),
            InterpolationModule.stub(effective.interpolate),
            BeatAnalysisModule.stub(effective.beat),
        ]

        for ep in entry_points(group="oridecon.multimedia.modules"):
            if ep.name in CORE_SUBSYSTEMS:
                continue
            try:
                stub_imports.append(ep.load().stub())
            except (AttributeError, ImportError, RuntimeError):
                pass

        return DynamicModule(
            module=cls,
            imports=stub_imports,
            exports=[
                TTSProvider,
                MusicProvider,
                VideoProvider,
                ImageProvider,
                UpscaleProvider,
                InterpolationProvider,
                BeatAnalysisProvider,
            ],
        )


__all__ = ["MultimediaModule"]
