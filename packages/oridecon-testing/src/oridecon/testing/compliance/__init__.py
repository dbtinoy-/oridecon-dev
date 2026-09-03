"""Contract compliance test suites for Oridecon protocol implementations.

Each suite is a base test class.  Subclass it, implement the abstract
factory method, and pytest will run all contract checks automatically::

    class TestRedisCacheCompliance(CacheBackendCompliance):
        async def create_backend(self):
            return RedisCacheBackend("redis://localhost:6379/15")

Available suites:

- :class:`~oridecon.testing.compliance.AuditLoggerCompliance`
- :class:`~oridecon.testing.compliance.AuditStoreCompliance`
- :class:`~oridecon.testing.compliance.BlobStoreCompliance`
- :class:`~oridecon.testing.compliance.CacheBackendCompliance`
- :class:`~oridecon.testing.compliance.DatabaseProviderCompliance`
- :class:`~oridecon.testing.compliance.DistributedLockCompliance`
- :class:`~oridecon.testing.compliance.EventBusCompliance`
- :class:`~oridecon.testing.compliance.FlagProviderCompliance`
- :class:`~oridecon.testing.compliance.MiddlewareCompliance`
- :class:`~oridecon.testing.compliance.NotificationChannelCompliance`
- :class:`~oridecon.testing.compliance.QueueBackendCompliance`
- :class:`~oridecon.testing.compliance.RepositoryCompliance`
- :class:`~oridecon.testing.compliance.SearchEngineCompliance`
- :class:`~oridecon.testing.compliance.TaskQueueCompliance`
- :class:`~oridecon.testing.compliance.VectorStoreCompliance`
- :class:`~oridecon.testing.compliance.WebhookDeliveryStoreCompliance`
- :class:`~oridecon.testing.compliance.WebhookSubscriptionStoreCompliance`
"""

from __future__ import annotations

from oridecon.testing.compliance.audit import (
    AuditLoggerCompliance,
    AuditStoreCompliance,
)
from oridecon.testing.compliance.blob_store import BlobStoreCompliance
from oridecon.testing.compliance.cache import CacheBackendCompliance
from oridecon.testing.compliance.database import DatabaseProviderCompliance
from oridecon.testing.compliance.distributed_lock import DistributedLockCompliance
from oridecon.testing.compliance.event_bus import EventBusCompliance
from oridecon.testing.compliance.flags import FlagProviderCompliance
from oridecon.testing.compliance.middleware import MiddlewareCompliance
from oridecon.testing.compliance.notification import NotificationChannelCompliance
from oridecon.testing.compliance.queue_backend import QueueBackendCompliance
from oridecon.testing.compliance.repository import RepositoryCompliance
from oridecon.testing.compliance.search import SearchEngineCompliance
from oridecon.testing.compliance.secrets import (
    StoreConformanceSuite,
    parametrize_rotatable_store,
)
from oridecon.testing.compliance.task_queue import TaskQueueCompliance
from oridecon.testing.compliance.vector_store import VectorStoreCompliance
from oridecon.testing.compliance.webhook import (
    WebhookDeliveryStoreCompliance,
    WebhookSubscriptionStoreCompliance,
)

__all__ = [
    "AuditLoggerCompliance",
    "AuditStoreCompliance",
    "BlobStoreCompliance",
    "CacheBackendCompliance",
    "DatabaseProviderCompliance",
    "DistributedLockCompliance",
    "EventBusCompliance",
    "FlagProviderCompliance",
    "MiddlewareCompliance",
    "NotificationChannelCompliance",
    "QueueBackendCompliance",
    "RepositoryCompliance",
    "SearchEngineCompliance",
    "StoreConformanceSuite",
    "TaskQueueCompliance",
    "VectorStoreCompliance",
    "WebhookDeliveryStoreCompliance",
    "WebhookSubscriptionStoreCompliance",
    "parametrize_rotatable_store",
]
