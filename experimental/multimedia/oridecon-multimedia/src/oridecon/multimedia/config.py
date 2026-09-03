"""Umbrella configuration for the multimedia subsystem."""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from oridecon.config import BaseConfig
from oridecon.contracts.core.config import Environment
from oridecon.multimedia.beat.config import BeatAnalysisConfig
from oridecon.multimedia.image.config import ImageConfig
from oridecon.multimedia.interpolate.config import InterpolationConfig
from oridecon.multimedia.music.config import MusicConfig
from oridecon.multimedia.tts.config import TTSConfig
from oridecon.multimedia.upscale.config import UpscaleConfig
from oridecon.multimedia.video.config import VideoConfig
from oridecon.validation import Field


@dataclass(init=False)
class MultimediaConfig(BaseConfig):
    """Umbrella configuration for the multimedia subsystem."""

    config_section: ClassVar[str] = "multimedia"
    name: str = "multimedia"
    enabled: bool = True
    env: Environment | None = Field(None, description="Deployment environment")
    tts: TTSConfig = Field(default_factory=TTSConfig)
    music: MusicConfig = Field(default_factory=MusicConfig)
    video: VideoConfig = Field(default_factory=VideoConfig)
    image: ImageConfig = Field(default_factory=ImageConfig)
    upscale: UpscaleConfig = Field(default_factory=UpscaleConfig)
    interpolate: InterpolationConfig = Field(default_factory=InterpolationConfig)
    beat: BeatAnalysisConfig = Field(default_factory=BeatAnalysisConfig)
    storage_path_prefix: str = "multimedia/"
    cache_results: bool = False


__all__ = ["MultimediaConfig"]
