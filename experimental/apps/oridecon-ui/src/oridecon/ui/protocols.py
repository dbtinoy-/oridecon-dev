"""UI rendering protocols for oridecon-ui components."""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class RenderableProtocol(Protocol):
    """Any object that can render to an HTML string.

    Implemented by Component, Element, and any custom renderable
    in oridecon-ui. Export this protocol from the UIModule so that
    other packages can accept UI objects without importing from
    oridecon-ui implementation modules.
    """

    def __str__(self) -> str:
        """Return the rendered HTML string."""
        ...


__all__ = ["RenderableProtocol"]
