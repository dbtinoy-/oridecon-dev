"""Error Boundary component for Oridecon Admin."""

from __future__ import annotations

from typing import Any

from oridecon.logging import get_logger
from oridecon.ui.core.base import Component, el, render_child_to_string
from oridecon.ui.core.trusted_html import trusted_html
from oridecon.ui.molecules.error_state import ErrorState

logger = get_logger(__name__)


class ErrorBoundary(Component):
    """Component that catches rendering errors in its children.

    This provides a fallback UI when a sub-component fails to render,
    preventing the entire page from breaking.
    """

    def __init__(self, fallback: Any | None = None, **props: Any) -> None:
        super().__init__(**props)
        self.fallback = fallback

    def render(self) -> Any:
        try:
            # Force child-context rendering to catch exceptions while preserving
            # the strings-are-data escaping policy.
            content = render_child_to_string(self.children)
            return el(
                "div",
                trusted_html(
                    content,
                    source="ErrorBoundary concrete child renderer",
                ),
                **self.props,
            )
        except Exception as e:  # error boundary must catch all rendering errors
            logger.exception("Error rendering component inside ErrorBoundary")
            if self.fallback:
                return el("div", self.fallback, role="alert")

            return el(
                "div",
                ErrorState(
                    title="Rendering Error",
                    message=f"A component failed to display: {e!s}",
                    action=el(
                        "button",
                        "Reload Page",
                        data_action="reload",
                        class_="px-4 py-2 bg-destructive text-destructive-foreground rounded hover:bg-destructive/90 transition-colors",
                    ),
                ),
                role="alert",
            )
