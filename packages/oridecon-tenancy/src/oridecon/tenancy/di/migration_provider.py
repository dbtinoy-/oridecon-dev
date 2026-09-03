"""Migration sub-provider — registers the migration service and its dependencies."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.di.provider import Provider
from oridecon.tenancy.migration import TenantMigrationService
from oridecon.tenancy.migration.copy import RowToSchemaCopy
from oridecon.tenancy.migration.write_pause import WritePauseRegistry

if TYPE_CHECKING:
    from oridecon.contracts.core.di import (
        BootContainerProtocol,
        ContainerRegistrarProtocol,
    )
    from oridecon.di.resolution.resolver import ServiceResolver


class TenantMigrationProvider(Provider):
    """Registers the tenant migration service and write-pause registry.

    Expects the following dependencies to already be bound in the container:

    - ``TenantProviderProtocol``
    - ``IsolationStrategyRegistry``
    - ``TenantConfigService``
    - ``ContentCheckpointStoreProtocol``
    - ``DomainEventPublisherProtocol`` (optional)
    - ``DatabaseProviderProtocol`` (optional)

    Usage::

        from oridecon.tenancy.di.migration_provider import TenantMigrationProvider

        provider = TenantMigrationProvider()
    """

    name = "tenant_migration"

    def __init__(self) -> None:
        from oridecon.contracts.core.provider import ProviderPriority

        super().__init__()
        self.priority = ProviderPriority.APPLICATION

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        """Register write-pause registry and migration service.

        Args:
            container: The DI container registrar.
        """
        write_pause = WritePauseRegistry()
        container.singleton(WritePauseRegistry, write_pause)

        copy_strategy = RowToSchemaCopy()
        container.singleton(RowToSchemaCopy, copy_strategy)

        async def _service_factory(
            resolver: ServiceResolver,
        ) -> TenantMigrationService:
            from oridecon.contracts.tenancy.protocols import (
                TenantProviderProtocol,
            )
            from oridecon.contracts.workflow.content_checkpoint import (
                ContentCheckpointStoreProtocol,
            )
            from oridecon.tenancy.config_overrides.service import (
                TenantConfigService,
            )
            from oridecon.tenancy.isolation.registry import (
                IsolationStrategyRegistry,
            )

            tenant_provider = await resolver.resolve(TenantProviderProtocol)
            isolation_registry = await resolver.resolve(IsolationStrategyRegistry)
            config_service = await resolver.resolve(TenantConfigService)
            write_pause = await resolver.resolve(WritePauseRegistry)
            copy_strategy = await resolver.resolve(RowToSchemaCopy)

            checkpoint_store = await resolver.resolve(ContentCheckpointStoreProtocol)

            try:
                from oridecon.contracts.events import EventBusProtocol

                event_bus = await resolver.resolve(EventBusProtocol)
            except Exception:
                event_bus = None

            return TenantMigrationService(
                tenant_provider=tenant_provider,
                isolation_registry=isolation_registry,
                config_service=config_service,
                write_pause_registry=write_pause,
                checkpoint_store=checkpoint_store,
                copy_strategy=copy_strategy,
                event_bus=event_bus,
            )

        container.singleton(TenantMigrationService, factory=_service_factory)

    async def boot(self, container: BootContainerProtocol) -> None:
        """Wire the migration service.

        Args:
            container: The DI container for boot phase.
        """

    async def shutdown(self) -> None:
        """No-op shutdown."""


__all__ = ["TenantMigrationProvider"]
