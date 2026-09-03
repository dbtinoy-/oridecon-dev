"""Oridecon Monitor Package - Observability and monitoring"""

from __future__ import annotations

import importlib.metadata

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from typing import TYPE_CHECKING, Any

from oridecon.monitor.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.contracts.observability.metrics import (
        AlertDispatcherProtocol,
        MetricProtocol,
        MetricsBackendProtocol,
    )
    from oridecon.contracts.observability.tracing import TracerProtocol
    from oridecon.contracts.observability.tracing import (
        TracerProtocol as TraceProvider,
    )
    from oridecon.logging import (
        Logger,
        configure_logging,
        get_logger,
    )
    from oridecon.monitor.alerts import LoggingAlertDispatcher
    from oridecon.monitor.backends import (
        OpenTelemetryBackend,
        PrometheusBackend,
    )
    from oridecon.monitor.backends.exporters import PrometheusMetricsExporter
    from oridecon.monitor.backends.exporters.otel_registry import (
        ConsoleMetricsExporterHandler,
        ConsoleTracingExporterHandler,
        MetricsExporterRegistry,
        OTLPMetricsExporterHandler,
        OTLPTracingExporterHandler,
        TracingExporterRegistry,
    )
    from oridecon.monitor.config import (
        BackendType,
        ErrorTrackingConfig,
        HealthCheckConfig,
        MetricsConfig,
        MonitorConfig,
        OpenTelemetryConfig,
        PrometheusConfig,
        SamplerType,
        TracingConfig,
    )
    from oridecon.monitor.decorators import monitor
    from oridecon.monitor.di.factories import (
        create_opentelemetry_provider,
        create_prometheus_provider,
        create_provider_from_config,
    )
    from oridecon.monitor.di.provider import (
        MonitorProvider,
    )
    from oridecon.monitor.di.sub_providers.observability import ObservabilityProvider
    from oridecon.monitor.error_tracking import (
        ErrorTrackerProtocol,
        NullErrorTracker,
        SentryErrorTracker,
        setup_error_tracking,
    )
    from oridecon.monitor.exceptions import (
        BackendNotAvailableError,
        InvalidMetricError,
        MetricNotFoundError,
        MonitorError,
        SpanError,
    )
    from oridecon.monitor.health import (
        FunctionHealthCheck,
        HealthCheck,
        HealthCheckCategory,
        HealthChecker,
        HealthCheckerRegistry,
        HealthCheckRegistry,
        HealthCheckResult,
        HealthStatus,
        health_checker,
    )
    from oridecon.monitor.instrumentation.database import instrument_database
    from oridecon.monitor.instrumentation.decorators import (
        metered,
        traced,
    )
    from oridecon.monitor.instrumentation.http import OTelMiddleware
    from oridecon.monitor.instrumentation.messaging import (
        inject_trace_context,
        trace_consume,
        trace_publish,
    )
    from oridecon.monitor.metrics import (
        BufferedMetricEntry,
        BufferedMetricRecorder,
        Counter,
        Gauge,
        Histogram,
        MetricsCollectorProtocol,
        Summary,
    )
    from oridecon.monitor.middleware import (
        HealthCheckProvider,
        PrometheusMiddleware,
    )
    from oridecon.monitor.profiling import (
        FunctionProfileResult,
        PerformanceMetrics,
        PerformanceMonitor,
        PerformanceMonitorConfig,
        PerformanceMonitorError,
        PerformanceMonitorState,
        PerformanceSnapshot,
        get_performance_summary,
        monitor_async_operation,
        profile_async_function,
    )
    from oridecon.monitor.services.core import (
        MetricProxy,
        ObservabilityService,
    )
    from oridecon.monitor.slo.monitor import SLOMonitor
    from oridecon.monitor.slo.objective import (
        SLO,
        SLOViolation,
    )
    from oridecon.monitor.tracing import (
        ConsoleSpanExporter,
        InMemoryTraceProvider,
        Span,
        SpanContext,
        SpanExporter,
        SpanKind,
        SpanStatus,
        Tracer,
    )
    from oridecon.monitor.types import HealthCheckerProtocol, MetricValue
    from oridecon.observability.core import (
        NoOpHealthCheckRegistry,
        NoOpMetricsCollector,
        NoOpSpan,
        NoOpTracer,
    )


_LAZY_IMPORTS = {
    # Module
    "MonitorModule": "oridecon.monitor.module",
    # Config
    "BackendType": "oridecon.monitor.config",
    "SamplerType": "oridecon.monitor.config",
    "MetricsConfig": "oridecon.monitor.config",
    "TracingConfig": "oridecon.monitor.config",
    "HealthCheckConfig": "oridecon.monitor.config",
    "OpenTelemetryConfig": "oridecon.monitor.config",
    "PrometheusConfig": "oridecon.monitor.config",
    "MonitorConfig": "oridecon.monitor.config",
    "ErrorTrackingConfig": "oridecon.monitor.config",
    # Error tracking
    "ErrorTrackerProtocol": "oridecon.monitor.error_tracking",
    "NullErrorTracker": "oridecon.monitor.error_tracking",
    "SentryErrorTracker": "oridecon.monitor.error_tracking",
    "setup_error_tracking": "oridecon.monitor.error_tracking",
    # Protocols
    "MetricProtocol": "oridecon.contracts.observability",
    "TraceProvider": "oridecon.contracts.observability",
    "MetricsBackendProtocol": "oridecon.contracts.observability",
    "AlertDispatcherProtocol": "oridecon.contracts.observability",
    # Types
    "MetricValue": "oridecon.monitor.types",
    "HealthCheckerProtocol": "oridecon.monitor.types",
    "SpanKind": "oridecon.monitor.tracing",
    "SpanStatus": "oridecon.monitor.tracing",
    # Exceptions
    "MonitorError": "oridecon.monitor.exceptions",
    "BackendNotAvailableError": "oridecon.monitor.exceptions",
    "MetricNotFoundError": "oridecon.monitor.exceptions",
    "InvalidMetricError": "oridecon.monitor.exceptions",
    "SpanError": "oridecon.monitor.exceptions",
    # Metrics
    "MetricsCollectorProtocol": "oridecon.monitor.metrics",
    "Counter": "oridecon.monitor.metrics",
    "Gauge": "oridecon.monitor.metrics",
    "Histogram": "oridecon.monitor.metrics",
    "Summary": "oridecon.monitor.metrics",
    "BufferedMetricEntry": "oridecon.monitor.metrics",
    "BufferedMetricRecorder": "oridecon.monitor.metrics",
    # Tracing
    "Tracer": "oridecon.monitor.tracing",
    "Span": "oridecon.monitor.tracing",
    "SpanContext": "oridecon.monitor.tracing",
    "SpanExporter": "oridecon.monitor.tracing",
    "ConsoleSpanExporter": "oridecon.monitor.tracing",
    "InMemoryTraceProvider": "oridecon.monitor.tracing",
    # Logging
    "Logger": "oridecon.logging",
    "get_logger": "oridecon.logging",
    "configure_logging": "oridecon.logging",
    # Backends
    "OpenTelemetryBackend": "oridecon.monitor.backends",
    "PrometheusBackend": "oridecon.monitor.backends",
    # Middleware
    "PrometheusMiddleware": "oridecon.monitor.middleware",
    "HealthCheckProvider": "oridecon.monitor.middleware",
    # Health
    "HealthStatus": "oridecon.monitor.health",
    "HealthCheck": "oridecon.monitor.health",
    "HealthCheckCategory": "oridecon.monitor.health",
    "HealthCheckResult": "oridecon.monitor.health",
    "HealthCheckRegistry": "oridecon.monitor.health",
    "HealthChecker": "oridecon.monitor.health",
    "HealthCheckerRegistry": "oridecon.monitor.health",
    "FunctionHealthCheck": "oridecon.monitor.health",
    "health_checker": "oridecon.monitor.health",
    # NoOp stubs
    "NoOpSpan": "oridecon.observability.core",
    "NoOpTracer": "oridecon.observability.core",
    "NoOpMetricsCollector": "oridecon.observability.core",
    "NoOpHealthCheckRegistry": "oridecon.observability.core",
    # Observability service
    "ObservabilityService": "oridecon.monitor.services.core",
    "MetricProxy": "oridecon.monitor.services.core",
    # Decorators
    "metered": "oridecon.monitor.instrumentation.decorators",
    "traced": "oridecon.monitor.instrumentation.decorators",
    "monitor": "oridecon.monitor.decorators",
    # Provider
    "ObservabilityProvider": "oridecon.monitor.di.sub_providers.observability",
    "MonitorProvider": "oridecon.monitor.di.provider",
    "create_opentelemetry_provider": "oridecon.monitor.di.provider",
    "create_prometheus_provider": "oridecon.monitor.di.provider",
    "create_provider_from_config": "oridecon.monitor.di.provider",
    "PrometheusMetricsExporter": "oridecon.monitor.backends.exporters",
    "ConsoleTracingExporterHandler": "oridecon.monitor.backends.exporters.otel_registry",
    "OTLPTracingExporterHandler": "oridecon.monitor.backends.exporters.otel_registry",
    "ConsoleMetricsExporterHandler": "oridecon.monitor.backends.exporters.otel_registry",
    "OTLPMetricsExporterHandler": "oridecon.monitor.backends.exporters.otel_registry",
    "TracingExporterRegistry": "oridecon.monitor.backends.exporters.otel_registry",
    "MetricsExporterRegistry": "oridecon.monitor.backends.exporters.otel_registry",
    # Instrumentation
    "instrument_database": "oridecon.monitor.instrumentation.database",
    "OTelMiddleware": "oridecon.monitor.instrumentation.http",
    "trace_publish": "oridecon.monitor.instrumentation.messaging",
    "trace_consume": "oridecon.monitor.instrumentation.messaging",
    "inject_trace_context": "oridecon.monitor.instrumentation.messaging",
    # Profiling
    "PerformanceMonitor": "oridecon.monitor.profiling",
    "PerformanceMonitorConfig": "oridecon.monitor.profiling",
    "PerformanceMonitorError": "oridecon.monitor.profiling",
    "PerformanceMonitorState": "oridecon.monitor.profiling",
    "PerformanceMetrics": "oridecon.monitor.profiling",
    "PerformanceSnapshot": "oridecon.monitor.profiling",
    "FunctionProfileResult": "oridecon.monitor.profiling",
    "get_performance_summary": "oridecon.monitor.profiling",
    "monitor_async_operation": "oridecon.monitor.profiling",
    "profile_async_function": "oridecon.monitor.profiling",
    # SLO
    "SLO": "oridecon.monitor.slo.objective",
    "SLOViolation": "oridecon.monitor.slo.objective",
    "SLOMonitor": "oridecon.monitor.slo.monitor",
    # Alerts
    "LoggingAlertDispatcher": "oridecon.monitor.alerts",
    # Hooks
    "AlertFiredHook": "oridecon.monitor.hooks",
    "HealthCheckRunHook": "oridecon.monitor.hooks",
    "MetricRecordedHook": "oridecon.monitor.hooks",
}


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib

        module_path = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__} has no attribute {name}")


def __dir__() -> list[str]:
    return [*list(_LAZY_IMPORTS.keys()), "__version__"]


__all__ = list(_LAZY_IMPORTS.keys())
