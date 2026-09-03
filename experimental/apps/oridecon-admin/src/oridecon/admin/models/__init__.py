"""Models module for oridecon-admin.

Re-exports AdminUser and related models.
"""

from __future__ import annotations

from oridecon.admin.auth.integration import AdminUser

__all__ = ["AdminUser"]
