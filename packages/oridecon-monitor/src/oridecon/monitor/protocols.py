"""Public protocol surface for ``oridecon.monitor``."""

from __future__ import annotations

from oridecon.contracts.observability.metrics import (
    AlertDispatcherProtocol,
    MetricProtocol,
    MetricsBackendProtocol,
    MetricsCollectorProtocol,
)
from oridecon.contracts.observability.tracing import TracerProtocol
from oridecon.contracts.observability.tracing import TracerProtocol as TraceProvider
from oridecon.monitor.types import HealthCheckerProtocol

__all__ = [
    "AlertDispatcherProtocol",
    "HealthCheckerProtocol",
    "MetricProtocol",
    "MetricsBackendProtocol",
    "MetricsCollectorProtocol",
    "TraceProvider",
    "TracerProtocol",
]
