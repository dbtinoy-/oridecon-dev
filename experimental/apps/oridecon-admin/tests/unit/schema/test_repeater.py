from __future__ import annotations

import re

import pytest

from oridecon.admin.schema import (
    BooleanField,
    FieldError,
    NumberField,
    SchemaField,
    TextField,
)
from oridecon.admin.schema.repeater import RepeaterField
from oridecon.result import Err, Ok
from oridecon.serialization import loads_str
from oridecon.ui import Element


class TestRepeaterField:
    def test_construct_with_minimum_args(self) -> None:
        field = RepeaterField(name="items")
        assert field.name == "items"
        assert field.fields == []

    def test_construct_with_fields(self) -> None:
        field = RepeaterField(
            name="items",
            fields=[TextField(name="name"), TextField(name="value")],
        )
        assert len(field.fields) == 2

    def test_render_form_returns_element(self) -> None:
        field = RepeaterField(name="items")
        element = field.render_form(None)
        assert isinstance(element, Element)

    def test_render_form_with_label(self) -> None:
        field = RepeaterField(name="items", label="Items")
        element = field.render_form(None)
        output = str(element)
        assert "Items" in output

    def test_render_form_with_values(self) -> None:
        field = RepeaterField(name="items")
        element = field.render_form([{"name": "foo", "value": "bar"}])
        output = str(element)
        assert "foo" in output or "serialized" in output

    def test_render_form_add_button_present(self) -> None:
        field = RepeaterField(name="items", add_button_label="Add Row")
        element = field.render_form(None)
        output = str(element)
        assert "Add Row" in output

    def test_render_column_with_values(self) -> None:
        field = RepeaterField(name="items")
        element = field.render_column(None, [{"name": "a"}, {"name": "b"}])
        output = str(element)
        assert "2" in output
        assert "items" in output

    def test_render_column_single_item(self) -> None:
        field = RepeaterField(name="items")
        element = field.render_column(None, [{"name": "a"}])
        output = str(element)
        assert "1" in output
        assert "item" in output

    def test_render_column_with_none(self) -> None:
        field = RepeaterField(name="items")
        element = field.render_column(None, None)
        output = str(element)
        assert "\u2014" in output

    def test_from_form_valid_json(self) -> None:
        field = RepeaterField(
            name="items",
            fields=[TextField(name="name")],
        )
        result = field.from_form('[{"name":"hello"}]')
        assert isinstance(result, Ok)
        assert result.unwrap() == [{"name": "hello"}]

    def test_from_form_invalid_json_returns_err(self) -> None:
        field = RepeaterField(name="items")
        result = field.from_form("not json")
        assert isinstance(result, Err)
        assert isinstance(result.unwrap_err(), FieldError)

    def test_from_form_non_list_returns_err(self) -> None:
        field = RepeaterField(name="items")
        result = field.from_form('{"key":"val"}')
        assert isinstance(result, Err)
        assert isinstance(result.unwrap_err(), FieldError)

    def test_from_form_empty_returns_none_when_nullable(self) -> None:
        field = RepeaterField(name="items", nullable=True)
        result = field.from_form("")
        assert isinstance(result, Ok)
        assert result.unwrap() is None

    def test_from_form_none_returns_ok_none(self) -> None:
        field = RepeaterField(name="items")
        result = field.from_form(None)
        assert isinstance(result, Ok)
        assert result.unwrap() is None

    def test_to_form_with_list(self) -> None:
        field = RepeaterField(name="items")
        result = field.to_form([{"name": "a"}])

        assert loads_str(result) == [{"name": "a"}]

    def test_to_form_with_none(self) -> None:
        field = RepeaterField(name="items")
        assert field.to_form(None) == ""

    def test_is_schema_field(self) -> None:
        field = RepeaterField(name="items")
        assert isinstance(field, SchemaField)

    def test_render_filter_returns_none(self) -> None:
        field = RepeaterField(name="items")
        assert field.render_filter() is None

    def test_max_items(self) -> None:
        field = RepeaterField(name="items", max_items=5)
        assert field.max_items == 5

    def test_min_items(self) -> None:
        field = RepeaterField(name="items", min_items=1)
        assert field.min_items == 1


class TestRepeaterFieldInteractionContracts:
    def test_existing_items_render_once_through_the_alpine_template(self) -> None:
        field = RepeaterField(
            name="items",
            fields=[TextField(name="name", label="Name")],
        )

        html = str(field.render_form([{"name": "First"}]))

        assert html.count('data-repeater-field="name"') == 1
        assert 'x-model="item[&quot;name&quot;]"' in html
        assert 'name="name"' not in html
        assert html.count('name="items"') == 1
        assert "First" in html

    def test_numeric_fields_preserve_numeric_item_types(self) -> None:
        field = RepeaterField(
            name="items",
            fields=[NumberField(name="quantity", label="Quantity")],
        )

        html = str(field.render_form([{"quantity": 2}]))

        assert 'x-model.number="item[&quot;quantity&quot;]"' in html

    def test_boolean_switch_reads_and_writes_item_state(self) -> None:
        field = RepeaterField(
            name="items",
            fields=[BooleanField(name="enabled", label="Enabled")],
        )

        html = str(field.render_form([{"enabled": True}]))

        assert 'x-model="item[&quot;enabled&quot;]"' in html
        assert "get enabled()" in html
        assert "set enabled(value)" in html
        assert "item[&quot;" in html

    def test_template_uses_stable_item_keys(self) -> None:
        html = str(RepeaterField(name="items").render_form([{}]))

        assert "_orideconKey: &#x27;existing-&#x27; + index" in html
        assert "_orideconKey: &#x27;new-&#x27; + this.nextKey++" in html
        assert 'x-bind:key="item._orideconKey"' in html
        assert 'x-bind:key="index"' not in html

    def test_initial_items_are_not_mutated(self) -> None:
        items = [{"name": "First"}]
        field = RepeaterField(name="items", min_items=2)

        field.render_form(items)

        assert items == [{"name": "First"}]

    def test_minimum_items_are_initialized_and_cannot_be_removed(self) -> None:
        field = RepeaterField(name="items", min_items=2)

        html = str(field.render_form(None))

        assert "items: [{}, {}]" in html
        assert "this.items.length &lt;= this.minItems" in html
        assert 'x-show="items.length &gt; minItems"' in html

    def test_maximum_disables_add_in_live_state(self) -> None:
        field = RepeaterField(name="items", max_items=2)

        html = str(field.render_form([{}, {}]))

        assert "maxItems: 2" in html
        assert 'x-bind:disabled="maxItems !== null' in html
        assert "disabled:cursor-not-allowed" in html

    def test_move_and_remove_controls_have_contextual_labels(self) -> None:
        html = str(RepeaterField(name="items").render_form([{}]))

        assert "moveItem(index, index - 1)" in html
        assert "moveItem(index, index + 1)" in html
        assert "removeItem(index)" in html
        assert html.count("x-bind:aria-label=") == 3
        assert "<svg" in html
        assert 'class="&lt;svg' not in html


class TestRepeaterFieldIdentityAndValidation:
    def test_subfield_labels_reference_dynamic_scoped_ids(self) -> None:
        field = RepeaterField(
            name="line_items",
            fields=[TextField(name="sku", label="SKU")],
            repeater_key="order-lines",
        )

        html = str(field.render_form([{"sku": "ABC"}]))

        bound_id = re.search(r'x-bind:id="([^"]+)"', html)
        bound_for = re.search(r'x-bind:for="([^"]+)"', html)
        assert bound_id is not None
        assert bound_for is not None
        assert bound_id.group(1) == bound_for.group(1)
        assert 'id="oridecon-repeater-field-group-order-lines"' in html

    def test_errors_describe_the_group(self) -> None:
        field = RepeaterField(name="items", label="Items")

        html = str(field.render_form([], errors=["Add at least one item"]))
        error_id = re.search(r'<p id="([^"]+)" role="alert"', html)

        assert error_id is not None
        assert f'aria-describedby="{error_id.group(1)}"' in html
        assert "Add at least one item" in html

    def test_dynamic_values_cannot_break_alpine_state(self) -> None:
        payload = "</script><script>window.pwned=true</script>"
        field = RepeaterField(
            name="items",
            fields=[TextField(name="name", label=payload)],
            add_button_label=payload,
        )

        html = str(field.render_form([{"name": payload}]))

        assert "<script>window.pwned" not in html
        assert "\\u003c/script\\u003e\\u003cscript\\u003e" in html
        assert "&lt;/script&gt;&lt;script&gt;" in html

    def test_duplicate_subfield_names_are_rejected(self) -> None:
        with pytest.raises(ValueError, match="sub-field names must be unique"):
            RepeaterField(
                name="items",
                fields=[TextField(name="name"), TextField(name="name")],
            )

    @pytest.mark.parametrize(
        "kwargs",
        [
            {"min_items": -1},
            {"min_items": 2, "max_items": 1},
        ],
    )
    def test_invalid_limits_are_rejected(self, kwargs: dict[str, int]) -> None:
        with pytest.raises(ValueError, match="RepeaterField"):
            RepeaterField(name="items", **kwargs)

    def test_from_form_enforces_minimum(self) -> None:
        field = RepeaterField(name="items", min_items=1)

        result = field.from_form("[]")

        assert isinstance(result, Err)
        assert "at least 1" in str(result.unwrap_err())

    def test_from_form_enforces_maximum(self) -> None:
        field = RepeaterField(name="items", max_items=1)

        result = field.from_form("[{}, {}]")

        assert isinstance(result, Err)
        assert "at most 1" in str(result.unwrap_err())

    def test_structured_subfield_values_use_json_during_coercion(self) -> None:
        from oridecon.admin.schema.composite import JsonField

        field = RepeaterField(
            name="items",
            fields=[JsonField(name="metadata")],
        )

        result = field.from_form('[{"metadata":{"priority":1}}]')

        assert isinstance(result, Ok)
        assert result.unwrap() == [{"metadata": {"priority": 1}}]
