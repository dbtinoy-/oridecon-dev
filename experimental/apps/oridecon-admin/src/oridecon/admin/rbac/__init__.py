"""Unified RBAC system for Lexigram Admin."""

from __future__ import annotations

from oridecon.admin.rbac.effective import (
    EffectivePermissions,
    resolve_effective_permissions,
)
from oridecon.admin.rbac.policies import (
    PolicyRegistry,
    get_policy,
    register_policy,
)
from oridecon.admin.rbac.protocols import AdminRoleStoreProtocol
from oridecon.admin.rbac.registry import (
    ResourcePermissionRegistry,
    get_resource_permissions,
    register_resource_permissions,
)
from oridecon.admin.rbac.schema import (
    ActionPermission,
    FieldPermission,
    ResourcePermissions,
)
from oridecon.admin.rbac.types import Policy, PolicyContext
from oridecon.contracts.auth import RoleDefinition

__all__ = [
    "ActionPermission",
    "AdminRoleStoreProtocol",
    "EffectivePermissions",
    "FieldPermission",
    "Policy",
    "PolicyContext",
    "PolicyRegistry",
    "ResourcePermissionRegistry",
    "ResourcePermissions",
    "RoleDefinition",
    "get_policy",
    "get_resource_permissions",
    "register_policy",
    "register_resource_permissions",
    "resolve_effective_permissions",
]
