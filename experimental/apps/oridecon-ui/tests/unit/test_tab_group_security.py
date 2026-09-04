"""Trust, identity, and accessibility contracts for schema tab groups."""

from __future__ import annotations

import re
from typing import Any

import pytest

from oridecon.ui import Element, trusted_html
from oridecon.ui.molecules.tab_group import Tab, TabGroup


def _render(*tabs: Tab, **kwargs: Any) -> str:
    return str(TabGroup(tabs=list(tabs), **kwargs))


class TestTabGroupTrust:
    def test_tab_values_are_serialized_for_alpine_expressions(self) -> None:
        payload = 'settings"; window.pwned = true; </script><script>'

        output = _render(Tab(name=payload, label="Settings"), default_tab=payload)

        assert "<script" not in output.lower()
        assert "\\u003c/script\\u003e\\u003cscript\\u003e" in output
        assert "activeTab: &quot;settings\\&quot;; window.pwned" in output

    def test_plain_icon_markup_is_display_text(self) -> None:
        output = _render(
            Tab(
                name="general",
                label="General",
                icon='<svg onload="window.pwned=true"></svg>',
            )
        )

        assert "<svg" not in output
        assert "&lt;svg onload=" in output

    def test_explicit_trusted_icon_markup_remains_supported(self) -> None:
        output = _render(
            Tab(
                name="general",
                label="General",
                icon=trusted_html("<svg></svg>", source="test-authored icon"),
            )
        )

        assert "<svg></svg>" in output

    def test_plain_schema_renderer_output_is_escaped(self) -> None:
        class PlainStringField:
            def render_form(self, value: Any) -> str:
                return '<img src=x onerror="window.pwned=true">'

        output = _render(
            Tab(name="general", label="General", schema_fields=[PlainStringField()])
        )

        assert "<img" not in output
        assert "&lt;img src=x onerror=" in output

    def test_configuration_does_not_leak_as_dom_attributes(self) -> None:
        output = _render(Tab(name="general", label="General"))

        assert " default-tab=" not in output
        assert " tabs=" not in output


class TestTabGroupIdentityAndAccessibility:
    def test_tabs_and_panels_have_unique_bidirectional_id_references(self) -> None:
        output = _render(
            Tab(name="general", label="General"),
            Tab(name="settings", label="Settings"),
            tab_group_key="account",
        )
        ids = re.findall(r' id="([^"]+)"', output)
        controls = re.findall(r' aria-controls="([^"]+)"', output)
        labelled_by = re.findall(r' aria-labelledby="([^"]+)"', output)

        assert len(ids) == len(set(ids)) == 5
        assert len(controls) == len(labelled_by) == 2
        assert set(controls).issubset(ids)
        assert set(labelled_by).issubset(ids)

    def test_only_default_tab_starts_selected_and_focusable(self) -> None:
        output = _render(
            Tab(name="general", label="General"),
            Tab(name="settings", label="Settings"),
            default_tab="settings",
        )

        assert output.count('aria-selected="true"') == 1
        assert output.count('tabindex="0"') == 1
        assert output.count('style="display: none;"') == 1

    def test_keyboard_navigation_contract_is_rendered(self) -> None:
        output = _render(Tab(name="general", label="General"))

        assert "x-on:keydown.right.prevent=" in output
        assert "x-on:keydown.left.prevent=" in output
        assert "x-on:keydown.home.prevent=" in output
        assert "x-on:keydown.end.prevent=" in output

    def test_sibling_groups_receive_distinct_ids(self) -> None:
        page = Element(
            "main",
            TabGroup(tabs=[Tab(name="general", label="First")]),
            TabGroup(tabs=[Tab(name="general", label="Second")]),
        )

        output = str(page)
        ids = re.findall(r' id="([^"]+)"', output)

        assert len(ids) == len(set(ids)) == 6

    def test_explicit_key_is_stable_across_independent_renders(self) -> None:
        first = _render(Tab(name="general", label="General"), tab_group_key="account")
        second = _render(Tab(name="general", label="General"), tab_group_key="account")

        assert re.findall(r' id="([^"]+)"', first) == re.findall(
            r' id="([^"]+)"', second
        )

    def test_duplicate_explicit_keys_fail_in_one_render_tree(self) -> None:
        page = Element(
            "main",
            TabGroup(
                tabs=[Tab(name="general", label="First")],
                tab_group_key="account",
            ),
            TabGroup(
                tabs=[Tab(name="general", label="Second")],
                tab_group_key="account",
            ),
        )

        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            str(page)


class TestTabGroupValidation:
    def test_duplicate_tab_names_are_rejected(self) -> None:
        with pytest.raises(ValueError, match="tab names must be unique"):
            TabGroup(
                tabs=[
                    Tab(name="general", label="First"),
                    Tab(name="general", label="Second"),
                ]
            )

    def test_unknown_default_tab_is_rejected(self) -> None:
        with pytest.raises(ValueError, match="is not a tab name"):
            TabGroup(
                tabs=[Tab(name="general", label="General")],
                default_tab="missing",
            )

    def test_root_props_and_classes_are_preserved(self) -> None:
        output = _render(
            Tab(name="general", label="General"),
            id="profile-tabs",
            class_="custom-tabs",
            data_testid="profile-tabs",
        )

        assert 'id="profile-tabs"' in output
        assert 'class="w-full custom-tabs"' in output
        assert 'data-testid="profile-tabs"' in output
