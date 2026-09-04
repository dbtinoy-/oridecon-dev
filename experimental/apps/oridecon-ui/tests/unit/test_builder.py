"""Builder state, field binding, identity, and accessibility contracts."""

from __future__ import annotations

from html import unescape
import re
from types import SimpleNamespace
from typing import Any

import pytest

from oridecon.serialization import loads_str
from oridecon.ui import Component, Element, TrustedHTML
from oridecon.ui.molecules.builder import Builder


class DemoField(Component):
    def __init__(
        self,
        name: str,
        *,
        input_type: str = "text",
        model: str | None = None,
    ) -> None:
        super().__init__(data_original="preserved")
        self.name = name
        self.input_type = input_type
        self.model = model

    def render(self) -> Element:
        attrs: dict[str, Any] = {
            "id": f"{self.name}-input",
            "name": self.name,
            "type": self.input_type,
            "aria_describedby": f"{self.name}-help",
        }
        if self.model is not None:
            attrs["x-model"] = self.model
        return Element(
            "div",
            Element("label", self.name.title(), for_=f"{self.name}-input"),
            Element("input", **attrs),
            Element("p", "Help", id=f"{self.name}-help"),
        )


class TextOnlyField(Component):
    name = "broken"

    def render(self) -> str:
        return "not a control"


def block(
    name: str = "text",
    label: str = "Text",
    fields: list[Component] | None = None,
    icon: object = "box",
) -> SimpleNamespace:
    return SimpleNamespace(
        name=name,
        label=label,
        fields=fields if fields is not None else [DemoField("body")],
        icon=icon,
    )


def hidden_value(output: str) -> object:
    match = re.search(r'<input(?=[^>]*type="hidden")[^>]*\svalue="([^"]*)"', output)
    assert match is not None
    return loads_str(unescape(match.group(1)))


class TestBuilderState:
    def test_hidden_input_preserves_a_no_js_json_value(self) -> None:
        value = [{"type": "text", "data": {"body": "Hello"}}]
        output = str(Builder([block()], name="content", value=value))

        assert hidden_value(output) == value
        assert 'name="content"' in output
        assert 'x-bind:value="serialize()"' in output

    def test_methods_are_controller_code_not_json_string_properties(self) -> None:
        output = unescape(str(Builder([block()], name="content")))

        assert "addBlock(type)" in output
        assert "removeBlock(id)" in output
        assert "moveBlock(id, direction)" in output
        assert '"addBlock(type)":' not in output
        assert '"moveBlock(id, direction)":' not in output

    def test_initial_items_have_stable_keys_and_transport_omits_them(self) -> None:
        output = unescape(
            str(
                Builder(
                    [block()],
                    name="content",
                    value=[{"type": "text", "data": {"body": "Hello"}}],
                )
            )
        )

        assert '"id": "item-1"' in output
        assert 'x-bind:key="item.id"' in output
        assert "type: item.type, data: item.data" in output
        assert hidden_value(str(Builder([block()], name="other"))) == []

    def test_add_remove_and_reorder_announce_the_result(self) -> None:
        output = unescape(str(Builder([block()], name="content")))

        assert "block added" in output
        assert "block removed" in output
        assert "block moved" in output
        assert 'role="status" aria-live="polite"' in output

    def test_empty_state_is_visible_when_no_blocks_exist(self) -> None:
        output = str(Builder([block()], name="content"))

        assert "No blocks added yet." in output
        assert 'x-show="items.length === 0"' in output


class TestBuilderFieldBinding:
    def test_field_models_and_ids_are_scoped_to_each_item(self) -> None:
        output = unescape(str(Builder([block()], name="content")))

        model = 'item.data["body"]'
        assert f'x-model="{model}"' in output
        assert "fieldId(item.id" in output
        assert 'x-bind:id="fieldId(item.id' in output
        assert 'x-bind:for="fieldId(item.id' in output
        assert 'x-bind:aria-describedby="fieldId(item.id' in output

    def test_visible_controls_do_not_submit_outside_the_json_payload(self) -> None:
        output = str(Builder([block()], name="content"))

        assert output.count('name="content"') == 1
        assert 'name="body"' not in output
        assert 'data-builder-field="body"' in output

    def test_number_fields_use_numeric_model_coercion(self) -> None:
        output = unescape(
            str(
                Builder(
                    [block(fields=[DemoField("count", input_type="number")])],
                    name="content",
                )
            )
        )

        assert 'x-model.number="item.data["count"]"' in output

    def test_checkbox_fields_keep_standard_model_semantics(self) -> None:
        output = unescape(
            str(
                Builder(
                    [block(fields=[DemoField("enabled", input_type="checkbox")])],
                    name="content",
                )
            )
        )

        assert 'x-model="item.data["enabled"]"' in output
        assert "x-model.number" not in output

    def test_rendering_does_not_mutate_reusable_field_components(self) -> None:
        field = DemoField("body")
        before = dict(field.props)

        str(Builder([block(fields=[field])], name="content"))
        str(Builder([block(fields=[field])], name="secondary"))

        assert field.props == before
        assert "x-model" not in field.props

    def test_file_and_prebound_controls_fail_clearly(self) -> None:
        with pytest.raises(ValueError, match="file fields"):
            str(
                Builder(
                    [block(fields=[DemoField("upload", input_type="file")])],
                    name="content",
                )
            )
        with pytest.raises(ValueError, match="already owns an x-model"):
            str(
                Builder(
                    [block(fields=[DemoField("body", model="external")])],
                    name="content",
                )
            )

    def test_non_structural_field_output_is_rejected(self) -> None:
        with pytest.raises(TypeError, match="structured Element"):
            str(Builder([block(fields=[TextOnlyField()])], name="content"))


class TestBuilderValidationAndSafety:
    def test_block_and_value_shapes_are_validated(self) -> None:
        with pytest.raises(ValueError, match="duplicate Builder block"):
            Builder([block(), block()], name="content")
        with pytest.raises(ValueError, match="unknown Builder block"):
            Builder(
                [block()],
                name="content",
                value=[{"type": "unknown", "data": {}}],
            )
        with pytest.raises(TypeError, match="data must be an object"):
            Builder(
                [block()],
                name="content",
                value=[{"type": "text", "data": []}],
            )

    def test_duplicate_field_names_are_rejected(self) -> None:
        with pytest.raises(ValueError, match="duplicate field"):
            Builder(
                [block(fields=[DemoField("body"), DemoField("body")])],
                name="content",
            )

    def test_unknown_icons_fall_back_to_the_owned_registry(self) -> None:
        output = str(Builder([block(icon="fas fa-virus")], name="content"))

        assert "fas fa-virus" not in output
        assert "<svg" in output

    def test_dynamic_values_cannot_close_the_controller_script(self) -> None:
        payload = "</script><script>window.pwned=true</script>"
        output = str(
            Builder(
                [block(name=payload, label=payload, fields=[DemoField(payload)])],
                name=payload,
                value=[{"type": payload, "data": {payload: payload}}],
            )
        )
        script_body = output.split("<script>", 1)[1].split("</script>", 1)[0]

        assert output.count("<script") == 1
        assert "<script>window.pwned" not in script_body
        assert "\\u003c/script\\u003e" in script_body
        assert "&lt;/script&gt;&lt;script&gt;" in output


class TestBuilderIdentityAndAccessibility:
    def test_sibling_builders_have_unique_ids(self) -> None:
        output = str(
            Element(
                "main",
                Builder([block()], name="primary"),
                Builder([block()], name="secondary"),
            )
        )
        ids = re.findall(r' id="([^"]+)"', output)

        # Static IDs are only the two roots, hidden inputs, and live statuses;
        # repeated field IDs are Alpine-bound per stable item key.
        assert len(ids) == len(set(ids)) == 6

    def test_duplicate_identity_fails_in_one_render_tree(self) -> None:
        page = Element(
            "main",
            Builder([block()], name="content"),
            Builder([block()], name="content"),
        )

        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            str(page)

    def test_reorder_controls_have_contextual_names_and_boundary_state(self) -> None:
        output = unescape(str(Builder([block()], name="content")))

        assert "'Move ' + itemLabel(item) + ' block up'" in output
        assert "'Move ' + itemLabel(item) + ' block down'" in output
        assert "'Remove ' + itemLabel(item) + ' block'" in output
        assert 'x-bind:disabled="index === 0"' in output
        assert 'x-bind:disabled="index === items.length - 1"' in output

    def test_generated_controller_has_specific_provenance(self) -> None:
        root = Builder([block()], name="content").render()
        script = root.children[-1]

        assert isinstance(script, Element)
        assert script.tag == "script"
        assert isinstance(script.children[0], TrustedHTML)
        assert script.children[0].source == "generated Builder Alpine controller"

    def test_root_props_are_preserved_but_controller_state_is_protected(self) -> None:
        output = str(
            Builder(
                [block()],
                name="content",
                id="custom-builder",
                class_="custom-builder",
                data_testid="builder",
                x_data="untrusted",
                role="region",
            )
        )

        assert 'id="custom-builder"' in output
        assert "custom-builder" in output
        assert 'data-testid="builder"' in output
        assert 'x-data="untrusted"' not in output
        assert 'role="region"' not in output
