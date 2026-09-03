"""Upscale provider backends."""

from __future__ import annotations

from oridecon.multimedia.upscale.providers.hat import HatUpscaleProvider
from oridecon.multimedia.upscale.providers.real_esrgan import RealEsrganUpscaleProvider

__all__ = ["HatUpscaleProvider", "RealEsrganUpscaleProvider"]
