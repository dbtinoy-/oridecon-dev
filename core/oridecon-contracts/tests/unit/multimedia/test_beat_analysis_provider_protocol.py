from oridecon.contracts.core.result import Ok, Result
from oridecon.contracts.multimedia.exceptions import MultimediaError
from oridecon.contracts.multimedia.protocols import BeatAnalysisProvider
from oridecon.contracts.multimedia.types import (
    BeatAnalysisRequest,
    BeatAnalysisResult,
    MediaAsset,
)


class _FakeBeatAnalysisProvider:
    async def analyze(self, request):
        return Ok(BeatAnalysisResult(tempo_bpm=128.0, beat_timestamps=[0.0, 0.47]))


async def test_fake_provider_satisfies_protocol() -> None:
    provider: BeatAnalysisProvider = _FakeBeatAnalysisProvider()
    asset = MediaAsset(mime_type="audio/mpeg", provider="test", bytes_data=b"audio")
    result: Result[BeatAnalysisResult, MultimediaError] = await provider.analyze(
        BeatAnalysisRequest(asset=asset)
    )
    assert result.is_ok()
    assert result.unwrap().tempo_bpm == 128.0


def test_isinstance_check_via_runtime_checkable() -> None:
    assert isinstance(_FakeBeatAnalysisProvider(), BeatAnalysisProvider)
