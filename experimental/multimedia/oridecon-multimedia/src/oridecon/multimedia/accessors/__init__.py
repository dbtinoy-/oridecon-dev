"""Accessors exposing multimedia capabilities — sync and queued.

``SubsystemAccessor`` wraps one sub-provider's backend + task manager +
storage normalizer; ``VideoAccessor`` composes generation and processing
accessors for the video subsystem; ``ComposeAccessor`` exposes timeline
rendering — sync and queued — under ``multimedia.compose``; ``BeatAccessor``
exposes sync-only beat analysis under ``multimedia.beat``.
"""

from oridecon.multimedia.accessors.beat import BeatAccessor
from oridecon.multimedia.accessors.compose import ComposeAccessor
from oridecon.multimedia.accessors.subsystem import SubsystemAccessor
from oridecon.multimedia.accessors.video import VideoAccessor

__all__ = ["BeatAccessor", "ComposeAccessor", "SubsystemAccessor", "VideoAccessor"]
