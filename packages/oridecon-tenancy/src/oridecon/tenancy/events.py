"""Tenancy domain events — re-exports from contracts."""

from __future__ import annotations

from oridecon.contracts.tenancy.events import (
    TenantActivated,
    TenantConfigChanged,
    TenantDeactivated,
    TenantProvisioned,
    TenantSuspended,
)

__all__ = [
    "TenantActivated",
    "TenantConfigChanged",
    "TenantDeactivated",
    "TenantProvisioned",
    "TenantSuspended",
]
