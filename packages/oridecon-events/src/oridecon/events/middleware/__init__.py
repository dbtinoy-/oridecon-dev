"""AbstractMiddleware module for CQRS buses.

This module provides reusable middleware components:
- LoggingMiddleware: Log command/query execution
- ValidationMiddleware: Validate messages before handling
- TransactionMiddleware: Wrap handlers in transactions
- RetryMiddleware: Retry failed handlers
- MetricsMiddleware: Collect execution metrics
- CircuitBreakerMiddleware: Prevent cascading failures
"""

from __future__ import annotations

from oridecon.events.middleware.base import (
    AbstractMiddleware,
    MiddlewareChain,
    NextHandler,
    middleware,
)
from oridecon.events.middleware.circuit_breaker import CircuitBreakerMiddleware
from oridecon.events.middleware.logging import LoggingMiddleware
from oridecon.events.middleware.metrics import (
    MessageMetrics,
    MetricsMiddleware,
)
from oridecon.events.middleware.retry import RetryMiddleware
from oridecon.events.middleware.transaction import (
    TransactionContext,
    TransactionMiddleware,
    UnitOfWorkMiddleware,
)
from oridecon.events.middleware.validation import ValidationMiddleware

__all__ = [
    "AbstractMiddleware",
    "CircuitBreakerMiddleware",
    "LoggingMiddleware",
    "MessageMetrics",
    "MetricsMiddleware",
    "MiddlewareChain",
    "NextHandler",
    "RetryMiddleware",
    "TransactionContext",
    "TransactionMiddleware",
    "UnitOfWorkMiddleware",
    "ValidationMiddleware",
    "middleware",
]
