"""Toast notification components for admin layout.

Renders toast notifications with HTMX support.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any

from markupsafe import escape

from oridecon.ui.config import ToastConfig


class ToastType(StrEnum):
    """Toast notification types."""

    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class ToastData:
    """A toast notification message."""

    message: str
    type: str | ToastType = ToastType.INFO
    title: str | None = None
    icon: str | None = None
    dismissible: bool = True
    auto_dismiss: bool = True
    duration_ms: int = 5000
    id: str | None = None
    actions: list[dict[str, str]] = field(default_factory=list)

    def __post_init__(self) -> None:
        if isinstance(self.type, str):
            self.type = ToastType(self.type)


# Default icons for toast types
DEFAULT_ICONS = {
    ToastType.SUCCESS: "check-circle",
    ToastType.ERROR: "x-circle",
    ToastType.WARNING: "alert-triangle",
    ToastType.INFO: "info",
}

# Default colors for toast types
DEFAULT_COLORS = {
    ToastType.SUCCESS: "green",
    ToastType.ERROR: "red",
    ToastType.WARNING: "yellow",
    ToastType.INFO: "blue",
}


class ServerToastChannel:
    """Renders toast notification container and messages (server-driven via HTMX)."""

    def __init__(self, config: ToastConfig | None = None):
        """Initialize the renderer.

        Args:
            config: Toast configuration
        """
        self.config = config or ToastConfig()

    def render(self, toasts: list[ToastData]) -> str:
        """Render toast payloads as HTML.

        Args:
            toasts: List of toast data objects

        Returns:
            HTML string for the toast container with toasts
        """
        return self.render_container(toasts)

    def render_container(self, toasts: list[ToastData] | None = None) -> str:
        """Render the toast container with optional initial toasts.

        Args:
            toasts: List of toast messages to show initially

        Returns:
            HTML string for toast container
        """
        parts: list[str] = []

        position_classes = self._get_position_classes()

        parts.append(f"""
        <div id="toast-container"
             class="toast-container {position_classes}"
             aria-live="polite"
             aria-label="Notifications">
        """)

        # Render initial toasts
        if toasts:
            for toast in toasts[: self.config.max_toasts]:
                parts.append(self.render_toast(toast))

        parts.append("</div>")

        # Add toast handling script
        if self.config.listen_for_events:
            parts.append(self._render_toast_script())

        return "\n".join(parts)

    def render_toast(self, toast: ToastData) -> str:
        """Render a single toast notification.

        Args:
            toast: Toast to render

        Returns:
            HTML string for toast
        """
        toast_type: ToastType = toast.type  # type: ignore[assignment]
        icon = toast.icon or DEFAULT_ICONS.get(toast_type, "info")
        color = DEFAULT_COLORS.get(toast_type, "blue")
        toast_id = toast.id or f"toast-{id(toast)}"

        auto_dismiss_attrs = ""
        if toast.auto_dismiss:
            auto_dismiss_attrs = (
                f'data-auto-dismiss="true" data-duration="{toast.duration_ms}"'
            )

        parts: list[str] = []

        parts.append(f"""
        <div id="{escape(toast_id)}"
             class="toast toast-{escape(toast_type.value)} toast-{escape(color)} show"
             role="alert"
             {auto_dismiss_attrs}>
        """)

        # Icon
        parts.append(f"""
            <div class="toast-icon">
                <i data-lucide="{escape(icon)}" class="w-5 h-5"></i>
            </div>
        """)

        # Content
        parts.append('<div class="toast-content">')

        if toast.title:
            parts.append(f'<div class="toast-title">{escape(toast.title)}</div>')

        parts.append(f'<div class="toast-message">{escape(toast.message)}</div>')

        # Actions (CSP-clean: no inline onclick). An entry carries either an
        # ``href`` (rendered as a link) or an ``action`` descriptor handled by
        # the delegated listener in the external shell bundle
        # (static/js/admin-shell.js / admin.js): "reload" or "dismiss".
        if toast.actions:
            parts.append('<div class="toast-actions">')
            for action in toast.actions:
                href = action.get("href")
                label = escape(action.get("label", "Action"))
                if href:
                    parts.append(
                        f'<a class="toast-action" href="{escape(href)}">'
                        f"{label}</a>"
                    )
                else:
                    descriptor = action.get("action", "reload")
                    parts.append(
                        f'<button type="button" class="toast-action" '
                        f'data-action="{escape(descriptor)}">{label}</button>'
                    )
            parts.append("</div>")

        parts.append("</div>")  # toast-content

        # Dismiss button
        if toast.dismissible:
            parts.append(f"""
            <button type="button"
                    class="toast-dismiss"
                    data-action="dismiss-toast"
                    data-dismiss-toast="{escape(toast_id)}"
                    aria-label="Dismiss notification">
                <i data-lucide="x" class="w-4 h-4"></i>
            </button>
            """)

        parts.append("</div>")  # toast

        return "\n".join(parts)

    def _get_position_classes(self) -> str:
        """Get CSS classes for toast position."""
        position_map = {
            "top-right": "toast-top toast-right",
            "top-left": "toast-top toast-left",
            "top-center": "toast-top toast-center",
            "bottom-right": "toast-bottom toast-right",
            "bottom-left": "toast-bottom toast-left",
            "bottom-center": "toast-bottom toast-center",
        }
        return position_map.get(self.config.position, "toast-top toast-right")

    def _render_toast_script(self) -> str:
        """Return the (now external) toast runtime.

        The toast behaviour (``showToast``/``dismissToast``, HTMX
        ``X-Toast`` header handling, auto-dismiss of initial toasts) moved to
        the generated ``static/js/admin-shell.js`` bundle (admin shell pages)
        and ``static/js/admin.js`` (legacy layouts) — both external assets, so
        no inline ``<script>`` block is emitted (CSP ``script-src 'self'``).

        Returns:
            Empty string; the channel markup is script-free.
        """
        return ""


def flash_to_toast(
    flash_messages: Sequence[dict[str, Any] | tuple[str, str]] | None,
) -> list[ToastData]:
    """Convert flash messages to toasts.

    Accepts structured dict entries (``message``, ``category``, plus the
    optional ``title``, ``icon``, ``duration_ms``, ``auto_dismiss``,
    ``dismissible`` and ``actions`` keys for full-fidelity toasts) and the
    legacy ``(category, message)`` tuple form.

    Args:
        flash_messages: List of flash message dicts or (category, message)
            tuples.

    Returns:
        List of ToastData objects
    """
    if not flash_messages:
        return []

    toasts: list[ToastData] = []

    category_map = {
        "success": ToastType.SUCCESS,
        "error": ToastType.ERROR,
        "danger": ToastType.ERROR,
        "warning": ToastType.WARNING,
        "info": ToastType.INFO,
        "message": ToastType.INFO,
    }

    def _make_toast(entry: Any) -> ToastData:
        if isinstance(entry, dict):
            toast = ToastData(
                message=str(entry.get("message", "")),
                type=category_map.get(
                    str(entry.get("category", "info")).lower(), ToastType.INFO
                ),
            )
            if entry.get("title"):
                toast.title = str(entry["title"])
            if entry.get("icon"):
                toast.icon = str(entry["icon"])
            duration = entry.get("duration_ms")
            if duration is not None:
                toast.duration_ms = max(int(duration), 0)
                toast.auto_dismiss = toast.duration_ms > 0
            if "auto_dismiss" in entry:
                toast.auto_dismiss = bool(entry["auto_dismiss"])
            if "dismissible" in entry:
                toast.dismissible = bool(entry["dismissible"])
            if entry.get("actions"):
                toast.actions = list(entry["actions"])
            return toast
        category, message = entry
        return ToastData(
            message=message,
            type=category_map.get(str(category).lower(), ToastType.INFO),
        )

    for entry in flash_messages:
        toasts.append(_make_toast(entry))

    return toasts


__all__ = [
    "ToastConfig",
    "ToastData",
    "ServerToastChannel",
    "ToastType",
    "flash_to_toast",
]
