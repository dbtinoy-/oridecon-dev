from __future__ import annotations

from typing import Any

from oridecon.ui.core.base import Component, el


class Fieldset(Component):
    """
    Native fieldset component for grouping form fields with a legend.

    Args:
        legend: The title of the fieldset
        description: Optional description text
    """

    def __init__(
        self,
        *children: Any,
        legend: str,
        description: str | None = None,
        **props: Any,
    ) -> None:
        super().__init__(*children, legend=legend, description=description, **props)
        self.legend = legend
        self.description = description

    def render(self) -> Any:
        legend_el = el(
            "legend",
            self.legend,
            class_="text-base font-semibold leading-6 text-foreground px-2",
        )

        desc_el = (
            el(
                "p",
                self.description,
                class_="mt-1 text-sm text-muted-foreground mb-4 px-2",
            )
            if self.description
            else ""
        )

        # Filter out props that shouldn't be attributes
        attrs = {
            k: v
            for k, v in self.props.items()
            if k not in ("legend", "description", "children")
        }

        return el(
            "fieldset",
            legend_el,
            desc_el,
            el("div", *self.children, class_="space-y-4"),
            class_="border border-border rounded-lg p-6 mb-6",
            **attrs,
        )
