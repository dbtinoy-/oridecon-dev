"""Integration helpers for oridecon-sql.

Use :class:`~oridecon.sql.config.DatabaseConfig` directly — it auto-loads
from ``ORI_DB__*`` environment variables via Pydantic's ``model_config``.
"""

from __future__ import annotations

from oridecon.sql.di.provider import DatabaseProvider
from oridecon.sql.module import DatabaseModule

__all__ = ["DatabaseModule", "DatabaseProvider"]
