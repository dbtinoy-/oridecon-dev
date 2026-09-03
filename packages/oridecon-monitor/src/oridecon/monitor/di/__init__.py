"""Framework integration for oridecon-monitor."""

from __future__ import annotations

from oridecon.monitor.di.factories import (
    create_opentelemetry_provider,
    create_prometheus_provider,
    create_provider_from_config,
)
from oridecon.monitor.di.provider import MonitorProvider
from oridecon.monitor.di.sub_providers.observability import ObservabilityProvider

__all__ = [
    "MonitorProvider",
    "ObservabilityProvider",
    "create_opentelemetry_provider",
    "create_prometheus_provider",
    "create_provider_from_config",
]
