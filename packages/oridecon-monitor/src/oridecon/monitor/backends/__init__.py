"""Backend implementations module.

This module provides various monitoring backend implementations
including OpenTelemetry and Prometheus.
"""

from __future__ import annotations

from oridecon.monitor.backends.opentelemetry import OpenTelemetryBackend
from oridecon.monitor.backends.prometheus import PrometheusBackend

__all__ = [
    "OpenTelemetryBackend",
    "PrometheusBackend",
]
