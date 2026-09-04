"""Explicit capability type for already-sanitized or framework-owned HTML."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TrustedHTML:
    """Markup that may cross the renderer's verbatim-output boundary.

    ``source`` identifies the sanitizer, template, or owned static producer
    responsible for the value. It is audit metadata, not sanitization: callers
    must never grant trust directly to unvalidated user input.
    """

    value: str
    source: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("TrustedHTML value must be a string")
        if not isinstance(self.source, str) or not self.source.strip():
            raise ValueError("TrustedHTML requires a non-empty source")

    def __html__(self) -> str:
        """Return the explicitly trusted markup verbatim."""
        return self.value

    def __str__(self) -> str:
        """Preserve compatibility with HTML response and template adapters."""
        return self.value


def trusted_html(value: str, *, source: str) -> TrustedHTML:
    """Grant explicit verbatim-markup trust with attributable ownership."""
    return TrustedHTML(value=value, source=source)


__all__ = ["TrustedHTML", "trusted_html"]
