from oridecon.contracts.multimedia.exceptions import ImageGenerationError
from oridecon.multimedia.image.exceptions import (
    ImageGenerationAuthenticationError,
    ImageTimeoutError,
)


def test_package_errors_extend_contracts_image_error() -> None:
    assert issubclass(ImageTimeoutError, ImageGenerationError)
    assert issubclass(ImageGenerationAuthenticationError, ImageGenerationError)


def test_error_codes_are_dedicated_not_inherited() -> None:
    assert ImageTimeoutError().code == "ORI_ERR_MM_IMAGE_001"
    assert ImageGenerationAuthenticationError().code == "ORI_ERR_MM_IMAGE_002"
