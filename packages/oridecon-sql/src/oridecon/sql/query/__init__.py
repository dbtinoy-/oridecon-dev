"""Query building and compilation utilities.

`oridecon.sql.query` now hosts both SQL query layers:

1. The domain-level immutable query model (`Query`, `QueryBuilder`,
   `SearchQueryBuilder`, `PredicateCompiler`)
2. The SQL-rendering layer (`AsyncQueryBuilder`, `Operator`, and related SQL
   builder types)

The domain layer expresses *what* to query. The SQL builder layer renders
that intent into dialect-specific SQL for PostgreSQL, MySQL, and SQLite.
"""

from __future__ import annotations

from oridecon.sql.query.admin_builder import SqlQueryBuilder
from oridecon.sql.query.builder import Query, QueryBuilder, SearchQueryBuilder
from oridecon.sql.query.compiler import Predicate, PredicateCompiler
from oridecon.sql.query.cursor import CursorCodec
from oridecon.sql.query.operators import Operator, QueryOperator, QueryOperatorRegistry
from oridecon.sql.query.sql_builder import AsyncQueryBuilder, SQLDialect

__all__ = [
    "AsyncQueryBuilder",
    "CursorCodec",
    "Operator",
    "Predicate",
    "PredicateCompiler",
    "Query",
    "QueryBuilder",
    "QueryOperator",
    "QueryOperatorRegistry",
    "SQLDialect",
    "SearchQueryBuilder",
    "SqlQueryBuilder",
]
