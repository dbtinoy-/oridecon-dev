"""Shared fixtures for oridecon-audit tests."""

from __future__ import annotations

import pytest

from oridecon.audit.logging.logger import AuditLogger
from oridecon.audit.store.memory import InMemoryAuditStore
from oridecon.contracts.audit import AuditEntry, AuditEventSeverity



@pytest.fixture
def memory_store() -> InMemoryAuditStore:
    return InMemoryAuditStore()


@pytest.fixture
def audit_logger(memory_store: InMemoryAuditStore) -> AuditLogger:
    return AuditLogger(store=memory_store)


@pytest.fixture
def sample_entry() -> AuditEntry:
    return AuditEntry(
        action="user.login",
        actor_id="user-1",
        resource_type="User",
        resource_id="user-1",
        outcome="success",
        severity=AuditEventSeverity.MEDIUM,
        source="test",
    )
