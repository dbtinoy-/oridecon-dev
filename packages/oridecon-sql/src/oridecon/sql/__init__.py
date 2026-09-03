"""Oridecon DB Package — Database integration and repository pattern.

**Preferred import paths (D9.1)**

Use the most specific sub-namespace rather than the root namespace wherever
possible — this keeps import times low and makes dependencies clear:

+------------------------+-----------------------------------------------+
| What you need          | Import from                                   |
+========================+===============================================+
| DI provider            | ``oridecon.sql.di.provider``                   |
+------------------------+-----------------------------------------------+
| Query building         | ``oridecon.sql.query``                         |
+------------------------+-----------------------------------------------+
| SQL dialect builder    | ``oridecon.sql.query``                         |
+------------------------+-----------------------------------------------+
| RepositoryProtocol base        | ``oridecon.sql.repositories``                  |
+------------------------+-----------------------------------------------+
| Schema / ORM models    | ``oridecon.sql.schema`` or ``oridecon.sql.orm`` |
+------------------------+-----------------------------------------------+
| Migration tools        | ``oridecon.sql.migrations``                    |
+------------------------+-----------------------------------------------+
| Unit of Work           | ``oridecon.sql.unit_of_work``                  |
+------------------------+-----------------------------------------------+
| DatabaseService        | ``oridecon.sql.providers``                     |
+------------------------+-----------------------------------------------+
| Contracts              | ``oridecon.contracts.data``                   |
+------------------------+-----------------------------------------------+

The root namespace (``from oridecon.sql import ...``) is retained for
backward compatibility and for the handful of frequently-used types
documented below.  It should **not** grow further.
"""

from __future__ import annotations

import importlib.metadata
import sys
from typing import TYPE_CHECKING, Any

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from oridecon.sql.constants import __version__ as __version__

# Lazy loading to avoid circular imports

if TYPE_CHECKING:
    from oridecon.contracts.audit import AuditEntry
    from oridecon.contracts.core import HealthStatus
    from oridecon.contracts.core.lifecycle import (  # type: ignore[attr-defined]
        HealthCheckResult,
    )
    from oridecon.contracts.data import (
        ConnectionPoolProtocol,
        DatabaseProviderProtocol,
        DeleteResult,
        InsertResult,
        QueryLogEntry,
        QueryLoggerProtocol,
        QueryResult,
        UpdateResult,
    )
    from oridecon.contracts.data.sql.sql import (
        InvalidIdentifierError,
        RawSQL,
    )
    from oridecon.contracts.data.sql.sql_dialect import SQLDialect
    from oridecon.sql.audit.mixin import AuditRepositoryMixin
    from oridecon.sql.config import DatabaseConfig
    from oridecon.sql.context import (
        DbContext,
        RequestContextManager,
        create_db_context,
        create_task_with_context,
        run_in_threadpool_with_context,
    )
    from oridecon.sql.di.provider import DatabaseProvider
    from oridecon.sql.exceptions import (
        DatabaseError,
        OptimisticLockError,
        RepositoryError,
    )
    from oridecon.sql.identifiers import (
        Column,
        Identifier,
        QualifiedTable,
        Schema,
        Table,
        column,
        schema,
        table,
    )
    from oridecon.sql.monitoring.database_monitor import DatabaseMonitor
    from oridecon.sql.providers import (
        AbstractConnectionPool,
        ConsoleQueryLogger,
        DatabaseService,
        FileQueryLogger,
        MemoryQueryLogger,
        MySQLProvider,
        PostgresProvider,
        QueryLoggerBase,
        SimpleConnectionPool,
        SimpleMigrationManager,
        SQLiteProvider,
    )
    from oridecon.sql.query import AsyncQueryBuilder, Operator
    from oridecon.sql.repositories import F, Filter, field
    from oridecon.sql.repositories.base import (  # type: ignore[attr-defined]
        RepositoryProtocol,
    )
    from oridecon.sql.repositories.generic_repository import GenericRepository
    from oridecon.sql.resilience import DatabaseResilienceHandler
    from oridecon.sql.row_level_security import (
        NoSecurityPolicyError,
        RowLevelSecurityPolicy,
        ScopeColumn,
    )
    from oridecon.sql.search import (
        FTSDialect,
        FTSResult,
        MySQLFTSQuery,
        PostgresFTSQuery,
        full_text_search,
    )
    from oridecon.sql.stores import (
        DatabaseLockStore,
        DatabaseSecretStore,
        DatabaseStateStore,
    )
    from oridecon.sql.types import Entity
    from oridecon.sql.unit_of_work.manager import (
        SimpleTransactionManager,
        transaction,
    )
    from oridecon.sql.unit_of_work.simple import (
        SimpleUnitOfWork,
        unit_of_work,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "HealthStatus": ("oridecon.contracts.core", "HealthStatus"),
    "HealthCheckResult": ("oridecon.contracts.core.lifecycle", "HealthCheckResult"),
    # Contracts
    "ConnectionPoolProtocol": ("oridecon.contracts.data", "ConnectionPoolProtocol"),
    "DatabaseProviderProtocol": ("oridecon.contracts.data", "DatabaseProviderProtocol"),
    "DeleteResult": ("oridecon.contracts.data", "DeleteResult"),
    "InsertResult": ("oridecon.contracts.data", "InsertResult"),
    "QueryLogEntry": ("oridecon.contracts.data", "QueryLogEntry"),
    "QueryLoggerProtocol": ("oridecon.contracts.data", "QueryLoggerProtocol"),
    "QueryResult": ("oridecon.contracts.data", "QueryResult"),
    "UpdateResult": ("oridecon.contracts.data", "UpdateResult"),
    # Internal - lazy loaded to avoid circular imports
    "AuditEntry": ("oridecon.contracts.audit.models", "AuditEntry"),
    "AuditRepositoryMixin": ("oridecon.sql.audit.mixin", "AuditRepositoryMixin"),
    "AsyncQueryBuilder": ("oridecon.sql.query", "AsyncQueryBuilder"),
    "DatabaseConfig": ("oridecon.sql.config", "DatabaseConfig"),
    "DatabaseError": ("oridecon.sql.exceptions", "DatabaseError"),
    "DatabaseModule": ("oridecon.sql.module", "DatabaseModule"),
    "DatabaseProvider": ("oridecon.sql.di.provider", "DatabaseProvider"),
    "DatabaseMonitor": ("oridecon.sql.monitoring.database_monitor", "DatabaseMonitor"),
    "DatabaseService": ("oridecon.sql.providers", "DatabaseService"),
    "Entity": ("oridecon.sql.types", "Entity"),
    "F": ("oridecon.sql.repositories", "F"),
    "Filter": ("oridecon.sql.repositories", "Filter"),
    "GenericRepository": (
        "oridecon.sql.repositories.generic_repository",
        "GenericRepository",
    ),
    "NoSecurityPolicyError": (
        "oridecon.sql.row_level_security",
        "NoSecurityPolicyError",
    ),
    "RepositoryProtocol": ("oridecon.sql.repositories.base", "RepositoryProtocol"),
    "RowLevelSecurityPolicy": (
        "oridecon.sql.row_level_security",
        "RowLevelSecurityPolicy",
    ),
    "ScopeColumn": ("oridecon.sql.row_level_security", "ScopeColumn"),
    "OptimisticLockError": ("oridecon.sql.exceptions", "OptimisticLockError"),
    "RepositoryError": ("oridecon.sql.exceptions", "RepositoryError"),
    "SimpleUnitOfWork": ("oridecon.sql.unit_of_work.simple", "SimpleUnitOfWork"),
    "SimpleTransactionManager": (
        "oridecon.sql.unit_of_work.manager",
        "SimpleTransactionManager",
    ),
    "transaction": ("oridecon.sql.unit_of_work.manager", "transaction"),
    "unit_of_work": ("oridecon.sql.unit_of_work.simple", "unit_of_work"),
    # Implementations re-exported from providers
    "AbstractConnectionPool": ("oridecon.sql.providers", "AbstractConnectionPool"),
    "SimpleConnectionPool": ("oridecon.sql.providers", "SimpleConnectionPool"),
    "QueryLoggerBase": ("oridecon.sql.providers", "QueryLoggerBase"),
    "ConsoleQueryLogger": ("oridecon.sql.providers", "ConsoleQueryLogger"),
    "FileQueryLogger": ("oridecon.sql.providers", "FileQueryLogger"),
    "MemoryQueryLogger": ("oridecon.sql.providers", "MemoryQueryLogger"),
    "SimpleMigrationManager": ("oridecon.sql.providers", "SimpleMigrationManager"),
    "SQLiteProvider": ("oridecon.sql.providers", "SQLiteProvider"),
    "Operator": ("oridecon.sql.query", "Operator"),
    "PostgresProvider": ("oridecon.sql.providers", "PostgresProvider"),
    "MySQLProvider": ("oridecon.sql.providers", "MySQLProvider"),
    # SQL identifiers - type-safe SQL construction (moved to oridecon-sql)
    "Table": ("oridecon.sql.identifiers", "Table"),
    "Column": ("oridecon.sql.identifiers", "Column"),
    "Schema": ("oridecon.sql.identifiers", "Schema"),
    "Identifier": ("oridecon.sql.identifiers", "Identifier"),
    "QualifiedTable": ("oridecon.sql.identifiers", "QualifiedTable"),
    # SQL exceptions (still in contracts)
    "InvalidIdentifierError": (
        "oridecon.contracts.data.sql.sql",
        "InvalidIdentifierError",
    ),
    "RawSQL": ("oridecon.contracts.data.sql.sql", "RawSQL"),
    "SQLDialect": ("oridecon.contracts.data.sql.sql_dialect", "SQLDialect"),
    # Factory functions (moved to oridecon-sql)
    "table": ("oridecon.sql.identifiers", "table"),
    "column": ("oridecon.sql.identifiers", "column"),
    "schema": ("oridecon.sql.identifiers", "schema"),
    # Database-backed persistent stores (moved from oridecon-cache)
    "DatabaseStateStore": ("oridecon.sql.stores", "DatabaseStateStore"),
    "DatabaseSecretStore": ("oridecon.sql.stores", "DatabaseSecretStore"),
    "DatabaseLockStore": ("oridecon.sql.stores", "DatabaseLockStore"),
    # Context management (P0)
    "DbContext": ("oridecon.sql.context", "DbContext"),
    "create_db_context": ("oridecon.sql.context", "create_db_context"),
    "RequestContextManager": ("oridecon.sql.context", "RequestContextManager"),
    "create_task_with_context": ("oridecon.sql.context", "create_task_with_context"),
    "field": ("oridecon.sql.repositories", "field"),
    "run_in_threadpool_with_context": (
        "oridecon.sql.context",
        "run_in_threadpool_with_context",
    ),
    # Resilience (P0)
    "DatabaseResilienceHandler": (
        "oridecon.sql.resilience",
        "DatabaseResilienceHandler",
    ),
    # Full-text search utilities (P1)
    "FTSDialect": ("oridecon.sql.search", "FTSDialect"),
    "FTSResult": ("oridecon.sql.search", "FTSResult"),
    "PostgresFTSQuery": ("oridecon.sql.search", "PostgresFTSQuery"),
    "MySQLFTSQuery": ("oridecon.sql.search", "MySQLFTSQuery"),
    "full_text_search": ("oridecon.sql.search", "full_text_search"),
    # Hooks
    "SQLConnectionReadyHook": ("oridecon.sql.hooks", "SQLConnectionReadyHook"),
    "SQLTransactionBegunHook": ("oridecon.sql.hooks", "SQLTransactionBegunHook"),
    "SQLTransactionEndedHook": ("oridecon.sql.hooks", "SQLTransactionEndedHook"),
}


def __getattr__(name: str) -> Any:
    """Lazy load attributes to avoid circular imports, with caching."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value  # Cache for subsequent access
        return value
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)


def __dir__() -> list[str]:
    """List available attributes for IDE support."""
    return list(__all__) + list(_LAZY_IMPORTS.keys())


__all__ = [
    "AbstractConnectionPool",
    "AuditEntry",
    "AuditRepositoryMixin",
    "Column",
    "ConnectionPoolProtocol",
    "ConsoleQueryLogger",
    "DatabaseConfig",
    "DatabaseError",
    "DatabaseLockStore",
    "DatabaseModule",
    "DatabaseMonitor",
    "DatabaseProvider",
    "DatabaseProviderProtocol",
    "DatabaseResilienceHandler",
    "DatabaseSecretStore",
    "DatabaseService",
    "DatabaseStateStore",
    "DbContext",
    "DeleteResult",
    "Entity",
    "F",
    "FTSDialect",
    "FTSResult",
    "FileQueryLogger",
    "Filter",
    "GenericRepository",
    "HealthCheckResult",
    "HealthStatus",
    "Identifier",
    "InsertResult",
    "InvalidIdentifierError",
    "MemoryQueryLogger",
    "MySQLFTSQuery",
    "MySQLProvider",
    "NoSecurityPolicyError",
    "OptimisticLockError",
    "PostgresFTSQuery",
    "PostgresProvider",
    "QualifiedTable",
    "QueryLogEntry",
    "QueryLoggerBase",
    "QueryLoggerProtocol",
    "QueryResult",
    "RawSQL",
    "RepositoryError",
    "RepositoryProtocol",
    "RequestContextManager",
    "RowLevelSecurityPolicy",
    "SQLConnectionReadyHook",
    "SQLDialect",
    "SQLTransactionBegunHook",
    "SQLTransactionEndedHook",
    "SQLiteProvider",
    "Schema",
    "ScopeColumn",
    "SimpleConnectionPool",
    "SimpleMigrationManager",
    "SimpleTransactionManager",
    "SimpleUnitOfWork",
    "Table",
    "UpdateResult",
    "column",
    "create_db_context",
    "create_task_with_context",
    "field",
    "full_text_search",
    "run_in_threadpool_with_context",
    "schema",
    "table",
    "transaction",
    "unit_of_work",
]
