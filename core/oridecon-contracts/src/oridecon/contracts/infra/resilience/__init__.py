"""Resilience pattern protocols."""

from __future__ import annotations

from oridecon.contracts.infra.resilience.enums import CircuitState
from oridecon.contracts.infra.resilience.exceptions import (
    BulkheadError,
    CircuitBreakerError,
    CircuitOpenError,
    FallbackError,
    ResilienceError,
    RetryError,
    RetryExhaustedError,
)
from oridecon.contracts.infra.resilience.models import (
    CircuitBreakerConfig,
    RetryConfig,
    TimeoutConfig,
)
from oridecon.contracts.infra.resilience.protocols import (
    BulkheadProtocol,
    CircuitBreakerProtocol,
    CircuitBreakerRegistryProtocol,
    RateLimiterProtocol,
    ResilienceFallbackProtocol,
    ResiliencePipelineFactoryProtocol,
    ResiliencePipelineProtocol,
    RetryPolicyProtocol,
    ThrottlerProtocol,
    TimeoutProtocol,
)

__all__ = [
    "BulkheadError",
    "BulkheadProtocol",
    "CircuitBreakerConfig",
    "CircuitBreakerError",
    "CircuitBreakerProtocol",
    "CircuitBreakerRegistryProtocol",
    "CircuitOpenError",
    "CircuitState",
    "FallbackError",
    "RateLimiterProtocol",
    "ResilienceError",
    "ResilienceFallbackProtocol",
    "ResiliencePipelineFactoryProtocol",
    "ResiliencePipelineProtocol",
    "RetryConfig",
    "RetryError",
    "RetryExhaustedError",
    "RetryPolicyProtocol",
    "ThrottlerProtocol",
    "TimeoutConfig",
    "TimeoutProtocol",
]
