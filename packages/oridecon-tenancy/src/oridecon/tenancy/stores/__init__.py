"""Stores subpackage — public re-exports."""

from __future__ import annotations

from oridecon.tenancy.stores.memory import InMemoryTenantProvider

__all__ = [
    "InMemoryTenantProvider",
]
