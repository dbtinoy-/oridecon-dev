"""
oridecon-auth — Authentication and authorisation for the Oridecon platform.

Canonical import paths
-----------------------
User authentication:   from oridecon.auth.authn.services import AuthenticationService
Token refresh:         from oridecon.auth.authn.services import AuthenticationService
                       await service.refresh_token(existing_refresh_token)
JWT tokens:            from oridecon.auth.authn.jwt import JWTTokenManager
RBAC / authorisation:  from oridecon.auth.authz.service import AuthorizationService
Session management:    from oridecon.auth.session import SessionManagerImpl
OAuth:                 from oridecon.auth.authn.oauth import OAuthService
Account verification:  from oridecon.auth.authn.verification import AccountVerificationService

All commonly-used symbols are also re-exported from this root package so
``from oridecon.auth import JWTTokenManager`` always works.

Key APIs
--------
- ``AuthenticationService.refresh_token(refresh_token: str) -> Result[AuthToken, TokenError]``
  Refresh an expired access token using a refresh token. Returns new access + refresh tokens.
- ``AuthenticationService.authenticate(user_id, password) -> Result[AuthToken, AuthenticationFailed]``
  Authenticate a user with credentials.
- ``AuthorizationService.authorize(user, required_roles) -> Result[True, AuthorizationFailed]``
  Enforce RBAC policies.

GuardProtocol decorators
----------------
``use_guards`` is intentionally **not** exported from this root package.
Use ``oridecon.security.guards.use_guards`` (the canonical, general-purpose
version backed by ``GuardChain``) or the auth-specific decorators
``require_auth``, ``require_roles``, and ``require_permissions``.
"""

from __future__ import annotations

import importlib.metadata
from typing import TYPE_CHECKING, Any

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from oridecon.auth.constants import __version__ as __version__

# =============================================================================
# Lazy Loading to Avoid Circular Imports
# =============================================================================


if TYPE_CHECKING:
    from oridecon.auth.authn.api_key import (
        APIKeyAuthenticator,
        APIKeyConfig,
    )
    from oridecon.auth.authn.google_oauth import GoogleOAuthService
    from oridecon.auth.authn.jwt import JWTTokenManager
    from oridecon.auth.authn.revocation import PersistentTokenRevocationStore
    from oridecon.auth.authn.security import (
        PasswordHasher,
        PasswordPolicy,
    )
    from oridecon.auth.authn.services import (
        AuthenticationService,
        LockoutConfig,
        LoginAttemptTracker,
    )
    from oridecon.auth.authn.user_service import UserService
    from oridecon.auth.authz.guards import (
        optional_auth,
        require_auth,
        require_permissions,
        require_roles,
    )
    from oridecon.auth.config import (
        AuthConfig,
        JWTConfig,
        MFAConfig,
        RBACConfig,
    )
    from oridecon.auth.di import (
        AuthenticationProvider,
        AuthorizationProvider,
        GoogleOAuthProvider,
    )
    from oridecon.auth.di.bundle_provider import AuthBundleProvider
    from oridecon.auth.events import (
        AuthenticationFailed,
        PasswordChanged,
        SessionCreated,
        SessionRevoked,
        TokenRevoked,
        UserAuthenticated,
        UserLockedOut,
        UserLoggedIn,
        UserLoggedOut,
        UserLoginFailed,
        UserRegistered,
    )
    from oridecon.auth.exceptions import (
        AlreadyVerifiedError,
        AuthenticationError,
        AuthError,
        AuthorizationError,
        InvalidTokenError,
        TokenAudienceError,
        TokenBlacklistedError,
        TokenError,
        TokenExpiredError,
        TokenExpiredVerificationError,
        TokenInvalidError,
        TokenNotFoundError,
        VerificationError,
    )
    from oridecon.auth.models import (
        AuthToken,
        User,
    )
    from oridecon.auth.protocols import TokenValidatorProtocol
    from oridecon.auth.session.cookie_backend import SessionCookieBackend
    from oridecon.auth.storage.oauth_identity_store import (
        MongoDBOAuthIdentityStore,
        OAuthIdentity,
        OAuthIdentityStore,
        SQLAlchemyOAuthIdentityStore,
    )
    from oridecon.auth.types import (
        AuthResult,
        AuthStatus,
        RoleDefinition,
        UserStatus,
    )
    from oridecon.contracts.auth import (
        IdentityResolverProtocol,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # Session cookie backend
    "SessionCookieBackend": (
        "oridecon.auth.session.cookie_backend",
        "SessionCookieBackend",
    ),
    # Module
    "AuthModule": ("oridecon.auth.module", "AuthModule"),
    # Config
    "AuthConfig": ("oridecon.auth.config", "AuthConfig"),
    "JWTConfig": ("oridecon.auth.config", "JWTConfig"),
    "MFAConfig": ("oridecon.auth.config", "MFAConfig"),
    "RBACConfig": ("oridecon.auth.config", "RBACConfig"),
    # Providers
    "AuthBundleProvider": ("oridecon.auth.di.bundle_provider", "AuthBundleProvider"),
    "AuthenticationProvider": ("oridecon.auth.di", "AuthenticationProvider"),
    "AuthorizationProvider": ("oridecon.auth.di", "AuthorizationProvider"),
    "GoogleOAuthProvider": ("oridecon.auth.di", "GoogleOAuthProvider"),
    # Services
    "AuthenticationService": ("oridecon.auth.authn.services", "AuthenticationService"),
    "LoginAttemptTracker": ("oridecon.auth.authn.services", "LoginAttemptTracker"),
    "LockoutConfig": ("oridecon.auth.authn.services", "LockoutConfig"),
    "UserService": ("oridecon.auth.authn.user_service", "UserService"),
    # API Key AuthenticatorProtocol
    "APIKeyAuthenticator": ("oridecon.auth.authn.api_key", "APIKeyAuthenticator"),
    "APIKeyConfig": ("oridecon.auth.authn.api_key", "APIKeyConfig"),
    # Core Security
    "JWTTokenManager": ("oridecon.auth.authn.jwt", "JWTTokenManager"),
    "GoogleOAuthService": ("oridecon.auth.authn.google_oauth", "GoogleOAuthService"),
    "PasswordHasher": ("oridecon.auth.authn.security", "PasswordHasher"),
    "PasswordPolicy": ("oridecon.auth.authn.security", "PasswordPolicy"),
    # Token Revocation
    "PersistentTokenRevocationStore": (
        "oridecon.auth.authn.revocation",
        "PersistentTokenRevocationStore",
    ),
    # Types
    "User": ("oridecon.auth.models", "User"),
    "AuthToken": ("oridecon.auth.models", "AuthToken"),
    "AuthResult": ("oridecon.auth.types", "AuthResult"),
    "AuthStatus": ("oridecon.auth.types", "AuthStatus"),
    "UserStatus": ("oridecon.auth.types", "UserStatus"),
    "RoleDefinition": ("oridecon.auth.types", "RoleDefinition"),
    # OAuth Identity Store
    "OAuthIdentityStore": (
        "oridecon.auth.storage.oauth_identity_store",
        "OAuthIdentityStore",
    ),
    "OAuthIdentity": ("oridecon.auth.storage.oauth_identity_store", "OAuthIdentity"),
    "SQLAlchemyOAuthIdentityStore": (
        "oridecon.auth.storage.oauth_identity_store",
        "SQLAlchemyOAuthIdentityStore",
    ),
    "MongoDBOAuthIdentityStore": (
        "oridecon.auth.storage.oauth_identity_store",
        "MongoDBOAuthIdentityStore",
    ),
    # Protocols
    "IdentityResolverProtocol": (
        "oridecon.contracts.auth",
        "IdentityResolverProtocol",
    ),
    "OAuthIdentityStoreProtocol": (
        "oridecon.contracts.auth",
        "OAuthIdentityStoreProtocol",
    ),
    "TokenValidatorProtocol": (
        "oridecon.auth.protocols",
        "TokenValidatorProtocol",
    ),
    # Exceptions (all from single canonical exceptions.py)
    "AuthError": ("oridecon.auth.exceptions", "AuthError"),
    "AuthenticationError": ("oridecon.auth.exceptions", "AuthenticationError"),
    "AuthorizationError": ("oridecon.auth.exceptions", "AuthorizationError"),
    "TokenError": ("oridecon.auth.exceptions", "TokenError"),
    "InvalidTokenError": ("oridecon.auth.exceptions", "InvalidTokenError"),
    "TokenExpiredError": ("oridecon.auth.exceptions", "TokenExpiredError"),
    # Leaf token/verification exceptions (merged from former errors.py)
    "AlreadyVerifiedError": ("oridecon.auth.exceptions", "AlreadyVerifiedError"),
    "TokenAudienceError": ("oridecon.auth.exceptions", "TokenAudienceError"),
    "TokenBlacklistedError": ("oridecon.auth.exceptions", "TokenBlacklistedError"),
    "TokenExpiredVerificationError": (
        "oridecon.auth.exceptions",
        "TokenExpiredVerificationError",
    ),
    "TokenInvalidError": ("oridecon.auth.exceptions", "TokenInvalidError"),
    "TokenNotFoundError": ("oridecon.auth.exceptions", "TokenNotFoundError"),
    "VerificationError": ("oridecon.auth.exceptions", "VerificationError"),
    # Guards & Dependencies
    "require_auth": ("oridecon.auth.authz.guards", "require_auth"),
    "require_roles": ("oridecon.auth.authz.guards", "require_roles"),
    "require_permissions": ("oridecon.auth.authz.guards", "require_permissions"),
    "optional_auth": ("oridecon.auth.authz.guards", "optional_auth"),
    # Domain Events
    "AuthenticationFailed": ("oridecon.auth.events", "AuthenticationFailed"),
    "PasswordChanged": ("oridecon.auth.events", "PasswordChanged"),
    "SessionCreated": ("oridecon.auth.events", "SessionCreated"),
    "SessionRevoked": ("oridecon.auth.events", "SessionRevoked"),
    "TokenRevoked": ("oridecon.auth.events", "TokenRevoked"),
    "UserAuthenticated": ("oridecon.auth.events", "UserAuthenticated"),
    "UserLoggedIn": ("oridecon.auth.events", "UserLoggedIn"),
    "UserLoggedOut": ("oridecon.auth.events", "UserLoggedOut"),
    "UserLoginFailed": ("oridecon.auth.events", "UserLoginFailed"),
    "UserLockedOut": ("oridecon.auth.events", "UserLockedOut"),
    "UserRegistered": ("oridecon.auth.events", "UserRegistered"),
    # Hooks
    "AuthAuthenticationFailedHook": (
        "oridecon.auth.hooks",
        "AuthAuthenticationFailedHook",
    ),
    "AuthTokenIssuedHook": ("oridecon.auth.hooks", "AuthTokenIssuedHook"),
    "AuthTokenRefreshedHook": ("oridecon.auth.hooks", "AuthTokenRefreshedHook"),
    "AuthTokenRevokedHook": ("oridecon.auth.hooks", "AuthTokenRevokedHook"),
    "AuthUserAuthenticatedHook": ("oridecon.auth.hooks", "AuthUserAuthenticatedHook"),
}


def __getattr__(name: str) -> Any:
    """Lazy load attributes to avoid circular imports."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """List available attributes for IDE support."""
    return list(__all__) + list(_LAZY_IMPORTS.keys())


__all__ = [
    "APIKeyAuthenticator",
    "APIKeyConfig",
    "AlreadyVerifiedError",
    "AuthAuthenticationFailedHook",
    "AuthBundleProvider",
    "AuthConfig",
    "AuthError",
    "AuthModule",
    "AuthResult",
    "AuthStatus",
    "AuthToken",
    "AuthTokenIssuedHook",
    "AuthTokenRefreshedHook",
    "AuthTokenRevokedHook",
    "AuthUserAuthenticatedHook",
    "AuthenticationFailed",
    "AuthenticationProvider",
    "AuthenticationService",
    "AuthorizationError",
    "AuthorizationProvider",
    "GoogleOAuthProvider",
    "GoogleOAuthService",
    "IdentityResolverProtocol",
    "InvalidTokenError",
    "JWTConfig",
    "JWTTokenManager",
    "LockoutConfig",
    "LoginAttemptTracker",
    "MFAConfig",
    "MongoDBOAuthIdentityStore",
    "OAuthIdentity",
    "OAuthIdentityStore",
    "PasswordChanged",
    "PasswordHasher",
    "PasswordPolicy",
    "PersistentTokenRevocationStore",
    "RBACConfig",
    "RoleDefinition",
    "SQLAlchemyOAuthIdentityStore",
    "SessionCookieBackend",
    "SessionCreated",
    "SessionRevoked",
    "TokenAudienceError",
    "TokenBlacklistedError",
    "TokenError",
    "TokenExpiredError",
    "TokenExpiredVerificationError",
    "TokenInvalidError",
    "TokenNotFoundError",
    "TokenRevoked",
    "TokenValidatorProtocol",
    "User",
    "UserAuthenticated",
    "UserLockedOut",
    "UserLoggedIn",
    "UserLoggedOut",
    "UserLoginFailed",
    "UserRegistered",
    "UserService",
    "UserStatus",
    "VerificationError",
    "optional_auth",
    "require_auth",
    "require_permissions",
    "require_roles",
]
