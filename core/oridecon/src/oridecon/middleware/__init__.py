"""Middleware system for Oridecon Framework.

Provides middleware pipeline, registry, common middleware implementations,
and exception filter chain for composable request processing.

Exports:
    Middleware, MiddlewareProtocol, GuardProtocol: Contracts.
    MiddlewareGuardError: Raised when a guard rejects a request.
    MiddlewareChain, MiddlewarePipeline, MiddlewareRegistry: Pipeline components.
    ExceptionFilterChain: Ordered exception handler chain.
    CachingMiddleware, CorrelationIdMiddleware, ...: Built-in middleware.
"""

from __future__ import annotations

import importlib.metadata
from typing import TYPE_CHECKING, Any

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from oridecon.middleware.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.app.pipeline import MiddlewarePipeline
    from oridecon.contracts.exceptions.middleware import MiddlewareGuardError
    from oridecon.contracts.web import (
        GuardProtocol,
        Middleware,
        MiddlewareProtocol,
    )
    from oridecon.middleware.builtins import (
        CachingMiddleware,
        CircuitBreakerMiddleware,
        ConditionalMiddleware,
        CorrelationIdMiddleware,
        ErrorHandlerMiddleware,
        LoggingMiddleware,
        RateLimiterMiddleware,
        RetryMiddleware,
        ScopedMiddleware,
        TimeoutMiddleware,
        TimingMiddleware,
        ValidationMiddleware,
    )
    from oridecon.middleware.core.chain import MiddlewareChain
    from oridecon.middleware.core.exception_filters import ExceptionFilterChain
    from oridecon.middleware.core.registry import MiddlewareRegistry

_LAZY_IMPORTS: dict[str, str] = {
    # contracts
    "GuardProtocol": "oridecon.contracts.web",
    "MiddlewareGuardError": "oridecon.contracts.exceptions.middleware",
    "Middleware": "oridecon.contracts.core",
    "MiddlewareProtocol": "oridecon.contracts.core",
    # implementations
    "CachingMiddleware": "oridecon.middleware.builtins",
    "CircuitBreakerMiddleware": "oridecon.middleware.builtins",
    "ConditionalMiddleware": "oridecon.middleware.builtins",
    "CorrelationIdMiddleware": "oridecon.middleware.builtins",
    "ErrorHandlerMiddleware": "oridecon.middleware.builtins",
    "LoggingMiddleware": "oridecon.middleware.builtins",
    "RateLimiterMiddleware": "oridecon.middleware.builtins",
    "RetryMiddleware": "oridecon.middleware.builtins",
    "ScopedMiddleware": "oridecon.middleware.builtins",
    "TimingMiddleware": "oridecon.middleware.builtins",
    "TimeoutMiddleware": "oridecon.middleware.builtins",
    "ValidationMiddleware": "oridecon.middleware.builtins",
    "ExceptionFilterChain": "oridecon.middleware.core.exception_filters",
    "InfrastructureExceptionFilter": "oridecon.middleware.core.exception_filters",
    "MiddlewarePolicyExceptionFilter": "oridecon.middleware.core.exception_filters",
    "NotFoundExceptionFilter": "oridecon.middleware.core.exception_filters",
    "ValidationExceptionFilter": "oridecon.middleware.core.exception_filters",
    "MiddlewareChain": "oridecon.middleware.core.chain",
    "MiddlewarePipeline": "oridecon.app.pipeline",
    "MiddlewareRegistry": "oridecon.middleware.core.registry",
    # types
    "C": "oridecon.middleware.types",
    "MiddlewareCallable": "oridecon.middleware.types",
    "NextHandler": "oridecon.middleware.types",
    # constants
    "DEFAULT_CIRCUIT_FAILURE_THRESHOLD": "oridecon.middleware.constants",
    "DEFAULT_CIRCUIT_RECOVERY_TIMEOUT": "oridecon.middleware.constants",
    "DEFAULT_CORRELATION_HEADER": "oridecon.middleware.constants",
    "DEFAULT_RATE_LIMIT_MAX_REQUESTS": "oridecon.middleware.constants",
    "DEFAULT_RATE_LIMIT_WINDOW": "oridecon.middleware.constants",
    "DEFAULT_RETRY_COUNT": "oridecon.middleware.constants",
    "DEFAULT_RETRY_DELAY": "oridecon.middleware.constants",
    "DEFAULT_TIMEOUT": "oridecon.middleware.constants",
    "HOOK_CIRCUIT_BREAKER_CLOSED": "oridecon.middleware.constants",
    "HOOK_CIRCUIT_BREAKER_OPENED": "oridecon.middleware.constants",
    "HOOK_RATE_LIMIT_EXCEEDED": "oridecon.middleware.constants",
    "HOOK_TIMEOUT": "oridecon.middleware.constants",
    # --- added by migration script ---
    "MiddlewareConfig": "oridecon.middleware.config",
    "MiddlewareError": "oridecon.middleware.exceptions",
    "MiddlewareExecutionError": "oridecon.middleware.exceptions",
    "MiddlewareConfigurationError": "oridecon.middleware.exceptions",
    "MiddlewareChainError": "oridecon.middleware.exceptions",
    "MiddlewareTimeoutError": "oridecon.middleware.exceptions",
    "MiddlewareAuthError": "oridecon.middleware.exceptions",
    "MiddlewarePolicyError": "oridecon.middleware.exceptions",
    "MiddlewareRateLimitError": "oridecon.middleware.exceptions",
    "MiddlewareCircuitOpenError": "oridecon.middleware.exceptions",
    "MiddlewareModule": "oridecon.middleware.module",
    "MiddlewareProvider": "oridecon.middleware.di.provider",
}


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib

        module = importlib.import_module(_LAZY_IMPORTS[name])
        value = getattr(module, name)
        globals()[name] = value
        return value
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = list(_LAZY_IMPORTS.keys())
