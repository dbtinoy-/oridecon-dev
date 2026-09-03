"""Database provider protocols.

These protocols define the contract for database implementations,
enabling swappable database backends (PostgreSQL, MySQL, SQLite, MongoDB).
"""

from __future__ import annotations

from oridecon.contracts.data.sql.database._connection import ConnectionProtocol
from oridecon.contracts.data.sql.database._managers import (
    CrudOperationsProtocol,
    DatabaseMetricsProtocol,
    HealthMonitorProtocol,
    SchemaManagerProtocol,
    TransactionManagerProtocol,
)
from oridecon.contracts.data.sql.database._migration import (
    MigrationManagerProtocol,
    MigrationRecord,
)
from oridecon.contracts.data.sql.database._pool import ConnectionPoolProtocol
from oridecon.contracts.data.sql.database._provider import DatabaseProviderProtocol
from oridecon.contracts.data.sql.database._results import (
    DeleteResult,
    InsertResult,
    IsolationLevel,
    QueryResult,
    UpdateResult,
)

__all__ = [
    "ConnectionPoolProtocol",
    "ConnectionProtocol",
    "CrudOperationsProtocol",
    "DatabaseMetricsProtocol",
    "DatabaseProviderProtocol",
    "DeleteResult",
    "HealthMonitorProtocol",
    "InsertResult",
    "IsolationLevel",
    "MigrationManagerProtocol",
    "MigrationRecord",
    "QueryResult",
    "SchemaManagerProtocol",
    "TransactionManagerProtocol",
    "UpdateResult",
]
