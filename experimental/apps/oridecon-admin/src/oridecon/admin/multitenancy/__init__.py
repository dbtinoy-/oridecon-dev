"""Multi-tenancy support for oridecon-admin.

Delegates to ``oridecon-tenancy`` when installed; falls back to the
built-in in-memory implementation otherwise.
"""

from __future__ import annotations

from oridecon.admin.multitenancy.adapter import (
    TenantProviderRegistry,
    resolve_tenant_id,
)
from oridecon.admin.multitenancy.data_source import TenantScopedDataSource
from oridecon.admin.multitenancy.models import TenantConfig, TenantNotFoundError

__all__ = [
    "TenantConfig",
    "TenantNotFoundError",
    "TenantProviderRegistry",
    "TenantScopedDataSource",
    "resolve_tenant_id",
]
