"""Public protocol surface for ``oridecon.secrets``.

Re-exports the canonical ``RotatableSecretStoreProtocol`` along with
contract-level protocols relevant to secret management.
"""

from __future__ import annotations

from oridecon.contracts.security.stores import AsyncSecretStoreProtocol
from oridecon.secrets.tenancy import TenantScopedSecretStore
from oridecon.secrets.types import RotatableSecretStoreProtocol

__all__ = [
    "AsyncSecretStoreProtocol",
    "RotatableSecretStoreProtocol",
    "TenantScopedSecretStore",
]
