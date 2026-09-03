"""Oridecon audit — unified audit trail with retention and HMAC verification."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oridecon.audit.admin.contributor import AuditAdminContributor
    from oridecon.audit.config import AuditConfig
    from oridecon.audit.di.bundle_provider import AuditBundleProvider
    from oridecon.audit.logging.logger import AuditLogger
    from oridecon.audit.module import AuditModule
    from oridecon.audit.retention.policy import PolicyBasedRetention
    from oridecon.audit.retention.purge import AuditPurger
    from oridecon.audit.store.memory import InMemoryAuditStore
    from oridecon.audit.verification.checksum import (
        compute_audit_checksum,
        verify_audit_checksum,
    )
    from oridecon.audit.verification.verifier import AuditVerifier

_LAZY_IMPORTS: dict[str, str] = {
    "AuditAdminContributor": "oridecon.audit.admin.contributor",
    "AuditConfig": "oridecon.audit.config",
    "AuditBundleProvider": "oridecon.audit.di.bundle_provider",
    "AuditLogger": "oridecon.audit.logging.logger",
    "AuditModule": "oridecon.audit.module",
    "PolicyBasedRetention": "oridecon.audit.retention.policy",
    "AuditPurger": "oridecon.audit.retention.purge",
    "InMemoryAuditStore": "oridecon.audit.store.memory",
    "compute_audit_checksum": "oridecon.audit.verification.checksum",
    "verify_audit_checksum": "oridecon.audit.verification.checksum",
    "AuditVerifier": "oridecon.audit.verification.verifier",
    "audited": "oridecon.audit.decorators",
}


def __getattr__(name: str) -> object:
    if name in _LAZY_IMPORTS:
        import importlib

        mod = importlib.import_module(_LAZY_IMPORTS[name])
        return getattr(mod, name)
    raise AttributeError(f"module 'oridecon.audit' has no attribute {name!r}")


__all__ = list(_LAZY_IMPORTS)
