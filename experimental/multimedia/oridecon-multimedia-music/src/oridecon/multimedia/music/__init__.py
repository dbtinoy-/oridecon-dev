"""Music generation subsystem for the Oridecon multimedia package family."""

from __future__ import annotations

from oridecon.multimedia.music.config import MusicConfig
from oridecon.multimedia.music.di import AudioMusicProvider
from oridecon.multimedia.music.module import AudioMusicModule
from oridecon.multimedia.music.providers import (
    AceStepMusicProvider,
    LocalHttpMusicProvider,
    StabilityAudioMusicProvider,
    StableAudioOpenMusicProvider,
)
from oridecon.multimedia.music.tasks import MusicGenerationTask

__all__ = [
    "AceStepMusicProvider",
    "AudioMusicModule",
    "AudioMusicProvider",
    "LocalHttpMusicProvider",
    "MusicConfig",
    "MusicGenerationTask",
    "StabilityAudioMusicProvider",
    "StableAudioOpenMusicProvider",
]
