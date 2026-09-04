"""JSON-backed repeatable schema field."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from oridecon.admin.schema.base import SchemaField
from oridecon.admin.schema.exceptions import FieldError
from oridecon.result import Err, Ok, Result
from oridecon.serialization import dumps_str, loads_str
from oridecon.ui import Element, RenderScope, get_render_scope, js_json, js_string
from oridecon.ui.attributes.alpine import alpine


@dataclass(frozen=True, kw_only=True)
class RepeaterField(SchemaField[list[dict[str, Any]]]):
    """Edit an ordered collection through one JSON form value.

    Sub-field controls are bound to Alpine item state. Only the hidden JSON
    input is submitted, preventing duplicate scalar values from competing with
    the collection payload.
    """

    fields: list[SchemaField[Any]] = field(default_factory=list)
    min_items: int = 0
    max_items: int | None = None
    add_button_label: str = "Add Item"
    repeater_key: str | None = None

    def __post_init__(self) -> None:
        if self.min_items < 0:
            raise ValueError("RepeaterField min_items must be zero or greater")
        if self.max_items is not None and self.max_items < self.min_items:
            raise ValueError("RepeaterField max_items must be at least min_items")
        names = [subfield.name for subfield in self.fields]
        if len(names) != len(set(names)):
            raise ValueError("RepeaterField sub-field names must be unique")

    @staticmethod
    def _remove_icon() -> Element:
        return Element(
            "svg",
            Element(
                "path",
                stroke_linecap="round",
                stroke_linejoin="round",
                stroke_width="2",
                d="M6 18L18 6M6 6l12 12",
            ),
            class_="w-4 h-4",
            fill="none",
            viewBox="0 0 24 24",
            stroke="currentColor",
            aria_hidden=True,
        )

    @staticmethod
    def _arrow_icon(path: str) -> Element:
        return Element(
            "svg",
            Element(
                "path",
                stroke_linecap="round",
                stroke_linejoin="round",
                stroke_width="2",
                d=path,
            ),
            class_="w-3 h-3",
            fill="none",
            viewBox="0 0 24 24",
            stroke="currentColor",
            aria_hidden=True,
        )

    def _initial_items(
        self, value: list[dict[str, Any]] | None
    ) -> list[dict[str, Any]]:
        items = [dict(item) for item in (value or [])]
        items.extend({} for _ in range(max(0, self.min_items - len(items))))
        return items

    def _alpine_data(self, items: list[dict[str, Any]]) -> str:
        return (
            "{ "
            f"nextKey: {len(items)}, "
            f"items: {js_json(items)}.map((item, index) => "
            "({ ...item, _orideconKey: 'existing-' + index })), "
            f"minItems: {self.min_items}, "
            f"maxItems: {js_json(self.max_items)}, "
            "addItem() { if (this.maxItems !== null && "
            "this.items.length >= this.maxItems) return; "
            "this.items.push({ _orideconKey: 'new-' + this.nextKey++ }); }, "
            "removeItem(index) { if (this.items.length <= this.minItems) return; "
            "this.items.splice(index, 1); }, "
            "moveItem(from, to) { if (to < 0 || to >= this.items.length) return; "
            "const [removed] = this.items.splice(from, 1); "
            "this.items.splice(to, 0, removed); }, "
            "get serialized() { return JSON.stringify(this.items.map(item => { "
            "const { _orideconKey, ...value } = item; return value; })); } "
            "}"
        )

    @staticmethod
    def _pop_attr(attrs: dict[str, Any], *names: str) -> Any:
        result = None
        for name in names:
            if name in attrs:
                result = attrs.pop(name)
        return result

    def _bind_template_node(
        self,
        node: Any,
        *,
        subfield: SchemaField[Any],
        scope: RenderScope,
        reference_ids: dict[str, str],
    ) -> None:
        if isinstance(node, (list, tuple)):
            for child in node:
                self._bind_template_node(
                    child,
                    subfield=subfield,
                    scope=scope,
                    reference_ids=reference_ids,
                )
            return
        if not isinstance(node, Element):
            return

        attrs = node.attrs
        original_name = self._pop_attr(attrs, "name")
        if node.tag in {"input", "select", "textarea"} and original_name is not None:
            normalized_name = str(original_name).removesuffix("[]")
            if normalized_name == subfield.name:
                model_expression = f"item[{js_string(subfield.name)}]"
                input_type = str(attrs.get("type", "")).lower()
                if input_type == "file":
                    raise ValueError(
                        "RepeaterField does not support file sub-fields because "
                        "its payload is JSON"
                    )
                model_attribute = (
                    "x-model.number" if input_type in {"number", "range"} else "x-model"
                )
                attrs[model_attribute] = model_expression
                attrs["data-repeater-field"] = subfield.name

        for attribute, aliases in (
            ("id", ("id", "id_")),
            ("for", ("for", "for_")),
            ("aria-describedby", ("aria-describedby", "aria_describedby")),
            ("aria-labelledby", ("aria-labelledby", "aria_labelledby")),
        ):
            original = self._pop_attr(attrs, *aliases)
            if not original:
                continue
            original_text = str(original)
            if original_text not in reference_ids:
                reference_ids[original_text] = scope.id(
                    "control",
                    key=f"{subfield.name}-{original_text}",
                )
            expression = f"{js_string(reference_ids[original_text])} + '-' + index"
            attrs.update(alpine.bind(attribute, alpine.expr(expression)))

        if attrs.get("role") == "switch":
            model = f"item[{js_string(subfield.name)}]"
            self._pop_attr(attrs, "x-data", "x_data")
            attrs.update(
                alpine.data(
                    alpine.expr(
                        "{ get enabled() { return Boolean("
                        f"{model}); }}, set enabled(value) {{ {model} = value; }} }}"
                    )
                )
            )

        for child in node.children:
            self._bind_template_node(
                child,
                subfield=subfield,
                scope=scope,
                reference_ids=reference_ids,
            )

    def _template_fields(self, scope: RenderScope) -> list[Element]:
        rows: list[Element] = []
        for subfield in self.fields:
            rendered = subfield.render_form(None)
            self._bind_template_node(
                rendered,
                subfield=subfield,
                scope=scope.child(subfield.name),
                reference_ids={},
            )
            rows.append(rendered)
        return rows

    def _action_button(
        self,
        *,
        label: str,
        expression: str,
        icon: Element,
        show: str | None = None,
    ) -> Element:
        attrs: dict[str, Any] = {
            "type": "button",
            "aria_label": label,
            "title": label,
            "class_": (
                "p-1 text-muted-foreground hover:text-primary "
                "transition-colors rounded focus:outline-none focus:ring-2 focus:ring-ring"
            ),
            **alpine.on("click", alpine.expr(expression)),
            **alpine.bind(
                "aria-label",
                alpine.expr(f"{js_string(label)} + ' item ' + (index + 1)"),
            ),
        }
        if show is not None:
            attrs.update(alpine.show(alpine.expr(show)))
        return Element("button", icon, **attrs)

    def _item_template(self, scope: RenderScope) -> Element:
        return Element(
            "template",
            Element(
                "div",
                Element(
                    "div",
                    Element(
                        "span",
                        **{"x-text": "'Item ' + (index + 1)"},
                        class_="text-xs font-semibold text-muted-foreground",
                    ),
                    Element(
                        "div",
                        self._action_button(
                            label="Move up",
                            expression="moveItem(index, index - 1)",
                            icon=self._arrow_icon("M5 15l7-7 7 7"),
                            show="index > 0",
                        ),
                        self._action_button(
                            label="Move down",
                            expression="moveItem(index, index + 1)",
                            icon=self._arrow_icon("M19 9l-7 7-7-7"),
                            show="index < items.length - 1",
                        ),
                        self._action_button(
                            label="Remove",
                            expression="removeItem(index)",
                            icon=self._remove_icon(),
                            show="items.length > minItems",
                        ),
                        class_="flex items-center gap-1",
                    ),
                    class_="mb-3 flex items-center justify-between",
                ),
                *self._template_fields(scope),
                class_=(
                    "relative p-4 border border-border rounded-xl "
                    "bg-card dark:bg-background"
                ),
            ),
            **{"x-for": "(item, index) in items"},
            **alpine.bind("key", alpine.expr("item._orideconKey")),
        )

    def render_form(
        self, value: list[dict[str, Any]] | None, *, errors: list[str] | None = None
    ) -> Element:
        items = self._initial_items(value)
        scope = get_render_scope().child("repeater-field")
        identity_key = self.repeater_key or self.name
        group_id = scope.id("group", key=identity_key)
        label_id = scope.id("label", key=identity_key) if self.label else None
        input_id = scope.id("input", key=identity_key)
        error_id = scope.id("error", key=identity_key) if errors else None

        add_button = Element(
            "button",
            self.add_button_label,
            type="button",
            **alpine.on("click", alpine.expr("addItem()")),
            **alpine.bind(
                "disabled",
                alpine.expr("maxItems !== null && items.length >= maxItems"),
            ),
            **alpine.bind(
                "aria-disabled",
                alpine.expr(
                    "(maxItems !== null && items.length >= maxItems).toString()"
                ),
            ),
            class_=(
                "mt-3 inline-flex items-center px-3 py-1.5 text-xs font-medium "
                "text-primary-600 bg-primary-50 dark:bg-primary-900/30 "
                "dark:text-primary-400 rounded-lg hover:bg-primary-100 "
                "disabled:cursor-not-allowed disabled:opacity-50 transition-colors"
            ),
        )
        hidden = Element(
            "input",
            id=input_id,
            type="hidden",
            name=self.name,
            **alpine.bind("value", alpine.expr("serialized")),
        )
        counter = Element(
            "p",
            **{
                "x-text": (
                    "maxItems === null ? `${items.length} item(s)` : "
                    "`${items.length} of ${maxItems} item(s)`"
                )
            },
            class_="text-xs text-muted-foreground mt-1",
            aria_live="polite",
        )
        error_node = (
            Element(
                "p",
                errors[0],
                id=error_id,
                role="alert",
                class_="mt-2 text-sm text-destructive",
            )
            if errors
            else None
        )

        return Element(
            "div",
            (
                Element(
                    "p",
                    self.label,
                    id=label_id,
                    class_="block text-sm font-medium text-foreground mb-2",
                )
                if self.label
                else None
            ),
            self._item_template(scope.child(group_id)),
            Element(
                "p",
                "No items added.",
                **alpine.show(alpine.expr("items.length === 0")),
                class_=(
                    "rounded-lg border border-dashed border-border p-4 "
                    "text-center text-sm text-muted-foreground"
                ),
            ),
            add_button,
            hidden,
            counter,
            error_node,
            id=group_id,
            role="group",
            aria_labelledby=label_id,
            aria_label=None if label_id else self.name.replace("_", " ").title(),
            aria_describedby=error_id,
            **alpine.data(alpine.expr(self._alpine_data(items))),
            class_="space-y-3 mb-6",
        )

    def render_column(self, record: Any, value: list[dict[str, Any]] | None) -> Element:
        if value is None:
            return Element("span", "\u2014", class_="text-muted")
        count = len(value)
        label = "item" if count == 1 else "items"
        return Element(
            "span",
            f"{count} {label}",
            class_="text-sm text-muted-foreground",
        )

    @staticmethod
    def _subfield_raw_value(value: Any) -> str | None:
        if value is None:
            return None
        if isinstance(value, str):
            return value
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, (dict, list)):
            return dumps_str(value)
        return str(value)

    def from_form(
        self, raw: str | None
    ) -> Result[list[dict[str, Any]] | None, FieldError]:
        if raw is None:
            if self.min_items:
                return Err(
                    FieldError(f"Must contain at least {self.min_items} item(s)")
                )
            return Ok(None)
        stripped = raw.strip()
        if not stripped:
            if self.min_items:
                return Err(
                    FieldError(f"Must contain at least {self.min_items} item(s)")
                )
            if self.nullable:
                return Ok(None)
            return Err(FieldError("Invalid JSON array"))
        try:
            parsed = loads_str(stripped)
        except ValueError:
            return Err(FieldError("Invalid JSON array"))
        if not isinstance(parsed, list):
            return Err(FieldError("Must be a JSON array"))
        if len(parsed) < self.min_items:
            return Err(FieldError(f"Must contain at least {self.min_items} item(s)"))
        if self.max_items is not None and len(parsed) > self.max_items:
            return Err(FieldError(f"Must contain at most {self.max_items} item(s)"))

        validated: list[dict[str, Any]] = []
        for index, item in enumerate(parsed):
            if not isinstance(item, dict):
                return Err(FieldError(f"Item {index} must be a JSON object"))
            validated_item: dict[str, Any] = {}
            for subfield in self.fields:
                sub_result = subfield.from_form(
                    self._subfield_raw_value(item.get(subfield.name))
                )
                if sub_result.is_err():
                    return Err(
                        FieldError(
                            f"Item {index}.{subfield.name}: {sub_result.unwrap_err()}"
                        )
                    )
                validated_item[subfield.name] = sub_result.unwrap()
            validated.append(validated_item)
        return Ok(validated)

    def to_form(self, value: list[dict[str, Any]] | None) -> str:
        return "" if value is None else dumps_str(value)
