"""Auth Providers - Framework integration and service registration"""

from __future__ import annotations

from oridecon.auth.authn.security import PasswordHasher, PasswordPolicy
from oridecon.auth.di.bundle_provider import AuthBundleProvider
from oridecon.auth.di.sub_providers.authentication_provider import (
    AuthenticationProvider,
)
from oridecon.auth.di.sub_providers.authorization_provider import AuthorizationProvider
from oridecon.auth.di.sub_providers.google_oauth_provider import GoogleOAuthProvider

__all__ = [
    "AuthBundleProvider",
    "AuthenticationProvider",
    "AuthorizationProvider",
    "GoogleOAuthProvider",
    "PasswordHasher",
    "PasswordPolicy",
]
