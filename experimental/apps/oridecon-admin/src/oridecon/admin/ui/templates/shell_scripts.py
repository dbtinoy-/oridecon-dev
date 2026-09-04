"""Markup builders for the AdminShell chrome.

The shell behaviour that used to be shipped as inline ``<script>`` /
``<style>`` blocks (search overlay, navigation controller, delegated form
UX, loading-bar error handling) now lives in the generated static assets
``static/js/admin-shell.js`` and ``static/css/admin-shell.css`` (single
source of truth: ``dev/generators/admin_shell_assets.py``). Under the strict
CSP v2 candidate (``script-src 'self'`` / ``style-src 'self'``) inline blocks
would be reported as ``script-src-elem`` / ``style-src-elem`` violations, so
the shell markup below only emits structural HTML and ``data-*`` hooks.
"""

from __future__ import annotations

from typing import Any

from oridecon.ui import el


def loading_bar_script(flash_zone_id: str) -> Any:
    """Return the global HTMX loading-bar markup.

    The surrounding behaviour (loading indicator, error toasts, Alpine
    re-init after body swaps) is in ``static/js/admin-shell.js``; the
    ``flash_zone_id`` argument is accepted for backwards compatibility and is
    no longer interpolated into inline script.

    Args:
        flash_zone_id: DOM id of the flash container (kept for API
            compatibility with ``Zones.FLASH.id`` callers).
    """
    # Reference the injected zone id through a data attribute so the
    # generated bundle can still target the right container.
    return el(
        "div",
        el(
            "div",
            class_="h-full bg-primary-400 animate-pulse",
        ),
        el(
            "span",
            "",
            data_flash_zone=flash_zone_id,
            class_="hidden",
        ),
        id="htmx-loading-bar",
        class_="hidden fixed top-0 left-0 right-0 h-1 bg-primary-600 z-50 transition-opacity",
    )


def dark_mode_expr(dark_mode: str) -> str:
    """Build the Alpine expression resolving the initial dark-mode state."""
    if dark_mode == "dark":
        server_default_expr = "true"
    elif dark_mode == "light":
        server_default_expr = "false"
    else:
        server_default_expr = (
            "(window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches)"
        )
    return (
        "localStorage.getItem('darkMode') !== null ? "
        "localStorage.getItem('darkMode') === 'true' : "
        f"{server_default_expr}"
    )


__all__ = ["dark_mode_expr", "loading_bar_script"]
