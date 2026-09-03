"""HTTP-specific sanitization package for oridecon-web.

Contains header sanitization (CRLF injection prevention).
Transport-agnostic sanitization (HTML, URL, filename) lives in
``oridecon.security.sanitization`` (core).
"""

from __future__ import annotations

from oridecon.web.security.sanitization.header import HeaderSanitizer

__all__ = ["HeaderSanitizer"]
