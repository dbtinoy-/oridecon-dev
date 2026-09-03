"""HTTP security public API for Oridecon Web."""

from __future__ import annotations

from oridecon.web.middleware.security import SecurityHeadersMiddleware
from oridecon.web.security.config import (
    CORSConfig,
    CrossOriginConfig,
    CSPConfig,
    CSRFConfig,
    HSTSConfig,
    SecurityConfig,
    SecurityHeadersConfig,
)
from oridecon.web.security.context import SecurityContext, get_security_context
from oridecon.web.security.cors.middleware import CORSMiddleware, CORSMiddlewareFactory
from oridecon.web.security.csp.builder import CSPPolicy
from oridecon.web.security.csrf.middleware import CSRFProtectionMiddleware
from oridecon.web.security.guards import (
    AuthGuard,
    GuardProtocol,
    PermissionGuard,
    RoleGuard,
    use_guards,
)

__all__ = [
    "AuthGuard",
    "CORSConfig",
    "CORSMiddleware",
    "CORSMiddlewareFactory",
    "CSPConfig",
    "CSPPolicy",
    "CSRFConfig",
    "CSRFProtectionMiddleware",
    "CrossOriginConfig",
    "GuardProtocol",
    "HSTSConfig",
    "PermissionGuard",
    "RoleGuard",
    "SecurityConfig",
    "SecurityContext",
    "SecurityHeadersConfig",
    "SecurityHeadersMiddleware",
    "get_security_context",
    "use_guards",
]
