"""Entry-point plugin discovery and boot-time enable/disable state."""

from __future__ import annotations

from oridecon.plugins.discovery import discover_plugins, discover_providers
from oridecon.plugins.engine import PluginEngineProvider
from oridecon.plugins.module import PluginsModule
from oridecon.plugins.state import load_disabled, save_disabled, update_disabled

__all__ = [
    "PluginEngineProvider",
    "PluginsModule",
    "discover_plugins",
    "discover_providers",
    "load_disabled",
    "save_disabled",
    "update_disabled",
]
