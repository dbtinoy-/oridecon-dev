"""Resilience exception contracts."""

from __future__ import annotations

from oridecon.contracts.exceptions.resilience import (
    BulkheadError,
    CircuitBreakerError,
    CircuitOpenError,
    FallbackError,
    ResilienceError,
    RetryError,
    RetryExhaustedError,
)

__all__ = [
    "BulkheadError",
    "CircuitBreakerError",
    "CircuitOpenError",
    "FallbackError",
    "ResilienceError",
    "RetryError",
    "RetryExhaustedError",
]
