"""Beat-analysis provider backends."""

from __future__ import annotations

from oridecon.multimedia.beat.providers.librosa import LibrosaBeatAnalysisProvider
from oridecon.multimedia.beat.providers.madmom import MadmomBeatAnalysisProvider

__all__ = ["LibrosaBeatAnalysisProvider", "MadmomBeatAnalysisProvider"]
