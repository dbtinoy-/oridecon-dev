from oridecon.contracts.multimedia.exceptions import TTSError
from oridecon.multimedia.tts.exceptions import TTSAuthenticationError


def test_package_errors_extend_contracts_tts_error() -> None:
    assert issubclass(TTSAuthenticationError, TTSError)
