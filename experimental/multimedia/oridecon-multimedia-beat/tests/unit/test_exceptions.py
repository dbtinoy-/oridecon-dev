from oridecon.contracts.multimedia.exceptions import BeatAnalysisError
from oridecon.multimedia.beat.exceptions import BeatAnalysisDecodeError


def test_beat_analysis_leaf_errors_extend_beat_analysis_error() -> None:
    for exc_cls, code in (
        (BeatAnalysisDecodeError, "ORI_ERR_MM_BEAT_003"),
    ):
        assert issubclass(exc_cls, BeatAnalysisError)
        assert exc_cls._code == code
