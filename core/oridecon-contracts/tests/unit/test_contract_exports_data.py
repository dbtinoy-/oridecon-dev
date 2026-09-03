from __future__ import annotations

import importlib
import sys

import pytest

EXPECTED_MODULE_EXPORTS: dict[str, list[str]] = {
    "oridecon.contracts.data.graph.enums": [
        "ConstraintKind",
        "EdgeDirection",
        "IndexKind",
        "MergeAction",
        "ReturnType",
    ],
    "oridecon.contracts.data.graph.filters": [
        "Prop",
        "PropertyCondition",
        "PropertyConditionGroup",
        "PropertyFilter",
        "PropertyOperator",
    ],
    "oridecon.contracts.data.graph.protocols": [
        "GraphProtocol",
        "GraphStoreProtocol",
    ],
    "oridecon.contracts.data.graph.types": [
        "BulkEdgeResult",
        "BulkNodeResult",
        "ConstraintSpec",
        "EdgeResult",
        "EdgeSpec",
        "GraphEdge",
        "GraphInfo",
        "GraphNode",
        "GraphPath",
        "IndexSpec",
        "NodeResult",
        "NodeSpec",
        "StartSpec",
        "TraversalQuery",
        "TraversalStep",
    ],
    "oridecon.contracts.data.nosql": [
        "BulkWriteResult",
        "CollectionProtocol",
        "DocumentRepositoryProtocol",
        "DocumentResult",
        "DocumentStoreProtocol",
    ],
    "oridecon.contracts.data.outbox": ["OutboxStoreProtocol"],
    "oridecon.contracts.data.repository": [
        "ReadOnlyRepositoryProtocol",
        "RepositoryProtocol",
        "T",
    ],
    "oridecon.contracts.data.sql": [
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
    ],
    "oridecon.contracts.data.sql.database": [
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
    ],
    "oridecon.contracts.data.sql.query_log": [
        "QueryLogEntry",
        "QueryLoggerProtocol",
    ],
    "oridecon.contracts.data.sql.sql": [
        "InvalidIdentifierError",
        "RawSQL",
    ],
    "oridecon.contracts.data.sql.sql_dialect": [
        "DEFAULT_MAX_IDENTIFIER_LENGTH",
        "MAX_IDENTIFIER_LENGTHS",
        "SQLDialect",
    ],
    "oridecon.contracts.data.sql.unit_of_work": ["UnitOfWorkProtocol"],
    "oridecon.contracts.data.vector.enums": [
        "DistanceMetric",
        "IndexState",
        "IndexType",
    ],
    "oridecon.contracts.data.vector.filters": [
        "Filter",
        "FilterOperator",
        "LogicalOperator",
        "MetadataCondition",
        "MetadataConditionGroup",
        "MetadataFilter",
    ],
    "oridecon.contracts.data.vector.protocols": [
        "VectorCollectionProtocol",
        "VectorStoreProtocol",
    ],
    "oridecon.contracts.data.vector.types": [
        "CollectionConfig",
        "CollectionInfo",
        "DeleteResult",
        "SearchQuery",
        "SearchResult",
        "UpsertResult",
        "VectorRecord",
    ],
}


@pytest.mark.parametrize(
    ("module_path", "expected_exports"),
    EXPECTED_MODULE_EXPORTS.items(),
)
def test_module_declares_explicit_all(
    module_path: str,
    expected_exports: list[str],
) -> None:
    module = importlib.import_module(module_path)
    exported = getattr(module, "__all__", None)

    assert isinstance(exported, list)
    assert exported == expected_exports
    for name in exported:
        assert not name.startswith("_")
        assert hasattr(module, name)


def _import_fresh(module_path: str):
    sys.modules.pop(module_path, None)
    return importlib.import_module(module_path)


@pytest.mark.parametrize(
    "module_path",
    [
        "oridecon.contracts.data.sql",
        "oridecon.contracts.data.nosql",
    ],
)
def test_data_facade_keys_match_all(module_path: str) -> None:
    module = _import_fresh(module_path)

    assert set(module.__all__) == set(module._LAZY_IMPORTS)


@pytest.mark.parametrize(
    "module_path",
    [
        "oridecon.contracts.data.sql",
        "oridecon.contracts.data.nosql",
    ],
)
def test_data_facade_raises_for_unknown_name(module_path: str) -> None:
    module = _import_fresh(module_path)

    with pytest.raises(AttributeError):
        _ = module.__definitely_missing__


@pytest.mark.parametrize(
    ("module_path", "symbol"),
    [
        ("oridecon.contracts.data.sql", "DatabaseProviderProtocol"),
        ("oridecon.contracts.data.nosql", "DocumentStoreProtocol"),
    ],
)
def test_data_facade_loads_symbol_on_first_access(
    module_path: str,
    symbol: str,
) -> None:
    module = _import_fresh(module_path)

    assert symbol not in module.__dict__

    value = getattr(module, symbol)

    assert value is not None
    assert symbol in module.__dict__
