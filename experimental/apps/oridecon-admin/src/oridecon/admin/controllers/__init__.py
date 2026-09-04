"""Controllers module for Lexigram Admin."""

from __future__ import annotations

from oridecon.admin.controllers.auth import AuthController
from oridecon.admin.controllers.base import AdminController
from oridecon.admin.controllers.dashboard import DashboardController
from oridecon.admin.controllers.profile import ProfileController
from oridecon.admin.controllers.search import SearchController
from oridecon.admin.controllers.settings import SettingsController
from oridecon.admin.controllers.setup import SetupController
from oridecon.admin.controllers.widgets import WidgetController

__all__ = [
    "AdminController",
    "AuthController",
    "DashboardController",
    "ProfileController",
    "SearchController",
    "SettingsController",
    "SetupController",
    "WidgetController",
]
