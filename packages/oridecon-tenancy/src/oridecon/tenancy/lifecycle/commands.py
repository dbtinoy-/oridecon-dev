"""Lifecycle commands — re-export from contracts."""

from __future__ import annotations

from oridecon.contracts.tenancy.commands import CreateTenantCommand, UpdateTenantCommand

__all__ = [
    "CreateTenantCommand",
    "UpdateTenantCommand",
]
