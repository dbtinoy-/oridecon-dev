"""Oridecon testing utilities."""

from __future__ import annotations

# Re-export from clients (optional deps guarded)
try:
    from oridecon.testing.clients.ai.bed import AITestBed
    from oridecon.testing.clients.ai.client import AITestClient
except ImportError:
    pass
try:
    from oridecon.testing.clients.db.bed import DatabaseTestBed
    from oridecon.testing.clients.db.client import DatabaseTestClient
except ImportError:
    pass
try:
    from oridecon.testing.clients.tasks.bed import TaskTestBed
    from oridecon.testing.clients.tasks.client import TaskTestClient
except ImportError:
    pass
try:
    from oridecon.testing.clients.web.bed import WebTestBed
    from oridecon.testing.clients.web.client import WebTestClient
except ImportError:
    pass

# Re-export from clock
from oridecon.testing.clock import FixedClock

# Re-export from compliance
from oridecon.testing.compliance import (
    AuditLoggerCompliance,
    AuditStoreCompliance,
    BlobStoreCompliance,
    CacheBackendCompliance,
    DatabaseProviderCompliance,
    DistributedLockCompliance,
    EventBusCompliance,
    FlagProviderCompliance,
    MiddlewareCompliance,
    NotificationChannelCompliance,
    QueueBackendCompliance,
    RepositoryCompliance,
    SearchEngineCompliance,
    TaskQueueCompliance,
    VectorStoreCompliance,
    WebhookDeliveryStoreCompliance,
    WebhookSubscriptionStoreCompliance,
)

# Re-export version
from oridecon.testing.constants import __version__

# Re-export from fakes
from oridecon.testing.fakes import (
    Clock,
    FakeAuditLogger,
    FakeCache,
    FakeClock,
    FakeCommandBus,
    FakeConfig,
    FakeEventBus,
    FakeLogger,
    FakeMetricsCollector,
    FakeQueryBus,
    FakeSpan,
    FakeStateStore,
    FakeTracer,
    FakeUnitOfWork,
    LogEntry,
    SystemClock,
)

# Re-export from fixtures
from oridecon.testing.fixtures.container import ContainerTestFixture
from oridecon.testing.fixtures.containers import ContainerFactory
from oridecon.testing.generators_contract import (
    assert_contributor_generators_render,
)

# Re-export from harness
from oridecon.testing.harness.container import OrideconContainerHarness

# Re-export from harness decorators
from oridecon.testing.harness.decorators import override, testbed
from oridecon.testing.harness.environment import IntegrationEnvironment
from oridecon.testing.harness.testbed import AppTestBed

# Re-export from integration (markers and probes)
from oridecon.testing.integration import (
    ServiceProbe,
    requires_postgres,
    requires_rabbitmq,
    requires_redis,
)

# Re-export from lib
from oridecon.testing.lib.admin_helpers import (
    AdminResponse,
    AdminTestClient,
    make_resource_record,
)
from oridecon.testing.lib.assertions import (
    TestAssertions,
    assert_all_ok,
    assert_err,
    assert_healthy,
    assert_ok,
    assert_result_err,
    assert_result_err_contains,
    assert_result_err_type,
    assert_result_ok,
    assert_result_ok_value,
)
from oridecon.testing.lib.async_helper import AsyncTestHelper
from oridecon.testing.lib.factory import TestDataFactory

# Re-export from lib (snapshots)
from oridecon.testing.lib.snapshots import SnapshotAsserter, SnapshotMismatchError

# Re-export from memory
from oridecon.testing.memory import (
    FileInfo,
    InMemoryAuditLogger,
    InMemoryBlobStore,
    InMemoryCacheBackend,
    InMemoryCommandBus,
    InMemoryDistributedLock,
    InMemoryEventBus,
    InMemoryOutbox,
    InMemoryQueryBus,
    InMemoryRepository,
    InMemoryUnitOfWork,
    MemoryProvider,
    OutboxRelay,
)

# Re-export from module
from oridecon.testing.module import TestingModule

# Re-export from testkit
from oridecon.testing.testkit.environment import TestEnvironment

__all__ = [
    "AITestBed",
    "AITestClient",
    "AdminResponse",
    "AdminTestClient",
    "AppTestBed",
    "AsyncTestHelper",
    "AuditLoggerCompliance",
    "AuditStoreCompliance",
    "BlobStoreCompliance",
    "CacheBackendCompliance",
    "Clock",
    "ContainerFactory",
    "ContainerTestFixture",
    "DatabaseProviderCompliance",
    "DatabaseTestBed",
    "DatabaseTestClient",
    "DistributedLockCompliance",
    "EventBusCompliance",
    "FakeAuditLogger",
    "FakeCache",
    "FakeClock",
    "FakeCommandBus",
    "FakeConfig",
    "FakeEventBus",
    "FakeLogger",
    "FakeMetricsCollector",
    "FakeQueryBus",
    "FakeSpan",
    "FakeStateStore",
    "FakeTracer",
    "FakeUnitOfWork",
    "FileInfo",
    "FixedClock",
    "FlagProviderCompliance",
    "InMemoryAuditLogger",
    "InMemoryBlobStore",
    "InMemoryCacheBackend",
    "InMemoryCommandBus",
    "InMemoryDistributedLock",
    "InMemoryEventBus",
    "InMemoryOutbox",
    "InMemoryQueryBus",
    "InMemoryRepository",
    "InMemoryUnitOfWork",
    "IntegrationEnvironment",
    "OrideconContainerHarness",
    "LogEntry",
    "MemoryProvider",
    "MiddlewareCompliance",
    "NotificationChannelCompliance",
    "OutboxRelay",
    "QueueBackendCompliance",
    "RepositoryCompliance",
    "SearchEngineCompliance",
    "ServiceProbe",
    "SnapshotAsserter",
    "SnapshotMismatchError",
    "TaskQueueCompliance",
    "TaskTestBed",
    "TaskTestClient",
    "TestAssertions",
    "TestDataFactory",
    "TestEnvironment",
    "TestingModule",
    "VectorStoreCompliance",
    "WebTestBed",
    "WebTestClient",
    "WebhookDeliveryStoreCompliance",
    "WebhookSubscriptionStoreCompliance",
    "__version__",
    "assert_all_ok",
    "assert_contributor_generators_render",
    "assert_err",
    "assert_healthy",
    "assert_ok",
    "assert_result_err",
    "assert_result_err_contains",
    "assert_result_err_type",
    "assert_result_ok",
    "assert_result_ok_value",
    "make_resource_record",
    "override",
    "requires_postgres",
    "requires_rabbitmq",
    "requires_redis",
    "testbed",
]
