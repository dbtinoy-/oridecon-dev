"""Tenancy contracts — protocols, types, commands, events, and errors."""

from __future__ import annotations

from oridecon.contracts.tenancy.commands import CreateTenantCommand, UpdateTenantCommand
from oridecon.contracts.tenancy.errors import (
    MigrationError,
    TenantConfigError,
    TenantError,
    TenantInactiveError,
    TenantNotFoundError,
    TenantProvisioningError,
    TenantResolutionError,
    TenantSlugConflictError,
    TenantSuspendedError,
)
from oridecon.contracts.tenancy.events import (
    TenantActivated,
    TenantConfigChanged,
    TenantDeactivated,
    TenantProvisioned,
    TenantSuspended,
    TenantTierMigrationCheckpoint,
    TenantTierMigrationFailed,
    TenantTierMigrationStarted,
    TenantTierMigrationSucceeded,
)
from oridecon.contracts.tenancy.migration import (
    ISOLATION_TIER_ORDER,
    TIER_ISOLATION_MAP,
    CopyResult,
    MigrationContext,
    MigrationCopyStrategy,
    SnapshotResult,
)
from oridecon.contracts.tenancy.protocols import (
    TenantConfigProviderProtocol,
    TenantIsolationStrategyProtocol,
    TenantProviderProtocol,
    TenantResolverProtocol,
)
from oridecon.contracts.tenancy.types import (
    TenantInfo,
    TenantResolutionContext,
    TenantStatus,
)

__all__ = [
    "ISOLATION_TIER_ORDER",
    "TIER_ISOLATION_MAP",
    "CopyResult",
    "CreateTenantCommand",
    "MigrationContext",
    "MigrationCopyStrategy",
    "MigrationError",
    "SnapshotResult",
    "TenantActivated",
    "TenantConfigChanged",
    "TenantConfigError",
    "TenantConfigProviderProtocol",
    "TenantDeactivated",
    "TenantError",
    "TenantInactiveError",
    "TenantInfo",
    "TenantIsolationStrategyProtocol",
    "TenantNotFoundError",
    "TenantProviderProtocol",
    "TenantProvisioned",
    "TenantProvisioningError",
    "TenantResolutionContext",
    "TenantResolutionError",
    "TenantResolverProtocol",
    "TenantSlugConflictError",
    "TenantStatus",
    "TenantSuspended",
    "TenantSuspendedError",
    "TenantTierMigrationCheckpoint",
    "TenantTierMigrationFailed",
    "TenantTierMigrationStarted",
    "TenantTierMigrationSucceeded",
    "UpdateTenantCommand",
]
