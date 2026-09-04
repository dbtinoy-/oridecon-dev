"""Tests for ErrorBoundary molecule."""

from __future__ import annotations

from oridecon.ui.core.base import Component, Element, el
from oridecon.ui.core.trusted_html import TrustedHTML
from oridecon.ui.molecules.error_boundary import ErrorBoundary


class TestErrorBoundary:
    def test_renders_children_normally(self) -> None:
        boundary = ErrorBoundary()
        boundary.children = [el("span", "Hello")]
        result = str(boundary)
        assert "Hello" in result

    def test_catches_render_error_uses_default_fallback(self) -> None:
        class Broken(Component):
            def render(self):
                msg = "broken"
                raise RuntimeError(msg)

        boundary = ErrorBoundary()
        boundary.children = [Broken()]
        result = str(boundary)
        assert "Rendering Error" in result

    def test_catches_render_error_uses_custom_fallback(self) -> None:
        class Broken(Component):
            def render(self):
                raise RuntimeError("broken")

        boundary = ErrorBoundary(fallback=el("div", "Custom Error"))
        boundary.children = [Broken()]
        result = str(boundary)
        assert "Custom Error" in result
        assert "Rendering Error" not in result

    def test_concrete_child_output_has_attributed_trust(self) -> None:
        boundary = ErrorBoundary()
        boundary.children = [el("span", "Hello")]

        result = boundary.render()

        assert isinstance(result, Element)
        assert isinstance(result.children[0], TrustedHTML)
        assert result.children[0].source == "ErrorBoundary concrete child renderer"

    def test_plain_child_markup_remains_escaped(self) -> None:
        boundary = ErrorBoundary()
        boundary.children = ['<img src=x onerror="window.pwned=true">']

        result = str(boundary)

        assert "<img" not in result
        assert "&lt;img src=x onerror=" in result

    def test_plain_component_result_remains_escaped(self) -> None:
        class UntrustedMarkup(Component):
            def render(self) -> str:
                return "<script>window.pwned=true</script>"

        boundary = ErrorBoundary()
        boundary.children = [UntrustedMarkup()]

        result = str(boundary)

        assert "<script>" not in result
        assert "&lt;script&gt;window.pwned=true&lt;/script&gt;" in result
