"""Idempotency subsystem for the Oridecon resilience package.

Provides in-memory, Redis-backed, and SQL-backed idempotency stores,
HTTP middleware, DI providers, and a self-contained module.
"""

from __future__ import annotations

from oridecon.resilience.idempotency.constants import (
    DEFAULT_CLEANUP_INTERVAL,
    DEFAULT_KEY_PREFIX,
    DEFAULT_MAX_ENTRIES,
    DEFAULT_MAX_KEY_LENGTH,
    DEFAULT_TTL,
    ENV_NESTED_DELIMITER,
    ENV_PREFIX,
)
from oridecon.resilience.idempotency.database import DatabaseIdempotencyStore
from oridecon.resilience.idempotency.durable_provider import DurableIdempotencyProvider
from oridecon.resilience.idempotency.middleware import IdempotencyMiddleware
from oridecon.resilience.idempotency.module import IdempotencyModule
from oridecon.resilience.idempotency.provider import IdempotencyProvider
from oridecon.resilience.idempotency.redis import RedisIdempotencyStore
from oridecon.resilience.idempotency.store import InMemoryIdempotencyStore

__all__ = [
    "DEFAULT_CLEANUP_INTERVAL",
    "DEFAULT_KEY_PREFIX",
    "DEFAULT_MAX_ENTRIES",
    "DEFAULT_MAX_KEY_LENGTH",
    "DEFAULT_TTL",
    "ENV_NESTED_DELIMITER",
    "ENV_PREFIX",
    "DatabaseIdempotencyStore",
    "DurableIdempotencyProvider",
    "IdempotencyMiddleware",
    "IdempotencyModule",
    "IdempotencyProvider",
    "InMemoryIdempotencyStore",
    "RedisIdempotencyStore",
]
