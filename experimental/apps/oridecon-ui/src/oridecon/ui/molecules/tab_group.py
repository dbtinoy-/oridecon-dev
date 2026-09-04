"""Alpine-managed tab groups for schema-driven resource forms."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from oridecon.ui import Component, Element, get_render_scope, js_string
from oridecon.ui.attributes.alpine import alpine


@dataclass(frozen=True, kw_only=True)
class Tab:
    """A single tab within a :class:`TabGroup`.

    ``icon`` is a structured renderable. Plain strings are display text; use a
    real element or ``TrustedHTML`` for intentionally authored icon markup.
    """

    name: str
    label: str
    schema_fields: list[Any] = field(default_factory=list)
    icon: Any | None = None
    badge: str | int | None = None


class TabGroup(Component):
    """Render schema fields in deterministic, ARIA-linked tab panels."""

    def __init__(
        self,
        tabs: list[Tab],
        default_tab: str | None = None,
        *,
        tab_group_key: str | None = None,
        **props: Any,
    ) -> None:
        super().__init__(**props)
        names = [tab.name for tab in tabs]
        if len(names) != len(set(names)):
            raise ValueError("TabGroup tab names must be unique")

        default = default_tab or (tabs[0].name if tabs else "")
        if tabs and default not in names:
            raise ValueError(f"TabGroup default_tab {default!r} is not a tab name")

        self.tabs = tabs
        self.default_tab = default
        self.tab_group_key = tab_group_key

    def render(self) -> Element:
        if not self.tabs:
            return Element("div", **self.props)

        scope = get_render_scope().child("tab-group")
        root_scope_id = scope.id("root", key=self.tab_group_key)
        identities = {
            tab.name: (
                scope.id("tab", key=f"{root_scope_id}-{tab.name}"),
                scope.id("panel", key=f"{root_scope_id}-{tab.name}"),
            )
            for tab in self.tabs
        }

        root_props = dict(self.props)
        custom_class = root_props.pop("class_", root_props.pop("class", ""))
        root_id = root_props.pop("id", root_scope_id)
        class_name = " ".join(value for value in ("w-full", custom_class) if value)
        return Element(
            "div",
            self._render_tab_bar(identities),
            self._render_panels(identities),
            id=root_id,
            **alpine.data(
                alpine.expr(f"{{ activeTab: {js_string(self.default_tab)} }}")
            ),
            class_=class_name,
            **root_props,
        )

    def _render_tab_bar(
        self,
        identities: dict[str, tuple[str, str]],
    ) -> Element:
        buttons: list[Element] = []
        for tab in self.tabs:
            tab_id, panel_id = identities[tab.name]
            active_expression = f"activeTab === {js_string(tab.name)}"
            classes = (
                "inline-flex items-center gap-1.5 px-4 py-2.5 text-sm font-medium "
                "border-b-2 transition-all duration-200 focus:outline-none "
                "data-[active=true]:border-primary-600 data-[active=true]:text-primary-600 "
                "border-transparent text-muted-foreground dark:text-muted-foreground "
                "hover:text-foreground dark:hover:text-foreground "
                "hover:border-border dark:hover:border-border"
            )

            button_content: list[Any] = []
            if tab.icon is not None:
                button_content.append(
                    Element("span", tab.icon, class_="w-4 h-4", aria_hidden=True)
                )
            button_content.append(Element("span", tab.label))
            if tab.badge is not None:
                button_content.append(
                    Element(
                        "span",
                        str(tab.badge),
                        class_=(
                            "ml-1.5 inline-flex items-center px-2 py-0.5 "
                            "rounded-full text-xs font-medium "
                            "bg-primary-100 text-primary-800 "
                            "dark:bg-primary-900 dark:text-primary-200"
                        ),
                    )
                )

            buttons.append(
                Element(
                    "button",
                    *button_content,
                    id=tab_id,
                    type="button",
                    role="tab",
                    aria_controls=panel_id,
                    aria_selected="true" if tab.name == self.default_tab else "false",
                    tabindex="0" if tab.name == self.default_tab else "-1",
                    **alpine.on(
                        "click",
                        alpine.expr(f"activeTab = {js_string(tab.name)}"),
                    ),
                    **alpine.on(
                        "keydown",
                        alpine.expr(
                            "const target = $el.nextElementSibling || "
                            "$el.parentElement.firstElementChild; "
                            "target.focus(); target.click()"
                        ),
                        "right",
                        "prevent",
                    ),
                    **alpine.on(
                        "keydown",
                        alpine.expr(
                            "const target = $el.previousElementSibling || "
                            "$el.parentElement.lastElementChild; "
                            "target.focus(); target.click()"
                        ),
                        "left",
                        "prevent",
                    ),
                    **alpine.on(
                        "keydown",
                        alpine.expr(
                            "const target = $el.parentElement.firstElementChild; "
                            "target.focus(); target.click()"
                        ),
                        "home",
                        "prevent",
                    ),
                    **alpine.on(
                        "keydown",
                        alpine.expr(
                            "const target = $el.parentElement.lastElementChild; "
                            "target.focus(); target.click()"
                        ),
                        "end",
                        "prevent",
                    ),
                    **alpine.bind("data-active", alpine.expr(active_expression)),
                    **alpine.bind("aria-selected", alpine.expr(active_expression)),
                    **alpine.bind(
                        "tabindex", alpine.expr(f"{active_expression} ? 0 : -1")
                    ),
                    class_=classes,
                )
            )

        return Element(
            "div",
            *buttons,
            role="tablist",
            class_="flex border-b border-border overflow-x-auto",
        )

    def _render_panels(
        self,
        identities: dict[str, tuple[str, str]],
    ) -> Element:
        panels: list[Element] = []
        for tab in self.tabs:
            tab_id, panel_id = identities[tab.name]
            panels.append(
                Element(
                    "div",
                    self._render_tab_content(tab),
                    id=panel_id,
                    role="tabpanel",
                    aria_labelledby=tab_id,
                    style=None if tab.name == self.default_tab else "display: none;",
                    **alpine.show(alpine.expr(f"activeTab === {js_string(tab.name)}")),
                    class_="pt-4",
                )
            )
        return Element("div", *panels, class_="w-full")

    def _render_tab_content(self, tab: Tab) -> Element:
        """Render schema controls without coercing structured output to text."""
        if not tab.schema_fields:
            return Element("div")

        rows: list[Any] = []
        for schema_field in tab.schema_fields:
            rows.append(schema_field.render_form(None))
        return Element("div", *rows, class_="space-y-4")
