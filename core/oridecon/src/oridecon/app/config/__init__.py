"""Configuration public exports for the app subsystem."""

from __future__ import annotations

from oridecon.app.config.discovery import ModuleDiscoveryConfig
from oridecon.app.config.models import AppConfig

__all__ = [
    "AppConfig",
    "ModuleDiscoveryConfig",
]
