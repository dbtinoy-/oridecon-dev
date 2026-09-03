"""CLI shell context factories for oridecon-resilience."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from oridecon.contracts.infra.resilience.protocols import CircuitBreakerProtocol

if TYPE_CHECKING:
    from oridecon.contracts.core.di import ContainerResolverProtocol


async def provide_resilience_pipeline(
    container: ContainerResolverProtocol,
) -> CircuitBreakerProtocol:
    """Provide the resilience pipeline for interactive shell use.

    Args:
        container: Booted DI container.

    Returns:
        The resolved resilience pipeline instance.
    """
    return cast(
        "CircuitBreakerProtocol",
        await container.resolve(CircuitBreakerProtocol),
    )
