"""Middleware Domain - Web-Specific Middleware"""

from __future__ import annotations

from oridecon.web.middleware.access_log import AccessLogMiddleware
from oridecon.web.middleware.auth import (
    AuthenticationError,
    AuthenticationMiddleware,
    AuthenticatorProtocol,
    AuthorizationError,
    AuthorizerProtocol,
)
from oridecon.web.middleware.base import (
    MiddlewareChain,
    MiddlewareRegistry,
)
from oridecon.web.middleware.body_limit import RequestBodySizeLimitMiddleware
from oridecon.web.middleware.compression import CompressionMiddleware
from oridecon.web.middleware.cors import (
    CORSMiddleware,
    create_development_cors,
    create_production_cors,
)
from oridecon.web.middleware.rate_limit import (
    RateLimiter,
    RateLimitMiddleware,
    rate_limit,
)
from oridecon.web.middleware.request_id import (
    RequestIDLogFilter,
    RequestIDMiddleware,
    configure_logging_with_request_id,
)
from oridecon.web.middleware.role_guard import (
    RoleGuardMiddleware,
    RoleGuardRule,
    RoleResolverProtocol,
)
from oridecon.web.middleware.sanitization import InputSanitizationMiddleware
from oridecon.web.middleware.security import (
    SecurityHeadersMiddleware,
    create_development_config,
    create_production_config,
    create_security_middleware,
)
from oridecon.web.middleware.stack import DefaultMiddlewareStack
from oridecon.web.middleware.static import StaticFileProvider, StaticFilesMiddleware
from oridecon.web.middleware.timing import TimingMiddleware

__all__ = [
    # Access logging
    "AccessLogMiddleware",
    # Exceptions
    "AuthenticationError",
    # Authentication middleware (transport layer only)
    "AuthenticationMiddleware",
    # Protocols for authentication
    "AuthenticatorProtocol",
    "AuthorizationError",
    "AuthorizerProtocol",
    "CORSMiddleware",
    # HTTP middleware
    "CompressionMiddleware",
    # Default stack
    "DefaultMiddlewareStack",
    # Input sanitization
    "InputSanitizationMiddleware",
    "MiddlewareChain",
    "MiddlewareRegistry",
    "RateLimitMiddleware",
    "RateLimiter",
    # Body size protection
    "RequestBodySizeLimitMiddleware",
    "RequestIDLogFilter",
    "RequestIDMiddleware",
    # Role guard
    "RoleGuardMiddleware",
    "RoleGuardRule",
    "RoleResolverProtocol",
    # Security headers middleware
    "SecurityHeadersMiddleware",
    "StaticFileProvider",
    "StaticFilesMiddleware",
    "TimingMiddleware",
    "configure_logging_with_request_id",
    "create_development_config",
    "create_development_cors",
    "create_production_config",
    "create_production_cors",
    "create_security_middleware",
    "rate_limit",
]
