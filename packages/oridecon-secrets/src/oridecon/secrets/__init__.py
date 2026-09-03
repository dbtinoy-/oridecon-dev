"""Secret vaults with rotation, tenant scoping, and audit.

Provides ``RotatableSecretStoreProtocol``, versioned rotation,
tenant isolation, audit logging, and a conformance test suite.
"""

from __future__ import annotations

import importlib
import pkgutil
from typing import TYPE_CHECKING, Any

from oridecon.secrets.constants import __version__ as __version__

__path__ = pkgutil.extend_path(__path__, __name__)

if TYPE_CHECKING:
    from oridecon.secrets.config import SecretsConfig
    from oridecon.secrets.events import (
        SecretAccessedEvent,
        SecretCreatedEvent,
        SecretDeletedEvent,
        SecretRotatedEvent,
    )
    from oridecon.secrets.exceptions import (
        SecretAccessError,
        SecretBackendError,
        SecretConfigError,
        SecretNotFoundError,
        SecretRotationError,
        SecretsError,
    )
    from oridecon.secrets.hooks import (
        SecretAccessedHook,
        SecretCreatedHook,
        SecretDeletedHook,
        SecretRotatedHook,
    )
    from oridecon.secrets.module import SecretsModule
    from oridecon.secrets.protocols import (
        AsyncSecretStoreProtocol,
        RotatableSecretStoreProtocol,
    )
    from oridecon.secrets.types import SecretVersion, VersionedSecret

_LAZY_IMPORTS: dict[str, str] = {
    "AsyncSecretStoreProtocol": "oridecon.secrets.protocols",
    "RotatableSecretStoreProtocol": "oridecon.secrets.protocols",
    "RotationDecorator": "oridecon.secrets.rotation",
    "RotationSchedule": "oridecon.secrets.rotation",
    "SecretAccessError": "oridecon.secrets.exceptions",
    "SecretAccessedEvent": "oridecon.secrets.events",
    "SecretAccessedHook": "oridecon.secrets.hooks",
    "SecretAuditDecorator": "oridecon.secrets.audit",
    "SecretBackendError": "oridecon.secrets.exceptions",
    "SecretConfigError": "oridecon.secrets.exceptions",
    "SecretCreatedEvent": "oridecon.secrets.events",
    "SecretCreatedHook": "oridecon.secrets.hooks",
    "SecretDeletedEvent": "oridecon.secrets.events",
    "SecretDeletedHook": "oridecon.secrets.hooks",
    "SecretNotFoundError": "oridecon.secrets.exceptions",
    "SecretRotatedEvent": "oridecon.secrets.events",
    "SecretRotatedHook": "oridecon.secrets.hooks",
    "SecretRotationError": "oridecon.secrets.exceptions",
    "SecretVersion": "oridecon.secrets.types",
    "SecretsConfig": "oridecon.secrets.config",
    "SecretsError": "oridecon.secrets.exceptions",
    "SecretsModule": "oridecon.secrets.module",
    "TenantScopedSecretStore": "oridecon.secrets.tenancy",
    "VersionedSecret": "oridecon.secrets.types",
}


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        module_path = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__} has no attribute {name}")


def __dir__() -> list[str]:
    return [*list(_LAZY_IMPORTS.keys()), "__version__"]


__all__ = [
    "AsyncSecretStoreProtocol",
    "RotatableSecretStoreProtocol",
    "RotationDecorator",
    "RotationSchedule",
    "SecretAccessError",
    "SecretAccessedEvent",
    "SecretAccessedHook",
    "SecretAuditDecorator",
    "SecretBackendError",
    "SecretConfigError",
    "SecretCreatedEvent",
    "SecretCreatedHook",
    "SecretDeletedEvent",
    "SecretDeletedHook",
    "SecretNotFoundError",
    "SecretRotatedEvent",
    "SecretRotatedHook",
    "SecretRotationError",
    "SecretVersion",
    "SecretsConfig",
    "SecretsError",
    "SecretsModule",
    "TenantScopedSecretStore",
    "VersionedSecret",
    "__version__",
]
