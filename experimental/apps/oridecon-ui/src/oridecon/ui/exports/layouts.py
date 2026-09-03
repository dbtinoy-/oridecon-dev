"""Static layout re-exports for the ``oridecon.ui`` public surface.

Type-checker only: the top-level package resolves names lazily via
``__getattr__`` at runtime, so these imports never execute eagerly.
"""

# File-level suppression: this module is an intentional lazy-re-export
# manifest — imports live under TYPE_CHECKING on purpose.
# ruff: noqa: TC004

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oridecon.ui.layouts import (
        BaseLayoutContext,
        CSSManager,
        HTMLDocument,
        JSManager,
        LayoutBase,
    )
    from oridecon.ui.layouts.footer import FooterLink, FooterRenderer
    from oridecon.ui.layouts.head import HeadRenderer

    __all__ = (
        "BaseLayoutContext",
        "CSSManager",
        "HTMLDocument",
        "JSManager",
        "LayoutBase",
        "FooterLink",
        "FooterRenderer",
        "HeadRenderer",
    )
