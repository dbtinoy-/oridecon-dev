"""Intelligence monitoring and observability.

This module provides tools for monitoring the health, performance,
and behavior of the intelligence layer.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from typing import TYPE_CHECKING, Any

try:
    __version__ = version("oridecon-ai-observability")
except PackageNotFoundError:
    __version__ = "0.0.0"

if TYPE_CHECKING:
    from oridecon.ai.observability.callbacks.manager import CallbackManagerImpl
    from oridecon.ai.observability.config import ObservabilityConfig
    from oridecon.ai.observability.decorators import (
        trace_llm,
        trace_rag,
        trace_vector,
        track_embedding_operation,
        track_llm_call,
        track_vector_operation,
    )
    from oridecon.ai.observability.di.provider import ObservabilityProvider
    from oridecon.ai.observability.exceptions import (
        HealthCheckError,
        MetricsError,
        ObservabilityError,
        TracingError,
    )
    from oridecon.ai.observability.health import AIHealthMonitor
    from oridecon.ai.observability.hooks import (
        AIObservabilityStartedHook,
        HealthCheckRunHook,
        LLMCallTracedHook,
    )
    from oridecon.ai.observability.metrics import (
        AIMetrics,
    )
    from oridecon.ai.observability.module import ObservabilityModule
    from oridecon.ai.observability.protocols import (
        AIHealthMonitorProtocol,
        AIMetricsProtocol,
        AITracerProtocol,
        ObservabilityProtocol,
    )
    from oridecon.ai.observability.tracing import (
        AITracer,
    )
    from oridecon.ai.observability.wrappers import (
        ObservableLLMClient,
        ObservableVectorStore,
    )
    from oridecon.contracts import HealthCheckResult, HealthStatus

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # --- Callback ---
    "CallbackManagerImpl": (
        "oridecon.ai.observability.callback_manager",
        "CallbackManagerImpl",
    ),
    # --- Hooks ---
    "AIObservabilityStartedHook": (
        "oridecon.ai.observability.hooks",
        "AIObservabilityStartedHook",
    ),
    "HealthCheckRunHook": (
        "oridecon.ai.observability.hooks",
        "HealthCheckRunHook",
    ),
    "LLMCallTracedHook": (
        "oridecon.ai.observability.hooks",
        "LLMCallTracedHook",
    ),
    # --- Config ---
    "ObservabilityConfig": ("oridecon.ai.observability.config", "ObservabilityConfig"),
    # --- DI ---
    "ObservabilityProvider": (
        "oridecon.ai.observability.di.provider",
        "ObservabilityProvider",
    ),
    "ObservabilityModule": ("oridecon.ai.observability.module", "ObservabilityModule"),
    # --- Exceptions ---
    "ObservabilityError": (
        "oridecon.ai.observability.exceptions",
        "ObservabilityError",
    ),
    "HealthCheckError": ("oridecon.ai.observability.exceptions", "HealthCheckError"),
    "MetricsError": ("oridecon.ai.observability.exceptions", "MetricsError"),
    "TracingError": ("oridecon.ai.observability.exceptions", "TracingError"),
    # --- Health ---
    "AIHealthMonitor": ("oridecon.ai.observability.health", "AIHealthMonitor"),
    # --- Metrics ---
    "AIMetrics": ("oridecon.ai.observability.metrics", "AIMetrics"),
    "track_llm_call": ("oridecon.ai.observability.decorators", "track_llm_call"),
    "track_vector_operation": (
        "oridecon.ai.observability.decorators",
        "track_vector_operation",
    ),
    "track_embedding_operation": (
        "oridecon.ai.observability.decorators",
        "track_embedding_operation",
    ),
    # --- Protocols ---
    "ObservabilityProtocol": (
        "oridecon.ai.observability.protocols",
        "ObservabilityProtocol",
    ),
    "AITracerProtocol": ("oridecon.ai.observability.protocols", "AITracerProtocol"),
    "AIMetricsProtocol": ("oridecon.ai.observability.protocols", "AIMetricsProtocol"),
    "AIHealthMonitorProtocol": (
        "oridecon.ai.observability.protocols",
        "AIHealthMonitorProtocol",
    ),
    # --- Tracing ---
    "AITracer": ("oridecon.ai.observability.tracing", "AITracer"),
    "trace_llm": ("oridecon.ai.observability.decorators", "trace_llm"),
    "trace_rag": ("oridecon.ai.observability.decorators", "trace_rag"),
    "trace_vector": ("oridecon.ai.observability.decorators", "trace_vector"),
    # --- Wrappers ---
    "ObservableLLMClient": (
        "oridecon.ai.observability.wrappers",
        "ObservableLLMClient",
    ),
    "ObservableVectorStore": (
        "oridecon.ai.observability.wrappers",
        "ObservableVectorStore",
    ),
    # --- Contracts Re-exports ---
    "HealthCheckResult": ("oridecon.contracts", "HealthCheckResult"),
    "HealthStatus": ("oridecon.contracts", "HealthStatus"),
}


def __getattr__(name: str) -> Any:
    """Lazy-load symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """Enumerate available attributes for IDE support."""
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = [
    "AIHealthMonitor",
    "AIHealthMonitorProtocol",
    "AIMetrics",
    "AIMetricsProtocol",
    "AIObservabilityStartedHook",
    "AITracer",
    "AITracerProtocol",
    "CallbackManagerImpl",
    "HealthCheckError",
    "HealthCheckResult",
    "HealthCheckRunHook",
    "HealthStatus",
    "LLMCallTracedHook",
    "MetricsError",
    "ObservabilityConfig",
    "ObservabilityError",
    "ObservabilityModule",
    "ObservabilityProtocol",
    "ObservabilityProvider",
    "ObservableLLMClient",
    "ObservableVectorStore",
    "TracingError",
    "trace_llm",
    "trace_rag",
    "trace_vector",
    "track_embedding_operation",
    "track_llm_call",
    "track_vector_operation",
]
