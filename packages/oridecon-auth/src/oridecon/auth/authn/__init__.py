"""Authentication (AuthN) - Identity verification and session management"""

from __future__ import annotations

from oridecon.auth.authn._binding import TokenBindingConfig
from oridecon.auth.authn.account_verification import AccountVerificationService
from oridecon.auth.authn.api_key import APIKeyAuthenticator, APIKeyConfig
from oridecon.auth.authn.blacklist import JWTBlacklist
from oridecon.auth.authn.google_oauth import GoogleOAuthService
from oridecon.auth.authn.jwt import JWTTokenManager
from oridecon.auth.authn.oauth2 import OAuth2IdentityProvider, OAuth2Manager
from oridecon.auth.authn.password_reset import PasswordResetService
from oridecon.auth.authn.relay import RelayApiKeyVerifier
from oridecon.auth.authn.schemas import (
    LoginRequest,
    OAuth2AuthorizeRequest,
    OAuth2TokenRequest,
    PasswordResetConfirm,
    PasswordResetRequest,
    RefreshTokenRequest,
    RegisterRequest,
    TokenResponse,
    UserProfile,
)
from oridecon.auth.authn.security import PasswordHasher, PasswordPolicy
from oridecon.auth.authn.services import (
    AuthenticationService,
    LockoutConfig,
    LoginAttemptTracker,
)
from oridecon.auth.authn.user_service import UserService
from oridecon.auth.models.user import User
from oridecon.contracts.auth.user import AuthenticatedUserProtocol

__all__ = [
    "APIKeyAuthenticator",
    "APIKeyConfig",
    "AccountVerificationService",
    "AuthenticatedUserProtocol",
    "AuthenticationService",
    "GoogleOAuthService",
    "JWTBlacklist",
    "JWTTokenManager",
    "LockoutConfig",
    "LoginAttemptTracker",
    "LoginRequest",
    "OAuth2AuthorizeRequest",
    "OAuth2IdentityProvider",
    "OAuth2Manager",
    "OAuth2TokenRequest",
    "PasswordHasher",
    "PasswordPolicy",
    "PasswordResetConfirm",
    "PasswordResetRequest",
    "PasswordResetService",
    "RefreshTokenRequest",
    "RegisterRequest",
    "RelayApiKeyVerifier",
    "TokenBindingConfig",
    "TokenResponse",
    "User",
    "UserProfile",
    "UserService",
]
