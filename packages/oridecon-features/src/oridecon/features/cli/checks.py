"""CLI health checks for oridecon-features."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oridecon.contracts.core.di import ContainerResolverProtocol


async def check_flag_manager(container: ContainerResolverProtocol) -> dict[str, object]:
    """Check that the feature flag manager is operational.

    Args:
        container: Booted DI container.

    Returns:
        A HealthCheckResult-compatible dict.
    """
    return {
        "status": "healthy",
        "message": "Flag manager health check not yet implemented",
    }
