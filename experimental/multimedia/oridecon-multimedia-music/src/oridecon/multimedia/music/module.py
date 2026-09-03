"""Music generation module for dependency injection."""

from __future__ import annotations

from oridecon.contracts.multimedia.protocols import MusicProvider
from oridecon.di.module import DynamicModule, Module, module
from oridecon.multimedia.music.config import MusicConfig
from oridecon.multimedia.music.tasks import MusicGenerationTask


@module()
class AudioMusicModule(Module):
    """Music generation integration."""

    @classmethod
    def configure(cls, config: MusicConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.music.di.provider import AudioMusicProvider

        return DynamicModule(
            module=cls,
            providers=[AudioMusicProvider(config=config)],
            exports=[MusicProvider, MusicGenerationTask],
        )

    @classmethod
    def stub(cls, config: MusicConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.music.di.provider import AudioMusicProvider

        return DynamicModule(
            module=cls,
            providers=[
                AudioMusicProvider(config=config or MusicConfig(backend="local-http"))
            ],
            exports=[MusicProvider, MusicGenerationTask],
        )


__all__ = ["AudioMusicModule"]
