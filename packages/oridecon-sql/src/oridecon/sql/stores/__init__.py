"""Database-backed store implementations for state, secrets, and locks.

These classes were previously housed in ``oridecon-cache`` as
``DatabaseBridge*`` classes but have been relocated here because they
depend on :class:`~oridecon.contracts.DatabaseProviderProtocol` — a purely
database concern — and sharing the connection pool with the rest of the
application is their defining feature.

They implement the protocols defined in
:mod:`oridecon.contracts.stores`:

- :class:`DatabaseStateStore` → :class:`~oridecon.contracts.stores.StateStoreProtocol`
- :class:`DatabaseSecretStore` → :class:`~oridecon.contracts.stores.AsyncSecretStoreProtocol`
- :class:`DatabaseLockStore`  → :class:`~oridecon.contracts.stores.LockStoreProtocol`
"""

from __future__ import annotations

from oridecon.sql.stores.locks import DatabaseLockStore
from oridecon.sql.stores.secrets import DatabaseSecretStore
from oridecon.sql.stores.state import DatabaseStateStore

__all__ = [
    "DatabaseLockStore",
    "DatabaseSecretStore",
    "DatabaseStateStore",
]
