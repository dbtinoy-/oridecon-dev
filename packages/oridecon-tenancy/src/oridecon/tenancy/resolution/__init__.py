"""Resolution subpackage — public re-exports."""

from __future__ import annotations

from oridecon.tenancy.resolution.chain import CompositeResolver
from oridecon.tenancy.resolution.header import HeaderTenantResolver
from oridecon.tenancy.resolution.jwt_claim import JWTClaimTenantResolver
from oridecon.tenancy.resolution.path import PathTenantResolver
from oridecon.tenancy.resolution.registry import ResolverRegistry
from oridecon.tenancy.resolution.subdomain import SubdomainTenantResolver

__all__ = [
    "CompositeResolver",
    "HeaderTenantResolver",
    "JWTClaimTenantResolver",
    "PathTenantResolver",
    "ResolverRegistry",
    "SubdomainTenantResolver",
]
