"""Virtual Scroll component for Oridecon Admin."""

from __future__ import annotations

from copy import copy
import re
from typing import Any

from oridecon.ui.atoms.icons import get_icon
from oridecon.ui.core.base import Component, Element, el
from oridecon.ui.core.render_context import get_render_scope
from oridecon.ui.core.url import is_safe_navigation_url

_DOM_ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")


class VirtualScroll(Component):
    """Own a stable, caller-named infinite-scroll result region.

    ``target_id`` is required because a fixed fallback ID collides as soon as
    two result sets are composed on one page. The ID must also be safe to use
    directly as an HTMX/CSS selector.
    """

    def __init__(
        self,
        url: str,
        total_items: int | None = None,
        chunk_size: int = 50,
        target_id: str | None = None,
        placeholder: Any | None = None,
        **props: Any,
    ) -> None:
        if not is_safe_navigation_url(url):
            raise ValueError("VirtualScroll requires a safe HTTP(S) or relative url")
        if not target_id:
            raise ValueError("VirtualScroll requires a stable target_id")
        if not _DOM_ID_RE.fullmatch(target_id):
            raise ValueError(
                "target_id must start with a letter and contain only letters, "
                "numbers, underscores, or hyphens"
            )
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than zero")
        if total_items is not None and total_items < 0:
            raise ValueError("total_items cannot be negative")

        supplied_id = props.pop("id", None)
        supplied_id_alias = props.pop("id_", None)
        supplied_ids = {
            str(value)
            for value in (supplied_id, supplied_id_alias)
            if value is not None
        }
        if any(value != target_id for value in supplied_ids):
            raise ValueError("target_id conflicts with the supplied id attribute")
        super().__init__(**props)
        self.url = url
        self.total_items = total_items
        self.chunk_size = chunk_size
        self.target_id = target_id
        self.placeholder = placeholder

    def render(self) -> Any:
        # Reserve the caller-facing ID in the response-local scope so sibling
        # virtual regions cannot silently emit the same target.
        get_render_scope().child("virtual-scroll").id("root", key=self.target_id)
        custom_class = self.props.get("class_", self.props.get("class"))
        attrs = {
            key: value
            for key, value in self.props.items()
            if key not in {"class", "class_"}
        }
        content = self.children or (
            [self.placeholder] if self.placeholder is not None else []
        )
        return el(
            "div",
            *content,
            id=self.target_id,
            class_=" ".join(filter(None, ("virtual-scroll", custom_class))),
            **attrs,
        )


def render_infinite_row(
    row_content: Any,
    next_url: str | None = None,
    trigger: str = "intersect once",
    threshold: str = "0.5",
) -> Any:
    """Helper to render a row that triggers the next page load.

    Args:
        row_content: The content of the current row
        next_url: URL to fetch the next page. If None, no trigger is added.
        trigger: HTMX trigger (defaults to a one-shot intersection observer).
        threshold: Intersection observer threshold between zero and one.
    """
    if not next_url:
        return row_content
    if not is_safe_navigation_url(next_url):
        raise ValueError("next_url must be a safe HTTP(S) or relative URL")
    try:
        threshold_value = float(threshold)
    except (TypeError, ValueError) as exc:
        raise ValueError("threshold must be a number between zero and one") from exc
    if not 0 <= threshold_value <= 1:
        raise ValueError("threshold must be between zero and one")

    trigger_spec = trigger.strip()
    if trigger_spec.startswith("intersect"):
        trigger_spec = f"{trigger_spec} threshold:{threshold_value:g}"
    attrs = {
        "hx-get": next_url,
        "hx-trigger": trigger_spec,
        "hx-swap": "afterend",
    }

    if isinstance(row_content, Element):
        cloned_row = copy(row_content)
        cloned_row.attrs = {**row_content.attrs, **attrs}
        cloned_row.children = list(row_content.children)
        return cloned_row

    return el("div", row_content, **attrs)


class InfiniteScrollTrigger(Component):
    """Load the next page automatically, with an ordinary-link fallback."""

    def __init__(
        self,
        url: str,
        trigger: str = "revealed once",
        target: str | None = None,
        swap: str = "afterend",
        select: str | None = None,
        **props: Any,
    ) -> None:
        if not is_safe_navigation_url(url):
            raise ValueError(
                "InfiniteScrollTrigger requires a safe HTTP(S) or relative url"
            )
        controlled_props = {
            "href",
            "hx-get",
            "hx_get",
            "hx-trigger",
            "hx_trigger",
            "hx-target",
            "hx_target",
            "hx-swap",
            "hx_swap",
            "hx-select",
            "hx_select",
        }
        conflicts = sorted(controlled_props.intersection(props))
        if conflicts:
            raise ValueError(
                "Use InfiniteScrollTrigger parameters instead of overriding: "
                + ", ".join(conflicts)
            )
        super().__init__(**props)
        self.url = url
        self.trigger = trigger
        self.target = target
        self.swap = swap
        # Omitting hx-select lets the endpoint own its fragment shape. A
        # page-global #table-content fallback selected rows from the first
        # table when multiple feeds were composed.
        self.select = select

    def render(self) -> Any:
        children = self.children or [
            get_icon(
                "refresh-cw",
                class_name="htmx-indicator mr-2 h-4 w-4 animate-spin text-primary",
            ),
            el("span", "Load more", class_="text-muted-foreground text-sm"),
        ]
        custom_class = self.props.get("class_", self.props.get("class"))
        attrs = {
            key: value
            for key, value in self.props.items()
            if key not in {"class", "class_", "href"}
        }

        # The same anchor is progressively enhanced by HTMX. Without the
        # shipped client bundle it remains a keyboard-operable next-page link.
        return el(
            "a",
            *children,
            href=self.url,
            aria_label="Load more results",
            class_=" ".join(
                filter(
                    None,
                    (
                        "flex items-center justify-center p-4 w-full",
                        custom_class,
                    ),
                )
            ),
            **{
                "hx-get": self.url,
                "hx-trigger": self.trigger,
                "hx-target": self.target,
                "hx-swap": self.swap,
                "hx-select": self.select,
                **attrs,
            },
        )
