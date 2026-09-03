"""Schema setup contributions for the oridecon-auth package."""

from __future__ import annotations

from oridecon.contracts.cli.contributions import SchemaSetupOutcome, SchemaSetupResult
from oridecon.contracts.data.sql.database import DatabaseProviderProtocol

_OAUTH_TABLE = "oauth_identities"


async def ensure_oauth_identities(db: DatabaseProviderProtocol) -> SchemaSetupOutcome:
    """Ensure the ``oauth_identities`` table exists.

    Args:
        db: The database provider.

    Returns:
        Outcome reporting CREATED, ALREADY_PRESENT, or FAILED.
    """
    from oridecon.auth.storage.oauth_identity_store import SQLAlchemyOAuthIdentityStore

    try:
        existed = await db.table_exists(_OAUTH_TABLE)
        await SQLAlchemyOAuthIdentityStore(db)._ensure_tables()
        return SchemaSetupOutcome(
            status=(
                SchemaSetupResult.ALREADY_PRESENT
                if existed
                else SchemaSetupResult.CREATED
            )
        )
    except Exception as exc:
        return SchemaSetupOutcome(status=SchemaSetupResult.FAILED, message=str(exc))
