"""Scoped Alpine query-tree editor with a JSON form fallback."""

from __future__ import annotations

from typing import Any

from oridecon.serialization import dumps_str, loads_str
from oridecon.ui.atoms.icons import get_icon
from oridecon.ui.attributes import alpine
from oridecon.ui.core.base import Component, Element
from oridecon.ui.core.js import js_json, js_string
from oridecon.ui.core.render_context import get_render_scope
from oridecon.ui.core.trusted_html import trusted_html

DEFAULT_OPERATORS = ("eq", "neq", "contains", "gt", "gte", "lt", "lte")

OPERATOR_LABELS: dict[str, str] = {
    "eq": "equals",
    "neq": "does not equal",
    "contains": "contains",
    "gt": "is greater than",
    "gte": "is greater than or equal",
    "lt": "is less than",
    "lte": "is less than or equal",
}

_FIELD_TYPES = frozenset({"text", "number", "integer", "float", "select"})


class QueryBuilder(Component):
    """Edit recursive AND/OR constraints and submit their block-model JSON."""

    def __init__(
        self,
        name: str,
        value: str | dict[str, Any] | None = None,
        label: str | None = None,
        fields: list[dict[str, Any]] | None = None,
        operators: tuple[str, ...] | None = None,
        max_depth: int = 4,
        query_builder_key: str | None = None,
        **props: Any,
    ) -> None:
        super().__init__(**props)
        if not name:
            raise ValueError("QueryBuilder name must not be empty")
        if (
            isinstance(max_depth, bool)
            or not isinstance(max_depth, int)
            or max_depth < 1
        ):
            raise ValueError("QueryBuilder max_depth must be an integer of at least 1")

        configured_operators = DEFAULT_OPERATORS if operators is None else operators
        if not configured_operators:
            raise ValueError("QueryBuilder requires at least one operator")
        if len(set(configured_operators)) != len(configured_operators):
            raise ValueError("QueryBuilder operators must be unique")
        unknown = set(configured_operators).difference(OPERATOR_LABELS)
        if unknown:
            raise ValueError(
                "unsupported QueryBuilder operators: " + ", ".join(sorted(unknown))
            )

        self.name = name
        self.label = label
        self.fields = self._normalize_fields(fields or [])
        self.operators = tuple(configured_operators)
        self.max_depth = max_depth
        self.query_builder_key = query_builder_key
        self.tree, self.next_id = self._build_tree(value)
        self._normalize_tree(self.tree)

    @staticmethod
    def _normalize_fields(fields: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Validate and copy the caller-owned field catalog."""
        normalized: list[dict[str, Any]] = []
        names: set[str] = set()
        for field in fields:
            if (
                not isinstance(field, dict)
                or not field.get("name")
                or not field.get("label")
            ):
                raise ValueError("each query-builder field requires 'name' and 'label'")
            name = str(field["name"])
            if name in names:
                raise ValueError(f"duplicate query-builder field name: {name!r}")
            names.add(name)

            field_type = str(field.get("type", "text"))
            if field_type not in _FIELD_TYPES:
                raise ValueError(
                    f"unsupported query-builder field type: {field_type!r}"
                )
            entry: dict[str, Any] = {
                "name": name,
                "label": str(field["label"]),
                "type": field_type,
            }
            if field_type == "select":
                options: list[dict[str, Any]] = []
                for option in field.get("options") or []:
                    if isinstance(option, dict):
                        if "value" not in option or "label" not in option:
                            raise ValueError(
                                f"select field {name!r} options require value and label"
                            )
                        options.append(
                            {
                                "value": option["value"],
                                "label": str(option["label"]),
                            }
                        )
                    else:
                        options.append({"value": str(option), "label": str(option)})
                entry["options"] = options
            normalized.append(entry)
        return normalized

    def _build_tree(
        self, value: str | dict[str, Any] | None
    ) -> tuple[dict[str, Any], int]:
        """Convert block-model data into copied, keyed client state."""
        if isinstance(value, str):
            try:
                value = loads_str(value)
            except (ValueError, TypeError):
                value = None
        if value is not None and not isinstance(value, dict):
            value = None

        counter = 0

        def next_key() -> str:
            nonlocal counter
            counter += 1
            return f"node-{counter}"

        def node_for(entry: dict[str, Any]) -> dict[str, Any]:
            if not isinstance(entry, dict):
                raise TypeError("query-builder rules must be objects")
            key = next_key()
            if "field" in entry or "operator" in entry:
                operator = str(entry.get("operator", self.operators[0]))
                if operator not in self.operators:
                    operator = self.operators[0]
                return {
                    "id": key,
                    "kind": "rule",
                    "field": str(entry.get("field", "")),
                    "operator": operator,
                    "value": entry.get("value"),
                }

            logic = str(entry.get("logic", "AND")).upper()
            if logic not in {"AND", "OR"}:
                logic = "AND"
            rules = entry.get("rules", [])
            if rules is None:
                rules = []
            if not isinstance(rules, list):
                raise TypeError("query-builder group rules must be a list")
            return {
                "id": key,
                "kind": "group",
                "logic": logic,
                "rules": [node_for(child) for child in rules],
            }

        source = value or {"logic": "AND", "rules": []}
        root = node_for(source)
        if root["kind"] != "group":
            root = {
                "id": next_key(),
                "kind": "group",
                "logic": "AND",
                "rules": [root],
            }
        return root, counter + 1

    def _compatible_operators(self, field_name: str) -> tuple[str, ...]:
        field = next(
            (candidate for candidate in self.fields if candidate["name"] == field_name),
            None,
        )
        allowed: frozenset[str] | None = None
        if field is not None:
            field_type = field["type"]
            if field_type == "select":
                allowed = frozenset({"eq", "neq"})
            elif field_type in {"number", "integer", "float"}:
                allowed = frozenset({"eq", "neq", "gt", "gte", "lt", "lte"})
            elif field_type == "text":
                allowed = frozenset({"eq", "neq", "contains"})
        compatible = tuple(
            operator
            for operator in self.operators
            if allowed is None or operator in allowed
        )
        return compatible or self.operators

    def _normalize_tree(self, node: dict[str, Any]) -> None:
        if node["kind"] == "rule":
            if self.fields and node["field"] not in {
                field["name"] for field in self.fields
            }:
                node["field"] = self.fields[0]["name"]
            compatible = self._compatible_operators(node["field"])
            if node["operator"] not in compatible:
                node["operator"] = compatible[0]
            return
        for child in node["rules"]:
            self._normalize_tree(child)

    @staticmethod
    def _serialize_node(node: dict[str, Any]) -> dict[str, Any]:
        if node["kind"] == "rule":
            return {
                "field": node["field"],
                "operator": node["operator"],
                "value": node["value"],
            }
        return {
            "logic": node["logic"],
            "rules": [QueryBuilder._serialize_node(child) for child in node["rules"]],
        }

    def _controller_script(self, controller_name: str) -> str:
        operator_options = [
            {"value": operator, "label": OPERATOR_LABELS[operator]}
            for operator in self.operators
        ]
        return f"""
(() => {{
    const controllerName = {js_string(controller_name)};
    const initialTree = {js_json(self.tree)};
    const initialNextId = {js_json(self.next_id)};
    const configuredFields = {js_json(self.fields)};
    const configuredOperators = {js_json(operator_options)};
    const maxDepth = {js_json(self.max_depth)};

    const controller = () => ({{
        tree: JSON.parse(JSON.stringify(initialTree)),
        nextId: initialNextId,
        fieldOptions: configuredFields,
        operatorOptions: configuredOperators,
        announcement: '',
        init() {{ this.normalizeTree(this.tree); }},
        newId() {{ return `${{controllerName}}-${{this.nextId++}}`; }},
        findNode(nodeId) {{
            const queue = [this.tree];
            while (queue.length) {{
                const node = queue.shift();
                if (node.id === nodeId) return node;
                if (node.kind === 'group') queue.push(...node.rules);
            }}
            return null;
        }},
        findGroup(nodeId) {{
            const node = this.findNode(nodeId);
            return node?.kind === 'group' ? node : null;
        }},
        nodeDepth(nodeId) {{
            const queue = [{{node: this.tree, depth: 0}}];
            while (queue.length) {{
                const current = queue.shift();
                if (current.node.id === nodeId) return current.depth;
                if (current.node.kind === 'group') {{
                    queue.push(...current.node.rules.map(node => ({{
                        node, depth: current.depth + 1
                    }})));
                }}
            }}
            return -1;
        }},
        canAddGroup(groupId) {{
            const depth = this.nodeDepth(groupId);
            return depth >= 0 && depth < maxDepth - 1;
        }},
        addRule(groupId) {{
            const group = this.findGroup(groupId);
            if (!group) return;
            const field = this.fieldOptions[0]?.name || '';
            const rule = {{
                id: this.newId(), kind: 'rule', field,
                operator: this.operatorOptions[0]?.value || 'eq', value: null
            }};
            this.normalizeRule(rule);
            group.rules.push(rule);
            this.announcement = `Rule added to ${{group.logic}} group`;
        }},
        addGroup(groupId, logic = 'AND') {{
            const group = this.findGroup(groupId);
            if (!group || !this.canAddGroup(groupId)) return;
            group.rules.push({{
                id: this.newId(), kind: 'group',
                logic: logic === 'OR' ? 'OR' : 'AND', rules: []
            }});
            this.announcement = `Group added to ${{group.logic}} group`;
        }},
        removeNode(nodeId) {{
            if (nodeId === this.tree.id) return;
            const prune = nodes => {{
                for (let index = nodes.length - 1; index >= 0; index--) {{
                    if (nodes[index].id === nodeId) {{
                        nodes.splice(index, 1);
                        return true;
                    }}
                    if (nodes[index].kind === 'group' && prune(nodes[index].rules)) {{
                        return true;
                    }}
                }}
                return false;
            }};
            if (prune(this.tree.rules)) this.announcement = 'Condition removed';
        }},
        setLogic(groupId, logic) {{
            const group = this.findGroup(groupId);
            if (!group || !['AND', 'OR'].includes(logic)) return;
            group.logic = logic;
            this.announcement = `Group now uses ${{logic}} logic`;
        }},
        fieldDefinition(node) {{
            return this.fieldOptions.find(field => field.name === node.field) || null;
        }},
        inputTypeFor(node) {{
            const type = this.fieldDefinition(node)?.type;
            return ['number', 'integer', 'float'].includes(type) ? 'number' :
                (type === 'select' ? 'select' : 'text');
        }},
        optionsFor(node) {{
            const field = this.fieldDefinition(node);
            return field?.type === 'select' ? (field.options || []) : [];
        }},
        operatorsFor(node) {{
            const type = this.fieldDefinition(node)?.type;
            let names = null;
            if (type === 'select') names = new Set(['eq', 'neq']);
            else if (['number', 'integer', 'float'].includes(type)) {{
                names = new Set(['eq', 'neq', 'gt', 'gte', 'lt', 'lte']);
            }} else if (type === 'text') names = new Set(['eq', 'neq', 'contains']);
            const compatible = names
                ? this.operatorOptions.filter(option => names.has(option.value))
                : this.operatorOptions;
            return compatible.length ? compatible : this.operatorOptions;
        }},
        normalizeRule(node) {{
            if (this.fieldOptions.length && !this.fieldDefinition(node)) {{
                node.field = this.fieldOptions[0].name;
            }}
            const choices = this.operatorsFor(node);
            if (!choices.some(option => option.value === node.operator)) {{
                node.operator = choices[0]?.value || 'eq';
            }}
        }},
        normalizeTree(node) {{
            if (node.kind === 'rule') {{
                this.normalizeRule(node);
                return;
            }}
            node.logic = node.logic === 'OR' ? 'OR' : 'AND';
            node.rules.forEach(child => this.normalizeTree(child));
        }},
        fieldChanged(node) {{
            node.value = null;
            this.normalizeRule(node);
            this.announcement = 'Field changed; operator and value reset';
        }},
        serialize() {{
            const serializeNode = node => node.kind === 'rule'
                ? {{field: node.field, operator: node.operator, value: node.value}}
                : {{logic: node.logic, rules: node.rules.map(serializeNode)}};
            return JSON.stringify(serializeNode(this.tree));
        }}
    }});

    const register = () => window.Alpine.data(controllerName, controller);
    if (window.Alpine) register();
    else document.addEventListener('alpine:init', register, {{once: true}});
}})();
"""

    def _rule_row(self, variable: str) -> Element:
        if self.fields:
            field_control = Element(
                "select",
                Element(
                    "template",
                    Element(
                        "option",
                        **{"x-text": "field.label"},
                        **alpine.bind("value", alpine.expr("field.name")),
                    ),
                    **{"x-for": "field in fieldOptions"},
                    **alpine.bind("key", alpine.expr("field.name")),
                ),
                aria_label="Field",
                **alpine.model(alpine.expr(f"{variable}.field")),
                **alpine.on("change", alpine.expr(f"fieldChanged({variable})")),
                class_=(
                    "qb-field-input w-44 rounded-md border border-border "
                    "bg-background px-2 py-1 text-sm"
                ),
            )
        else:
            field_control = Element(
                "input",
                type="text",
                placeholder="Field",
                aria_label="Field",
                **alpine.model(alpine.expr(f"{variable}.field")),
                class_=(
                    "qb-field-input w-44 rounded-md border border-border "
                    "bg-background px-2 py-1 text-sm"
                ),
            )

        operator_control = Element(
            "select",
            Element(
                "template",
                Element(
                    "option",
                    **{"x-text": "operator.label"},
                    **alpine.bind("value", alpine.expr("operator.value")),
                ),
                **{"x-for": f"operator in operatorsFor({variable})"},
                **alpine.bind("key", alpine.expr("operator.value")),
            ),
            aria_label="Operator",
            **alpine.model(alpine.expr(f"{variable}.operator")),
            class_=(
                "qb-operator-input w-44 rounded-md border border-border "
                "bg-background px-2 py-1 text-sm"
            ),
        )

        value_controls = (
            Element(
                "template",
                Element(
                    "select",
                    Element(
                        "template",
                        Element(
                            "option",
                            **{"x-text": "option.label"},
                            **alpine.bind("value", alpine.expr("option.value")),
                        ),
                        **{"x-for": f"option in optionsFor({variable})"},
                        **alpine.bind("key", alpine.expr("option.value")),
                    ),
                    aria_label="Value",
                    **alpine.model(alpine.expr(f"{variable}.value")),
                    class_=(
                        "qb-value-input w-44 rounded-md border border-border "
                        "bg-background px-2 py-1 text-sm"
                    ),
                ),
                **{"x-if": f"inputTypeFor({variable}) === 'select'"},
            ),
            Element(
                "template",
                Element(
                    "input",
                    aria_label="Value",
                    **alpine.model(alpine.expr(f"{variable}.value")),
                    **alpine.bind("type", alpine.expr(f"inputTypeFor({variable})")),
                    class_=(
                        "qb-value-input w-44 rounded-md border border-border "
                        "bg-background px-2 py-1 text-sm"
                    ),
                ),
                **{"x-if": f"inputTypeFor({variable}) !== 'select'"},
            ),
        )

        remove_label = f"'Remove ' + ({variable}.field || 'unnamed') + ' rule'"
        return Element(
            "div",
            field_control,
            operator_control,
            *value_controls,
            Element(
                "button",
                get_icon("trash", class_name="h-4 w-4 text-destructive"),
                type="button",
                title="Remove rule",
                **alpine.bind("aria-label", alpine.expr(remove_label)),
                **alpine.on("click", alpine.expr(f"removeNode({variable}.id)")),
                class_=(
                    "rounded p-1 hover:bg-accent focus-visible:outline-none "
                    "focus-visible:ring-2 focus-visible:ring-ring"
                ),
            ),
            role="group",
            **alpine.bind(
                "aria-label",
                alpine.expr(f"'Rule for ' + ({variable}.field || 'unnamed field')"),
            ),
            class_=(
                "qb-rule mb-1.5 flex flex-wrap items-center gap-2 rounded-md "
                "border border-border bg-card px-2 py-1.5"
            ),
        )

    def _group_panel(self, depth: int, variable: str, *, removable: bool) -> Element:
        logic_buttons = [
            Element(
                "button",
                logic,
                type="button",
                **alpine.on(
                    "click", alpine.expr(f"setLogic({variable}.id, {js_string(logic)})")
                ),
                **alpine.bind(
                    "aria-pressed",
                    alpine.expr(f"{variable}.logic === {js_string(logic)}"),
                ),
                **alpine.bind(
                    "class",
                    alpine.expr(
                        f"{variable}.logic === {js_string(logic)} ? "
                        "'bg-primary text-primary-foreground' : "
                        "'bg-muted text-muted-foreground'"
                    ),
                ),
                class_=(
                    "qb-logic-toggle rounded px-2 py-0.5 text-xs font-semibold "
                    "focus-visible:outline-none focus-visible:ring-2 "
                    "focus-visible:ring-ring"
                ),
            )
            for logic in ("AND", "OR")
        ]
        if removable:
            logic_buttons.append(
                Element(
                    "button",
                    get_icon("trash", class_name="h-4 w-4 text-destructive"),
                    type="button",
                    title="Remove group",
                    **alpine.bind(
                        "aria-label",
                        alpine.expr(f"'Remove ' + {variable}.logic + ' group'"),
                    ),
                    **alpine.on("click", alpine.expr(f"removeNode({variable}.id)")),
                    class_=(
                        "ml-auto rounded p-1 hover:bg-accent "
                        "focus-visible:outline-none focus-visible:ring-2 "
                        "focus-visible:ring-ring"
                    ),
                )
            )

        child_variable = f"node{depth}"
        child_group = (
            self._group_panel(depth - 1, child_variable, removable=True)
            if depth > 1
            else Element(
                "p",
                "Nested group preserved beyond the editable depth limit.",
                class_=(
                    "rounded-md border border-dashed border-border px-2 py-1 "
                    "text-xs text-muted-foreground"
                ),
            )
        )
        add_group_expression = f"addGroup({variable}.id, 'AND')"
        can_add_expression = f"canAddGroup({variable}.id)"

        return Element(
            "div",
            Element("div", *logic_buttons, class_="mb-2 flex items-center gap-1"),
            Element(
                "template",
                Element(
                    "div",
                    Element(
                        "template",
                        self._rule_row(child_variable),
                        **{"x-if": f"{child_variable}.kind === 'rule'"},
                    ),
                    Element(
                        "template",
                        child_group,
                        **{"x-if": f"{child_variable}.kind === 'group'"},
                    ),
                ),
                **{"x-for": f"{child_variable} in {variable}.rules"},
                **alpine.bind("key", alpine.expr(f"{child_variable}.id")),
            ),
            Element(
                "div",
                Element(
                    "button",
                    get_icon("plus", class_name="mr-1 h-4 w-4"),
                    "Rule",
                    type="button",
                    **alpine.bind(
                        "aria-label",
                        alpine.expr(f"'Add rule to ' + {variable}.logic + ' group'"),
                    ),
                    **alpine.on("click", alpine.expr(f"addRule({variable}.id)")),
                    class_=(
                        "inline-flex items-center rounded border border-dashed "
                        "border-border bg-card px-2 py-1 text-xs text-foreground "
                        "hover:bg-accent focus-visible:outline-none "
                        "focus-visible:ring-2 focus-visible:ring-ring"
                    ),
                ),
                Element(
                    "button",
                    get_icon("layers", class_name="mr-1 h-4 w-4"),
                    "Group",
                    type="button",
                    title="Maximum nesting depth reached",
                    **alpine.bind(
                        "aria-label",
                        alpine.expr(f"'Add group to ' + {variable}.logic + ' group'"),
                    ),
                    **alpine.bind("disabled", alpine.expr(f"!{can_add_expression}")),
                    **alpine.bind(
                        "title",
                        alpine.expr(
                            f"{can_add_expression} ? 'Add nested group' : "
                            "'Maximum nesting depth reached'"
                        ),
                    ),
                    **alpine.on("click", alpine.expr(add_group_expression)),
                    class_=(
                        "inline-flex items-center rounded border border-dashed "
                        "border-border bg-card px-2 py-1 text-xs text-foreground "
                        "hover:bg-accent disabled:cursor-not-allowed "
                        "disabled:opacity-50 focus-visible:outline-none "
                        "focus-visible:ring-2 focus-visible:ring-ring"
                    ),
                ),
                class_="flex gap-2",
            ),
            role="group",
            **alpine.bind(
                "aria-label", alpine.expr(f"{variable}.logic + ' condition group'")
            ),
            class_=("qb-group mb-2 rounded-lg border border-border bg-muted/40 p-3"),
        )

    def render(self) -> Element:
        root_props = dict(self.props)
        explicit_id = root_props.pop("id", root_props.pop("id_", None))
        custom_class = root_props.pop("class_", root_props.pop("class", ""))
        for name in ("x-data", "x_data", "role"):
            root_props.pop(name, None)

        scope = get_render_scope().child("query-builder")
        identity_key = self.query_builder_key or (
            str(explicit_id) if explicit_id is not None else self.name
        )
        root_scope_id = scope.id("root", key=identity_key)
        root_id = str(explicit_id) if explicit_id is not None else root_scope_id
        input_id = scope.id("input", key=identity_key)
        status_id = scope.id("status", key=identity_key)
        controller_name = root_scope_id.replace("-", "_")
        root_class = " ".join(
            value for value in ("lex-query-builder w-full", custom_class) if value
        )

        return Element(
            "fieldset",
            Element(
                "legend",
                self.label or "Query filters",
                class_=(
                    "mb-1.5 block text-sm font-medium text-foreground"
                    if self.label
                    else "sr-only"
                ),
            ),
            Element(
                "input",
                id=input_id,
                type="hidden",
                name=self.name,
                value=dumps_str(self._serialize_node(self.tree)),
                **alpine.bind("value", alpine.expr("serialize()")),
            ),
            self._group_panel(self.max_depth, "tree", removable=False),
            Element(
                "p",
                id=status_id,
                **{"x-text": "announcement"},
                role="status",
                aria_live="polite",
                class_="sr-only",
            ),
            Element(
                "script",
                trusted_html(
                    self._controller_script(controller_name),
                    source="generated QueryBuilder Alpine controller",
                ),
            ),
            id=root_id,
            aria_describedby=status_id,
            **alpine.data(alpine.expr(controller_name)),
            class_=root_class,
            **root_props,
        )


__all__ = ["DEFAULT_OPERATORS", "OPERATOR_LABELS", "QueryBuilder"]
