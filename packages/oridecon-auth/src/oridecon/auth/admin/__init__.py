"""Admin dashboard widgets and contributor for oridecon-auth."""

from __future__ import annotations

from oridecon.auth.admin.contributor import AuthAdminContributor
from oridecon.auth.admin.handlers import (
    ActiveSessionsWidgetHandler,
    FailedLoginsWidgetHandler,
    TokenRefreshRateWidgetHandler,
)

__all__ = [
    "ActiveSessionsWidgetHandler",
    "AuthAdminContributor",
    "FailedLoginsWidgetHandler",
    "TokenRefreshRateWidgetHandler",
]
