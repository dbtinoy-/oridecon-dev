"""Accessible, trigger-owned tooltip atom."""

from __future__ import annotations

from copy import copy
from typing import Any

from oridecon.ui.attributes import alpine
from oridecon.ui.core.base import Component, Element, el

_POSITIONS = {
    "top": "bottom-full left-1/2 mb-2 -translate-x-1/2",
    "right": "left-full top-1/2 ml-2 -translate-y-1/2",
    "bottom": "top-full left-1/2 mt-2 -translate-x-1/2",
    "left": "right-full top-1/2 mr-2 -translate-y-1/2",
}
_TRIGGER_EVENTS = {
    "x-on:mouseenter": "open = true",
    "x-on:mouseleave": "open = false",
    "x-on:focus": "open = true",
    "x-on:blur": "open = false",
    "x-on:keydown.escape.stop": "open = false; $el.blur()",
}


class Tooltip(Component):
    """Attach non-interactive help text to exactly one focusable trigger.

    The trigger is cloned before ``aria-describedby`` and Alpine handlers are
    applied, so caller-owned elements remain unchanged. Supply a stable
    ``tooltip_id`` or a stable trigger ``id``/``trigger_id`` from which the
    tooltip ID can be derived.

    Args:
        content: Plain-text tooltip content.
        children: Exactly one trigger element or component rendering one root.
        position: One of ``top``, ``right``, ``bottom``, or ``left``.
        tooltip_id: Stable ID for the tooltip node.
        trigger_id: Stable trigger ID. Conflicts with an existing child ID fail.
        wrap_non_focusable: Opt in to wrapping a non-focusable child in a button.
    """

    def __init__(
        self,
        content: str,
        *children: Any,
        position: str = "top",
        tooltip_id: str | None = None,
        trigger_id: str | None = None,
        wrap_non_focusable: bool = False,
        **props: Any,
    ) -> None:
        if position not in _POSITIONS:
            supported = ", ".join(_POSITIONS)
            raise ValueError(f"position must be one of: {supported}")
        super().__init__(*children, **props)
        self.content = content
        self.position = position
        self.tooltip_id = tooltip_id
        self.trigger_id = trigger_id
        self.wrap_non_focusable = wrap_non_focusable

    @staticmethod
    def _is_focusable(trigger: Element) -> bool:
        attrs = trigger.attrs
        if attrs.get("disabled") is True:
            return False
        tabindex = attrs.get("tabindex", attrs.get("tab_index"))
        if tabindex is not None:
            try:
                return int(tabindex) >= 0
            except (TypeError, ValueError):
                return False
        if trigger.tag == "a":
            return bool(attrs.get("href"))
        return trigger.tag in {"button", "input", "select", "textarea", "summary"}

    def _trigger_element(self) -> Element:
        if len(self.children) != 1:
            raise ValueError("Tooltip requires exactly one trigger child")

        trigger = self.children[0]
        if isinstance(trigger, Component):
            trigger = trigger.render()
        if not isinstance(trigger, Element):
            if not self.wrap_non_focusable:
                raise TypeError("Tooltip trigger must render exactly one Element")
            trigger = Element("button", trigger, type="button")

        if not self._is_focusable(trigger):
            if not self.wrap_non_focusable:
                raise ValueError(
                    "Tooltip trigger must be focusable; pass wrap_non_focusable=True "
                    "to opt in to a button wrapper"
                )
            trigger = Element("button", trigger, type="button")
        return trigger

    def _decorate_trigger(self, trigger: Element, tooltip_id: str) -> Element:
        attrs = dict(trigger.attrs)
        child_id = attrs.get("id", attrs.get("id_"))
        if self.trigger_id and child_id and str(child_id) != self.trigger_id:
            raise ValueError(
                "trigger_id conflicts with the trigger element's existing id"
            )
        if self.trigger_id:
            attrs.pop("id_", None)
            attrs["id"] = self.trigger_id

        descriptions: list[str] = []
        for key in ("aria-describedby", "aria_describedby"):
            value = attrs.pop(key, None)
            if value:
                descriptions.extend(str(value).split())
        if tooltip_id not in descriptions:
            descriptions.append(tooltip_id)
        attrs["aria-describedby"] = " ".join(descriptions)

        conflicts = sorted(set(attrs).intersection(_TRIGGER_EVENTS))
        if conflicts:
            raise ValueError(
                "Tooltip cannot overwrite trigger handlers: " + ", ".join(conflicts)
            )
        attrs.update(_TRIGGER_EVENTS)

        clone = copy(trigger)
        clone.attrs = attrs
        clone.children = list(trigger.children)
        return clone

    def render(self) -> Any:
        trigger = self._trigger_element()
        stable_trigger_id = (
            self.trigger_id or trigger.attrs.get("id") or trigger.attrs.get("id_")
        )
        tooltip_id = self.tooltip_id or (
            f"{stable_trigger_id}-tooltip" if stable_trigger_id else None
        )
        if not tooltip_id:
            raise ValueError(
                "Tooltip requires tooltip_id or a trigger with a stable id"
            )

        wrapper_class = "group relative inline-flex justify-center"
        if extra_class := self.props.get("class_"):
            wrapper_class = f"{wrapper_class} {extra_class}"

        return el(
            "span",
            self._decorate_trigger(trigger, str(tooltip_id)),
            el(
                "span",
                self.content,
                id=tooltip_id,
                role="tooltip",
                x_cloak="true",
                class_=(
                    f"pointer-events-none absolute z-50 whitespace-nowrap rounded "
                    f"bg-popover p-2 text-xs text-popover-foreground shadow "
                    f"opacity-0 transition-opacity duration-150 "
                    f"group-hover:opacity-100 group-focus-within:opacity-100 "
                    f"motion-reduce:transition-none {_POSITIONS[self.position]}"
                ),
                **alpine.show(alpine.expr("open")),
            ),
            class_=wrapper_class,
            **alpine.data(alpine.expr("{ open: false }")),
        )
