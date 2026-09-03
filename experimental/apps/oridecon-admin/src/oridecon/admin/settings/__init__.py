"""Admin settings package."""

from __future__ import annotations

from oridecon.admin.settings.loader import AdminConfigLoader
from oridecon.admin.settings.settings import AdminSettings, get_admin_settings

__all__ = ["AdminConfigLoader", "AdminSettings", "get_admin_settings"]
