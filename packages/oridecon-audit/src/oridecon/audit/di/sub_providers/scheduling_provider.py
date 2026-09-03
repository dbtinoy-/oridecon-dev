"""Scheduling DI sub-provider: registers AuditVerifierSchedulerProtocol."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.contracts.core.di import (
    BootContainerProtocol,
    ContainerRegistrarProtocol,
)
from oridecon.contracts.core.provider import ProviderPriority
from oridecon.contracts.observability.audit import AuditVerifierSchedulerProtocol
from oridecon.di.provider import Provider

if TYPE_CHECKING:
    from oridecon.audit.config import AuditConfig

__all__ = ["AuditSchedulingProvider"]


class AuditSchedulingProvider(Provider):
    """Registers AuditVerifierSchedulerProtocol → AuditScheduler.

    Args:
        config: Audit configuration. Defaults to AuditConfig() if not provided.
    """

    def __init__(self, config: AuditConfig | None = None) -> None:
        super().__init__(
            name="audit_scheduling", priority=ProviderPriority.INFRASTRUCTURE
        )
        self._config = config

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        """Bind AuditVerifierSchedulerProtocol to AuditScheduler."""
        from oridecon.audit.scheduling.scheduler import AuditScheduler

        # AuditScheduler auto-injects AuditVerifierProtocol + AuditConfig from container
        container.singleton(AuditVerifierSchedulerProtocol, AuditScheduler)

    async def boot(self, container: BootContainerProtocol) -> None:
        """No boot-time work required."""
