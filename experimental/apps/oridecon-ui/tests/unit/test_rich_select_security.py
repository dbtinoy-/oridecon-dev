"""Security, identity, and interaction contracts for RichSelect."""

from __future__ import annotations

import re

import pytest

from oridecon.ui import Element
from oridecon.ui.molecules.rich_select import RichSelect


class TestRichSelectTrust:
    def test_placeholder_is_serialized_as_a_javascript_string(self) -> None:
        payload = "Choose'; window.pwned = true; </script><script>"

        output = str(RichSelect(label="Choice", name="choice", placeholder=payload))

        assert "<script" not in output.lower()
        assert "\\u003c/script\\u003e\\u003cscript\\u003e" in output
        assert "Choose&#x27;; window.pwned" in output

    def test_option_values_and_labels_cannot_break_alpine_expressions(self) -> None:
        payload = '"; window.pwned = true; </script><script>'
        control = RichSelect(
            label="Choice",
            name="choice",
            options=[{"value": payload, "label": payload}],
        )

        output = str(control)

        assert "<script" not in output.lower()
        assert "\\u003c/script\\u003e\\u003cscript\\u003e" in output
        assert "&lt;/script&gt;&lt;script&gt;" in output

    def test_multi_input_name_is_an_escaped_structured_attribute(self) -> None:
        output = str(
            RichSelect(
                label="Choice",
                name='choice" autofocus onfocus="window.pwned=true',
                multi=True,
            )
        )

        assert (
            'name="choice&quot; autofocus onfocus=&quot;window.pwned=true[]"' in output
        )
        assert '<input type="hidden" name="choice" autofocus' not in output

    def test_render_tree_contains_no_legacy_raw_html_nodes(self) -> None:
        rendered = RichSelect(
            label="Choice",
            name="choice",
            options=[{"value": "a", "label": "Alpha"}],
            multi=True,
        ).render()

        def descendants(node: object) -> list[object]:
            if not isinstance(node, Element):
                return [node]
            values: list[object] = [node]
            for child in node.children:
                values.extend(descendants(child))
            return values

        assert all(type(node).__name__ != "RawHTML" for node in descendants(rendered))


class TestRichSelectIdentityAndAccessibility:
    def test_label_trigger_and_listbox_are_linked(self) -> None:
        output = str(
            RichSelect(
                label="Choice",
                name="choice",
                options=[{"value": "a", "label": "Alpha"}],
            )
        )
        trigger_id = re.search(r'<button[^>]* id="([^"]+)"', output)
        options_id = re.search(r'<div[^>]* id="([^"]+)" role="listbox"', output)

        assert trigger_id is not None
        assert options_id is not None
        assert f'for="{trigger_id.group(1)}"' in output
        assert f'aria-controls="{options_id.group(1)}"' in output

    def test_error_is_described_by_trigger(self) -> None:
        output = str(RichSelect(label="Choice", name="choice", error="Required"))
        error_id = re.search(r'<p[^>]* id="([^"]+)"', output)

        assert error_id is not None
        assert f'aria-describedby="{error_id.group(1)}"' in output
        assert 'aria-invalid="true"' in output

    def test_multi_listbox_declares_multiselect_behavior(self) -> None:
        output = str(RichSelect(label="Choice", name="choice", multi=True))

        assert 'aria-multiselectable="true"' in output
        assert 'x-for="value in selected"' in output
        assert 'x-bind:key="value"' in output

    def test_keyboard_navigation_uses_listbox_and_trigger_refs(self) -> None:
        output = str(
            RichSelect(
                label="Choice",
                name="choice",
                options=[{"value": "a", "label": "Alpha"}],
            )
        )

        assert 'x-ref="trigger"' in output
        assert 'x-ref="listbox"' in output
        assert "x-on:keydown.down.prevent=" in output
        assert "x-on:keydown.up.prevent=" in output
        assert "x-on:keydown.enter.prevent=" in output
        assert "x-on:keydown.space.prevent=" in output
        assert "x-on:keydown.escape.prevent=" in output

    def test_sibling_controls_receive_unique_ids(self) -> None:
        page = Element(
            "main",
            RichSelect(label="First", name="first"),
            RichSelect(label="Second", name="second"),
        )

        output = str(page)
        ids = re.findall(r' id="([^"]+)"', output)

        assert len(ids) == len(set(ids)) == 6

    def test_duplicate_implicit_identity_fails_fast(self) -> None:
        page = Element(
            "main",
            RichSelect(label="First", name="choice"),
            RichSelect(label="Second", name="choice"),
        )

        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            str(page)

    def test_explicit_keys_disambiguate_repeated_names(self) -> None:
        page = Element(
            "main",
            RichSelect(label="First", name="choice", rich_select_key="first"),
            RichSelect(label="Second", name="choice", rich_select_key="second"),
        )

        output = str(page)
        ids = re.findall(r' id="([^"]+)"', output)

        assert len(ids) == len(set(ids)) == 6

    def test_identity_is_stable_for_partial_renders(self) -> None:
        first = str(
            RichSelect(label="Choice", name="choice", rich_select_key="account")
        )
        second = str(
            RichSelect(label="Choice", name="choice", rich_select_key="account")
        )

        assert re.findall(r' id="([^"]+)"', first) == re.findall(
            r' id="([^"]+)"', second
        )

    def test_root_props_are_preserved_without_leaking_configuration(self) -> None:
        output = str(
            RichSelect(
                label="Choice",
                name="choice",
                id="profile-choice",
                class_="custom-select",
                data_testid="profile-choice",
            )
        )

        assert 'id="profile-choice"' in output
        assert 'class="mb-6 custom-select"' in output
        assert 'data-testid="profile-choice"' in output
        assert " rich-select-key=" not in output
        assert " placeholder=" not in output.split(">", 1)[0]
