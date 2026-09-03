"""Video generation backend providers."""

from __future__ import annotations

from oridecon.multimedia.video.providers.cogvideox import CogVideoXVideoProvider
from oridecon.multimedia.video.providers.comfyui import ComfyUiVideoProvider
from oridecon.multimedia.video.providers.local_http import LocalHttpVideoProvider
from oridecon.multimedia.video.providers.openai import OpenAIVideoProvider
from oridecon.multimedia.video.providers.runway import RunwayVideoProvider
from oridecon.multimedia.video.providers.svd import SVDVideoProvider
from oridecon.multimedia.video.providers.wan22 import Wan22VideoProvider

__all__ = [
    "CogVideoXVideoProvider",
    "ComfyUiVideoProvider",
    "LocalHttpVideoProvider",
    "OpenAIVideoProvider",
    "RunwayVideoProvider",
    "SVDVideoProvider",
    "Wan22VideoProvider",
]
