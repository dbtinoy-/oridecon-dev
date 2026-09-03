"""Admin CQRS message types.

Commands are defined canonically in ``oridecon.admin.cqrs.commands``.
Queries are defined in ``oridecon.admin.cqrs.queries``.

The framework command and query buses (``CommandBusImpl`` / ``QueryBusImpl``)
live in ``oridecon-events`` and satisfy ``CommandBusProtocol`` /
``QueryBusProtocol`` from ``oridecon-contracts``.  There are no admin-specific
bus reimplementations.
"""

from __future__ import annotations

from oridecon.admin.cqrs.commands import AdminCommand
from oridecon.admin.cqrs.queries import AdminQuery

__all__ = ["AdminCommand", "AdminQuery"]
