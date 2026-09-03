"""CLI health checks for oridecon-nosql."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oridecon.contracts.core.di import ContainerResolverProtocol


async def check_nosql_connection(
    container: ContainerResolverProtocol,
) -> dict[str, object]:
    """Verify NoSQL document store connectivity.

    Args:
        container: Booted DI container.

    Returns:
        A HealthCheckResult-compatible dict.
    """
    return {"status": "ok", "message": "NoSQL health check not yet implemented"}
