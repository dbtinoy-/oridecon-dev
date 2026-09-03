"""Input sanitization package."""

from __future__ import annotations

from oridecon.security.config import InputSanitizerConfig
from oridecon.security.sanitization.sanitizer import InputSanitizer

__all__ = ["InputSanitizer", "InputSanitizerConfig"]
