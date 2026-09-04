"""Accessible Alpine-powered single- and multi-select controls."""

from __future__ import annotations

from typing import Any

from oridecon.ui.attributes.alpine import alpine
from oridecon.ui.core.base import Component, Element
from oridecon.ui.core.js import js_string
from oridecon.ui.core.render_context import get_render_scope

__all__ = ["RichSelect"]

_TRIGGER_CLS = (
    "w-full flex items-center justify-between gap-2 px-3 py-2 text-sm "
    "bg-background text-foreground border border-input rounded-lg shadow-sm "
    "focus:outline-none focus:ring-2 focus:ring-ring "
    "hover:border-ring transition-colors duration-150"
)
_DROPDOWN_CLS = (
    "absolute z-50 mt-1 w-full bg-card border "
    "border-border rounded-lg shadow-lg overflow-hidden"
)
_SEARCH_CLS = (
    "w-full px-3 py-2 text-sm border-b border-border "
    "bg-background text-foreground placeholder:text-muted-foreground focus:outline-none"
)
_OPTION_CLS = (
    "flex items-center gap-2 px-3 py-2 text-sm cursor-pointer "
    "text-foreground hover:bg-accent transition-colors duration-100 "
    "focus:outline-none focus:bg-accent"
)
_GROUP_LABEL_CLS = (
    "px-3 pt-3 pb-1 text-xs font-semibold uppercase tracking-wide text-muted-foreground"
)
_SELECTED_OPTION_CLS = "bg-accent text-accent-foreground"
_EMPTY_CLS = "px-3 py-4 text-sm text-center text-muted-foreground"
_ERROR_CLS = "mt-1.5 text-sm text-destructive"

_FOCUS_FIRST_OPTION = (
    "open = true; $nextTick(() => "
    "$refs.listbox.querySelector('[role=option]')?.focus())"
)
_FOCUS_LAST_OPTION = (
    "open = true; $nextTick(() => { "
    "const options = $refs.listbox.querySelectorAll('[role=option]'); "
    "options[options.length - 1]?.focus() })"
)
_FOCUS_NEXT_OPTION = (
    "const options = [...$refs.listbox.querySelectorAll('[role=option]')]"
    ".filter(option => option.offsetParent !== null); "
    "const index = options.indexOf($el); "
    "options[(index + 1) % options.length]?.focus()"
)
_FOCUS_PREVIOUS_OPTION = (
    "const options = [...$refs.listbox.querySelectorAll('[role=option]')]"
    ".filter(option => option.offsetParent !== null); "
    "const index = options.indexOf($el); "
    "options[(index - 1 + options.length) % options.length]?.focus()"
)


class RichSelect(Component):
    """Render a searchable single- or multi-select control.

    ``rich_select_key`` gives independently rendered fragments a stable DOM
    identity. Controls sharing a ``name`` in one render tree must provide
    distinct keys so duplicate labels, listboxes, and HTMX targets fail fast.
    """

    SEARCH_THRESHOLD = 8

    def __init__(
        self,
        label: str,
        name: str,
        options: list[dict[str, Any]] | None = None,
        multi: bool = False,
        search_url: str = "",
        groups: list[dict[str, Any]] | None = None,
        error: str | None = None,
        placeholder: str = "Select an option",
        rich_select_key: str | None = None,
        **props: Any,
    ) -> None:
        super().__init__(**props)
        self.label = label
        self.name = name
        self.options: list[dict[str, Any]] = options or []
        self.multi = multi
        self.search_url = search_url
        self.groups: list[dict[str, Any]] = groups or []
        self.error = error
        self.placeholder = placeholder
        self.rich_select_key = rich_select_key

    def _needs_search(self) -> bool:
        flat_count = len(self.options) + sum(
            len(group.get("options", [])) for group in self.groups
        )
        return (
            bool(self.search_url)
            or flat_count > self.SEARCH_THRESHOLD
            or bool(self.groups)
        )

    def _alpine_data(self) -> str:
        placeholder = js_string(self.placeholder)
        if self.multi:
            return (
                "{ open: false, search: '', selected: [], "
                "getLabel() { return this.selected.length ? "
                f"this.selected.length + ' selected' : {placeholder}; }}, "
                "isSelected(value) { return this.selected.includes(value); }, "
                "toggle(value) { const index = this.selected.indexOf(value); "
                "if (index > -1) this.selected.splice(index, 1); "
                "else this.selected.push(value); } }"
            )
        return (
            "{ open: false, search: '', selected: '', selectedLabel: '', "
            f"getLabel() {{ return this.selectedLabel || {placeholder}; }}, "
            "isSelected(value) { return this.selected === value; }, "
            "pick(value, label) { this.selected = value; "
            "this.selectedLabel = label; this.open = false; } }"
        )

    def _selection_icon(self, value_literal: str) -> Element:
        return Element(
            "svg",
            Element(
                "path",
                stroke_linecap="round",
                stroke_linejoin="round",
                d="M5 13l4 4L19 7",
            ),
            **alpine.show(alpine.expr(f"isSelected({value_literal})")),
            class_="w-3 h-3 text-white",
            fill="none",
            viewBox="0 0 24 24",
            stroke="currentColor",
            stroke_width="3",
            aria_hidden=True,
        )

    def _tick_icon(self, value_literal: str) -> Element:
        return Element(
            "svg",
            Element(
                "path",
                stroke_linecap="round",
                stroke_linejoin="round",
                d="M5 13l4 4L19 7",
            ),
            **alpine.show(alpine.expr(f"isSelected({value_literal})")),
            class_="ml-auto w-4 h-4 text-primary flex-shrink-0",
            fill="none",
            viewBox="0 0 24 24",
            stroke="currentColor",
            stroke_width="2.5",
            aria_hidden=True,
        )

    def _render_option(self, option: dict[str, Any]) -> Element:
        value = str(option.get("value", ""))
        label = str(option.get("label", ""))
        value_literal = js_string(value)
        label_literal = js_string(label)
        selected_expression = f"isSelected({value_literal})"
        click_expression = (
            f"toggle({value_literal})"
            if self.multi
            else f"pick({value_literal}, {label_literal}); $refs.trigger.focus()"
        )

        if self.multi:
            indicator = Element(
                "span",
                self._selection_icon(value_literal),
                **alpine.bind(
                    "class",
                    alpine.expr(
                        f"{selected_expression} ? "
                        "'bg-primary border-primary' : 'border-input'"
                    ),
                ),
                class_=(
                    "flex-shrink-0 w-4 h-4 border-2 rounded flex items-center "
                    "justify-center transition-colors"
                ),
                aria_hidden=True,
            )
            children: list[Any] = [indicator, Element("span", label)]
        else:
            children = [
                Element("span", label, class_="flex-1"),
                self._tick_icon(value_literal),
            ]

        attrs: dict[str, Any] = {
            "class_": _OPTION_CLS,
            "role": "option",
            "tabindex": "-1",
            "aria_selected": "false",
            **alpine.on("click", alpine.expr(click_expression)),
            **alpine.on("keydown", alpine.expr(click_expression), "enter", "prevent"),
            **alpine.on("keydown", alpine.expr(click_expression), "space", "prevent"),
            **alpine.on("keydown", alpine.expr(_FOCUS_NEXT_OPTION), "down", "prevent"),
            **alpine.on(
                "keydown", alpine.expr(_FOCUS_PREVIOUS_OPTION), "up", "prevent"
            ),
            **alpine.on(
                "keydown",
                alpine.expr("open = false; $refs.trigger.focus()"),
                "escape",
                "prevent",
            ),
            **alpine.bind(
                "class",
                alpine.expr(
                    f"{selected_expression} ? {js_string(_SELECTED_OPTION_CLS)} : ''"
                ),
            ),
            **alpine.bind("aria-selected", alpine.expr(selected_expression)),
        }
        if not self.search_url:
            attrs.update(
                alpine.show(
                    alpine.expr(
                        f"!search || {label_literal}.toLowerCase()"
                        ".includes(search.toLowerCase())"
                    )
                )
            )
        return Element("div", *children, **attrs)

    def _render_options(self) -> list[Element]:
        if self.groups:
            groups: list[Element] = []
            for group in self.groups:
                group_label = str(group.get("label", ""))
                group_options = [
                    self._render_option(option) for option in group.get("options", [])
                ]
                groups.append(
                    Element(
                        "div",
                        Element("div", group_label, class_=_GROUP_LABEL_CLS),
                        *group_options,
                        role="group",
                        aria_label=group_label,
                    )
                )
            return groups
        return [self._render_option(option) for option in self.options]

    def _render_trigger(self, trigger_id: str, options_id: str) -> Element:
        return Element(
            "button",
            Element("span", **{"x-text": "getLabel()"}, class_="truncate"),
            Element(
                "svg",
                Element(
                    "path",
                    stroke_linecap="round",
                    stroke_linejoin="round",
                    d="M19 9l-7 7-7-7",
                ),
                **alpine.bind("class", alpine.expr("open ? 'rotate-180' : ''")),
                class_=(
                    "w-4 h-4 flex-shrink-0 text-muted-foreground "
                    "transition-transform duration-200"
                ),
                fill="none",
                viewBox="0 0 24 24",
                stroke="currentColor",
                stroke_width="2",
                aria_hidden=True,
            ),
            id=trigger_id,
            type="button",
            role="combobox",
            aria_haspopup="listbox",
            aria_controls=options_id,
            aria_expanded="false",
            aria_label=self.label,
            aria_invalid="true" if self.error else None,
            **{"x-ref": "trigger"},
            **alpine.on("click", alpine.expr("open = !open")),
            **alpine.on("keydown", alpine.expr(_FOCUS_FIRST_OPTION), "down", "prevent"),
            **alpine.on("keydown", alpine.expr(_FOCUS_LAST_OPTION), "up", "prevent"),
            **alpine.on(
                "keydown", alpine.expr(_FOCUS_FIRST_OPTION), "enter", "prevent"
            ),
            **alpine.bind("aria-expanded", alpine.expr("open")),
            class_=_TRIGGER_CLS,
        )

    def _render_dropdown(self, options_id: str) -> Element:
        search_input: Any = None
        if self._needs_search():
            search_attrs: dict[str, Any] = {
                "type": "search",
                "placeholder": "Search…",
                "class_": _SEARCH_CLS,
                "autocomplete": "off",
                **alpine.model(alpine.expr("search")),
            }
            if self.search_url:
                search_attrs.update(
                    {
                        "hx-get": self.search_url,
                        "hx-trigger": "input changed delay:300ms",
                        "hx-target": f"#{options_id}",
                        "hx-include": "this",
                        "name": "q",
                    }
                )
            search_input = Element("input", **search_attrs)

        option_nodes = self._render_options()
        if not option_nodes and not self.search_url:
            option_nodes.append(
                Element("div", "No options available", class_=_EMPTY_CLS)
            )

        options_container = Element(
            "div",
            *option_nodes,
            id=options_id,
            role="listbox",
            aria_multiselectable="true" if self.multi else None,
            **{"x-ref": "listbox"},
            class_="max-h-56 overflow-y-auto py-1",
        )
        return Element(
            "div",
            search_input,
            options_container,
            **alpine.show(alpine.expr("open")),
            **alpine.transition(
                "enter", alpine.expr("transition ease-out duration-100")
            ),
            **alpine.transition("enter-start", alpine.expr("opacity-0 scale-95")),
            **alpine.transition("enter-end", alpine.expr("opacity-100 scale-100")),
            **alpine.transition("leave", alpine.expr("transition ease-in duration-75")),
            **alpine.transition("leave-start", alpine.expr("opacity-100 scale-100")),
            **alpine.transition("leave-end", alpine.expr("opacity-0 scale-95")),
            **{"x-cloak": True},
            class_=_DROPDOWN_CLS,
        )

    def _render_hidden_inputs(self) -> Element:
        if not self.multi:
            return Element(
                "input",
                type="hidden",
                name=self.name,
                **alpine.bind("value", alpine.expr("selected")),
            )
        return Element(
            "template",
            Element(
                "input",
                type="hidden",
                name=f"{self.name}[]",
                **alpine.bind("value", alpine.expr("value")),
            ),
            **{"x-for": "value in selected"},
            **alpine.bind("key", alpine.expr("value")),
        )

    def render(self) -> Element:
        root_props = dict(self.props)
        explicit_root_id = root_props.pop("id", None)
        identity_key = (
            self.rich_select_key or explicit_root_id or self.name.strip() or None
        )
        scope = get_render_scope().child("rich-select")
        root_scope_id = scope.id("root", key=identity_key)
        trigger_id = scope.id("trigger", key=identity_key)
        options_id = scope.id("options", key=identity_key)
        error_id = scope.id("error", key=identity_key) if self.error else None

        custom_class = root_props.pop("class_", root_props.pop("class", ""))
        root_class = " ".join(value for value in ("mb-6", custom_class) if value)
        trigger = self._render_trigger(trigger_id, options_id)
        if error_id is not None:
            trigger.attrs["aria_describedby"] = error_id

        error_node = (
            Element("p", self.error, id=error_id, class_=_ERROR_CLS)
            if self.error
            else None
        )
        ring_class = (
            "ring-destructive focus-within:ring-destructive"
            if self.error
            else "ring-[var(--input)] focus-within:ring-ring"
        )

        return Element(
            "div",
            Element(
                "label",
                self.label,
                for_=trigger_id,
                class_="block text-sm font-medium text-foreground mb-1",
            ),
            Element(
                "div",
                trigger,
                self._render_dropdown(options_id),
                self._render_hidden_inputs(),
                class_=f"relative block w-full rounded-lg ring-1 ring-inset {ring_class}",
            ),
            error_node,
            id=explicit_root_id or root_scope_id,
            **alpine.data(alpine.expr(self._alpine_data())),
            **alpine.on(
                "keydown",
                alpine.expr("if (open) { open = false; $refs.trigger.focus() }"),
                "escape",
                "window",
            ),
            **alpine.on("click", alpine.expr("open = false"), "outside"),
            class_=root_class,
            **root_props,
        )
