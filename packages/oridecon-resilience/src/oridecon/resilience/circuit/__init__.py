"""Circuit breaker resilience pattern."""

from __future__ import annotations

from oridecon.resilience.circuit.backend import (
    CircuitBreakerBackend,
    CircuitBreakerState,
    DistributedCircuitBreakerBackend,
    InMemoryCircuitBreakerBackend,
)
from oridecon.resilience.circuit.breaker import (
    CircuitBreaker,
    CircuitBreakerMetrics,
    CircuitBreakerRegistry,
    CircuitState,
    circuit_breaker,
    circuit_breaker_sync,
)
from oridecon.resilience.circuit.timeout import (
    ResilienceTimeoutError,
    timeout_context,
)

__all__ = [
    "CircuitBreaker",
    "CircuitBreakerBackend",
    "CircuitBreakerMetrics",
    "CircuitBreakerRegistry",
    "CircuitBreakerState",
    "CircuitState",
    "DistributedCircuitBreakerBackend",
    "InMemoryCircuitBreakerBackend",
    "ResilienceTimeoutError",
    "circuit_breaker",
    "circuit_breaker_sync",
    "timeout_context",
]
