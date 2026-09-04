"""Scoped block editor with structured field templates."""

from __future__ import annotations

from copy import copy, deepcopy
from typing import Any

from oridecon import serialization as json
from oridecon.serialization import dumps_str, loads_str
from oridecon.ui.atoms.icons import ICONS, get_icon
from oridecon.ui.attributes import alpine
from oridecon.ui.core.base import Component, Element, NoContext
from oridecon.ui.core.js import js_json, js_string
from oridecon.ui.core.render_context import get_render_scope
from oridecon.ui.core.trusted_html import trusted_html


class Builder(Component):
    """Edit an ordered list of typed blocks backed by one JSON form field."""

    def __init__(
        self,
        blocks: list[Any],
        name: str,
        value: list[dict[str, Any]] | str | None = None,
        label: str | None = None,
        builder_key: str | None = None,
        **props: Any,
    ) -> None:
        super().__init__(**props)
        if not name:
            raise ValueError("Builder name must not be empty")
        self.name = name
        self.label = label
        self.builder_key = builder_key
        self.blocks = list(blocks)
        self._block_definitions = self._validate_blocks(self.blocks)
        self.value = self._normalize_value(value)

    @staticmethod
    def _validate_blocks(blocks: list[Any]) -> list[dict[str, str]]:
        definitions: list[dict[str, str]] = []
        names: set[str] = set()
        for block in blocks:
            name = getattr(block, "name", None)
            label = getattr(block, "label", None)
            fields = getattr(block, "fields", None)
            if not isinstance(name, str) or not name:
                raise ValueError("each Builder block requires a non-empty name")
            if name in names:
                raise ValueError(f"duplicate Builder block name: {name!r}")
            if not isinstance(label, str) or not label:
                raise ValueError(f"Builder block {name!r} requires a label")
            if not isinstance(fields, (list, tuple)):
                raise TypeError(f"Builder block {name!r} fields must be a sequence")

            field_names: set[str] = set()
            for field in fields:
                field_name = getattr(field, "name", None)
                if not isinstance(field_name, str) or not field_name:
                    raise ValueError(
                        f"every field in Builder block {name!r} requires a name"
                    )
                if field_name in field_names:
                    raise ValueError(
                        f"duplicate field {field_name!r} in Builder block {name!r}"
                    )
                field_names.add(field_name)

            names.add(name)
            requested_icon = getattr(block, "icon", None)
            icon = (
                requested_icon
                if isinstance(requested_icon, str) and requested_icon in ICONS
                else "box"
            )
            definitions.append({"type": name, "label": label, "icon": icon})
        return definitions

    def _normalize_value(
        self, value: list[dict[str, Any]] | str | None
    ) -> list[dict[str, Any]]:
        if isinstance(value, str):
            if not value:
                value = []
            else:
                try:
                    value = loads_str(value)
                except (ValueError, TypeError, json.JSONDecodeError):
                    value = []
        if value is None:
            value = []
        if not isinstance(value, list):
            raise TypeError("Builder value must be a list or a JSON list")

        known_types = {definition["type"] for definition in self._block_definitions}
        normalized: list[dict[str, Any]] = []
        for index, item in enumerate(value):
            if not isinstance(item, dict):
                raise TypeError(f"Builder item {index} must be an object")
            block_type = item.get("type")
            if not isinstance(block_type, str) or block_type not in known_types:
                raise ValueError(f"unknown Builder block type: {block_type!r}")
            data = item.get("data", {})
            if not isinstance(data, dict):
                raise TypeError(f"Builder item {index} data must be an object")
            normalized.append({"type": block_type, "data": deepcopy(data)})
        return normalized

    @staticmethod
    def _resolve_field_element(field: Any) -> Element:
        candidate = field
        seen: set[int] = set()
        while isinstance(candidate, Component):
            identity = id(candidate)
            if identity in seen:
                raise TypeError("Builder field rendering contains a component cycle")
            seen.add(identity)
            with NoContext():
                candidate = candidate.render()
        if isinstance(candidate, (list, tuple)) and len(candidate) == 1:
            candidate = candidate[0]
        if not isinstance(candidate, Element):
            raise TypeError(
                "Builder fields must render exactly one structured Element root"
            )
        return candidate

    @staticmethod
    def _reference_expression(value: Any, reference_ids: dict[str, str]) -> str | None:
        tokens = str(value).split()
        if not tokens:
            return None
        expressions = [reference_ids.get(token, js_string(token)) for token in tokens]
        return " + ' ' + ".join(expressions)

    def _bind_field_element(
        self,
        field: Any,
        *,
        block_name: str,
        item_expression: str,
    ) -> Element:
        root = self._resolve_field_element(field)
        field_name = str(field.name)
        reference_ids: dict[str, str] = {}

        def collect_ids(node: Any) -> None:
            if isinstance(node, (list, tuple)):
                for child in node:
                    collect_ids(child)
                return
            if not isinstance(node, Element):
                return
            element_id = node.attrs.get("id", node.attrs.get("id_"))
            if element_id:
                reference_ids[str(element_id)] = (
                    f"fieldId({item_expression}.id, {js_string(block_name)}, "
                    f"{js_string(field_name)}, {js_string(str(element_id))})"
                )
            for child in node.children:
                collect_ids(child)

        collect_ids(root)
        control_number = 0

        def transform(node: Any) -> Any:
            nonlocal control_number
            if isinstance(node, list):
                return [transform(child) for child in node]
            if isinstance(node, tuple):
                return tuple(transform(child) for child in node)
            if not isinstance(node, Element):
                return node

            clone = copy(node)
            attrs = dict(node.attrs)
            static_id = attrs.pop("id", attrs.pop("id_", None))
            if static_id is not None:
                attrs["x-bind:id"] = reference_ids[str(static_id)]

            reference_attributes = (
                ("for", "for"),
                ("for_", "for"),
                ("aria-describedby", "aria-describedby"),
                ("aria_describedby", "aria-describedby"),
                ("aria-labelledby", "aria-labelledby"),
                ("aria_labelledby", "aria-labelledby"),
                ("aria-errormessage", "aria-errormessage"),
                ("aria_errormessage", "aria-errormessage"),
                ("aria-controls", "aria-controls"),
                ("aria_controls", "aria-controls"),
                ("list", "list"),
            )
            for attribute, rendered_name in reference_attributes:
                if attribute not in attrs:
                    continue
                expression = self._reference_expression(
                    attrs.pop(attribute), reference_ids
                )
                if expression:
                    attrs[f"x-bind:{rendered_name}"] = expression

            if node.tag in {"input", "select", "textarea"}:
                control_number += 1
                input_type = str(attrs.get("type", attrs.get("type_", ""))).lower()
                if input_type == "file":
                    raise ValueError(
                        "Builder does not support file fields because its payload is JSON"
                    )
                if any(
                    key in {"x-model", "x_model"}
                    or key.startswith(("x-model.", "x_model_"))
                    for key in attrs
                ):
                    raise ValueError(
                        f"Builder field {field_name!r} already owns an x-model binding"
                    )
                attrs.pop("name", None)
                attrs.pop("name_", None)
                model_attribute = (
                    "x-model.number" if input_type in {"number", "range"} else "x-model"
                )
                attrs[model_attribute] = (
                    f"{item_expression}.data[{js_string(field_name)}]"
                )
                attrs["data-builder-field"] = field_name
                if static_id is None:
                    suffix = f"control-{control_number}"
                    attrs["x-bind:id"] = (
                        f"fieldId({item_expression}.id, {js_string(block_name)}, "
                        f"{js_string(field_name)}, {js_string(suffix)})"
                    )

            clone.attrs = attrs
            clone.children = [transform(child) for child in node.children]
            return clone

        transformed = transform(root)
        if not isinstance(transformed, Element):  # pragma: no cover - root invariant
            raise TypeError("Builder field transformation lost its Element root")
        if control_number == 0:
            raise ValueError(
                f"Builder field {field_name!r} must render an input, select, or textarea"
            )
        return transformed

    def _controller_script(self, controller_name: str) -> str:
        initial_items = [
            {
                "id": f"item-{index}",
                "type": item["type"],
                "data": item["data"],
            }
            for index, item in enumerate(self.value, start=1)
        ]
        return f"""
(() => {{
    const controllerName = {js_string(controller_name)};
    const initialItems = {js_json(initial_items)};
    const blockDefinitions = {js_json(self._block_definitions)};
    const initialNextId = {js_json(len(initial_items) + 1)};

    const controller = () => ({{
        items: JSON.parse(JSON.stringify(initialItems)),
        blocks: blockDefinitions,
        nextId: initialNextId,
        announcement: '',
        newId() {{ return `${{controllerName}}-${{this.nextId++}}`; }},
        blockDefinition(type) {{
            return this.blocks.find(block => block.type === type) || null;
        }},
        itemLabel(item) {{
            return this.blockDefinition(item.type)?.label || item.type;
        }},
        fieldId(itemId, blockType, fieldName, suffix) {{
            const safe = value => String(value).replace(/[^A-Za-z0-9_-]+/g, '-');
            return [controllerName, safe(itemId), safe(blockType),
                safe(fieldName), safe(suffix)].join('-');
        }},
        addBlock(type) {{
            const definition = this.blockDefinition(type);
            if (!definition) return;
            this.items.push({{id: this.newId(), type, data: {{}}}});
            this.announcement = `${{definition.label}} block added`;
        }},
        removeBlock(id) {{
            const index = this.items.findIndex(item => item.id === id);
            if (index < 0) return;
            const label = this.itemLabel(this.items[index]);
            this.items.splice(index, 1);
            this.announcement = `${{label}} block removed`;
        }},
        moveBlock(id, direction) {{
            const index = this.items.findIndex(item => item.id === id);
            const target = direction === 'up' ? index - 1 :
                (direction === 'down' ? index + 1 : index);
            if (index < 0 || target < 0 || target >= this.items.length || target === index) {{
                return;
            }}
            const [item] = this.items.splice(index, 1);
            this.items.splice(target, 0, item);
            this.announcement = `${{this.itemLabel(item)}} block moved ${{direction}}`;
        }},
        serialize() {{
            return JSON.stringify(this.items.map(item => ({{
                type: item.type, data: item.data
            }})));
        }}
    }});

    const register = () => window.Alpine.data(controllerName, controller);
    if (window.Alpine) register();
    else document.addEventListener('alpine:init', register, {{once: true}});
}})();
"""

    def _block_template(self, block: Any) -> Element:
        fields = [
            self._bind_field_element(
                field,
                block_name=block.name,
                item_expression="item",
            )
            for field in block.fields
        ]
        return Element(
            "template",
            Element("div", *fields, class_="space-y-4"),
            **{"x-if": f"item.type === {js_string(block.name)}"},
        )

    def _item_template(self) -> Element:
        return Element(
            "template",
            Element(
                "article",
                Element(
                    "header",
                    Element(
                        "span",
                        **{"x-text": "itemLabel(item)"},
                        class_=(
                            "text-xs font-bold uppercase tracking-wider "
                            "text-muted-foreground"
                        ),
                    ),
                    Element(
                        "div",
                        Element(
                            "button",
                            get_icon("chevron-up", class_name="h-4 w-4"),
                            type="button",
                            title="Move block up",
                            **alpine.bind(
                                "aria-label",
                                alpine.expr("'Move ' + itemLabel(item) + ' block up'"),
                            ),
                            **alpine.bind("disabled", alpine.expr("index === 0")),
                            **alpine.on(
                                "click", alpine.expr("moveBlock(item.id, 'up')")
                            ),
                            class_=(
                                "rounded p-1 hover:bg-accent disabled:cursor-not-allowed "
                                "disabled:opacity-40 focus-visible:outline-none "
                                "focus-visible:ring-2 focus-visible:ring-ring"
                            ),
                        ),
                        Element(
                            "button",
                            get_icon("chevron-down", class_name="h-4 w-4"),
                            type="button",
                            title="Move block down",
                            **alpine.bind(
                                "aria-label",
                                alpine.expr(
                                    "'Move ' + itemLabel(item) + ' block down'"
                                ),
                            ),
                            **alpine.bind(
                                "disabled",
                                alpine.expr("index === items.length - 1"),
                            ),
                            **alpine.on(
                                "click", alpine.expr("moveBlock(item.id, 'down')")
                            ),
                            class_=(
                                "rounded p-1 hover:bg-accent disabled:cursor-not-allowed "
                                "disabled:opacity-40 focus-visible:outline-none "
                                "focus-visible:ring-2 focus-visible:ring-ring"
                            ),
                        ),
                        Element(
                            "button",
                            get_icon("trash", class_name="h-4 w-4 text-destructive"),
                            type="button",
                            title="Remove block",
                            **alpine.bind(
                                "aria-label",
                                alpine.expr("'Remove ' + itemLabel(item) + ' block'"),
                            ),
                            **alpine.on("click", alpine.expr("removeBlock(item.id)")),
                            class_=(
                                "ml-2 rounded p-1 hover:bg-accent "
                                "focus-visible:outline-none focus-visible:ring-2 "
                                "focus-visible:ring-ring"
                            ),
                        ),
                        class_="flex items-center gap-1",
                    ),
                    class_=(
                        "flex items-center justify-between border-b border-border "
                        "bg-muted px-4 py-2"
                    ),
                ),
                Element(
                    "div",
                    *[self._block_template(block) for block in self.blocks],
                    class_="p-4",
                ),
                **alpine.bind("aria-label", alpine.expr("itemLabel(item) + ' block'")),
                class_=("mb-4 overflow-hidden rounded-lg border border-border bg-card"),
            ),
            **{"x-for": "(item, index) in items"},
            **alpine.bind("key", alpine.expr("item.id")),
        )

    def _add_buttons(self) -> Element:
        return Element(
            "div",
            Element(
                "p",
                "Add a content block",
                class_="mb-3 text-sm font-medium text-foreground",
            ),
            Element(
                "div",
                *[
                    Element(
                        "button",
                        get_icon(definition["icon"], class_name="mr-2 h-4 w-4"),
                        definition["label"],
                        type="button",
                        **alpine.on(
                            "click",
                            alpine.expr(f"addBlock({js_string(definition['type'])})"),
                        ),
                        class_=(
                            "inline-flex items-center rounded-md border "
                            "border-dashed border-border bg-card px-4 py-2 "
                            "text-sm font-medium text-foreground shadow-sm "
                            "hover:bg-accent focus-visible:outline-none "
                            "focus-visible:ring-2 focus-visible:ring-ring"
                        ),
                    )
                    for definition in self._block_definitions
                ],
                class_="flex flex-wrap gap-2",
            ),
            class_=("mt-6 rounded-xl border-2 border-dashed border-border p-4"),
        )

    def render(self) -> Element:
        root_props = dict(self.props)
        explicit_id = root_props.pop("id", root_props.pop("id_", None))
        custom_class = root_props.pop("class_", root_props.pop("class", ""))
        for protected_name in ("x-data", "x_data", "role"):
            root_props.pop(protected_name, None)

        scope = get_render_scope().child("builder")
        identity_key = self.builder_key or (
            str(explicit_id) if explicit_id is not None else self.name
        )
        root_scope_id = scope.id("root", key=identity_key)
        root_id = str(explicit_id) if explicit_id is not None else root_scope_id
        input_id = scope.id("input", key=identity_key)
        status_id = scope.id("status", key=identity_key)
        controller_name = root_scope_id.replace("-", "_")
        root_class = " ".join(
            value for value in ("lex-builder w-full", custom_class) if value
        )

        return Element(
            "fieldset",
            Element(
                "legend",
                self.label or "Content blocks",
                class_=(
                    "mb-3 block text-sm font-medium text-foreground"
                    if self.label
                    else "sr-only"
                ),
            ),
            Element(
                "input",
                id=input_id,
                type="hidden",
                name=self.name,
                value=dumps_str(self.value),
                **alpine.bind("value", alpine.expr("serialize()")),
            ),
            Element("div", self._item_template(), class_="builder-items"),
            Element(
                "p",
                "No blocks added yet.",
                **alpine.show(alpine.expr("items.length === 0")),
                class_="rounded-lg border border-dashed border-border p-6 text-center text-sm text-muted-foreground",
            ),
            self._add_buttons(),
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
                    source="generated Builder Alpine controller",
                ),
            ),
            id=root_id,
            aria_describedby=status_id,
            **alpine.data(alpine.expr(controller_name)),
            class_=root_class,
            **root_props,
        )


__all__ = ["Builder"]
