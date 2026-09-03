"""Auth DI sub-providers — individual focused providers for the auth stack."""

from __future__ import annotations

from oridecon.auth.di.sub_providers.authentication_provider import (
    AuthenticationProvider,
)
from oridecon.auth.di.sub_providers.authorization_provider import AuthorizationProvider
from oridecon.auth.di.sub_providers.google_oauth_provider import GoogleOAuthProvider
from oridecon.auth.di.sub_providers.mfa_provider import MFAProvider
from oridecon.auth.di.sub_providers.oauth2_provider import OAuth2Provider
from oridecon.auth.di.sub_providers.oauth_provider import (
    detect_oauth_providers_from_config,
)
from oridecon.auth.di.sub_providers.passkey_provider import PasskeyProvider
from oridecon.auth.di.sub_providers.session_provider import SessionProvider
from oridecon.auth.di.sub_providers.token_provider import TokenProvider

__all__ = [
    "AuthenticationProvider",
    "AuthorizationProvider",
    "GoogleOAuthProvider",
    "MFAProvider",
    "OAuth2Provider",
    "PasskeyProvider",
    "SessionProvider",
    "TokenProvider",
    "detect_oauth_providers_from_config",
]
