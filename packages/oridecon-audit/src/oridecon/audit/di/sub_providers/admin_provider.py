"""Admin DI provider: registers AuditAdminContributor."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.contracts.core.di import (
    BootContainerProtocol,
    ContainerRegistrarProtocol,
)
from oridecon.contracts.core.provider import ProviderPriority
from oridecon.di.provider import Provider

if TYPE_CHECKING:
    from oridecon.audit.config import AuditConfig

__all__ = ["AuditAdminProvider"]


class AuditAdminProvider(Provider):
    """Registers AuditAdminContributor for admin panel integration.

    Args:
        config: Audit configuration.
    """

    def __init__(self, config: AuditConfig | None = None) -> None:
        super().__init__(name="audit_admin", priority=ProviderPriority.LOW)
        self._config = config

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        """Bind admin contributor singleton."""
        from oridecon.audit.admin.contributor import AuditAdminContributor

        container.singleton(AuditAdminContributor)

    async def boot(self, container: BootContainerProtocol) -> None:
        pass
