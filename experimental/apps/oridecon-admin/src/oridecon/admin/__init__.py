"""Oridecon Admin — Administrative panel for oridecon applications."""

from __future__ import annotations

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import importlib.metadata
from typing import TYPE_CHECKING, Any

from oridecon.admin.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.admin.contributors.base import BaseAdminContributor
    from oridecon.admin.contributors.core import CoreAdminContributor
    from oridecon.admin.contributors.registry import ContributorRegistry
    from oridecon.admin.di.bundle_provider import AdminProvider
    from oridecon.admin.exceptions import (
        AdminError,
        AdminValidationError,
        ConflictError,
        DataError,
        ErrorCode,
        NotFoundError,
        NotificationError,
        PermissionDeniedError,
    )
    from oridecon.admin.module import AdminModule
    from oridecon.admin.types import AdminStatus, AdminUser
    from oridecon.contracts.admin.protocols import (
        AdminContributorProtocol,
        AdminContributorRegistryProtocol,
        AdminDashboardProtocol,
    )

_LAZY_IMPORTS: dict[str, str] = {
    # Exceptions
    "AdminError": "oridecon.admin.exceptions",
    "AdminValidationError": "oridecon.admin.exceptions",
    "ConflictError": "oridecon.admin.exceptions",
    "DataError": "oridecon.admin.exceptions",
    "ErrorCode": "oridecon.admin.exceptions",
    "NotFoundError": "oridecon.admin.exceptions",
    "NotificationError": "oridecon.admin.exceptions",
    "PermissionDeniedError": "oridecon.admin.exceptions",
    # DI
    "AdminProvider": "oridecon.admin.di.bundle_provider",
    "AdminModule": "oridecon.admin.module",
    # Contributors
    "BaseAdminContributor": "oridecon.admin.contributors.base",
    "CoreAdminContributor": "oridecon.admin.contributors.core",
    "ContributorRegistry": "oridecon.admin.contributors.registry",
    # Protocols (canonical locations in oridecon-contracts)
    "AdminContributorProtocol": "oridecon.contracts.admin.protocols",
    "AdminContributorRegistryProtocol": "oridecon.contracts.admin.protocols",
    "AdminDashboardProtocol": "oridecon.contracts.admin.protocols",
    # Types
    "AdminStatus": "oridecon.admin.types",
    "AdminUser": "oridecon.admin.types",
    # Hooks
    "AdminPanelStartedHook": "oridecon.admin.hooks",
    "AdminPanelStoppedHook": "oridecon.admin.hooks",
    "AdminResourceAccessedHook": "oridecon.admin.hooks",
}


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib

        module = importlib.import_module(_LAZY_IMPORTS[name])
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = [
    "AdminContributorProtocol",
    "AdminContributorRegistryProtocol",
    "AdminDashboardProtocol",
    "AdminError",
    "AdminModule",
    "AdminPanelStartedHook",
    "AdminPanelStoppedHook",
    "AdminProvider",
    "AdminResourceAccessedHook",
    "AdminStatus",
    "AdminUser",
    "AdminValidationError",
    "BaseAdminContributor",
    "ConflictError",
    "ContributorRegistry",
    "CoreAdminContributor",
    "DataError",
    "ErrorCode",
    "NotFoundError",
    "NotificationError",
    "PermissionDeniedError",
]
