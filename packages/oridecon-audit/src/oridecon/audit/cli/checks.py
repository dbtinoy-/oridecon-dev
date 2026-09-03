"""CLI health checks for oridecon-audit."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oridecon.contracts.core.di import ContainerResolverProtocol


async def check_audit_store(container: ContainerResolverProtocol) -> dict[str, object]:
    """Verify audit log store is operational.

    Args:
        container: Booted DI container.

    Returns:
        A HealthCheckResult-compatible dict.
    """
    return {"status": "ok", "message": "Audit store health check not yet implemented"}
