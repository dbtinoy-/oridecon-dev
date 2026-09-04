"""Dynamic, reorderable groups of schema controls."""

from __future__ import annotations

import html
import re
from typing import TYPE_CHECKING, Any

from oridecon.ui.attributes.alpine import alpine
from oridecon.ui.core.base import Component, Element, render_child_to_string
from oridecon.ui.core.js import js_json, js_string
from oridecon.ui.core.render_context import get_render_scope
from oridecon.ui.core.trusted_html import trusted_html

if TYPE_CHECKING:
    from collections.abc import Callable

_ATTRIBUTE = re.compile(r'(?P<space>\s)(?P<name>name|id|for)="(?P<value>[^"]*)"')
_FORM_CONTROL = re.compile(
    r"<(?P<tag>input|select|textarea)\b(?P<attrs>[^>]*)>",
    re.IGNORECASE,
)
_NAME_ATTRIBUTE = re.compile(r'(?P<space>\s)name="(?P<value>[^"]*)"')
_INPUT_TYPE = re.compile(r'\stype="(?P<value>[^"]*)"', re.IGNORECASE)


class Repeater(Component):
    """Allow users to add, remove, and reorder repeated schema controls.

    ``repeater_key`` provides stable identity for independently rendered form
    fragments. Schema components are rendered under child escaping rules before
    their owned ``name``/``id``/``for`` attributes are adapted for Alpine.
    """

    def __init__(
        self,
        name: str,
        schema: list[Component] | Callable[[], list[Component]],
        value: list[dict[str, Any]] | None = None,
        label: str | None = None,
        add_label: str = "Add Item",
        item_label: str = "Item",
        repeater_key: str | None = None,
        **props: Any,
    ) -> None:
        super().__init__(**props)
        self.name = name
        self.schema = schema
        self.value = value or []
        self.label = label
        self.add_label = add_label
        self.item_label = item_label
        self.repeater_key = repeater_key

    def _attribute_binding(
        self,
        attribute: str,
        value: str,
        *,
        leading_space: str = " ",
    ) -> str:
        original = html.unescape(value)
        if attribute == "name":
            expression = (
                f"{js_string(self.name)} + '[' + index + '][' + "
                f"{js_string(original)} + ']'"
            )
        else:
            expression = (
                f"{js_string(self.name)} + '_' + index + '_' + {js_string(original)}"
            )
        return (
            f'{leading_space}x-bind:{attribute}="{html.escape(expression, quote=True)}"'
        )

    def _bind_form_control(self, match: re.Match[str]) -> str:
        tag = match.group("tag")
        attrs = match.group("attrs")
        name_match = _NAME_ATTRIBUTE.search(attrs)
        if name_match is None:
            return match.group(0)

        field_name = html.unescape(name_match.group("value"))
        name_binding = self._attribute_binding(
            "name",
            name_match.group("value"),
            leading_space=name_match.group("space"),
        )
        attrs = _NAME_ATTRIBUTE.sub(lambda _match: name_binding, attrs, count=1)

        has_model = " x-model=" in attrs or " x-model." in attrs
        type_match = _INPUT_TYPE.search(attrs)
        input_type = type_match.group("value").lower() if type_match else ""
        if not has_model and input_type != "file":
            modifier = ".number" if input_type in {"number", "range"} else ""
            model = html.escape(f"item[{js_string(field_name)}]", quote=True)
            if attrs.rstrip().endswith("/"):
                attrs = f'{attrs.rstrip()[:-1].rstrip()} x-model{modifier}="{model}" /'
            else:
                attrs = f'{attrs} x-model{modifier}="{model}"'
        return f"<{tag}{attrs}>"

    def _template_html(self) -> str:
        components = self.schema() if callable(self.schema) else self.schema
        rendered = render_child_to_string(components)
        rendered = _FORM_CONTROL.sub(self._bind_form_control, rendered)

        def replace_attribute(match: re.Match[str]) -> str:
            return self._attribute_binding(
                match.group("name"),
                match.group("value"),
                leading_space=match.group("space"),
            )

        return _ATTRIBUTE.sub(replace_attribute, rendered)

    def _alpine_data(self) -> str:
        initial_items = js_json(self.value)
        return (
            "{ "
            f"nextKey: {len(self.value)}, "
            f"items: {initial_items}.map((item, index) => "
            "({ ...item, _orideconKey: 'existing-' + index })), "
            "addItem() { this.items.push({ "
            "_orideconKey: 'new-' + this.nextKey++ }); }, "
            "removeItem(index) { this.items.splice(index, 1); }, "
            "moveUp(index) { if (index > 0) "
            "[this.items[index - 1], this.items[index]] = "
            "[this.items[index], this.items[index - 1]]; }, "
            "moveDown(index) { if (index < this.items.length - 1) "
            "[this.items[index + 1], this.items[index]] = "
            "[this.items[index], this.items[index + 1]]; } "
            "}"
        )

    @staticmethod
    def _icon(path: str, *, size: str) -> Element:
        return Element(
            "svg",
            Element(
                "path",
                d=path,
                stroke_linecap="round",
                stroke_linejoin="round",
                stroke_width="2",
            ),
            class_=size,
            fill="none",
            viewBox="0 0 24 24",
            stroke="currentColor",
            aria_hidden=True,
        )

    def _action_button(
        self,
        *,
        action: str,
        label: str,
        icon_path: str,
        class_name: str,
        show: str | None = None,
    ) -> Element:
        attrs: dict[str, Any] = {
            "type": "button",
            "title": label,
            "aria_label": label,
            "class_": class_name,
            **alpine.on("click", alpine.expr(action)),
            **alpine.bind(
                "aria-label",
                alpine.expr(
                    f"{js_string(label)} + ' ' + {js_string(self.item_label)} + "
                    "' ' + (index + 1)"
                ),
            ),
        }
        if show is not None:
            attrs.update(alpine.show(alpine.expr(show)))
        return Element(
            "button",
            self._icon(icon_path, size="w-4 h-4"),
            **attrs,
        )

    def _render_header(self, label_id: str | None) -> Element:
        return Element(
            "div",
            (
                Element(
                    "h4",
                    self.label,
                    id=label_id,
                    class_="text-sm font-semibold text-foreground",
                )
                if self.label
                else None
            ),
            Element(
                "button",
                self._icon("M12 4v16m8-8H4", size="w-4 h-4 mr-1"),
                self.add_label,
                type="button",
                **alpine.on("click", alpine.expr("addItem()")),
                class_=(
                    "inline-flex items-center px-3 py-1.5 text-xs font-semibold "
                    "text-primary bg-primary/5 rounded-lg hover:bg-primary/15 "
                    "transition-all duration-200"
                ),
            ),
            class_="flex items-center justify-between mb-4",
        )

    def _render_item_template(self) -> Element:
        item_heading = f"{js_string(self.item_label)} + ' #' + (index + 1)"
        return Element(
            "template",
            Element(
                "div",
                Element(
                    "div",
                    Element(
                        "span",
                        **{"x-text": item_heading},
                        class_=(
                            "text-xs font-bold text-muted-foreground uppercase "
                            "tracking-wider"
                        ),
                    ),
                    Element(
                        "div",
                        self._action_button(
                            action="moveUp(index)",
                            label="Move up",
                            icon_path="M5 15l7-7 7 7",
                            class_name=(
                                "p-1 text-muted-foreground hover:text-primary "
                                "transition-colors"
                            ),
                            show="index > 0",
                        ),
                        self._action_button(
                            action="moveDown(index)",
                            label="Move down",
                            icon_path="M19 9l-7 7-7-7",
                            class_name=(
                                "p-1 text-muted-foreground hover:text-primary "
                                "transition-colors"
                            ),
                            show="index < items.length - 1",
                        ),
                        self._action_button(
                            action="removeItem(index)",
                            label="Remove",
                            icon_path=(
                                "M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 "
                                "0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 "
                                "00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                            ),
                            class_name=(
                                "ml-2 p-1 text-muted-foreground hover:text-destructive "
                                "transition-colors"
                            ),
                        ),
                        class_="flex items-center gap-1",
                    ),
                    class_=(
                        "flex items-center justify-between px-4 py-2 bg-muted "
                        "border-b border-border"
                    ),
                ),
                Element(
                    "div",
                    trusted_html(
                        self._template_html(),
                        source="Repeater transformed schema template",
                    ),
                    class_="p-4 grid grid-cols-1 gap-4 sm:grid-cols-2",
                ),
                class_=(
                    "bg-card border border-border rounded-xl overflow-hidden "
                    "mb-4 shadow-sm"
                ),
            ),
            **{"x-for": "(item, index) in items"},
            **alpine.bind("key", alpine.expr("item._orideconKey")),
        )

    def render(self) -> Element:
        root_props = dict(self.props)
        explicit_id = root_props.pop("id", root_props.pop("id_", None))
        custom_class = root_props.pop("class_", root_props.pop("class", ""))
        for protected_name in (
            "x-data",
            "x_data",
            "role",
            "aria-labelledby",
            "aria_labelledby",
            "aria-label",
            "aria_label",
        ):
            root_props.pop(protected_name, None)

        scope = get_render_scope().child("repeater")
        identity_key = self.repeater_key or (
            str(explicit_id) if explicit_id is not None else self.name.strip() or None
        )
        root_scope_id = scope.id("group", key=identity_key)
        label_id = scope.id("label", key=root_scope_id) if self.label else None
        root_class = " ".join(
            value for value in ("repeater-container mb-8", custom_class) if value
        )

        return Element(
            "div",
            self._render_header(label_id),
            self._render_item_template(),
            Element(
                "p",
                "No items added.",
                **alpine.show(alpine.expr("items.length === 0")),
                class_=(
                    "text-center py-8 border-2 border-dashed border-border rounded-xl "
                    "text-sm text-muted-foreground"
                ),
                aria_live="polite",
            ),
            id=explicit_id or root_scope_id,
            role="group",
            aria_labelledby=label_id,
            aria_label=None if label_id else f"{self.item_label} collection",
            **alpine.data(alpine.expr(self._alpine_data())),
            class_=root_class,
            **root_props,
        )
