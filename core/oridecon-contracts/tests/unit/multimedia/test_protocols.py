from oridecon.contracts.core.result import Ok, Result
from oridecon.contracts.multimedia.exceptions import MultimediaError
from oridecon.contracts.multimedia.protocols import (
    ImageProvider,
    MusicProvider,
    TTSProvider,
    VideoProvider,
)
from oridecon.contracts.multimedia.types import ImageRequest, MediaAsset, TTSRequest


class _FakeTTS:
    async def generate(self, request: TTSRequest) -> Result[MediaAsset, MultimediaError]:
        return Ok(MediaAsset(mime_type="audio/mpeg", provider="fake", bytes_data=b"x"))


def test_fake_tts_satisfies_protocol_structurally() -> None:
    assert isinstance(_FakeTTS(), TTSProvider)


def test_all_four_protocols_share_generate_method_name() -> None:
    for proto in (TTSProvider, MusicProvider, VideoProvider, ImageProvider):
        assert hasattr(proto, "generate")
