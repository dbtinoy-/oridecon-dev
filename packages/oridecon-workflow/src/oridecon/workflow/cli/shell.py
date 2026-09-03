"""CLI shell context factories for oridecon-workflow."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.workflow.core.engine import (  # type: ignore[import-untyped]
    WorkflowEngine,
)

if TYPE_CHECKING:
    from oridecon.contracts.core.di import ContainerResolverProtocol


async def provide_workflow_engine(
    container: ContainerResolverProtocol,
) -> WorkflowEngine:
    """Provide workflow engine for interactive shell use.

    Args:
        container: Booted DI container.

    Returns:
        The resolved workflow engine instance.
    """
    return await container.resolve(WorkflowEngine)
