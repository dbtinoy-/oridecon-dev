"""Image generation exceptions for the oridecon-multimedia-image package."""

from __future__ import annotations

from oridecon.contracts.multimedia.exceptions import ImageGenerationError

__all__ = [
    "ImageGenerationAuthenticationError",
    "ImageGenerationError",
    "ImageTimeoutError",
]


class ImageTimeoutError(ImageGenerationError):
    """Raised when an image generation operation exceeds its timeout."""

    _code = "ORI_ERR_MM_IMAGE_001"


class ImageGenerationAuthenticationError(ImageGenerationError):
    """Raised when the image backend rejects the configured API credentials."""

    _code = "ORI_ERR_MM_IMAGE_002"
