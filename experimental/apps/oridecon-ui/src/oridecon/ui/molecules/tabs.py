"""Accessible client-side tabs and ordinary URL navigation tabs."""

from __future__ import annotations

import re
from typing import Any

from oridecon.ui.attributes import alpine
from oridecon.ui.core.base import Component, el
from oridecon.ui.core.js import js_string

_HTML_ID = re.compile(r"^[A-Za-z][A-Za-z0-9_.:-]*$")
_TAB_BASE_CLASS = (
    "inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 "
    "py-1.5 text-sm font-medium ring-offset-background transition-all "
    "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring "
    "focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50"
)
_ACTIVE_CLASS = "bg-background text-foreground shadow"
_INACTIVE_CLASS = "text-muted-foreground hover:text-foreground"


def _focus_tab(expression: str) -> str:
    return (
        "const tabs = Array.from($el.querySelectorAll('[role=tab]:not([disabled])')); "
        "if (tabs.length) { "
        "const current = Math.max(0, tabs.indexOf(document.activeElement)); "
        f"const target = {expression}; "
        "target.focus(); target.click(); }"
    )


class Tabs(Component):
    """Render WAI-ARIA tabs or a set of ordinary page-navigation links.

    ``tabs_id`` is required until render scopes can allocate a stable key. This
    makes duplicate IDs a caller-visible error rather than silently emitting a
    page-global ``#tabs`` ID. Client-side tabs require exactly one ``TabPanel``
    for every tab value.
    """

    def __init__(
        self,
        tabs: list[tuple[str, str]],
        active_tab: str | None = None,
        client_side: bool = True,
        *,
        tabs_id: str | None = None,
        **props: Any,
    ) -> None:
        super().__init__(**props)
        if not tabs:
            raise ValueError("Tabs requires at least one tab")
        if not tabs_id:
            raise ValueError("Tabs requires a stable tabs_id")
        if not _HTML_ID.fullmatch(tabs_id):
            raise ValueError(f"tabs_id is not a valid HTML id: {tabs_id!r}")

        values = [value for _, value in tabs]
        if len(set(values)) != len(values):
            raise ValueError("Tabs values must be unique")
        active_id = active_tab or values[0]
        if active_id not in values:
            raise ValueError(f"Unknown active_tab: {active_id!r}")

        self.tabs = tabs
        self.active_id = active_id
        self.client_side = client_side
        self.tabs_id = tabs_id

    def _client_panels(self) -> list[Any]:
        panels: dict[str, TabPanel] = {}
        for child in self.children:
            if not isinstance(child, TabPanel):
                raise TypeError(
                    "Client-side Tabs children must all be TabPanel instances"
                )
            if child.id in panels:
                raise ValueError(f"Duplicate TabPanel value: {child.id!r}")
            panels[child.id] = child

        expected = [value for _, value in self.tabs]
        missing = [value for value in expected if value not in panels]
        extra = [value for value in panels if value not in expected]
        if missing or extra:
            details = []
            if missing:
                details.append(f"missing: {', '.join(missing)}")
            if extra:
                details.append(f"unknown: {', '.join(extra)}")
            raise ValueError(
                "Tab/TabPanel values must correspond exactly ("
                + "; ".join(details)
                + ")"
            )

        return [
            panels[value]._render_for(
                tabs_id=self.tabs_id,
                index=index,
                active=(value == self.active_id),
            )
            for index, value in enumerate(expected)
        ]

    def _mobile_selector(self) -> Any:
        if not self.client_side:
            return el(
                "nav",
                *[
                    el(
                        "a",
                        label,
                        href=value,
                        aria_current="page" if value == self.active_id else None,
                        class_="block rounded-md px-3 py-2 text-sm hover:bg-muted",
                    )
                    for label, value in self.tabs
                ],
                class_="sm:hidden mb-4 space-y-1",
                aria_label="Tabs",
            )

        select_id = f"{self.tabs_id}-select"
        return el(
            "div",
            el("label", "Select a tab", for_=select_id, class_="sr-only"),
            el(
                "select",
                *[
                    el(
                        "option",
                        label,
                        value=value,
                        selected=(value == self.active_id),
                    )
                    for label, value in self.tabs
                ],
                id=select_id,
                name=select_id,
                class_="block w-full h-10 rounded-md border-border focus:border-ring focus-visible:ring-ring bg-background text-foreground",
                **alpine.model(alpine.expr("activeTab")),
            ),
            class_="sm:hidden mb-4",
        )

    def _client_tablist(self) -> Any:
        keyboard = {
            **alpine.on(
                "keydown",
                alpine.expr(_focus_tab("tabs[(current + 1) % tabs.length]")),
                "right",
                "prevent",
            ),
            **alpine.on(
                "keydown",
                alpine.expr(
                    _focus_tab("tabs[(current - 1 + tabs.length) % tabs.length]")
                ),
                "left",
                "prevent",
            ),
            **alpine.on(
                "keydown",
                alpine.expr(_focus_tab("tabs[0]")),
                "home",
                "prevent",
            ),
            **alpine.on(
                "keydown",
                alpine.expr(_focus_tab("tabs[tabs.length - 1]")),
                "end",
                "prevent",
            ),
        }

        return el(
            "nav",
            *[
                el(
                    "button",
                    label,
                    type="button",
                    id=f"{self.tabs_id}-tab-{index}",
                    role="tab",
                    tabindex="0" if value == self.active_id else "-1",
                    aria_selected="true" if value == self.active_id else "false",
                    aria_controls=f"{self.tabs_id}-panel-{index}",
                    class_=_TAB_BASE_CLASS,
                    **alpine.on(
                        "click",
                        alpine.expr(f"activeTab = {js_string(value)}"),
                    ),
                    **alpine.bind(
                        "class",
                        alpine.expr(
                            f"activeTab === {js_string(value)} ? "
                            f"{js_string(_ACTIVE_CLASS)} : {js_string(_INACTIVE_CLASS)}"
                        ),
                    ),
                    **alpine.bind(
                        "aria-selected",
                        alpine.expr(
                            f"activeTab === {js_string(value)} ? 'true' : 'false'"
                        ),
                    ),
                    **alpine.bind(
                        "tabindex",
                        alpine.expr(f"activeTab === {js_string(value)} ? 0 : -1"),
                    ),
                )
                for index, (label, value) in enumerate(self.tabs)
            ],
            class_="inline-flex h-10 items-center justify-center rounded-md bg-muted p-1 text-muted-foreground",
            role="tablist",
            aria_label="Tabs",
            aria_orientation="horizontal",
            **keyboard,
        )

    def _url_tablist(self) -> Any:
        return el(
            "nav",
            *[
                el(
                    "a",
                    label,
                    href=value,
                    class_=f"{_TAB_BASE_CLASS} "
                    + (_ACTIVE_CLASS if value == self.active_id else _INACTIVE_CLASS),
                    aria_current="page" if value == self.active_id else None,
                    hx_get=value if value.startswith("/") else None,
                    hx_target="#main-content",
                    hx_swap="innerHTML",
                    hx_push_url="true",
                )
                for label, value in self.tabs
            ],
            class_="inline-flex h-10 items-center justify-center rounded-md bg-muted p-1 text-muted-foreground",
            aria_label="Tabs",
        )

    def render(self) -> Any:
        panels = self._client_panels() if self.client_side else list(self.children)
        tablist = self._client_tablist() if self.client_side else self._url_tablist()
        root_class = "oridecon-tabs"
        if extra_class := self.props.get("class_"):
            root_class = f"{root_class} {extra_class}"

        root_attrs: dict[str, str] = {}
        if self.client_side:
            root_attrs.update(
                alpine.data(
                    alpine.expr(f"{{ activeTab: {js_string(self.active_id)} }}")
                )
            )

        return el(
            "div",
            self._mobile_selector(),
            el("div", tablist, class_="hidden sm:block mb-6"),
            el("div", *panels, class_="mt-4"),
            id=self.tabs_id,
            class_=root_class,
            **root_attrs,
        )


class TabPanel(Component):
    """One panel whose value must correspond to a parent ``Tabs`` entry."""

    def __init__(self, tab_id: str, *children: Any, **props: Any) -> None:
        super().__init__(*children, **props)
        self.id = tab_id

    def _render_for(self, *, tabs_id: str, index: int, active: bool) -> Any:
        return el(
            "div",
            *self.children,
            role="tabpanel",
            aria_labelledby=f"{tabs_id}-tab-{index}",
            id=f"{tabs_id}-panel-{index}",
            tabindex="0",
            class_="tab-panel",
            **alpine.bind(
                "hidden",
                alpine.expr(f"activeTab !== {js_string(self.id)}"),
            ),
            **alpine.bind(
                "aria-hidden",
                alpine.expr(f"activeTab === {js_string(self.id)} ? 'false' : 'true'"),
            ),
            **({"data-active": "true"} if active else {}),
        )

    def render(self) -> Any:
        raise ValueError("TabPanel must be rendered as a child of Tabs")
