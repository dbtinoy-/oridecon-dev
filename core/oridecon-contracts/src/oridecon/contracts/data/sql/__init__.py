"""SQL data contracts."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from oridecon.contracts.data.sql.append_log import (
        AppendLogProtocol,
        AppendLogSnapshotStore,
    )
    from oridecon.contracts.data.sql.database import (
        ConnectionPoolProtocol,
        ConnectionProtocol,
        CrudOperationsProtocol,
        DatabaseMetricsProtocol,
        DatabaseProviderProtocol,
        DeleteResult,
        HealthMonitorProtocol,
        InsertResult,
        IsolationLevel,
        MigrationManagerProtocol,
        MigrationRecord,
        QueryResult,
        SchemaManagerProtocol,
        TransactionManagerProtocol,
        UpdateResult,
    )
    from oridecon.contracts.data.sql.mapper import (
        DataMapperProtocol,
        ReadOnlyMapperProtocol,
    )
    from oridecon.contracts.data.sql.migrations import MigrationRunnerProtocol
    from oridecon.contracts.data.sql.query_log import QueryLogEntry, QueryLoggerProtocol
    from oridecon.contracts.data.sql.sql import InvalidIdentifierError, RawSQL
    from oridecon.contracts.data.sql.sql_dialect import (
        DEFAULT_MAX_IDENTIFIER_LENGTH,
        MAX_IDENTIFIER_LENGTHS,
        SQLDialect,
    )
    from oridecon.contracts.data.sql.unit_of_work import UnitOfWorkProtocol

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "DEFAULT_MAX_IDENTIFIER_LENGTH": (
        "oridecon.contracts.data.sql.sql_dialect",
        "DEFAULT_MAX_IDENTIFIER_LENGTH",
    ),
    "MAX_IDENTIFIER_LENGTHS": (
        "oridecon.contracts.data.sql.sql_dialect",
        "MAX_IDENTIFIER_LENGTHS",
    ),
    "AppendLogProtocol": (
        "oridecon.contracts.data.sql.append_log",
        "AppendLogProtocol",
    ),
    "AppendLogSnapshotStore": (
        "oridecon.contracts.data.sql.append_log",
        "AppendLogSnapshotStore",
    ),
    "ConnectionPoolProtocol": (
        "oridecon.contracts.data.sql.database",
        "ConnectionPoolProtocol",
    ),
    "ConnectionProtocol": (
        "oridecon.contracts.data.sql.database",
        "ConnectionProtocol",
    ),
    "CrudOperationsProtocol": (
        "oridecon.contracts.data.sql.database",
        "CrudOperationsProtocol",
    ),
    "DataMapperProtocol": (
        "oridecon.contracts.data.sql.mapper",
        "DataMapperProtocol",
    ),
    "DatabaseMetricsProtocol": (
        "oridecon.contracts.data.sql.database",
        "DatabaseMetricsProtocol",
    ),
    "DatabaseProviderProtocol": (
        "oridecon.contracts.data.sql.database",
        "DatabaseProviderProtocol",
    ),
    "DeleteResult": (
        "oridecon.contracts.data.sql.database",
        "DeleteResult",
    ),
    "HealthMonitorProtocol": (
        "oridecon.contracts.data.sql.database",
        "HealthMonitorProtocol",
    ),
    "InsertResult": (
        "oridecon.contracts.data.sql.database",
        "InsertResult",
    ),
    "InvalidIdentifierError": (
        "oridecon.contracts.data.sql.sql",
        "InvalidIdentifierError",
    ),
    "IsolationLevel": (
        "oridecon.contracts.data.sql.database",
        "IsolationLevel",
    ),
    "MigrationManagerProtocol": (
        "oridecon.contracts.data.sql.database",
        "MigrationManagerProtocol",
    ),
    "MigrationRecord": (
        "oridecon.contracts.data.sql.database",
        "MigrationRecord",
    ),
    "MigrationRunnerProtocol": (
        "oridecon.contracts.data.sql.migrations",
        "MigrationRunnerProtocol",
    ),
    "QueryLogEntry": (
        "oridecon.contracts.data.sql.query_log",
        "QueryLogEntry",
    ),
    "QueryLoggerProtocol": (
        "oridecon.contracts.data.sql.query_log",
        "QueryLoggerProtocol",
    ),
    "QueryResult": (
        "oridecon.contracts.data.sql.database",
        "QueryResult",
    ),
    "RawSQL": (
        "oridecon.contracts.data.sql.sql",
        "RawSQL",
    ),
    "ReadOnlyMapperProtocol": (
        "oridecon.contracts.data.sql.mapper",
        "ReadOnlyMapperProtocol",
    ),
    "SQLDialect": (
        "oridecon.contracts.data.sql.sql_dialect",
        "SQLDialect",
    ),
    "SchemaManagerProtocol": (
        "oridecon.contracts.data.sql.database",
        "SchemaManagerProtocol",
    ),
    "TransactionManagerProtocol": (
        "oridecon.contracts.data.sql.database",
        "TransactionManagerProtocol",
    ),
    "UnitOfWorkProtocol": (
        "oridecon.contracts.data.sql.unit_of_work",
        "UnitOfWorkProtocol",
    ),
    "UpdateResult": (
        "oridecon.contracts.data.sql.database",
        "UpdateResult",
    ),
}


def __getattr__(name: str) -> Any:
    """Lazy-load symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """Enumerate available attributes for IDE support."""
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = [
    "DEFAULT_MAX_IDENTIFIER_LENGTH",
    "MAX_IDENTIFIER_LENGTHS",
    "AppendLogProtocol",
    "AppendLogSnapshotStore",
    "ConnectionPoolProtocol",
    "ConnectionProtocol",
    "CrudOperationsProtocol",
    "DataMapperProtocol",
    "DatabaseMetricsProtocol",
    "DatabaseProviderProtocol",
    "DeleteResult",
    "HealthMonitorProtocol",
    "InsertResult",
    "InvalidIdentifierError",
    "IsolationLevel",
    "MigrationManagerProtocol",
    "MigrationRecord",
    "MigrationRunnerProtocol",
    "QueryLogEntry",
    "QueryLoggerProtocol",
    "QueryResult",
    "RawSQL",
    "ReadOnlyMapperProtocol",
    "SQLDialect",
    "SchemaManagerProtocol",
    "TransactionManagerProtocol",
    "UnitOfWorkProtocol",
    "UpdateResult",
]
