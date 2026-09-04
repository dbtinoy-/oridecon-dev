"""Unified render-boundary tests: strings are data at every depth.

Covers the audit acceptance criteria for the one-renderer policy
(docs/09-04-2026/02 §3 and §8):
- top-level and component-returned strings are escaped;
- only source-attributed ``TrustedHTML`` renders verbatim;
- legacy ``raw()``/``Markup`` survive one migration window with warnings;
- ``children=`` misuse has a targeted diagnostic;
- two same-type components inside one response scope get unique, stable IDs.
"""

from __future__ import annotations

import warnings

import pytest
from markupsafe import Markup

from oridecon.ui.core.base import (
    Component,
    el,
    fragment,
    raw,
    render_to_string,
)
from oridecon.ui.core.trusted_html import trusted_html
from oridecon.ui.core.render_context import (
    RenderContext,
    RenderScope,
    get_render_scope,
    render_context,
)

PAYLOADS = [
    "<script>alert(1)</script>",
    '<img src=x onerror=alert(1)>',
    "</script><script>alert(2)</script>",
    "<b data-x='\"'>&amp;</b>",
]


def _escaped(payload: str) -> str:
    """Reference html.escape with quote=False (text context)."""
    import html

    return html.escape(payload, quote=False)


class _StringRenderer(Component):
    def render(self):
        return "<b>" + self.props["data"] + "</b>"


class _ElementRenderer(Component):
    def render(self):
        return el("b", self.props["data"])


class TestStringsAreDataEverywhere:
    @pytest.mark.parametrize("payload", PAYLOADS)
    def test_top_level_string_escaped(self, payload: str) -> None:
        assert render_to_string(payload) == _escaped(payload)

    @pytest.mark.parametrize("payload", PAYLOADS)
    def test_component_string_result_escaped_top_level(self, payload: str) -> None:
        out = render_to_string(_StringRenderer(data=payload))
        assert _escaped(payload) in out
        assert "<b>" not in out
        assert "<script>" not in out

    @pytest.mark.parametrize("payload", PAYLOADS)
    def test_component_string_result_escaped_as_child(self, payload: str) -> None:
        out = render_to_string(el("td", _StringRenderer(data=payload)))
        assert _escaped(f"<b>{payload}</b>") in out
        assert "<b>" not in out
        assert "<script>" not in out

    @pytest.mark.parametrize("payload", PAYLOADS)
    def test_element_structure_keeps_real_nodes(self, payload: str) -> None:
        out = render_to_string(_ElementRenderer(data=payload))
        assert out == f"<b>{_escaped(payload)}</b>"

    def test_iterable_of_strings_escaped(self) -> None:
        out = render_to_string([f"<i>{item}</i>" for item in ("a", "b")])
        assert "&lt;i&gt;a&lt;/i&gt;" in out
        assert "<i>" not in out

    def test_nested_component_chain_escaped(self) -> None:
        class Outer(Component):
            def render(self):
                return el("div", _StringRenderer(data="<x>"))

        out = render_to_string(Outer())
        assert "&lt;b&gt;&lt;x&gt;&lt;/b&gt;" in out


class TestTrustedHtmlIsTheOnlyArbitraryVerbatimType:
    @pytest.fixture(autouse=True)
    def _fresh_deprecation_warnings(self) -> None:
        from oridecon.ui.core import base as ui_base

        ui_base._deprecation_warned.clear()

    def test_trusted_html_verbatim_top_level(self) -> None:
        value = trusted_html("<b>ok</b>", source="test sanitizer")
        assert render_to_string(value) == "<b>ok</b>"

    def test_trusted_html_verbatim_as_child(self) -> None:
        value = trusted_html("<b>ok</b>", source="test sanitizer")
        assert render_to_string(el("div", value)) == "<div><b>ok</b></div>"

    def test_arbitrary_html_object_is_not_trusted(self) -> None:
        class Forged:
            def __html__(self) -> str:
                return "<script>forged()</script>"

        out = render_to_string(el("div", Forged()))
        assert "<script>" not in out

    def test_markup_compat_warns_and_passes_verbatim(self) -> None:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            out = render_to_string(el("div", Markup("<b>legacy</b>")))
        assert any(issubclass(w.category, DeprecationWarning) for w in caught)
        assert out == "<div><b>legacy</b></div>"

    def test_raw_compat_warns_and_passes_verbatim(self) -> None:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            out = render_to_string(el("div", raw("<b>legacy</b>")))
        assert any(issubclass(w.category, DeprecationWarning) for w in caught)
        assert out == "<div><b>legacy</b></div>"

    def test_markup_top_level_warns_and_passes_verbatim(self) -> None:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            out = render_to_string(Markup("<b>legacy</b>"))
        assert any(issubclass(w.category, DeprecationWarning) for w in caught)
        assert out == "<b>legacy</b>"


class TestChildrenKeywordDiagnostics:
    def test_el_rejects_children_keyword(self) -> None:
        with pytest.raises(TypeError, match="children="):
            el("div", children=[el("span")])  # type: ignore[call-arg]

    def test_component_children_keyword_warns(self) -> None:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            comp = _StringRenderer(children=["x"], data="y")  # type: ignore[arg-type]
        assert any(issubclass(w.category, DeprecationWarning) for w in caught)
        assert comp.children == ["x"]

    def test_fragment_helper_builds_ordered_sequence(self) -> None:
        values = fragment("a", el("b", "c"))
        assert render_to_string(values) == "a<b>c</b>"


class TestResponseWideRenderScope:
    def test_two_components_share_one_response_scope(self) -> None:
        with render_context(RenderContext(scope=RenderScope())):
            ids = [get_render_scope().id("tab", key=None) for _ in range(2)]
        assert len(set(ids)) == 2

    def test_same_explicit_key_in_one_scope_raises(self) -> None:
        with render_context(RenderContext(scope=RenderScope())):
            get_render_scope().id("tab", key="users")
            with pytest.raises(ValueError, match="Duplicate"):
                get_render_scope().id("tab", key="users")

    def test_identical_keys_different_scopes_do_not_raise(self) -> None:
        first = get_render_scope().id("tab", key="users")
        second = get_render_scope().id("tab", key="users")
        assert first == second
