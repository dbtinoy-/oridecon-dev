"""Internal value objects for oridecon-tenancy."""

from __future__ import annotations

# Re-export contract types so application code can import from one place.
from oridecon.contracts.tenancy.types import (
    TenantInfo,
    TenantResolutionContext,
    TenantStatus,
)

__all__ = [
    "TenantInfo",
    "TenantResolutionContext",
    "TenantStatus",
]
