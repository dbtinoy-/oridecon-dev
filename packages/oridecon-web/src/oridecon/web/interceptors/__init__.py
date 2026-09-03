"""Interceptor system for Oridecon Web.

Two interception models are available:

- **HTTP Pipeline** (``interceptors.pipeline``): For HTTP request/response interception.
- **AOP Proxy** (``interceptors.aop``): For general-purpose method interception.
"""

from __future__ import annotations

from oridecon.di.extensions.aop_interceptors import (
    InterceptorTimeoutError,
    MethodInterceptorProtocol,
    MethodInterceptorRegistry,
    MethodInterceptorRegistryManager,
)
from oridecon.web.interceptors.builtin.cache import CacheInterceptor

# Built-in interceptors
from oridecon.web.interceptors.builtin.logging import LoggingInterceptor
from oridecon.web.interceptors.builtin.timing import HandlerTimingInterceptor
from oridecon.web.interceptors.builtin.transform import TransformInterceptor
from oridecon.web.interceptors.pipeline import InterceptorPipeline
from oridecon.web.protocols import (
    CallHandlerProtocol,
    ExecutionContextProtocol,
    WebInterceptorBase,
    WebInterceptorProtocol,
)
from oridecon.web.routing.execution_context import (
    WebExecutionContext,
)

__all__ = [
    "CacheInterceptor",
    # Protocols
    "CallHandlerProtocol",
    "ExecutionContextProtocol",
    "HandlerTimingInterceptor",
    # Pipeline
    "InterceptorPipeline",
    # Timeout
    "InterceptorTimeoutError",
    # Built-in interceptors
    "LoggingInterceptor",
    # AOP
    "MethodInterceptorProtocol",
    "MethodInterceptorRegistry",
    "MethodInterceptorRegistryManager",
    "TransformInterceptor",
    # Context
    "WebExecutionContext",
    "WebInterceptorBase",
    "WebInterceptorProtocol",
]
