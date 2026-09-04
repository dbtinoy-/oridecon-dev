"""Strict Slot composition contract."""

from __future__ import annotations

from typing import Any

import pytest

from oridecon.ui.attributes import expression
from oridecon.ui.core.base import Component, Element, el, render_to_string
from oridecon.ui.core.slot import Slot
from oridecon.ui.core.trusted_html import trusted_html


class _ElementComponent(Component):
    def render(self) -> Element:
        return Element("a", "world", href="/child", class_="child shared")


class _TextComponent(Component):
    def render(self) -> str:
        return "<strong>text is not a root</strong>"


class _FragmentComponent(Component):
    def render(self) -> list[Element]:
        return [Element("span", "one"), Element("span", "two")]


class TestSlotRootContract:
    def test_requires_a_child(self) -> None:
        with pytest.raises(TypeError, match="required positional argument"):
            Slot()  # type: ignore[call-arg]

    @pytest.mark.parametrize(
        "child",
        [
            pytest.param("text", id="text"),
            pytest.param([el("span", "one")], id="single-item-fragment"),
            pytest.param(
                trusted_html("<b>trusted</b>", source="test fixture"),
                id="trusted-html",
            ),
            pytest.param(_TextComponent(), id="text-component"),
            pytest.param(_FragmentComponent(), id="multi-root-component"),
        ],
    )
    def test_rejects_non_element_roots(self, child: Any) -> None:
        with pytest.raises(TypeError, match="exactly one Element root"):
            Slot(child).render()

    def test_resolves_a_component_to_one_element(self) -> None:
        output = render_to_string(Slot(_ElementComponent()))

        assert output == '<a href="/child" class="child shared">world</a>'


class TestSlotAttributeMerge:
    def test_merges_and_deduplicates_classes_in_child_order(self) -> None:
        child = el("button", "Save", class_="child shared")

        output = render_to_string(
            Slot(
                child,
                attrs={"class": "parent shared"},
                class_name="extra child",
            )
        )

        assert 'class="child shared parent extra"' in output

    def test_ordinary_attributes_are_child_wins(self) -> None:
        child = el("button", "Save", title="child")

        output = render_to_string(
            Slot(child, attrs={"title": "parent", "data_source": "slot"})
        )

        assert 'title="child"' in output
        assert 'data-source="slot"' in output

    @pytest.mark.parametrize("name", ["id", "name", "value", "href", "type"])
    def test_sensitive_attribute_conflicts_require_override(self, name: str) -> None:
        child = el("a", "Open", **{name: "child"})

        with pytest.raises(ValueError, match=rf"Conflicting Slot attribute '{name}'"):
            Slot(child, attrs={name: "slot"}).render()

    def test_explicit_override_replaces_sensitive_attribute(self) -> None:
        child = el("a", "Open", href="/child")

        output = render_to_string(
            Slot(child, attrs={"href": "/slot"}, overrides={"href"})
        )

        assert 'href="/slot"' in output
        assert 'href="/child"' not in output

    def test_attribute_alias_conflicts_are_rejected(self) -> None:
        child = Element("div", class_="one", **{"class": "two"})

        with pytest.raises(ValueError, match="aliases"):
            Slot(child).render()

    def test_merge_never_mutates_the_child(self) -> None:
        child = el("a", "Open", href="/child", class_="child")
        original_attrs = dict(child.attrs)
        original_children = list(child.children)
        slot = Slot(child, attrs={"data_owner": "slot"}, class_name="parent")

        first = slot.render()
        second = slot.render()

        assert first is not child
        assert second is not child
        assert first is not second
        assert child.attrs == original_attrs
        assert child.children == original_children
        assert "data-owner" in first.attrs
        assert "data-owner" in second.attrs


class TestSlotSemanticMerges:
    def test_style_dictionaries_merge_with_child_precedence(self) -> None:
        child = el("div", style={"color": "red"})

        output = render_to_string(
            Slot(child, attrs={"style": {"color": "blue", "display": "grid"}})
        )

        assert 'style="color: red; display: grid"' in output

    @pytest.mark.parametrize(
        ("child_style", "slot_style"),
        [
            ("color: red", "display: grid"),
            ("color: red", {"display": "grid"}),
            ({"color": "red"}, "display: grid"),
        ],
    )
    def test_conflicting_style_representations_raise(
        self, child_style: Any, slot_style: Any
    ) -> None:
        child = el("div", style=child_style)

        with pytest.raises(ValueError, match="style"):
            Slot(child, attrs={"style": slot_style}).render()

    def test_identical_style_strings_are_allowed(self) -> None:
        child = el("div", style="color: red")

        output = render_to_string(Slot(child, attrs={"style": "color: red"}))

        assert 'style="color: red"' in output

    @pytest.mark.parametrize("name", ["aria-describedby", "aria-labelledby"])
    def test_token_accessibility_attributes_merge(self, name: str) -> None:
        child = el("button", "Open", **{name: "child shared"})

        output = render_to_string(Slot(child, attrs={name: "slot shared"}))

        assert f'{name}="child shared slot"' in output

    def test_scalar_accessibility_conflicts_raise(self) -> None:
        child = el("button", "Open", **{"aria-label": "Child"})

        with pytest.raises(ValueError, match="accessibility"):
            Slot(child, attrs={"aria_label": "Slot"}).render()

    def test_ref_is_preserved_or_added(self) -> None:
        child_output = render_to_string(Slot(el("div", x_ref="child")))
        slot_output = render_to_string(Slot(el("div"), ref="slot"))

        assert 'x-ref="child"' in child_output
        assert 'x-ref="slot"' in slot_output

    def test_multiple_refs_raise(self) -> None:
        child = el("div", x_ref="child")

        with pytest.raises(ValueError, match="multiple refs"):
            Slot(child, ref="slot").render()


class TestSlotEvents:
    def test_event_values_must_be_typed(self) -> None:
        with pytest.raises(TypeError, match="AlpineExpression"):
            Slot(
                el("button", "Save"),
                events={"click": "save()"},  # type: ignore[dict-item]
            ).render()

    def test_adds_a_typed_event(self) -> None:
        output = render_to_string(
            Slot(el("button", "Save"), events={"click": expression("save()")})
        )

        assert 'x-on:click="save()"' in output

    def test_composes_typed_events_child_then_slot(self) -> None:
        child = el("button", "Save", **{"x-on:click": expression("validate()")})

        output = render_to_string(Slot(child, events={"click": expression("save()")}))

        assert 'x-on:click="validate(); save()"' in output

    def test_refuses_to_concatenate_an_untyped_child_event(self) -> None:
        child = el("button", "Save", **{"x-on:click": "validate()"})

        with pytest.raises(TypeError, match="untyped string event"):
            Slot(child, events={"click": expression("save()")}).render()

    def test_events_cannot_hide_in_generic_attrs(self) -> None:
        with pytest.raises(TypeError, match="events="):
            Slot(el("button", "Save"), attrs={"x-on:click": "save()"}).render()
