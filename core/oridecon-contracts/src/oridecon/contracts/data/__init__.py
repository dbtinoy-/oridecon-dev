"""Data access protocols."""

from __future__ import annotations

from oridecon.contracts.data.aggregatable import AggregatableProtocol
from oridecon.contracts.data.bulk_operations import BulkOperationsProtocol
from oridecon.contracts.data.data_source import DataSourceProtocol
from oridecon.contracts.data.exceptions import UnitOfWorkError
from oridecon.contracts.data.graph.protocols import GraphProtocol, GraphStoreProtocol
from oridecon.contracts.data.graph.types import (
    GraphEdge,
    GraphInfo,
    GraphNode,
    GraphPath,
)
from oridecon.contracts.data.identifiers import (
    DEFAULT_MAX_IDENTIFIER_LENGTH,
    MAX_IDENTIFIER_LENGTHS,
    Column,
    Identifier,
    QualifiedTable,
    Schema,
    Table,
    column,
    schema,
    table,
)
from oridecon.contracts.data.nosql.nosql import (
    BulkWriteResult,
    CollectionProtocol,
    DocumentResult,
    DocumentStoreProtocol,
)
from oridecon.contracts.data.nosql.nosql_repository import DocumentRepositoryProtocol
from oridecon.contracts.data.outbox import OutboxStoreProtocol
from oridecon.contracts.data.protocols import (
    AndExpr,
    CursorCodecProtocol,
    CursorPaginationSpec,
    FieldContains,
    FieldEq,
    FieldGt,
    FieldGte,
    FieldIn,
    FieldLt,
    FieldLte,
    FieldNeq,
    FilterCompilerProtocol,
    FilterExpression,
    NotExpr,
    OrExpr,
    PaginationSpec,
    PaginatorProtocol,
    ProjectionSpec,
    QueryFilterProtocol,
    SortSpecification,
)
from oridecon.contracts.data.relation_loader import RelationLoaderProtocol
from oridecon.contracts.data.repository import (
    ReadOnlyRepositoryProtocol,
    RepositoryProtocol,
)
from oridecon.contracts.data.searchable import SearchableProtocol
from oridecon.contracts.data.sql.append_log import (
    AppendLogProtocol,
    AppendLogSnapshotStore,
)
from oridecon.contracts.data.sql.context_protocol import DatabaseContextProtocol
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
from oridecon.contracts.data.sql.sql_dialect import SQLDialect
from oridecon.contracts.data.sql.unit_of_work import UnitOfWorkProtocol
from oridecon.contracts.data.timeseries import TimeSeriesStoreProtocol
from oridecon.contracts.data.vector.protocols import (
    VectorCollectionProtocol,
    VectorStoreProtocol,
)
from oridecon.contracts.data.vector.types import (
    CollectionConfig,
    CollectionInfo,
    SearchQuery,
    SearchResult,
    VectorRecord,
)

__all__ = [
    "DEFAULT_MAX_IDENTIFIER_LENGTH",
    "MAX_IDENTIFIER_LENGTHS",
    "AggregatableProtocol",
    "AndExpr",
    "AppendLogProtocol",
    "AppendLogSnapshotStore",
    "BulkOperationsProtocol",
    "BulkWriteResult",
    "CollectionConfig",
    "CollectionInfo",
    "CollectionProtocol",
    "Column",
    "ConnectionPoolProtocol",
    "ConnectionProtocol",
    "CrudOperationsProtocol",
    "CursorCodecProtocol",
    "CursorPaginationSpec",
    "DataMapperProtocol",
    "DataSourceProtocol",
    "DatabaseMetricsProtocol",
    "DatabaseProviderProtocol",
    "DeleteResult",
    "DocumentRepositoryProtocol",
    "DocumentResult",
    "DocumentStoreProtocol",
    "FieldContains",
    "FieldEq",
    "FieldGt",
    "FieldGte",
    "FieldIn",
    "FieldLt",
    "FieldLte",
    "FieldNeq",
    "FilterCompilerProtocol",
    "FilterExpression",
    "GraphEdge",
    "GraphInfo",
    "GraphNode",
    "GraphPath",
    "GraphProtocol",
    "GraphStoreProtocol",
    "HealthMonitorProtocol",
    "Identifier",
    "InsertResult",
    "InvalidIdentifierError",
    "IsolationLevel",
    "MigrationManagerProtocol",
    "MigrationRecord",
    "NotExpr",
    "OrExpr",
    "OutboxStoreProtocol",
    "PaginationSpec",
    "PaginatorProtocol",
    "ProjectionSpec",
    "QualifiedTable",
    "QueryFilterProtocol",
    "QueryLogEntry",
    "QueryLoggerProtocol",
    "QueryResult",
    "RawSQL",
    "ReadOnlyMapperProtocol",
    "ReadOnlyRepositoryProtocol",
    "RelationLoaderProtocol",
    "RepositoryProtocol",
    "SQLDialect",
    "Schema",
    "SchemaManagerProtocol",
    "SearchQuery",
    "SearchResult",
    "SearchableProtocol",
    "SortSpecification",
    "Table",
    "TimeSeriesStoreProtocol",
    "TransactionManagerProtocol",
    "UnitOfWorkError",
    "UnitOfWorkProtocol",
    "UpdateResult",
    "VectorCollectionProtocol",
    "VectorRecord",
    "VectorStoreProtocol",
    "column",
    "schema",
    "table",
]
