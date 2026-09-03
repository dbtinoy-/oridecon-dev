"""Pytest plugin for Oridecon Framework.

This module is loaded automatically by pytest via entry points when
oridecon-testing is installed in the environment.

Registers Oridecon-specific markers and wires up automatic test-skipping
for tests that require external services (Redis, PostgreSQL, Elasticsearch,
RabbitMQ, Meilisearch) when those services are not available.
"""

from __future__ import annotations

from oridecon.testing.plugins.pytest._hooks import (
    _MARKERS,
    _SERVICE_ENDPOINTS,
    _check_service,
    pytest_collection_modifyitems,
    pytest_configure,
)

__all__ = [
    "_MARKERS",
    "_SERVICE_ENDPOINTS",
    "_check_service",
    "pytest_collection_modifyitems",
    "pytest_configure",
    "pytest_plugins",
]

# Export the fixture declarations so this module is a complete entry point
pytest_plugins = [
    "oridecon.testing.fixtures.core",
    "oridecon.testing.fixtures.ai",
    "oridecon.testing.fixtures.db",
    "oridecon.testing.fixtures.messaging",
    "oridecon.testing.fixtures.web",
    "oridecon.testing.fixtures.tasks",
    "oridecon.testing.integration.fixtures",
]
