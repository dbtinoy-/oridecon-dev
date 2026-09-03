"""TTS module for dependency injection."""

from __future__ import annotations

from oridecon.contracts.multimedia.protocols import TTSProvider
from oridecon.di.module import DynamicModule, Module, module
from oridecon.multimedia.tts.config import TTSConfig
from oridecon.multimedia.tts.tasks import TTSGenerationTask


@module()
class AudioTTSModule(Module):
    """Text-to-speech generation integration."""

    @classmethod
    def configure(cls, config: TTSConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.tts.di.provider import AudioTTSProvider

        return DynamicModule(
            module=cls,
            providers=[AudioTTSProvider(config=config)],
            exports=[TTSProvider, TTSGenerationTask],
        )

    @classmethod
    def stub(cls, config: TTSConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.tts.di.provider import AudioTTSProvider

        return DynamicModule(
            module=cls,
            providers=[
                AudioTTSProvider(config=config or TTSConfig(backend="local-http"))
            ],
            exports=[TTSProvider, TTSGenerationTask],
        )


__all__ = ["AudioTTSModule"]
