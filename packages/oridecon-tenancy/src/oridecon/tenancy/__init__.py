"""oridecon-tenancy — Multi-tenant resolution, lifecycle, and isolation.

Public surface (lazy-loaded on first access)::

    from oridecon.tenancy import (
        TenancyModule,
        TenancyConfig,
        TenancyProvider,
        TenantLifecycleService,
        TenantConfigService,
        TenantValidator,
        CompositeResolver,
        InMemoryTenantProvider,
    )
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from oridecon.tenancy.config import (
        ConfigOverridesConfig,
        IntegrationConfig,
        LifecycleConfig,
        ResolutionConfig,
        TenancyConfig,
    )
    from oridecon.tenancy.config_overrides.cache import CachedTenantConfigProvider
    from oridecon.tenancy.config_overrides.service import TenantConfigService
    from oridecon.tenancy.di.provider import TenancyProvider
    from oridecon.tenancy.enforcement.guard import TenantGuard
    from oridecon.tenancy.enforcement.middleware import TenantContextMiddleware
    from oridecon.tenancy.enforcement.validator import TenantValidator
    from oridecon.tenancy.isolation.database import DatabaseIsolationStrategy
    from oridecon.tenancy.isolation.registry import IsolationStrategyRegistry
    from oridecon.tenancy.isolation.row_level import RowLevelIsolationStrategy
    from oridecon.tenancy.lifecycle.provisioner import TenantProvisioner
    from oridecon.tenancy.lifecycle.service import TenantLifecycleService
    from oridecon.tenancy.migration.service import (
        MigrationResult,
        MigrationServiceConfig,
    )
    from oridecon.tenancy.migration.write_pause import WritePauseRegistry
    from oridecon.tenancy.module import TenancyModule
    from oridecon.tenancy.resolution.chain import CompositeResolver
    from oridecon.tenancy.resolution.registry import ResolverRegistry
    from oridecon.tenancy.stores.memory import InMemoryTenantProvider

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "TenancyConfig": ("oridecon.tenancy.config", "TenancyConfig"),
    "ResolutionConfig": ("oridecon.tenancy.config", "ResolutionConfig"),
    "LifecycleConfig": ("oridecon.tenancy.config", "LifecycleConfig"),
    "ConfigOverridesConfig": ("oridecon.tenancy.config", "ConfigOverridesConfig"),
    "IntegrationConfig": ("oridecon.tenancy.config", "IntegrationConfig"),
    "TenancyProvider": ("oridecon.tenancy.di.provider", "TenancyProvider"),
    "TenantConfigService": (
        "oridecon.tenancy.config_overrides.service",
        "TenantConfigService",
    ),
    "CachedTenantConfigProvider": (
        "oridecon.tenancy.config_overrides.cache",
        "CachedTenantConfigProvider",
    ),
    "TenantGuard": ("oridecon.tenancy.enforcement.guard", "TenantGuard"),
    "TenantContextMiddleware": (
        "oridecon.tenancy.enforcement.middleware",
        "TenantContextMiddleware",
    ),
    "TenantValidator": ("oridecon.tenancy.enforcement.validator", "TenantValidator"),
    "DatabaseIsolationStrategy": (
        "oridecon.tenancy.isolation.database",
        "DatabaseIsolationStrategy",
    ),
    "IsolationStrategyRegistry": (
        "oridecon.tenancy.isolation.registry",
        "IsolationStrategyRegistry",
    ),
    "RowLevelIsolationStrategy": (
        "oridecon.tenancy.isolation.row_level",
        "RowLevelIsolationStrategy",
    ),
    "SchemaIsolationStrategy": (
        "oridecon.tenancy.isolation.schema",
        "SchemaIsolationStrategy",
    ),
    "TenantProvisioner": (
        "oridecon.tenancy.lifecycle.provisioner",
        "TenantProvisioner",
    ),
    "TenantLifecycleService": (
        "oridecon.tenancy.lifecycle.service",
        "TenantLifecycleService",
    ),
    "MigrationResult": ("oridecon.tenancy.migration.service", "MigrationResult"),
    "MigrationServiceConfig": (
        "oridecon.tenancy.migration.service",
        "MigrationServiceConfig",
    ),
    "TenancyModule": ("oridecon.tenancy.module", "TenancyModule"),
    "TenantMigrationService": (
        "oridecon.tenancy.migration.service",
        "TenantMigrationService",
    ),
    "WritePauseRegistry": (
        "oridecon.tenancy.migration.write_pause",
        "WritePauseRegistry",
    ),
    "CompositeResolver": ("oridecon.tenancy.resolution.chain", "CompositeResolver"),
    "ResolverRegistry": ("oridecon.tenancy.resolution.registry", "ResolverRegistry"),
    "InMemoryTenantProvider": (
        "oridecon.tenancy.stores.memory",
        "InMemoryTenantProvider",
    ),
}


def __getattr__(name: str) -> Any:
    """Lazy-load public symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = list(_LAZY_IMPORTS.keys())
