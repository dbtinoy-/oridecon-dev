"""Authentication and authorization protocols."""

from __future__ import annotations

from oridecon.contracts.auth.blacklist import TokenBlacklistProtocol
from oridecon.contracts.auth.exceptions import (
    AuthError,
    TokenError,
    VerificationError,
)
from oridecon.contracts.auth.guard import AuthenticatorProtocol, AuthorizerProtocol
from oridecon.contracts.auth.identity import IdentityResolverProtocol
from oridecon.contracts.auth.models import (
    UserIdentityProtocol,
    UserSession,
    VerifiedIdentityClaims,
)
from oridecon.contracts.auth.policy import PolicyStoreProtocol
from oridecon.contracts.auth.protocols import (
    AuthProviderProtocol,
    LoginAttemptTrackerProtocol,
    MFAManagerProtocol,
    PasswordHasherProtocol,
    PasswordPolicyProtocol,
)
from oridecon.contracts.auth.repositories import (
    APIKeyRepositoryProtocol,
    SessionRepositoryProtocol,
)
from oridecon.contracts.auth.roles import RoleDefinition
from oridecon.contracts.auth.store import (
    UserReaderProtocol,
    UserStoreProtocol,
    UserWriterProtocol,
)
from oridecon.contracts.auth.token import TokenManagerProtocol, VerifiedToken
from oridecon.contracts.auth.user import AuthenticatedUserProtocol, UserProtocol

__all__ = [
    "APIKeyRepositoryProtocol",
    "AuthError",
    "AuthProviderProtocol",
    "AuthenticatedUserProtocol",
    "AuthenticatorProtocol",
    "AuthorizerProtocol",
    "IdentityResolverProtocol",
    "LoginAttemptTrackerProtocol",
    "MFAManagerProtocol",
    "PasswordHasherProtocol",
    "PasswordPolicyProtocol",
    "PolicyStoreProtocol",
    "RoleDefinition",
    "SessionRepositoryProtocol",
    "TokenBlacklistProtocol",
    "TokenError",
    "TokenManagerProtocol",
    "UserIdentityProtocol",
    "UserProtocol",
    "UserReaderProtocol",
    "UserSession",
    "UserStoreProtocol",
    "UserWriterProtocol",
    "VerificationError",
    "VerifiedIdentityClaims",
    "VerifiedToken",
]
