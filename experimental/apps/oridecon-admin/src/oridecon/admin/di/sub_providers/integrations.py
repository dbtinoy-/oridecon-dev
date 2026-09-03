"""DI sub-provider that registers optional integration adapters.

Each optional extension (cache, tasks, search, resilience, storage, features,
monitor) has a corresponding ``*Integration`` class in
``oridecon.admin.integrations.*``.  This sub-provider instantiates them during
``register()``, skipping silently when the underlying extension is absent.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from oridecon.admin.config import AdminIntegrationsConfig
from oridecon.contracts.core.health import HealthCheckResult, HealthStatus

if TYPE_CHECKING:
    from oridecon.contracts.core.di import (
        ContainerRegistrarProtocol,
        ContainerResolverProtocol,
    )


class AdminIntegrationsSubProvider:
    """Registers and manages all optional integration adapters."""

    def __init__(self, config: AdminIntegrationsConfig) -> None:
        self._config = config
        self._sub_integrations: list[Any] = []

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        """Instantiate and register each integration adapter."""
        from oridecon.admin.integrations.cache import CacheIntegration
        from oridecon.admin.integrations.features import FeaturesIntegration
        from oridecon.admin.integrations.monitor import MonitorIntegration
        from oridecon.admin.integrations.resilience import ResilienceIntegration
        from oridecon.admin.integrations.search import SearchIntegration
        from oridecon.admin.integrations.storage import StorageIntegration
        from oridecon.admin.integrations.tasks import TasksIntegration

        integrations: list[Any] = [
            CacheIntegration(self._config.cache),
            TasksIntegration(self._config.tasks),
            SearchIntegration(self._config.search),
            ResilienceIntegration(self._config.resilience),
            StorageIntegration(self._config.storage),
            FeaturesIntegration(self._config.features),
            MonitorIntegration(self._config.monitor),
        ]
        for integ in integrations:
            integ.register(container)
            self._sub_integrations.append(integ)

    async def boot(self, container: ContainerResolverProtocol) -> None:
        """Boot all registered integrations and populate the integration registry."""
        from oridecon.admin.integrations import register as _register_integration

        for integ in self._sub_integrations:
            await integ.boot(container)
            _register_integration(integ.__class__.__name__, integ)

    async def shutdown(self) -> None:
        """Shut down all registered integrations in reverse order."""
        for integ in reversed(self._sub_integrations):
            await integ.shutdown()

    async def health_check(self, timeout: float = 5.0) -> HealthCheckResult:
        """Aggregate health from all integrations."""
        worst = HealthStatus.HEALTHY
        details: dict[str, Any] = {}
        for integ in self._sub_integrations:
            try:
                check = await integ.health_check()
                details[integ.__class__.__name__] = check.get("status", "unknown")
            except Exception as exc:  # noqa: BLE001
                details[integ.__class__.__name__] = "error"
                worst = HealthStatus.DEGRADED
        return HealthCheckResult(
            component="integrations",
            status=worst,
            details=details,
        )


__all__ = ["AdminIntegrationsSubProvider"]
