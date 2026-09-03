"""No-op observability provider registered by the Oridecon core framework."""

from __future__ import annotations

from oridecon.contracts.core.di import (
    ContainerRegistrarProtocol,
    ContainerResolverProtocol,
)
from oridecon.contracts.core.health import HealthCheckProtocol
from oridecon.contracts.observability.metrics import (
    HealthCheckRegistryProtocol,
    MetricsFactoryProtocol,
    MetricsRecorderProtocol,
)
from oridecon.contracts.observability.metrics import (
    MetricsCollectorProtocol as MetricsCollectorProtocol,
)
from oridecon.contracts.observability.tracing import TracerProtocol
from oridecon.di.provider import Provider, ProviderPriority
from oridecon.logging import get_logger
from oridecon.observability.core import (
    NoOpHealthCheckRegistry,
    NoOpMetricsCollector,
    NoOpTracer,
)

_logger = get_logger(__name__)


class ObservabilityProvider(Provider):
    """Provides observability: metrics, tracing, and health checks.

    Registers lightweight no-op stubs for every observability contract so
    that application code can always resolve ``MetricsCollectorProtocol``,
    ``TracerProtocol``, and ``HealthCheckRegistryProtocol`` via DI — even
    when ``oridecon-monitor`` is not installed.

    When ``oridecon-monitor`` **is** installed, its ``MonitorProvider`` runs
    at a higher priority and **overrides** these registrations with the full
    implementations.  This provider must not import from ``oridecon.monitor``
    directly; doing so would violate the core ↔ extension hierarchy.
    """

    name = "observability"
    priority = ProviderPriority.INFRASTRUCTURE

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        """Register no-op observability stubs into the container.

        ``oridecon-monitor``'s own provider will override these at its
        higher priority if the package is present.
        """
        _logger.debug(
            "observability.noop_registered",
            message=(
                "Registering no-op observability stubs. Install oridecon-monitor "
                "and add MonitorProvider to override with full implementations."
            ),
        )
        # 1. Metrics
        collector = NoOpMetricsCollector()
        container.singleton(MetricsCollectorProtocol, collector)
        container.singleton(MetricsRecorderProtocol, collector)
        container.singleton(MetricsFactoryProtocol, collector)

        # 2. Tracing
        container.singleton(TracerProtocol, NoOpTracer())

        # 3. Health
        registry = NoOpHealthCheckRegistry()
        container.singleton(HealthCheckRegistryProtocol, registry)
        container.singleton(HealthCheckProtocol, registry)

    async def boot(self, container: ContainerResolverProtocol) -> None:
        """No boot-time work required for the observability module."""

    async def shutdown(self) -> None:
        """No resources to release for the observability module."""


__all__ = ["ObservabilityProvider"]
