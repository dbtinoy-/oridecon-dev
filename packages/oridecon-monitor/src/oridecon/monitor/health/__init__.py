"""Unified Health Check System."""

from __future__ import annotations

from oridecon.contracts.core import HealthCheckResult, HealthStatus
from oridecon.contracts.core.health import HealthCheckCategory
from oridecon.monitor.health.base import HealthCheck
from oridecon.monitor.health.cached import CachedHealthChecker
from oridecon.monitor.health.checker import HealthChecker, health_checker
from oridecon.monitor.health.checker_registry import HealthCheckerRegistry
from oridecon.monitor.health.functions import FunctionHealthCheck
from oridecon.monitor.health.registry import HealthCheckRegistry

__all__ = [
    "CachedHealthChecker",
    "FunctionHealthCheck",
    "HealthCheck",
    "HealthCheckCategory",
    "HealthCheckRegistry",
    "HealthCheckResult",
    "HealthChecker",
    "HealthCheckerRegistry",
    "HealthStatus",
    "health_checker",
]
