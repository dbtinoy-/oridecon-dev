"""Engine module for oridecon-admin.

Provides rendering and template engine functionality.
"""

from __future__ import annotations

from oridecon.admin.engine.renderer import AdminRenderer, AdminRendererConfig

__all__ = [
    "AdminRenderer",
    "AdminRendererConfig",
]
