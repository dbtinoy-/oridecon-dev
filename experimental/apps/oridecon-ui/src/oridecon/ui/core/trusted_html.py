"""Explicit capability type for already-sanitized or framework-owned HTML.

``TrustedHTML`` is the only final-state arbitrary verbatim string type in
Oridecon UI. It subclasses ``str`` so template engines (Jinja) and response
adapters treat it as a safe string through ``__html__``, exactly like the
legacy ``markupsafe.Markup`` did — but with mandatory attributable ownership
and no silent import.

``source`` identifies the sanitizer, template, or owned static producer
responsible for the value. It is audit metadata, not sanitization: callers
must never grant trust directly to unvalidated user input.
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError
from typing import Any


class TrustedHTML(str):
    """An escape-safe string with mandatory attributable ownership.

    Immutable: attempts to replace ``source`` (or normal ``str`` mutation
    paths) raise :class:`FrozenInstanceError`, matching the dataclass
    semantics the capability had when it was introduced.
    """

    __slots__ = ("source",)

    @property
    def value(self) -> str:
        """Return the trusted markup string (compatibility accessor)."""
        return str.__str__(self)

    def __new__(cls, value: str, source: str) -> "TrustedHTML":
        if not isinstance(value, str):
            raise TypeError("TrustedHTML value must be a string")
        if not isinstance(source, str) or not source.strip():
            raise ValueError("TrustedHTML requires a non-empty source")
        instance = super().__new__(cls, value)
        object.__setattr__(instance, "source", source)
        return instance

    def __setattr__(self, name: str, value: Any) -> None:
        raise FrozenInstanceError(
            f"cannot assign to field {name!r}: TrustedHTML is immutable"
        )

    def __html__(self) -> str:
        """Return the explicitly trusted markup verbatim (Jinja-safe)."""
        return str(self)

    def __str__(self) -> str:
        """Return the string value (``str`` subclass)."""
        return str.__str__(self)

    def __repr__(self) -> str:
        return f"TrustedHTML({str.__str__(self)!r}, source={self.source!r})"


def trusted_html(value: str, *, source: str) -> TrustedHTML:
    """Grant explicit verbatim-markup trust with attributable ownership."""
    return TrustedHTML(value=value, source=source)


def trusted_template_output(value: str, *, template: str) -> TrustedHTML:
    """Trust markup produced by a template engine at its output boundary.

    The caller must record the template's autoescape policy in the template
    name/owner so review can confirm user data cannot reach the output raw.
    """
    return TrustedHTML(value=value, source=f"template output ({template})")


def trusted_svg_icon(value: str, *, name: str) -> TrustedHTML:
    """Trust an owned, versioned SVG icon definition (framework assets only)."""
    return TrustedHTML(value=value, source=f"owned SVG icon ({name})")


def trusted_static_script(value: str, *, asset: str) -> TrustedHTML:
    """Trust a shipped static script rendered inline at a named boundary."""
    return TrustedHTML(value=value, source=f"static script ({asset})")


__all__ = [
    "TrustedHTML",
    "trusted_html",
    "trusted_static_script",
    "trusted_svg_icon",
    "trusted_template_output",
]
