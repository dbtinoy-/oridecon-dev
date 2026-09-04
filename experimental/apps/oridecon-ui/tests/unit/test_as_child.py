"""Tests for asChild polymorphic rendering."""

from __future__ import annotations

from typing import Any

from oridecon.ui.core.base import Component, el
from oridecon.ui.core.slot import Slot


class Button(Component):
    tag = "button"

    def __init__(self, label: str = "", **kwargs) -> None:
        super().__init__(**kwargs)
        self.label = label

    def render(self) -> Any:
        return el(self.tag, self.label or "", class_="btn", **self.props)


class Link(Component):
    tag = "a"

    def __init__(self, text: str = "", **kwargs) -> None:
        super().__init__(**kwargs)
        self.text = text

    def render(self) -> Any:
        return el(self.tag, self.text or "", href="#", class_="link", **self.props)


def test_button_renders_as_link_with_as_child():
    """Button renders as <a> when as_child=True with Link child."""
    link = Link("click me")
    btn = Button(as_child=True, children=[link])
    html = btn.__html__()
    assert "<a" in html
    assert 'href="#' in html
    assert "click me" in html
    assert "btn" not in html  # Button's class should not appear


def test_as_child_clones_before_merging_parent_props():
    """Polymorphic rendering must not mutate or contaminate a reused child."""
    link = Link("click me", title="child title")
    original_props = dict(link.props)
    original_children = list(link.children)

    html = Button(
        as_child=True,
        children=[link],
        title="parent title",
        data_source="first-parent",
    ).__html__()

    assert 'title="child title"' in html
    assert 'data-source="first-parent"' in html
    assert link.props == original_props
    assert link.children == original_children

    reused = Button(as_child=True, children=[link]).__html__()
    assert "data-source" not in reused


def test_as_child_falls_back_to_normal_render():
    """Without as_child, button renders normally."""
    btn = Button("save")
    html = btn.__html__()
    assert "<button" in html
    assert "save" in html


def test_as_child_with_slot():
    """Slot child delegates one typed element without flattening it."""
    slot = Slot(el("a", "Open", href="/details"), class_name="slotted")
    btn = Button(as_child=True, children=[slot])
    html = btn.__html__()
    assert html == '<a href="/details" class="slotted">Open</a>'


def test_as_child_with_no_children():
    """With as_child=True but no children, falls through to normal render."""
    btn = Button("fallback", as_child=True)
    html = btn.__html__()
    assert "<button" in html
