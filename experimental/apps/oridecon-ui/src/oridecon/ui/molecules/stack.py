"""Structured vertical stack layout."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any, cast

from oridecon.ui.core.base import Element, el, render_to_string


class Stack:
    """Render children in a vertical flex-column container.

    Plain string children remain text and are escaped by ``Element``. Markup
    may cross the boundary only through a framework element or an explicit
    trusted HTML capability.
    """

    def __init__(
        self,
        children: list[Any] | None = None,
        gap: int = 4,
        class_: str = "",
    ) -> None:
        self.children = list(children or [])
        self.gap = gap
        self.class_ = class_

    def render(self) -> Element:
        """Build the structured stack element without pre-rendering children."""
        classes = f"flex flex-col gap-{self.gap}"
        if self.class_:
            classes = f"{classes} {self.class_}"
        return cast("Element", el("div", *self.children, class_=classes))

    def __iter__(self) -> Iterator[Element]:
        """Retain compatibility with callers that consume Stack as a fragment."""
        yield self.render()

    def __html__(self) -> str:
        """Render through the framework element boundary."""
        return render_to_string(self.render())

    def __str__(self) -> str:
        return self.__html__()


__all__ = ["Stack"]
