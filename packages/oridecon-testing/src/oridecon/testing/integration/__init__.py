"""Integration test infrastructure for Oridecon.

Provides async service availability probes and pytest skip-markers.
"""

from __future__ import annotations

from oridecon.testing.harness.environment import IntegrationEnvironment
from oridecon.testing.integration.config import IntegrationTestConfig
from oridecon.testing.integration.markers import (
    requires_elasticsearch,
    requires_kafka,
    requires_meilisearch,
    requires_minio,
    requires_mongodb,
    requires_neo4j,
    requires_postgres,
    requires_qdrant,
    requires_rabbitmq,
    requires_redis,
    requires_smtp,
)
from oridecon.testing.integration.probes import ServiceProbe

__all__ = [
    "IntegrationEnvironment",
    "IntegrationTestConfig",
    "ServiceProbe",
    "requires_elasticsearch",
    "requires_kafka",
    "requires_meilisearch",
    "requires_minio",
    "requires_mongodb",
    "requires_neo4j",
    "requires_postgres",
    "requires_qdrant",
    "requires_rabbitmq",
    "requires_redis",
    "requires_smtp",
]
