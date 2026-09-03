"""
Admin user store package.

This package provides the protocol and concrete implementations for the
admin-panel user store (the ``admin_users`` table — distinct from the
application user store managed by oridecon-auth):

- :class:`AdminUserStoreProtocol` — formal contract (use this for type hints)
- :class:`DirectSQLAdminUserStore` — production SQL backend
- :class:`MemoryAdminUserStore` — in-memory store for testing
- :class:`DatabaseAdminUserStore` — RepositoryProtocol-based backend
- :class:`AuthProviderAdminUserStore` — adapter for external auth providers
"""

from __future__ import annotations

from oridecon.admin.auth.store.auth_provider import AuthProviderAdminUserStore
from oridecon.admin.auth.store.base import AbstractAdminUserStore
from oridecon.admin.auth.store.database import DatabaseAdminUserStore
from oridecon.admin.auth.store.direct_sql import DirectSQLAdminUserStore
from oridecon.admin.auth.store.memory import MemoryAdminUserStore
from oridecon.admin.auth.store.protocols import AdminUserStoreProtocol
from oridecon.admin.auth.store.session_sql import AdminSessionSqlRepository

__all__ = [
    "AbstractAdminUserStore",
    "AdminSessionSqlRepository",
    "AdminUserStoreProtocol",
    "AuthProviderAdminUserStore",
    "DatabaseAdminUserStore",
    "DirectSQLAdminUserStore",
    "MemoryAdminUserStore",
]
