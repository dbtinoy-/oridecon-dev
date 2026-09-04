"""Explicit HTML trust grants are attributable and type constrained."""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest

from oridecon.ui.core.base import RawHTML, el, raw, render_to_string
from oridecon.ui.core.trusted_html import TrustedHTML, trusted_html


class _ForgedHtmlObject:
    __module__ = "htpy._elements"

    def __html__(self) -> str:
        return "<script>forgedTrust()</script>"

    def __str__(self) -> str:
        return '<img src=x onerror="forgedTrust()">'


class _ForeignRenderable:
    def render(self) -> str:
        return '<img src=x onerror="renderBypass()">'


class TestTrustedHTML:
    def test_requires_attributable_source(self) -> None:
        with pytest.raises(ValueError, match="non-empty source"):
            trusted_html("<strong>safe</strong>", source="  ")

    def test_requires_a_string_value(self) -> None:
        with pytest.raises(TypeError, match="value must be a string"):
            TrustedHTML(value=object(), source="test sanitizer")  # type: ignore[arg-type]

    def test_renders_verbatim_at_top_level_and_as_a_child(self) -> None:
        value = trusted_html("<strong>safe</strong>", source="test sanitizer")

        assert render_to_string(value) == "<strong>safe</strong>"
        assert render_to_string(el("div", value)) == (
            "<div><strong>safe</strong></div>"
        )

    def test_is_immutable(self) -> None:
        value = trusted_html("<b>safe</b>", source="test sanitizer")
        with pytest.raises(FrozenInstanceError):
            value.source = "different producer"  # type: ignore[misc]

    def test_legacy_raw_adapter_uses_the_typed_capability(self) -> None:
        value = raw("<em>legacy</em>")

        assert isinstance(value, RawHTML)
        assert isinstance(value, TrustedHTML)
        assert value.source == "legacy raw() compatibility adapter"
        assert not hasattr(value, "__dict__")
        with pytest.raises(FrozenInstanceError):
            value.value = "<script>changed()</script>"  # type: ignore[misc]
        assert render_to_string(el("div", value)) == "<div><em>legacy</em></div>"


class TestConcreteTrustBoundary:
    def test_arbitrary_html_method_does_not_grant_trust(self) -> None:
        output = render_to_string(el("div", _ForgedHtmlObject()))

        assert "<script>" not in output
        assert "<img " not in output
        assert "&lt;img src=x" in output

    def test_module_name_spoofing_does_not_grant_htpy_trust(self) -> None:
        output = render_to_string(_ForgedHtmlObject())

        assert "<script>" not in output
        assert output.startswith("&lt;img")

    def test_foreign_renderable_string_is_text_when_nested(self) -> None:
        output = render_to_string(el("div", _ForeignRenderable()))

        assert "<img " not in output
        assert "&lt;img src=x" in output

    def test_concrete_htpy_elements_remain_supported(self) -> None:
        from htpy import strong

        output = render_to_string(el("div", strong["safe < value"]))

        assert output == "<div><strong>safe &lt; value</strong></div>"
