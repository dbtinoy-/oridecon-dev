"""Audio tempo/beat analysis subsystem for the Oridecon multimedia package family."""

from __future__ import annotations

from oridecon.multimedia.beat.config import BeatAnalysisConfig
from oridecon.multimedia.beat.di import BeatAnalysisGenerationProvider
from oridecon.multimedia.beat.exceptions import BeatAnalysisDecodeError
from oridecon.multimedia.beat.module import BeatAnalysisModule
from oridecon.multimedia.beat.providers import (
    LibrosaBeatAnalysisProvider,
    MadmomBeatAnalysisProvider,
)

__all__ = [
    "BeatAnalysisConfig",
    "BeatAnalysisDecodeError",
    "BeatAnalysisGenerationProvider",
    "BeatAnalysisModule",
    "LibrosaBeatAnalysisProvider",
    "MadmomBeatAnalysisProvider",
]
