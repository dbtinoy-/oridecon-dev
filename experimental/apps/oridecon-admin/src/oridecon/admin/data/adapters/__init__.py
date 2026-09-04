"""Data source adapters for Oridecon Admin."""

from __future__ import annotations

from oridecon.admin.data.adapters.api_adapter import APIDataSource
from oridecon.admin.data.adapters.memory_adapter import InMemoryDataSource
from oridecon.admin.data.adapters.repository import RepositoryDataSource

__all__ = [
    "APIDataSource",
    "InMemoryDataSource",
    "RepositoryDataSource",
]
