"""Data layer for Oridecon Admin."""

from __future__ import annotations

from oridecon.admin.data.data_source import IDataSource, QueryResult
from oridecon.admin.data.paged_result import PagedResult
from oridecon.admin.data.query import FilterCondition, FilterOperator, QuerySpec
from oridecon.admin.data.read_only import ReadOnlyDataSource, ReadOnlyError

__all__ = [
    "FilterCondition",
    "FilterOperator",
    "IDataSource",
    "PagedResult",
    "QueryResult",
    "QuerySpec",
    "ReadOnlyDataSource",
    "ReadOnlyError",
]
