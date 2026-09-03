"""Public protocol surface for ``oridecon.resilience``."""

from __future__ import annotations

from oridecon.contracts.core.idempotency import IdempotencyStoreProtocol
from oridecon.contracts.infra.resilience import (
    BulkheadProtocol,
    CircuitBreakerProtocol,
    CircuitBreakerRegistryProtocol,
    RateLimiterProtocol,
    ResiliencePipelineProtocol,
    RetryPolicyProtocol,
    ThrottlerProtocol,
)

__all__ = [
    "BulkheadProtocol",
    "CircuitBreakerProtocol",
    "CircuitBreakerRegistryProtocol",
    "IdempotencyStoreProtocol",
    "RateLimiterProtocol",
    "ResiliencePipelineProtocol",
    "RetryPolicyProtocol",
    "ThrottlerProtocol",
]
