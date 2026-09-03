"""Admin management pages for oridecon-auth."""

from __future__ import annotations

from oridecon.auth.admin.pages.overview import AuthOverviewPage
from oridecon.auth.admin.pages.sessions import AuthSessionsPage
from oridecon.auth.admin.pages.tokens import AuthTokensPage
from oridecon.auth.admin.pages.users import AuthUsersPage

__all__ = [
    "AuthOverviewPage",
    "AuthSessionsPage",
    "AuthTokensPage",
    "AuthUsersPage",
]
