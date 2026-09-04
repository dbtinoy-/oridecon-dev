"""Branding and theme configuration specification."""

from __future__ import annotations

from oridecon.admin.settings.panel.models import BrandingSettings
from oridecon.admin.settings.panel.nodes import (
    ColorNode,
    EnumNode,
    PydanticConfigSpec,
)
from oridecon.admin.settings.panel.registry import ConfigRegistry

__all__ = ["BrandingSpec", "register_spec"]

# Human-readable labels for the dark-mode selector.
_DARK_MODE_OPTIONS: dict[str, str] = {
    "system": "System (follow OS)",
    "light": "Light",
    "dark": "Dark",
}

_dark_mode_node = EnumNode(
    label="Dark Mode",
    default="system",
    help_text=(
        "Theme preference: follow the system, force light, or force dark. "
        "Takes effect on the next full page load."
    ),
    options=_DARK_MODE_OPTIONS,
)


class BrandingSpec(PydanticConfigSpec):
    """Branding and theme settings spec."""

    namespace = "admin.branding"
    label = "Branding & Theme"
    icon = "palette"
    description = "Site name, colors, logo, and theme preference."
    model = BrandingSettings
    node_overrides = {
        "primary_color": ColorNode,
        "dark_mode": _dark_mode_node,
    }
    required_permissions = frozenset({"admin.settings.edit"})
    scope = "tenant"


def register_spec(registry: ConfigRegistry) -> None:
    """Register this spec with the config registry."""
    registry.register_spec(BrandingSpec)
