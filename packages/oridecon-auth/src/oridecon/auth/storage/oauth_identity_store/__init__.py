"""OAuth identity storage for linking users to OAuth providers.

This module provides storage abstractions for linking OAuth2 identities
to local user accounts. This enables "social login" where users can
authenticate using external identity providers.

Example:
    Implementing a custom OAuth identity store::

        from oridecon.auth.storage.oauth_identity_store import OAuthIdentityStore

        class MyOAuthStore(OAuthIdentityStore):
            async def create_oauth_identity(self, user_id, provider, provider_user_id):
                # Store the OAuth link
                return OAuthIdentity(...)

            async def get_oauth_identity(self, provider, provider_user_id):
                # Lookup by provider and external ID
                pass

            # ... implement other methods
"""

from __future__ import annotations

from oridecon.auth.storage.oauth_identity_store._mongodb import (
    MongoDBOAuthIdentityStore,
)
from oridecon.auth.storage.oauth_identity_store._protocol import (
    OAuthIdentity,
    OAuthIdentityStore,
)
from oridecon.auth.storage.oauth_identity_store._sqlalchemy import (
    SQLAlchemyOAuthIdentityStore,
)
from oridecon.logging import get_logger

logger = get_logger(__name__)

__all__ = [
    "MongoDBOAuthIdentityStore",
    "OAuthIdentity",
    "OAuthIdentityStore",
    "SQLAlchemyOAuthIdentityStore",
    "logger",
]
