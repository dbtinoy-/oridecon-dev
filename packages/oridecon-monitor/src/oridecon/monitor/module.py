"""Monitoring and observability module for dependency injection."""

from __future__ import annotations

from typing import Any

from oridecon.contracts.observability.metrics import (
    HealthCheckRegistryProtocol,
    MetricsFactoryProtocol,
    MetricsRecorderProtocol,
)
from oridecon.contracts.observability.metrics import (
    MetricsCollectorProtocol as MetricsCollectorProtocol,
)
from oridecon.contracts.observability.tracing import TracerProtocol
from oridecon.di.module import DynamicModule, Module, module


@module()
class MonitorModule(Module):
    """Metrics collection, distributed tracing, health checks, and profiling.

    Call :meth:`configure` to configure the monitoring subsystem.

    Usage (no-op / development)::

        from oridecon.monitor.backends.noop import NoopMetricsBackend

        @module(
            imports=[MonitorModule.configure(backend=NoopMetricsBackend())]
        )
        class AppModule(Module):
            pass

    Usage (Prometheus)::

        from oridecon.monitor.backends.exporters.prometheus import PrometheusMetricsExporter
        from oridecon.monitor.backends.prometheus import PrometheusBackend

        @module(
            imports=[MonitorModule.configure(backend=PrometheusBackend())]
        )
        class AppModule(Module):
            pass
    """

    @classmethod
    def configure(cls, backend: Any = None, config: Any | None = None) -> DynamicModule:
        """Create a MonitorModule with explicit configuration.

        Args:
            backend: ``MetricsBackendProtocol`` implementation.
                Defaults to ``NoOpMetricsBackend`` when omitted.
            config: ``MonitorConfig`` for advanced tracing and profiling settings.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.monitor.di.provider import MonitorProvider
        from oridecon.monitor.health import HealthCheckerRegistry, HealthCheckRegistry
        from oridecon.monitor.services.core import ObservabilityService
        from oridecon.observability.core import NoOpMetricsBackend

        if backend is None:
            backend = NoOpMetricsBackend()

        return DynamicModule(
            module=cls,
            providers=[MonitorProvider(backend=backend, config=config)],
            exports=[
                MetricsCollectorProtocol,
                MetricsRecorderProtocol,
                MetricsFactoryProtocol,
                TracerProtocol,
                HealthCheckRegistryProtocol,
                HealthCheckerRegistry,
                HealthCheckRegistry,
                ObservabilityService,
            ],
        )

    @classmethod
    def with_slo(cls, backend: Any = None, config: Any | None = None) -> DynamicModule:
        """Return a MonitorModule that also exports SLO types.

        Args:
            backend: ``MetricsBackendProtocol`` implementation.
            config: ``MonitorConfig`` for advanced settings.
        """
        from oridecon.monitor.di.provider import MonitorProvider
        from oridecon.monitor.health import HealthCheckerRegistry, HealthCheckRegistry
        from oridecon.monitor.services.core import ObservabilityService
        from oridecon.monitor.slo.monitor import SLOMonitor
        from oridecon.monitor.slo.worker import SLOEvaluationWorker
        from oridecon.observability.core import NoOpMetricsBackend

        if backend is None:
            backend = NoOpMetricsBackend()

        return DynamicModule(
            module=cls,
            providers=[MonitorProvider(backend=backend, config=config)],
            exports=[
                MetricsCollectorProtocol,
                MetricsRecorderProtocol,
                MetricsFactoryProtocol,
                TracerProtocol,
                HealthCheckRegistryProtocol,
                HealthCheckerRegistry,
                HealthCheckRegistry,
                ObservabilityService,
                SLOMonitor,
                SLOEvaluationWorker,
            ],
        )

    @classmethod
    def stub(cls, config: Any = None) -> DynamicModule:
        """Return a no-op MonitorModule for unit testing.

        Registers a :class:`~oridecon.monitor.noop.NoOpMetricsBackend`
        that discards all metrics. No external telemetry systems are
        connected.

        Args:
            config: Optional test configuration override.

        Returns:
            A DynamicModule with noop metrics and tracing.
        """
        from oridecon.monitor.di.provider import MonitorProvider
        from oridecon.monitor.health import HealthCheckerRegistry, HealthCheckRegistry
        from oridecon.monitor.services.core import ObservabilityService
        from oridecon.observability.core import NoOpMetricsBackend

        return DynamicModule(
            module=cls,
            providers=[MonitorProvider(backend=NoOpMetricsBackend())],
            exports=[
                MetricsCollectorProtocol,
                MetricsRecorderProtocol,
                MetricsFactoryProtocol,
                TracerProtocol,
                HealthCheckRegistryProtocol,
                HealthCheckerRegistry,
                HealthCheckRegistry,
                ObservabilityService,
            ],
        )


__all__ = ["MonitorModule"]
