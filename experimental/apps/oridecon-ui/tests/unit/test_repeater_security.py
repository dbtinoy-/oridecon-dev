"""Trust, state, and identity contracts for Repeater."""

from __future__ import annotations

import re
from typing import Any

import pytest

from oridecon.ui import Component, Element
from oridecon.ui.core.trusted_html import TrustedHTML
from oridecon.ui.organisms.repeater import Repeater


class ContactFields(Component):
    def render(self) -> Element:
        return Element(
            "div",
            Element("label", "Email", for_="email-field"),
            Element(
                "input",
                type="email",
                name="email",
                id="email-field",
                value="fallback@example.test",
            ),
            Element("input", type="number", name="priority", id="priority-field"),
            Element("input", type="file", name="attachment", id="attachment-field"),
        )


def _repeater(**kwargs: Any) -> Repeater:
    return Repeater(name="contacts", schema=[ContactFields()], **kwargs)


class TestRepeaterTrust:
    def test_transformed_template_has_specific_provenance(self) -> None:
        root = _repeater().render()

        def descendants(node: object) -> list[object]:
            if not isinstance(node, Element):
                return [node]
            values: list[object] = [node]
            for child in node.children:
                values.extend(descendants(child))
            return values

        fragments = [
            node for node in descendants(root) if isinstance(node, TrustedHTML)
        ]
        assert len(fragments) == 1
        assert fragments[0].source == "Repeater transformed schema template"

    def test_plain_component_markup_remains_escaped(self) -> None:
        class PlainMarkup(Component):
            def render(self) -> str:
                return "<script>window.pwned=true</script>"

        output = str(Repeater(name="items", schema=[PlainMarkup()]))

        assert "<script>window.pwned" not in output
        assert "&lt;script&gt;window.pwned=true&lt;/script&gt;" in output

    def test_dynamic_values_cannot_break_html_or_alpine_expressions(self) -> None:
        payload = '"; window.pwned=true; </script><script>'
        output = str(
            Repeater(
                name=payload,
                schema=[
                    ElementField(
                        Element(
                            "input",
                            name=payload,
                            id=payload,
                        )
                    )
                ],
                value=[{"payload": payload}],
                label=payload,
                add_label=payload,
                item_label=payload,
            )
        )

        assert "<script" not in output.lower()
        assert "\\u003c/script\\u003e\\u003cscript\\u003e" in output
        assert "&lt;/script&gt;&lt;script&gt;" in output


class ElementField(Component):
    def __init__(self, node: Element) -> None:
        super().__init__()
        self.node = node

    def render(self) -> Element:
        return self.node


class TestRepeaterFormState:
    def test_names_ids_and_labels_are_bound_to_the_item_index(self) -> None:
        output = str(_repeater())

        assert "x-bind:name=" in output
        assert "x-bind:id=" in output
        assert "x-bind:for=" in output
        assert "contacts&quot; + &#x27;[&#x27; + index" in output

    def test_form_controls_bind_to_each_items_values(self) -> None:
        output = str(_repeater(value=[{"email": "person@example.test"}]))

        assert 'x-model="item[&quot;email&quot;]"' in output
        assert 'x-model.number="item[&quot;priority&quot;]"' in output
        file_control = re.search(r'<input[^>]*type="file"[^>]*>', output)
        assert file_control is not None
        assert "x-model" not in file_control.group(0)

    def test_initial_data_uses_strict_safe_json(self) -> None:
        output = str(_repeater(value=[{"email": "</script><script>window.pwned=true"}]))

        assert "<script>window.pwned" not in output
        assert "\\u003c/script\\u003e\\u003cscript\\u003e" in output

    def test_items_use_stable_keys_instead_of_array_indices(self) -> None:
        output = str(_repeater(value=[{"email": "first@example.test"}]))

        assert "_orideconKey: &#x27;existing-&#x27; + index" in output
        assert "_orideconKey: &#x27;new-&#x27; + this.nextKey++" in output
        assert 'x-bind:key="item._orideconKey"' in output
        assert 'x-bind:key="index"' not in output

    def test_callable_schema_is_evaluated(self) -> None:
        calls = 0

        def schema() -> list[Component]:
            nonlocal calls
            calls += 1
            return [ContactFields()]

        output = str(Repeater(name="contacts", schema=schema))

        assert calls == 1
        assert "x-bind:name=" in output


class TestRepeaterIdentityAndAccessibility:
    def test_sibling_repeaters_receive_unique_ids(self) -> None:
        page = Element(
            "main",
            Repeater(name="contacts", schema=[]),
            Repeater(name="addresses", schema=[]),
        )

        output = str(page)
        ids = re.findall(r' id="([^"]+)"', output)

        assert len(ids) == len(set(ids)) == 2

    def test_duplicate_implicit_identity_fails_fast(self) -> None:
        page = Element(
            "main",
            Repeater(name="contacts", schema=[]),
            Repeater(name="contacts", schema=[]),
        )

        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            str(page)

    def test_explicit_keys_are_stable_for_partial_renders(self) -> None:
        first = str(Repeater(name="contacts", schema=[], repeater_key="profile"))
        second = str(Repeater(name="contacts", schema=[], repeater_key="profile"))

        assert 'id="oridecon-repeater-group-profile"' in first
        assert first == second

    def test_visible_label_names_the_group(self) -> None:
        output = str(_repeater(label="Emergency contacts"))
        label_id = re.search(r'<h4[^>]* id="([^"]+)"', output)

        assert label_id is not None
        assert f'aria-labelledby="{label_id.group(1)}"' in output
        assert 'role="group"' in output

    def test_action_labels_include_item_context(self) -> None:
        output = str(_repeater(item_label="Contact"))

        assert output.count("x-bind:aria-label=") == 3
        assert "Contact&quot; + &#x27; &#x27; + (index + 1)" in output

    def test_root_props_are_preserved_without_leaking_configuration(self) -> None:
        output = str(
            _repeater(
                id="emergency-contacts",
                class_="custom-repeater",
                data_testid="contacts",
                x_data="untrusted",
            )
        )

        assert 'id="emergency-contacts"' in output
        assert 'class="repeater-container mb-8 custom-repeater"' in output
        assert 'data-testid="contacts"' in output
        assert 'x-data="untrusted"' not in output
        assert " repeater-key=" not in output
