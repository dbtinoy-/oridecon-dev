"""TTS provider backends."""

from __future__ import annotations

from oridecon.multimedia.tts.providers.chatterbox import ChatterboxTTSProvider
from oridecon.multimedia.tts.providers.elevenlabs import ElevenLabsTTSProvider
from oridecon.multimedia.tts.providers.f5_tts import F5TTSProvider
from oridecon.multimedia.tts.providers.kokoro import KokoroTTSProvider
from oridecon.multimedia.tts.providers.local_http import LocalHttpTTSProvider
from oridecon.multimedia.tts.providers.openai import OpenAITTSProvider
from oridecon.multimedia.tts.providers.piper import PiperTTSProvider

__all__ = [
    "ChatterboxTTSProvider",
    "ElevenLabsTTSProvider",
    "F5TTSProvider",
    "KokoroTTSProvider",
    "LocalHttpTTSProvider",
    "OpenAITTSProvider",
    "PiperTTSProvider",
]
