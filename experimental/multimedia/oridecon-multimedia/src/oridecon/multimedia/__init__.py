"""Oridecon Multimedia — generation umbrella package.

Install `oridecon-multimedia` to get the full multimedia subsystem.
Import from sub-packages for granular control.
"""

from __future__ import annotations

import pkgutil

# Critical: enable namespace-package discovery for oridecon.multimedia.*
# sibling distributions (tts, music, video, image).
__path__ = pkgutil.extend_path(__path__, __name__)

from oridecon.multimedia.accessors import (
    ComposeAccessor,
    SubsystemAccessor,
    VideoAccessor,
)
from oridecon.multimedia.config import MultimediaConfig
from oridecon.multimedia.di.provider import MultimediaProvider
from oridecon.multimedia.events import MultimediaGenerationEvent
from oridecon.multimedia.module import MultimediaModule
from oridecon.multimedia.timeline import Timeline, TimelineRenderTask
from oridecon.multimedia.types import JobHandle

__all__ = [
    "ComposeAccessor",
    "JobHandle",
    "MultimediaConfig",
    "MultimediaGenerationEvent",
    "MultimediaModule",
    "MultimediaProvider",
    "SubsystemAccessor",
    "Timeline",
    "TimelineRenderTask",
    "VideoAccessor",
]
