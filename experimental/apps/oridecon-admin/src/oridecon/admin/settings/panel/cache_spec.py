"""Cache configuration specification."""

from __future__ import annotations

from oridecon.admin.settings.panel.models import CacheSettings
from oridecon.admin.settings.panel.nodes import PydanticConfigSpec
from oridecon.admin.settings.panel.registry import ConfigRegistry

__all__ = ["CacheSpec", "register_spec"]


class CacheSpec(PydanticConfigSpec):
    """Cache configuration spec."""

    namespace = "admin.cache"
    label = "Response Caching"
    icon = "cube-transparent"
    description = "Toggle response caching and set the default TTL."
    model = CacheSettings
    required_permissions = frozenset({"admin.settings.edit"})


def register_spec(registry: ConfigRegistry) -> None:
    """Register this spec with the config registry."""
    registry.register_spec(CacheSpec)
