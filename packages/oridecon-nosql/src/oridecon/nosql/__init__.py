"""oridecon-nosql — First-class NoSQL support for the Oridecon Framework.

Provides document-store backends (MongoDB). For graph database support
(Neo4j, in-memory), use the ``oridecon-graph`` package.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oridecon.nosql.config import DynamoDBConfig, MongoDBConfig, NoSQLConfig
    from oridecon.nosql.di.provider import NoSQLProvider
    from oridecon.nosql.events import (
        MigrationAppliedEvent,
        MigrationFailedEvent,
        NoSQLConnectedEvent,
        NoSQLDisconnectedEvent,
    )
    from oridecon.nosql.exceptions import (
        DocumentNotFoundError,
        DocumentValidationError,
        DuplicateKeyError,
        NoSQLConnectionError,
        NoSQLError,
        TransactionError,
    )
    from oridecon.nosql.migration.manager import MigrationManager
    from oridecon.nosql.migration.operations import (
        AddField,
        CreateIndex,
        DropCollection,
        DropIndex,
        RenameField,
    )
    from oridecon.nosql.module import NoSQLModule
    from oridecon.nosql.query.builder import DocumentQueryBuilder
    from oridecon.nosql.query.operators import (
        AccumulatorOp,
        AggregationOp,
        ComparisonOp,
        LogicalOp,
        UpdateOp,
    )
    from oridecon.nosql.query.pipeline import AggregationPipeline

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "AccumulatorOp": ("oridecon.nosql.query.operators", "AccumulatorOp"),
    "AddField": ("oridecon.nosql.migration.operations", "AddField"),
    "AggregationOp": ("oridecon.nosql.query.operators", "AggregationOp"),
    "AggregationPipeline": ("oridecon.nosql.query.pipeline", "AggregationPipeline"),
    "ComparisonOp": ("oridecon.nosql.query.operators", "ComparisonOp"),
    "CreateIndex": ("oridecon.nosql.migration.operations", "CreateIndex"),
    "DocumentNotFoundError": ("oridecon.nosql.exceptions", "DocumentNotFoundError"),
    "DocumentQueryBuilder": ("oridecon.nosql.query.builder", "DocumentQueryBuilder"),
    "DocumentValidationError": ("oridecon.nosql.exceptions", "DocumentValidationError"),
    "DropCollection": ("oridecon.nosql.migration.operations", "DropCollection"),
    "DropIndex": ("oridecon.nosql.migration.operations", "DropIndex"),
    "DuplicateKeyError": ("oridecon.nosql.exceptions", "DuplicateKeyError"),
    "LogicalOp": ("oridecon.nosql.query.operators", "LogicalOp"),
    "MigrationAppliedEvent": ("oridecon.nosql.events", "MigrationAppliedEvent"),
    "MigrationFailedEvent": ("oridecon.nosql.events", "MigrationFailedEvent"),
    "MigrationManager": ("oridecon.nosql.migration.manager", "MigrationManager"),
    "DynamoDBConfig": ("oridecon.nosql.config", "DynamoDBConfig"),
    "MongoDBConfig": ("oridecon.nosql.config", "MongoDBConfig"),
    "NamedNoSQLConfig": ("oridecon.nosql.config", "NamedNoSQLConfig"),
    "NoSQLConfig": ("oridecon.nosql.config", "NoSQLConfig"),
    "NoSQLConnectedEvent": ("oridecon.nosql.events", "NoSQLConnectedEvent"),
    "NoSQLConnectionError": ("oridecon.nosql.exceptions", "NoSQLConnectionError"),
    "NoSQLDisconnectedEvent": ("oridecon.nosql.events", "NoSQLDisconnectedEvent"),
    "NoSQLError": ("oridecon.nosql.exceptions", "NoSQLError"),
    "NoSQLModule": ("oridecon.nosql.module", "NoSQLModule"),
    "NoSQLProvider": ("oridecon.nosql.di.provider", "NoSQLProvider"),
    "RenameField": ("oridecon.nosql.migration.operations", "RenameField"),
    "TransactionError": ("oridecon.nosql.exceptions", "TransactionError"),
    "UpdateOp": ("oridecon.nosql.query.operators", "UpdateOp"),
    # Hooks
    "NoSQLConnectedHook": ("oridecon.nosql.hooks", "NoSQLConnectedHook"),
    "NoSQLDisconnectedHook": ("oridecon.nosql.hooks", "NoSQLDisconnectedHook"),
}

__all__ = list(_LAZY_IMPORTS)


def __getattr__(name: str) -> object:
    """Lazy-load public symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr = _LAZY_IMPORTS[name]
        mod = importlib.import_module(module_path)
        value = getattr(mod, attr)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """Expose lazy-loaded names for tab completion and dir()."""
    return list(_LAZY_IMPORTS)
