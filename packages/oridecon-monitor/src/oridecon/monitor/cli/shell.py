"""CLI shell context factories for oridecon-monitor."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.monitor.backends.base import (  # type: ignore[import-untyped]
    MetricsBackend,
)

if TYPE_CHECKING:
    from oridecon.contracts.core.di import ContainerResolverProtocol


async def provide_metrics(container: ContainerResolverProtocol) -> MetricsBackend:
    """Provide metrics backend for interactive shell use.

    Args:
        container: Booted DI container.

    Returns:
        The resolved metrics backend instance.
    """
    return await container.resolve(MetricsBackend)
