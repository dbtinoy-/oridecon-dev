"""DI extension points — discovery, interceptors, strategies, and protocol validation."""

from __future__ import annotations

from oridecon.di.extensions.discovery import ProviderScanner
from oridecon.di.extensions.interceptors import (
    DIInterceptor,
    InterceptorRegistry,
    wrap_with_interceptors,
)
from oridecon.di.extensions.strategies import ResolutionStrategy
from oridecon.di.extensions.validator import ProtocolValidator, validate_protocol

__all__ = [
    "DIInterceptor",
    "InterceptorRegistry",
    "ProtocolValidator",
    "ProviderScanner",
    "ResolutionStrategy",
    "validate_protocol",
    "wrap_with_interceptors",
]
