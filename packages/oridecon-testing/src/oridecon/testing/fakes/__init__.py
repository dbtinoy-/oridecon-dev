"""Fake implementations for testing."""

from __future__ import annotations

from oridecon.testing.fakes.audit import FakeAuditLogger
from oridecon.testing.fakes.buses import FakeCommandBus, FakeQueryBus
from oridecon.testing.fakes.cache import FakeCache, FakeStateStore
from oridecon.testing.fakes.clock import Clock, FakeClock, SystemClock
from oridecon.testing.fakes.config import FakeConfig
from oridecon.testing.fakes.events import FakeEventBus
from oridecon.testing.fakes.governance import FakeResourceUnitTracker
from oridecon.testing.fakes.lifecycle import FakeUnitOfWork
from oridecon.testing.fakes.logging import FakeLogger, LogEntry
from oridecon.testing.fakes.monitoring import FakeMetricsCollector
from oridecon.testing.fakes.redis import FakeRedisClient
from oridecon.testing.fakes.secrets import FakeRotatableSecretStore
from oridecon.testing.fakes.tracing import FakeSpan, FakeTracer

__all__ = [
    "Clock",
    "FakeAuditLogger",
    "FakeCache",
    "FakeClock",
    "FakeCommandBus",
    "FakeConfig",
    "FakeEventBus",
    "FakeLogger",
    "FakeMetricsCollector",
    "FakeQueryBus",
    "FakeRedisClient",
    "FakeResourceUnitTracker",
    "FakeRotatableSecretStore",
    "FakeSpan",
    "FakeStateStore",
    "FakeTracer",
    "FakeUnitOfWork",
    "LogEntry",
    "SystemClock",
]
