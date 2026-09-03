"""Core module for oridecon-admin.

Provides foundational utilities: caching, resilience, middleware,
decorators, and distributed locking.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

# PEP 562 lazy loading
_LAZY_IMPORTS = {
    # Cache
    "AdminCacheService": "oridecon.admin.core.cache",
    "CachedPermissionService": "oridecon.admin.core.cache",
    # Decorators
    "singleton": "oridecon.admin.core.decorators",
    "scoped": "oridecon.admin.core.decorators",
    "transient": "oridecon.admin.core.decorators",
    # Distributed Lock
    "LockError": "oridecon.admin.core.distributed_lock",
    "LockAcquisitionError": "oridecon.admin.core.distributed_lock",
    "LockTimeoutError": "oridecon.admin.core.distributed_lock",
    "LockConfig": "oridecon.admin.core.distributed_lock",
    "AdminLockManager": "oridecon.admin.core.distributed_lock",
    "ResourceLock": "oridecon.admin.core.distributed_lock",
    "BulkOperationLock": "oridecon.admin.core.distributed_lock",
    "distributed_lock": "oridecon.admin.core.distributed_lock",
    # Middleware
    "AdminErrorHandler": "oridecon.admin.core.middleware",
    "AdminEntity": "oridecon.admin.core.middleware",
    "SoftDeleteEntity": "oridecon.admin.core.middleware",
    "AuditedEntity": "oridecon.admin.core.middleware",
    "AdminRenderer": "oridecon.admin.core.rendering",
    "AdminRouter": "oridecon.admin.core.routing",
    "CircuitBreakerConfig": "oridecon.contracts.infra.resilience.models",
    "RetryConfig": "oridecon.contracts.infra.resilience.models",
    "TimeoutConfig": "oridecon.contracts.infra.resilience.models",
    "transaction": "oridecon.admin.core.resilience_config",
    "AuditRepositoryMixin": "oridecon.admin.core.resilience_config",
}

if TYPE_CHECKING:
    from oridecon.admin.core.cache import (
        AdminCacheService,
        CachedPermissionService,
    )
    from oridecon.admin.core.decorators import scoped, singleton, transient
    from oridecon.admin.core.distributed_lock import (
        AdminLockManager,
        BulkOperationLock,
        LockAcquisitionError,
        LockConfig,
        LockError,
        LockTimeoutError,
        ResourceLock,
        distributed_lock,
    )
    from oridecon.admin.core.middleware import (
        AdminEntity,
        AdminErrorHandler,
        AuditedEntity,
        SoftDeleteEntity,
    )
    from oridecon.admin.core.registry import AdminRegistry
    from oridecon.admin.core.rendering import AdminRenderer
    from oridecon.admin.core.resilience_config import (
        AuditRepositoryMixin,
        transaction,
    )
    from oridecon.admin.core.routing import AdminRouter
    from oridecon.contracts.infra.resilience.models import (
        CircuitBreakerConfig,
        RetryConfig,
        TimeoutConfig,
    )


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib

        module = importlib.import_module(_LAZY_IMPORTS[name], __package__)
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return list(_LAZY_IMPORTS.keys())


__all__ = [
    "AdminCacheService",
    "AdminEntity",
    "AdminErrorHandler",
    "AdminLockManager",
    "AdminRegistry",
    "AdminRenderer",
    "AdminRouter",
    "AuditRepositoryMixin",
    "AuditedEntity",
    "BulkOperationLock",
    "CachedPermissionService",
    "CircuitBreakerConfig",
    "LockAcquisitionError",
    "LockConfig",
    "LockError",
    "LockTimeoutError",
    "ResourceLock",
    "RetryConfig",
    "SoftDeleteEntity",
    "TimeoutConfig",
    "distributed_lock",
    "scoped",
    "singleton",
    "transaction",
    "transient",
]
