"""Internationalization configuration specification."""

from __future__ import annotations

from oridecon.admin.settings.panel.models import I18nSettings
from oridecon.admin.settings.panel.nodes import PydanticConfigSpec
from oridecon.admin.settings.panel.registry import ConfigRegistry

__all__ = ["I18nSpec", "register_spec"]


class I18nSpec(PydanticConfigSpec):
    """Internationalization configuration spec."""

    namespace = "admin.i18n"
    label = "Internationalization"
    icon = "globe"
    description = "Default locale and timezone for admin pages."
    model = I18nSettings
    required_permissions = frozenset({"admin.settings.edit"})
    scope = "tenant"


def register_spec(registry: ConfigRegistry) -> None:
    """Register this spec with the config registry."""
    registry.register_spec(I18nSpec)
