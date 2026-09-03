"""General-purpose layout base classes and components for oridecon-ui.

Layout hierarchy:
- HTMLDocument (abstract base)
  - LayoutBase (with composition: CSSManager, JSManager, HTMX, Theme methods)
"""

from __future__ import annotations

from oridecon.ui.layouts.base_layout import (
    BaseLayoutConfig,
    BaseLayoutContext,
    LayoutBase,
)
from oridecon.ui.layouts.footer import (
    FooterConfig,
    FooterLink,
    FooterRenderer,
)
from oridecon.ui.layouts.head import HeadConfig, HeadRenderer
from oridecon.ui.layouts.html_document import (
    HTMLDocument,
    HTMLDocumentConfig,
)
from oridecon.ui.layouts.mixins import (
    CSSManager,
    JSManager,
)
from oridecon.ui.layouts.server_toasts import (
    ServerToastChannel,
    ToastConfig,
    ToastData,
    ToastType,
    flash_to_toast,
)

__all__ = [
    "BaseLayoutConfig",
    "BaseLayoutContext",
    "CSSManager",
    "FooterConfig",
    "FooterLink",
    "FooterRenderer",
    "HTMLDocument",
    "HTMLDocumentConfig",
    "HeadConfig",
    "HeadRenderer",
    "JSManager",
    "LayoutBase",
    "ServerToastChannel",
    "ToastConfig",
    "ToastData",
    "ToastType",
    "flash_to_toast",
]
