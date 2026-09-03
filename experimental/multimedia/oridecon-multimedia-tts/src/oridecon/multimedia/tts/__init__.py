"""Text-to-speech generation subsystem for the Oridecon multimedia package family."""

from __future__ import annotations

from oridecon.multimedia.tts.config import TTSConfig
from oridecon.multimedia.tts.di import AudioTTSProvider
from oridecon.multimedia.tts.exceptions import TTSAuthenticationError
from oridecon.multimedia.tts.module import AudioTTSModule
from oridecon.multimedia.tts.providers import (
    ChatterboxTTSProvider,
    ElevenLabsTTSProvider,
    F5TTSProvider,
    KokoroTTSProvider,
    LocalHttpTTSProvider,
    OpenAITTSProvider,
    PiperTTSProvider,
)
from oridecon.multimedia.tts.tasks import TTSGenerationTask

__all__ = [
    "AudioTTSModule",
    "AudioTTSProvider",
    "ChatterboxTTSProvider",
    "ElevenLabsTTSProvider",
    "F5TTSProvider",
    "KokoroTTSProvider",
    "LocalHttpTTSProvider",
    "OpenAITTSProvider",
    "PiperTTSProvider",
    "TTSAuthenticationError",
    "TTSConfig",
    "TTSGenerationTask",
]
