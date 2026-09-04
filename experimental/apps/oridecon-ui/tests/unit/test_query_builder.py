"""Unit tests for the QueryBuilder organism.

These tests assert the *rendered markup and Alpine state* produced by the
component (hidden JSON input, operator/field catalogs, recursive group
markup).  Live Alpine behaviour is not executed here — the serialization
contract is exercised end-to-end by the block-model translator tests in
oridecon-search.
"""

from __future__ import annotations

from html import unescape
import re

import pytest

from oridecon.serialization import loads_str
from oridecon.ui import Element, TrustedHTML
from oridecon.ui.organisms.query_builder import (
    DEFAULT_OPERATORS,
    OPERATOR_LABELS,
    QueryBuilder,
)


def _render(qb: QueryBuilder) -> str:
    """Render and unescape entity-escaped markup for content assertions."""
    return unescape(str(qb))


class TestQueryBuilderCore:
    """Basic structure of the rendered component."""

    def test_renders_hidden_json_input(self) -> None:
        qb = QueryBuilder(name="filters")
        html = _render(qb)
        assert 'type="hidden"' in html
        assert 'name="filters"' in html
        assert "serialize()" in html

    def test_root_uses_named_alpine_controller(self) -> None:
        html = _render(QueryBuilder(name="filters"))
        assert 'x-data="oridecon_query_builder_root_filters"' in html
        assert "const initialTree =" in html
        assert '"kind": "group"' in html
        assert '"findGroup(nodes, id)"' not in html

    def test_renders_label_when_provided(self) -> None:
        html = _render(QueryBuilder(name="filters", label="Constraint filters"))
        assert "Constraint filters" in html

    def test_no_label_when_omitted(self) -> None:
        html = _render(QueryBuilder(name="filters"))
        assert "<label" not in html

    def test_operators_default_catalog(self) -> None:
        html = _render(QueryBuilder(name="filters"))
        assert '"eq"' in html
        assert '"neq"' in html
        assert '"contains"' in html
        # Unknown operators are not added
        assert '"is_null"' not in html

    def test_operator_subset_is_honoured(self) -> None:
        html = _render(QueryBuilder(name="filters", operators=("eq", "contains")))
        assert '"eq"' in html
        assert '"contains"' in html
        assert '"neq"' not in html

    def test_operator_labels_cover_shared_operators(self) -> None:
        for op in DEFAULT_OPERATORS:
            assert op in OPERATOR_LABELS

    def test_missing_field_name_label_raises(self) -> None:
        with pytest.raises(ValueError, match="requires 'name' and 'label'"):
            QueryBuilder(name="filters", fields=[{"name": "status"}])

    def test_select_options_normalised(self) -> None:
        qb = QueryBuilder(
            name="filters",
            fields=[
                {"name": "s", "label": "S", "type": "select", "options": ["a", "b"]}
            ],
        )
        assert qb.fields[0]["options"] == [
            {"value": "a", "label": "a"},
            {"value": "b", "label": "b"},
        ]


class TestQueryBuilderInitialValue:
    """Initial block-model value → Alpine tree."""

    def test_empty_value_yields_empty_group(self) -> None:
        qb = QueryBuilder(name="filters")
        assert qb.tree == {
            "id": "node-1",
            "kind": "group",
            "logic": "AND",
            "rules": [],
        }
        assert qb.next_id == 2

    def test_value_from_dict(self) -> None:
        qb = QueryBuilder(
            name="filters",
            value={
                "logic": "AND",
                "rules": [{"field": "status", "operator": "eq", "value": "active"}],
            },
        )
        assert qb.tree["rules"] == [
            {
                "id": "node-2",
                "kind": "rule",
                "field": "status",
                "operator": "eq",
                "value": "active",
            }
        ]

    def test_value_from_json_string(self) -> None:
        from oridecon.serialization import dumps_str

        payload = dumps_str(
            {
                "logic": "AND",
                "rules": [{"field": "score", "operator": "gte", "value": 80}],
            }
        )
        qb = QueryBuilder(name="filters", value=payload)
        assert qb.tree["rules"][0]["field"] == "score"
        assert qb.tree["rules"][0]["value"] == 80

    def test_invalid_json_string_falls_back_to_empty(self) -> None:
        qb = QueryBuilder(name="filters", value="not json {")
        assert qb.tree["rules"] == []

    def test_single_rule_value_wrapped_in_root_group(self) -> None:
        qb = QueryBuilder(
            name="filters",
            value={"field": "status", "operator": "eq", "value": "x"},
        )
        assert qb.tree["kind"] == "group"
        assert len(qb.tree["rules"]) == 1
        assert qb.tree["rules"][0]["kind"] == "rule"

    def test_nested_group_value_keeps_structure(self) -> None:
        qb = QueryBuilder(
            name="filters",
            value={
                "logic": "AND",
                "rules": [
                    {"field": "a", "operator": "eq", "value": 1},
                    {
                        "logic": "OR",
                        "rules": [{"field": "b", "operator": "contains", "value": "z"}],
                    },
                ],
            },
        )
        nested = qb.tree["rules"][1]
        assert nested["kind"] == "group"
        assert nested["logic"] == "OR"
        assert nested["rules"][0]["field"] == "b"


class TestQueryBuilderMarkup:
    """Recursive group markup and rendering details."""

    def test_rule_row_renders_field_catalog_select(self) -> None:
        qb = QueryBuilder(
            name="filters",
            fields=[{"name": "status", "label": "Status", "type": "text"}],
        )
        html = _render(qb)
        assert "fieldOptions" in html
        assert '"name": "status"' in html
        assert '"label": "Status"' in html

    def test_free_text_field_when_catalog_empty(self) -> None:
        html = _render(QueryBuilder(name="filters", fields=[]))
        assert "fieldOptions" in html
        assert html.count('placeholder="Field"') >= 1

    def test_recursive_group_markup_present(self) -> None:
        html = _render(QueryBuilder(name="filters", max_depth=4))
        # rule branch at the first nesting level
        assert "node4.kind" in html
        # nested group branch rendering its own rules
        assert "node3.kind" in html

    def test_beyond_max_depth_renders_collapsed_note(self) -> None:
        html = _render(QueryBuilder(name="filters", max_depth=2))
        assert "preserved beyond the editable depth limit" in html
        # no deeper recursion generated
        assert "node0.kind" not in html

    def test_serialization_contract_round_trips(self) -> None:
        value = {
            "logic": "AND",
            "rules": [{"field": "status", "operator": "eq", "value": "active"}],
        }
        qb = QueryBuilder(name="filters", value=value)
        submitted = loads_str(_extract_hidden_value(str(qb)))
        # The hidden no-JS value carries the same block contract that the
        # client serializer maintains after interactive edits.
        assert submitted["logic"] == "AND"
        assert submitted["rules"][0]["field"] == "status"
        assert "id" not in submitted
        assert "kind" not in submitted["rules"][0]


class TestQueryBuilderConfiguration:
    @pytest.mark.parametrize("max_depth", [0, -1, True, 1.5])
    def test_max_depth_must_be_a_positive_integer(self, max_depth: object) -> None:
        with pytest.raises(ValueError, match="max_depth"):
            QueryBuilder(name="filters", max_depth=max_depth)  # type: ignore[arg-type]

    @pytest.mark.parametrize(
        ("operators", "message"),
        [
            ((), "at least one"),
            (("eq", "eq"), "unique"),
            (("eq", "unknown"), "unsupported"),
        ],
    )
    def test_operator_configuration_is_validated(
        self, operators: tuple[str, ...], message: str
    ) -> None:
        with pytest.raises(ValueError, match=message):
            QueryBuilder(name="filters", operators=operators)

    def test_duplicate_fields_are_rejected(self) -> None:
        with pytest.raises(ValueError, match="duplicate"):
            QueryBuilder(
                name="filters",
                fields=[
                    {"name": "status", "label": "First"},
                    {"name": "status", "label": "Second"},
                ],
            )

    def test_unknown_field_type_is_rejected(self) -> None:
        with pytest.raises(ValueError, match="field type"):
            QueryBuilder(
                name="filters",
                fields=[{"name": "status", "label": "Status", "type": "file"}],
            )

    def test_field_configuration_is_copied(self) -> None:
        fields = [
            {
                "name": "status",
                "label": "Status",
                "type": "select",
                "options": [{"value": "active", "label": "Active"}],
            }
        ]
        before = repr(fields)

        QueryBuilder(name="filters", fields=fields)

        assert repr(fields) == before

    def test_malformed_nested_rules_are_rejected(self) -> None:
        with pytest.raises(TypeError, match="rules must be a list"):
            QueryBuilder(name="filters", value={"logic": "AND", "rules": {}})

    def test_initial_rules_are_normalized_for_the_field_type(self) -> None:
        builder = QueryBuilder(
            name="filters",
            fields=[{"name": "price", "label": "Price", "type": "number"}],
            value={
                "logic": "AND",
                "rules": [{"field": "unknown", "operator": "contains", "value": "3"}],
            },
        )

        rule = builder.tree["rules"][0]
        assert rule["field"] == "price"
        assert rule["operator"] == "eq"
        submitted = loads_str(_extract_hidden_value(str(builder)))
        assert submitted["rules"][0]["field"] == "price"
        assert submitted["rules"][0]["operator"] == "eq"


class TestQueryBuilderControllerContracts:
    def test_methods_are_executable_controller_code_not_json_strings(self) -> None:
        output = _render(QueryBuilder(name="filters"))

        assert "findNode(nodeId)" in output
        assert "addRule(groupId)" in output
        assert '"addRule(groupId)":' not in output
        assert '"serialize()":' not in output

    def test_root_group_is_included_in_lookup_and_cannot_be_removed(self) -> None:
        output = _render(QueryBuilder(name="filters"))

        assert "const queue = [this.tree]" in output
        assert "this.findGroup(groupId)" in output
        assert "if (nodeId === this.tree.id) return" in output
        assert "this.findGroup(this.tree.rules" not in output

    def test_max_depth_is_enforced_in_the_controller_and_button(self) -> None:
        output = _render(QueryBuilder(name="filters", max_depth=3))

        assert "const maxDepth = 3" in output
        assert "depth < maxDepth - 1" in output
        assert "!canAddGroup(tree.id)" in output
        assert "if (!group || !this.canAddGroup(groupId)) return" in output
        assert "Maximum nesting depth reached" in output

    def test_field_changes_reset_value_and_normalize_operator(self) -> None:
        output = _render(
            QueryBuilder(
                name="filters",
                fields=[{"name": "price", "label": "Price", "type": "number"}],
            )
        )

        assert "fieldChanged(node)" in output
        assert "node.value = null" in output
        assert "this.normalizeRule(node)" in output
        assert "operatorsFor(node)" in output

    def test_generated_controller_has_specific_provenance(self) -> None:
        root = QueryBuilder(name="filters").render()
        script = root.children[-1]

        assert isinstance(script, Element)
        assert script.tag == "script"
        assert isinstance(script.children[0], TrustedHTML)
        assert script.children[0].source == ("generated QueryBuilder Alpine controller")

    def test_owned_icons_replace_unshipped_font_awesome(self) -> None:
        output = _render(QueryBuilder(name="filters"))

        assert "fa-trash" not in output
        assert "fa-plus" not in output
        assert "fa-layer-group" not in output
        assert "<svg" in output

    def test_alpine_loops_are_owned_by_template_elements(self) -> None:
        output = _render(
            QueryBuilder(
                name="filters",
                fields=[
                    {
                        "name": "status",
                        "label": "Status",
                        "type": "select",
                        "options": ["active"],
                    }
                ],
            )
        )

        assert '<template x-for="field in fieldOptions"' in output
        assert '<template x-for="operator in operatorsFor(' in output
        assert '<template x-for="option in optionsFor(' in output
        assert "<option x-for=" not in output

    def test_script_breakout_values_remain_data(self) -> None:
        payload = "</script><script>window.pwned=true</script>"
        output = str(
            QueryBuilder(
                name=payload,
                fields=[{"name": payload, "label": payload}],
                value={
                    "logic": "AND",
                    "rules": [{"field": payload, "operator": "eq", "value": payload}],
                },
            )
        )

        assert output.count("<script") == 1
        script_body = output.split("<script>", 1)[1].split("</script>", 1)[0]
        assert "<script>window.pwned" not in script_body
        assert "\\u003c/script\\u003e" in script_body
        assert "&lt;/script&gt;&lt;script&gt;" in output


class TestQueryBuilderIdentityAndAccessibility:
    def test_sibling_builders_have_unique_linked_ids(self) -> None:
        output = str(
            Element(
                "main",
                QueryBuilder(name="primary"),
                QueryBuilder(name="secondary"),
            )
        )
        ids = re.findall(r' id="([^"]+)"', output)

        assert len(ids) == len(set(ids)) == 6
        assert output.count('role="progressbar"') == 0
        assert output.count('role="status"') == 2

    def test_duplicate_identity_fails_in_one_render_tree(self) -> None:
        page = Element(
            "main",
            QueryBuilder(name="filters"),
            QueryBuilder(name="filters"),
        )

        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            str(page)

    def test_controls_have_names_and_logic_exposes_pressed_state(self) -> None:
        output = _render(QueryBuilder(name="filters"))

        assert 'aria-label="Field"' in output
        assert 'aria-label="Operator"' in output
        assert 'aria-label="Value"' in output
        assert "x-bind:aria-pressed" in output
        assert "'Add rule to '" in output
        assert "'Remove '" in output
        assert '<legend class="sr-only">Query filters</legend>' in output

    def test_root_props_are_preserved_but_controller_state_is_protected(self) -> None:
        output = _render(
            QueryBuilder(
                name="filters",
                id="custom-builder",
                class_="custom-query",
                data_testid="query",
                x_data="untrusted",
                role="region",
            )
        )

        assert 'id="custom-builder"' in output
        assert "custom-query" in output
        assert 'data-testid="query"' in output
        assert 'x-data="untrusted"' not in output
        assert 'role="region"' not in output


def _extract_hidden_value(html: str) -> str:
    """Return the HTML-decoded fallback value from the hidden form input."""
    match = re.search(r'<input(?=[^>]*type="hidden")[^>]*\svalue="([^"]*)"', html)
    assert match is not None
    return unescape(match.group(1))
