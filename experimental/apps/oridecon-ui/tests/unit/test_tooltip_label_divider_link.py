"""Tests for Tooltip, Label, Divider, and Link atoms."""

from __future__ import annotations

import pytest

from oridecon.ui.atoms.divider import Divider
from oridecon.ui.atoms.label import Label
from oridecon.ui.atoms.link import Link
from oridecon.ui.atoms.tooltip import Tooltip
from oridecon.ui.core.base import el


class TestTooltip:
    @staticmethod
    def _tooltip(content: str = "Hint", **kwargs: object) -> Tooltip:
        return Tooltip(content, el("button", "Help", id="help-trigger"), **kwargs)

    def test_tooltip_renders_content(self) -> None:
        result = str(self._tooltip("Helpful hint"))
        assert "Helpful hint" in result

    def test_tooltip_span_has_role_tooltip(self) -> None:
        result = str(self._tooltip())
        assert 'role="tooltip"' in result

    def test_trigger_has_aria_describedby(self) -> None:
        result = str(self._tooltip())
        assert (
            '<button id="help-trigger" aria-describedby="help-trigger-tooltip"'
            in result
        )

    def test_tooltip_id_matches_aria_describedby(self) -> None:
        result = str(self._tooltip(tooltip_id="tip-1"))
        assert 'id="tip-1"' in result
        assert 'aria-describedby="tip-1"' in result

    def test_tooltip_derives_stable_id_from_trigger(self) -> None:
        result = str(self._tooltip("Auto ID"))
        assert 'id="help-trigger-tooltip"' in result

    def test_tooltip_requires_a_stable_id_source(self) -> None:
        tooltip = Tooltip("Hint", el("button", "Help"))

        with pytest.raises(ValueError, match="stable id"):
            str(tooltip)

    def test_tooltip_position_default(self) -> None:
        tooltip = self._tooltip()
        assert tooltip.position == "top"

    @pytest.mark.parametrize("position", ["top", "right", "bottom", "left"])
    def test_supported_position_stored(self, position: str) -> None:
        tooltip = self._tooltip(position=position)
        assert tooltip.position == position

    def test_invalid_position_fails_early(self) -> None:
        with pytest.raises(ValueError, match="position must be one of"):
            self._tooltip(position="diagonal")

    def test_tooltip_wraps_one_trigger(self) -> None:
        result = str(self._tooltip())
        assert "Help" in result
        assert "Hint" in result

    @pytest.mark.parametrize("children", [(), ("text",), (el("button"), el("button"))])
    def test_tooltip_requires_exactly_one_element_root(
        self, children: tuple[object, ...]
    ) -> None:
        tooltip = Tooltip("Hint", *children, tooltip_id="tip")

        with pytest.raises((TypeError, ValueError), match=r"exactly one|Element"):
            str(tooltip)

    def test_non_focusable_trigger_requires_explicit_wrapper(self) -> None:
        tooltip = Tooltip("Hint", el("span", "Term"), tooltip_id="tip")

        with pytest.raises(ValueError, match="must be focusable"):
            str(tooltip)

    def test_non_focusable_trigger_can_opt_into_button_wrapper(self) -> None:
        tooltip = Tooltip(
            "Hint",
            el("span", "Term"),
            tooltip_id="tip",
            wrap_non_focusable=True,
        )

        result = str(tooltip)

        assert '<button type="button" aria-describedby="tip"' in result
        assert "Term" in result

    def test_trigger_is_cloned_not_mutated(self) -> None:
        trigger = el("button", "Help", id="help")
        tooltip = Tooltip("Hint", trigger)

        result = str(tooltip)

        assert "aria-describedby" in result
        assert trigger.attrs == {"id": "help"}

    def test_existing_description_is_retained(self) -> None:
        trigger = el(
            "button",
            "Help",
            id="help",
            **{"aria-describedby": "existing-help"},
        )

        result = str(Tooltip("Hint", trigger))

        assert 'aria-describedby="existing-help help-tooltip"' in result

    def test_trigger_id_conflict_fails(self) -> None:
        tooltip = Tooltip(
            "Hint",
            el("button", "Help", id="original"),
            tooltip_id="tip",
            trigger_id="replacement",
        )

        with pytest.raises(ValueError, match="conflicts"):
            str(tooltip)

    def test_focus_hover_and_escape_handlers_are_on_trigger(self) -> None:
        result = str(self._tooltip())

        assert 'x-on:focus="open = true"' in result
        assert 'x-on:mouseenter="open = true"' in result
        assert 'x-on:keydown.escape.stop="open = false; $el.blur()"' in result
        assert 'x-show="open"' in result


class TestLabel:
    def test_label_renders_text(self) -> None:
        result = str(Label("Username"))
        assert "Username" in result

    def test_label_renders_label_tag(self) -> None:
        result = str(Label("Name"))
        assert "<label" in result

    def test_label_for_attribute(self) -> None:
        result = str(Label("Email", for_="email-input"))
        assert 'for="email-input"' in result

    def test_label_required_shows_asterisk(self) -> None:
        result = str(Label("Password", required=True))
        assert "*" in result

    def test_label_required_indicator_aria_hidden(self) -> None:
        result = str(Label("Field", required=True))
        assert 'aria-hidden="true"' in result

    def test_label_not_required_no_asterisk(self) -> None:
        result = str(Label("Optional"))
        assert "*" not in result

    def test_label_size_sm_class(self) -> None:
        result = str(Label("X", size="sm"))
        assert "text-sm" in result

    def test_label_size_lg_class(self) -> None:
        result = str(Label("X", size="lg"))
        assert "text-lg" in result

    def test_label_muted_color(self) -> None:
        result = str(Label("Hint", muted=True))
        assert "text-muted-foreground" in result

    def test_label_default_weight_medium(self) -> None:
        result = str(Label("X"))
        assert "font-medium" in result

    def test_label_bold_weight(self) -> None:
        result = str(Label("X", weight="bold"))
        assert "font-bold" in result


class TestDivider:
    def test_horizontal_divider_renders_hr(self) -> None:
        result = str(Divider())
        assert "<hr" in result

    def test_horizontal_divider_has_border_t(self) -> None:
        result = str(Divider())
        assert "border-t" in result

    def test_vertical_divider_renders_div(self) -> None:
        result = str(Divider(orientation="vertical"))
        assert "<div" in result

    def test_vertical_divider_has_border_l(self) -> None:
        result = str(Divider(orientation="vertical"))
        assert "border-l" in result

    def test_custom_class_applied(self) -> None:
        result = str(Divider(class_name="my-divider"))
        assert "my-divider" in result


class TestLink:
    def test_link_renders_anchor(self) -> None:
        result = str(Link("Home", href="/"))
        assert "<a" in result
        assert "Home" in result

    def test_link_href_attribute(self) -> None:
        result = str(Link("About", href="/about"))
        assert 'href="/about"' in result

    def test_link_primary_variant(self) -> None:
        result = str(Link("Click", href="#", variant="primary"))
        assert "text-primary" in result

    def test_link_muted_variant(self) -> None:
        result = str(Link("Skip", href="#", variant="muted"))
        assert "text-muted-foreground" in result

    def test_link_default_variant(self) -> None:
        result = str(Link("Go", href="#"))
        assert "text-foreground" in result

    def test_link_size_lg(self) -> None:
        result = str(Link("Big", href="#", size="lg"))
        assert "text-lg" in result

    def test_link_custom_class(self) -> None:
        result = str(Link("X", href="#", class_="underline"))
        assert "underline" in result
