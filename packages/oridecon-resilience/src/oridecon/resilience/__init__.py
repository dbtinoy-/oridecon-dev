"""Oridecon Resilience — core resilience patterns packaged with oridecon.

Exposes circuit breakers, retries, bulkheads, timeouts, throttling, and
related tools used throughout the framework.

Usage::

    from oridecon.resilience import retry, circuit_breaker, BulkheadConfig

No auxiliary package is required; everything lives under
``oridecon.resilience``.  The contracts layer remains separate and only
contains the abstract protocols/configurations.
"""

from __future__ import annotations

import importlib.metadata

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from typing import TYPE_CHECKING

from oridecon.resilience.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.contracts.exceptions import (
        BulkheadError,
        CircuitBreakerError,
        ResilienceError,
        RetryError,
    )
    from oridecon.contracts.infra.resilience import (
        BulkheadProtocol,
        CircuitBreakerProtocol,
        CircuitBreakerRegistryProtocol,
        ResiliencePipelineProtocol,
        RetryPolicyProtocol,
        ThrottlerProtocol,
    )
    from oridecon.contracts.infra.resilience.models import (
        CircuitBreakerConfig,
        RetryConfig,
        TimeoutConfig,
    )
    from oridecon.resilience.bulkhead import Bulkhead
    from oridecon.resilience.circuit import (
        CircuitBreaker,
        CircuitBreakerRegistry,
        CircuitState,
        DistributedCircuitBreakerBackend,
        InMemoryCircuitBreakerBackend,
        circuit_breaker,
    )
    from oridecon.resilience.config import BulkheadConfig as BulkheadConfig
    from oridecon.resilience.decorators import (
        bulkhead,
        circuit_breaker,
        circuit_breaker_sync,
        with_timeout,
    )
    from oridecon.resilience.exceptions import (
        BulkheadRejectedError,
        CircuitOpenError,
        ResilienceTimeoutError,
        RetryExhaustedError,
    )
    from oridecon.resilience.rate_limiter import (
        DistributedRateLimiter,
        RateLimiter,
        SlidingWindowLimiter,
    )
    from oridecon.resilience.retry import RetryPolicy
    from oridecon.resilience.retry.retry import retry
    from oridecon.resilience.throttle import Throttler
    from oridecon.resilience.timeout import TimeoutManager
    from oridecon.resilience.types import ResilienceStatus as ResilienceStatus

_LAZY_IMPORTS: dict[str, str] = {
    # contracts — protocols
    "BulkheadProtocol": "oridecon.contracts.infra.resilience",
    "CircuitBreakerProtocol": "oridecon.contracts.infra.resilience",
    "CircuitBreakerRegistryProtocol": "oridecon.contracts.infra.resilience",
    "ResiliencePipelineProtocol": "oridecon.contracts.infra.resilience",
    "RetryPolicyProtocol": "oridecon.contracts.infra.resilience",
    "ThrottlerProtocol": "oridecon.contracts.infra.resilience",
    # contracts — models/configs
    "BulkheadConfig": "oridecon.resilience.config",
    "CircuitBreakerConfig": "oridecon.contracts.infra.resilience.models",
    "ResilienceStatus": "oridecon.resilience.types",
    "RetryConfig": "oridecon.contracts.infra.resilience.models",
    "TimeoutConfig": "oridecon.contracts.infra.resilience.models",
    # exceptions — base classes remain in contracts
    "BulkheadError": "oridecon.contracts.exceptions",
    "CircuitBreakerError": "oridecon.contracts.exceptions",
    "ResilienceError": "oridecon.contracts.exceptions",
    "RetryError": "oridecon.contracts.exceptions",
    # exceptions — leaf exceptions
    "BulkheadRejectedError": "oridecon.resilience.exceptions",
    "CircuitOpenError": "oridecon.resilience.exceptions",
    "RetryExhaustedError": "oridecon.resilience.exceptions",
    "ResilienceTimeoutError": "oridecon.resilience.exceptions",
    # implementations
    "Bulkhead": "oridecon.resilience.bulkhead",
    "CircuitBreaker": "oridecon.resilience.circuit",
    "CircuitBreakerRegistry": "oridecon.resilience.circuit",
    "CircuitState": "oridecon.resilience.circuit",
    "DistributedCircuitBreakerBackend": "oridecon.resilience.circuit",
    "InMemoryCircuitBreakerBackend": "oridecon.resilience.circuit",
    "circuit_breaker": "oridecon.resilience.decorators",
    "circuit_breaker_sync": "oridecon.resilience.decorators",
    "bulkhead": "oridecon.resilience.decorators",
    "with_timeout": "oridecon.resilience.decorators",
    "RateLimiter": "oridecon.resilience.rate_limiter",
    "SlidingWindowLimiter": "oridecon.resilience.rate_limiter",
    "DistributedRateLimiter": "oridecon.resilience.rate_limiter",
    "RetryPolicy": "oridecon.resilience.retry",
    "ResiliencePipeline": "oridecon.resilience.pipeline.executor",
    "retry": "oridecon.resilience.retry.retry",
    "Throttler": "oridecon.resilience.throttle",
    # constants
    "DEFAULT_BULKHEAD_MAX_CONCURRENT": "oridecon.resilience.constants",
    "DEFAULT_CB_FAILURE_THRESHOLD": "oridecon.resilience.constants",
    "DEFAULT_CB_RECOVERY_TIMEOUT": "oridecon.resilience.constants",
    "DEFAULT_RATE_LIMIT_WINDOW": "oridecon.resilience.constants",
    "DEFAULT_RETRY_ATTEMPTS": "oridecon.resilience.constants",
    "DEFAULT_RETRY_DELAY": "oridecon.resilience.constants",
    "DEFAULT_TIMEOUT": "oridecon.resilience.constants",
    # --- added by migration script ---
    "ResilienceConfig": "oridecon.resilience.config",
    "ResilienceModule": "oridecon.resilience.module",
    "ResilienceProvider": "oridecon.resilience.di.provider",
    "TimeoutManager": "oridecon.resilience.timeout.manager",
    # --- Idempotency subsystem (merged from oridecon-idempotency) ---
    "IdempotencyStoreProtocol": "oridecon.contracts.core.idempotency",
    "InMemoryIdempotencyStore": "oridecon.resilience.idempotency.store",
    "idempotent": "oridecon.resilience.decorators",
    "IdempotencyRecord": "oridecon.contracts.domain.idempotency",
    "IdempotencyStatus": "oridecon.contracts.domain.idempotency",
    "IdempotencyResult": "oridecon.resilience.types",
    "DEFAULT_CLEANUP_INTERVAL": "oridecon.resilience.idempotency.constants",
    "DEFAULT_KEY_PREFIX": "oridecon.resilience.idempotency.constants",
    "DEFAULT_MAX_ENTRIES": "oridecon.resilience.idempotency.constants",
    "DEFAULT_MAX_KEY_LENGTH": "oridecon.resilience.idempotency.constants",
    "DEFAULT_TTL": "oridecon.resilience.idempotency.constants",
    "ENV_PREFIX": "oridecon.resilience.constants",
    "IdempotencyConfig": "oridecon.resilience.config",
    "DuplicateRequestError": "oridecon.resilience.exceptions",
    "IdempotencyBackendError": "oridecon.resilience.exceptions",
    "IdempotencyConfigurationError": "oridecon.resilience.exceptions",
    "IdempotencyConflictError": "oridecon.resilience.exceptions",
    "IdempotencyError": "oridecon.resilience.exceptions",
    "IdempotencyStoreError": "oridecon.resilience.exceptions",
    "DatabaseIdempotencyStore": "oridecon.resilience.idempotency.database",
    "RedisIdempotencyStore": "oridecon.resilience.idempotency.redis",
    "IdempotencyMiddleware": "oridecon.resilience.idempotency.middleware",
    "IdempotencyProvider": "oridecon.resilience.idempotency.provider",
    "DurableIdempotencyProvider": "oridecon.resilience.idempotency.durable_provider",
    "IdempotencyModule": "oridecon.resilience.idempotency.module",
    # Hooks
    "CircuitClosedHook": "oridecon.resilience.hooks",
    "CircuitOpenedHook": "oridecon.resilience.hooks",
    "RetryAttemptedHook": "oridecon.resilience.hooks",
    # Events
    "CircuitOpenedEvent": "oridecon.resilience.events",
    "CircuitClosedEvent": "oridecon.resilience.events",
    "RetryExhaustedEvent": "oridecon.resilience.events",
    "IdempotencyKeyHitEvent": "oridecon.resilience.events",
}


def __getattr__(name: str) -> object:
    if name in _LAZY_IMPORTS:
        import importlib

        mod = importlib.import_module(_LAZY_IMPORTS[name])
        value = getattr(mod, name)
        globals()[name] = value
        return value
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = list(_LAZY_IMPORTS.keys())
