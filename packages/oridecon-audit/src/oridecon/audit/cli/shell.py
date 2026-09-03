"""CLI shell context factories for oridecon-audit."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.audit.logging.logger import AuditLogger

if TYPE_CHECKING:
    from oridecon.contracts.core.di import ContainerResolverProtocol


async def provide_audit_logger(container: ContainerResolverProtocol) -> AuditLogger:
    """Provide audit logger for interactive shell use.

    Args:
        container: Booted DI container.

    Returns:
        The resolved audit logger instance.
    """
    return await container.resolve(AuditLogger)
