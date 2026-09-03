"""Lifecycle sub-provider — tenant store, lifecycle service, and provisioner."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.contracts.tenancy.protocols import TenantProviderProtocol
from oridecon.di.provider import Provider
from oridecon.tenancy.config import LifecycleConfig
from oridecon.tenancy.enforcement.validator import TenantValidator
from oridecon.tenancy.isolation.registry import IsolationStrategyRegistry
from oridecon.tenancy.lifecycle.provisioner import TenantProvisioner
from oridecon.tenancy.lifecycle.service import TenantLifecycleService
from oridecon.tenancy.stores.memory import InMemoryTenantProvider

if TYPE_CHECKING:
    from oridecon.contracts.core.di import (
        BootContainerProtocol,
        ContainerRegistrarProtocol,
    )
    from oridecon.di.resolution.resolver import ServiceResolver


class TenantLifecycleProvider(Provider):
    """Registers the tenant store, isolation registry, provisioner, and lifecycle service."""

    name = "tenant_lifecycle"

    def __init__(self, config: LifecycleConfig) -> None:
        """Initialise the provider.

        Args:
            config: Lifecycle configuration.
        """
        super().__init__()
        self._config = config

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        """Register lifecycle bindings.

        Args:
            container: The DI container registrar.
        """
        # Default to in-memory; applications override by binding SQLTenantProvider
        # before this provider runs.
        store = InMemoryTenantProvider()
        container.singleton(TenantProviderProtocol, store)
        container.singleton(InMemoryTenantProvider, store)

        isolation_registry = IsolationStrategyRegistry.with_defaults()
        container.singleton(IsolationStrategyRegistry, isolation_registry)

        async def _provisioner_factory(
            resolver: ServiceResolver,
        ) -> TenantProvisioner:
            registered = await resolver.resolve(IsolationStrategyRegistry)
            strategy = registered.get(self._config.isolation_strategy)
            return TenantProvisioner(
                strategy=strategy,
                auto_provision=self._config.auto_provision_isolation,
            )

        container.singleton(TenantProvisioner, factory=_provisioner_factory)

        async def _lifecycle_service_factory(
            resolver: ServiceResolver,
        ) -> TenantLifecycleService:
            provider = await resolver.resolve(TenantProviderProtocol)
            provisioner = await resolver.resolve(TenantProvisioner)
            validator = await resolver.resolve(TenantValidator)

            # Event bus is optional — provide a no-op if not registered
            try:
                from oridecon.contracts.events import EventBusProtocol

                event_bus = await resolver.resolve(EventBusProtocol)
            except Exception:
                event_bus = _NoOpEventBus()

            return TenantLifecycleService(
                provider=provider,
                provisioner=provisioner,
                event_bus=event_bus,
                validator=validator,
            )

        container.singleton(TenantLifecycleService, factory=_lifecycle_service_factory)

    async def boot(self, container: BootContainerProtocol) -> None:
        """Wire provisioner and lifecycle service.

        Args:
            container: The DI container for boot phase.
        """

    async def shutdown(self) -> None:
        """No-op shutdown."""


class _NoOpEventBus:
    """Fallback no-op event bus when oridecon-events is not registered."""

    async def publish(self, event: object) -> None:
        """Silently discard the event.

        Args:
            event: Any domain event (ignored).
        """


__all__ = ["TenantLifecycleProvider"]
