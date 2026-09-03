"""CQRS marker protocols for the admin system."""

from __future__ import annotations

from oridecon.contracts.admin.cqrs.command import AdminCommand
from oridecon.contracts.admin.cqrs.query import AdminQuery

__all__ = ["AdminCommand", "AdminQuery"]
