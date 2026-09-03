"""Text-to-speech package exceptions."""

from __future__ import annotations

from oridecon.contracts.multimedia.exceptions import TTSError

__all__ = ["TTSAuthenticationError", "TTSError"]


class TTSAuthenticationError(TTSError):
    """Invalid API key or credentials — infrastructure error, raised not wrapped."""

    _code = "ORI_ERR_MM_TTS_002"
