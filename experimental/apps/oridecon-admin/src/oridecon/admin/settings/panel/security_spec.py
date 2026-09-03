"""Security configuration specification."""

from __future__ import annotations

from oridecon.admin.settings.panel.models import SecuritySettings
from oridecon.admin.settings.panel.nodes import PydanticConfigSpec
from oridecon.admin.settings.panel.registry import ConfigRegistry

__all__ = ["SecuritySpec", "register_spec"]


class SecuritySpec(PydanticConfigSpec):
    """Security headers configuration spec."""

    namespace = "admin.security"
    label = "Security Headers"
    icon = "lock-closed"
    description = "Content-Security-Policy and HSTS settings."
    model = SecuritySettings
    required_permissions = frozenset({"admin.settings.edit"})


def register_spec(registry: ConfigRegistry) -> None:
    """Register this spec with the config registry."""
    registry.register_spec(SecuritySpec)
