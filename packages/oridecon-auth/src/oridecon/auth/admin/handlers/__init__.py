"""Widget handlers for auth admin dashboard."""

from __future__ import annotations

from oridecon.auth.admin.handlers.active_sessions import ActiveSessionsWidgetHandler
from oridecon.auth.admin.handlers.failed_logins import FailedLoginsWidgetHandler
from oridecon.auth.admin.handlers.token_refresh_rate import (
    TokenRefreshRateWidgetHandler,
)

__all__ = [
    "ActiveSessionsWidgetHandler",
    "FailedLoginsWidgetHandler",
    "TokenRefreshRateWidgetHandler",
]
