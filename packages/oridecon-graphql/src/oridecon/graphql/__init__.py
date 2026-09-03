"""Oridecon GraphQL - GraphQL support for Oridecon Framework.

This package provides GraphQL capabilities for Oridecon Framework applications,
including schema building, execution, subscriptions, and monitoring.
"""

from __future__ import annotations

import importlib.metadata

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from typing import TYPE_CHECKING, Any

from oridecon.graphql.constants import __version__ as __version__

if TYPE_CHECKING:
    # Types and configuration
    # Provider
    from oridecon.graphql.config import (
        CacheConfig,
        DataLoaderConfig,
        DepthLimitConfig,
        ErrorConfig,
        GraphQLConfig,
        IntrospectionConfig,
        MetricsConfig,
        PlaygroundConfig,
        SubscriptionConfig,
        TracingConfig,
    )

    # Core GraphQL components
    from oridecon.graphql.core.context import (
        ContextFactory,
        GraphQLContext,
        GraphQLRequest,
        GraphQLResponse,
    )
    from oridecon.graphql.core.execution import (
        ExecutionContextProtocol,
        GraphQLExecutorProtocol,
        execute_query,
    )
    from oridecon.graphql.core.introspection import (
        IntrospectionHandler,
        get_introspection_query,
    )
    from oridecon.graphql.core.validation import (
        SchemaValidator,
        ValidationResult,
        validate_query,
    )
    from oridecon.graphql.dataloader.cache import (
        InMemoryCache,
        LoaderCache,
        NoOpCache,
    )

    # DataLoaderProtocol support
    from oridecon.graphql.dataloader.loader import (
        DataLoaderProtocol,
        create_loader,
    )

    # Package-level decorators
    from oridecon.graphql.decorators import log_resolver, retry_resolver
    from oridecon.graphql.di.provider import GraphQLProvider
    from oridecon.graphql.events import (
        AfterExecuteEvent,
        BeforeExecuteEvent,
        OnErrorEvent,
        SchemaBuiltEvent,
        SubscriptionStartedEvent,
    )

    # Errors
    from oridecon.graphql.exceptions import (
        AuthenticationError,
        AuthorizationError,
        ForbiddenError,
        GraphQLError,
        InputGraphQLError,
        NotFoundError,
        ParseError,
        QueryTooComplexError,
        QueryTooDeepError,
        RateLimitError,
        ResolverError,
        SubscriptionError,
    )
    from oridecon.graphql.module import GraphQLModule

    # Monitoring
    from oridecon.graphql.monitoring.metrics import (
        GraphQLMetrics,
        MetricsCollectorProtocol,
        MetricsExtension,
        QueryStats,
        get_metrics_collector,
    )
    from oridecon.graphql.monitoring.tracing import (
        ExecutionTrace,
        TraceSpan,
        TracingExtension,
        trace_resolver,
    )
    from oridecon.graphql.schema.builder import (
        SchemaBuilderProtocol,
        create_schema,
    )

    # Schema decorators and utilities
    from oridecon.graphql.schema.decorators import (
        field,
        get_context,
        mutation,
        query,
        resolver,
        subscription,
    )
    from oridecon.graphql.schema.types import (
        Connection,
        CursorPaginationInput,
        DeleteResult,
        EnumType,
        InputType,
        InterfaceType,
        MutationResult,
        ObjectType,
        PagedResult,
        PaginationInput,
        ScalarType,
        SortInput,
        create_connection_type,
        union_type,
    )
    from oridecon.graphql.security.alias import (
        AliasLimitValidator,
    )

    # Security
    from oridecon.graphql.security.depth import (
        DepthLimitExtension,
        DepthLimitValidator,
        create_depth_limit,
    )
    from oridecon.graphql.security.extensions import RateLimitExtension
    from oridecon.graphql.security.permissions import (
        AbstractPermission,
        AllowAny,
        DenyAll,
        IsAdmin,
        IsAuthenticated,
        IsOwner,
        IsOwnerOrAdmin,
        allow_any,
        deny_all,
        is_admin,
        is_authenticated,
        is_owner,
        is_owner_or_admin,
    )
    from oridecon.graphql.security.rate_limit import (
        RateLimitConfig,
        RateLimiter,
        UnifiedRateLimiter,
    )
    from oridecon.graphql.types import (
        CacheControl,
        CacheScope,
        DataLoaderStats,
        DirectiveLocation,
        FieldInfo,
        GraphQLErrorCode,
        GraphQLErrorData,
        GraphQLErrorExtensions,
        GraphQLLocation,
        OperationInfo,
        OperationType,
        QueryMetrics,
        ResolverInfo,
        SubscriptionInfo,
        SubscriptionProtocol,
    )

_LAZY_IMPORTS = {
    # Module
    "GraphQLModule": "oridecon.graphql.module",
    # Types
    "OperationType": "oridecon.graphql.types",
    "GraphQLErrorCode": "oridecon.graphql.types",
    "DirectiveLocation": "oridecon.graphql.types",
    "CacheScope": "oridecon.graphql.types",
    "SubscriptionProtocol": "oridecon.graphql.types",
    "GraphQLLocation": "oridecon.graphql.types",
    "GraphQLErrorExtensions": "oridecon.graphql.types",
    "GraphQLErrorData": "oridecon.graphql.types",
    "FieldInfo": "oridecon.graphql.types",
    "OperationInfo": "oridecon.graphql.types",
    "ResolverInfo": "oridecon.graphql.types",
    "CacheControl": "oridecon.graphql.types",
    "QueryMetrics": "oridecon.graphql.types",
    "SubscriptionInfo": "oridecon.graphql.types",
    "DataLoaderStats": "oridecon.graphql.types",
    # Config
    "GraphQLConfig": "oridecon.graphql.config",
    "CacheConfig": "oridecon.graphql.config",
    "DepthLimitConfig": "oridecon.graphql.config",
    "IntrospectionConfig": "oridecon.graphql.config",
    "PlaygroundConfig": "oridecon.graphql.config",
    "SubscriptionConfig": "oridecon.graphql.config",
    "DataLoaderConfig": "oridecon.graphql.config",
    "TracingConfig": "oridecon.graphql.config",
    "MetricsConfig": "oridecon.graphql.config",
    "ErrorConfig": "oridecon.graphql.config",
    # Core
    "GraphQLContext": "oridecon.graphql.core.context",
    "GraphQLRequest": "oridecon.graphql.core.context",
    "GraphQLResponse": "oridecon.graphql.core.context",
    "ContextFactory": "oridecon.graphql.core.context",
    "GraphQLExecutorProtocol": "oridecon.graphql.core.execution",
    "ExecutionContextProtocol": "oridecon.graphql.core.execution",
    "execute_query": "oridecon.graphql.core.execution",
    # Events
    "BeforeExecuteEvent": "oridecon.graphql.events",
    "AfterExecuteEvent": "oridecon.graphql.events",
    "OnErrorEvent": "oridecon.graphql.events",
    "SchemaBuiltEvent": "oridecon.graphql.events",
    "SubscriptionStartedEvent": "oridecon.graphql.events",
    "SchemaValidator": "oridecon.graphql.core.validation",
    "ValidationResult": "oridecon.graphql.core.validation",
    "validate_query": "oridecon.graphql.core.validation",
    "IntrospectionHandler": "oridecon.graphql.core.introspection",
    "get_introspection_query": "oridecon.graphql.core.introspection",
    # Decorators
    "log_resolver": "oridecon.graphql.decorators",
    "retry_resolver": "oridecon.graphql.decorators",
    # Schema
    "query": "oridecon.graphql.schema.decorators",
    "mutation": "oridecon.graphql.schema.decorators",
    "subscription": "oridecon.graphql.schema.decorators",
    "resolver": "oridecon.graphql.schema.decorators",
    "field": "oridecon.graphql.schema.decorators",
    "get_context": "oridecon.graphql.schema.decorators",
    "SchemaBuilderProtocol": "oridecon.graphql.schema.builder",
    "create_schema": "oridecon.graphql.schema.builder",
    # Protocol re-exports (contracts + type aliases)
    "GraphQLResolver": "oridecon.graphql.protocols",
    "GraphQLSchema": "oridecon.graphql.protocols",
    "ObjectType": "oridecon.graphql.schema.types",
    "InputType": "oridecon.graphql.schema.types",
    "InterfaceType": "oridecon.graphql.schema.types",
    "union_type": "oridecon.graphql.schema.types",
    "EnumType": "oridecon.graphql.schema.types",
    "ScalarType": "oridecon.graphql.schema.types",
    "Connection": "oridecon.graphql.schema.types",
    "PagedResult": "oridecon.graphql.schema.types",
    "PaginationInput": "oridecon.graphql.schema.types",
    "CursorPaginationInput": "oridecon.graphql.schema.types",
    "SortInput": "oridecon.graphql.schema.types",
    "MutationResult": "oridecon.graphql.schema.types",
    "DeleteResult": "oridecon.graphql.schema.types",
    "create_connection_type": "oridecon.graphql.schema.types",
    # DataLoaderProtocol
    "DataLoaderProtocol": "oridecon.graphql.dataloader.loader",
    "create_loader": "oridecon.graphql.dataloader.loader",
    "LoaderCache": "oridecon.graphql.dataloader.cache",
    "InMemoryCache": "oridecon.graphql.dataloader.cache",
    "NoOpCache": "oridecon.graphql.dataloader.cache",
    # Security
    "DepthLimitExtension": "oridecon.graphql.security.depth",
    "DepthLimitValidator": "oridecon.graphql.security.depth",
    "create_depth_limit": "oridecon.graphql.security.depth",
    "AliasLimitValidator": "oridecon.graphql.security.alias",
    "AbstractPermission": "oridecon.graphql.security.permissions",
    "IsAuthenticated": "oridecon.graphql.security.permissions",
    "IsAdmin": "oridecon.graphql.security.permissions",
    "IsOwner": "oridecon.graphql.security.permissions",
    "IsOwnerOrAdmin": "oridecon.graphql.security.permissions",
    "AllowAny": "oridecon.graphql.security.permissions",
    "DenyAll": "oridecon.graphql.security.permissions",
    "is_authenticated": "oridecon.graphql.security.permissions",
    "is_admin": "oridecon.graphql.security.permissions",
    "is_owner": "oridecon.graphql.security.permissions",
    "is_owner_or_admin": "oridecon.graphql.security.permissions",
    "allow_any": "oridecon.graphql.security.permissions",
    "deny_all": "oridecon.graphql.security.permissions",
    "RateLimiter": "oridecon.graphql.security.rate_limit",
    "RateLimitConfig": "oridecon.graphql.security.rate_limit",
    "UnifiedRateLimiter": "oridecon.graphql.security.rate_limit",
    "RateLimitExtension": "oridecon.graphql.security.extensions",
    # Monitoring
    "GraphQLMetrics": "oridecon.graphql.monitoring.metrics",
    "MetricsCollectorProtocol": "oridecon.graphql.monitoring.metrics",
    "MetricsExtension": "oridecon.graphql.monitoring.metrics",
    "QueryStats": "oridecon.graphql.monitoring.metrics",
    "get_metrics_collector": "oridecon.graphql.monitoring.metrics",
    "TracingExtension": "oridecon.graphql.monitoring.tracing",
    "trace_resolver": "oridecon.graphql.monitoring.tracing",
    "ExecutionTrace": "oridecon.graphql.monitoring.tracing",
    "TraceSpan": "oridecon.graphql.monitoring.tracing",
    # Errors
    "GraphQLError": "oridecon.graphql.exceptions",
    "InputGraphQLError": "oridecon.graphql.exceptions",
    "ResolverError": "oridecon.graphql.exceptions",
    "ParseError": "oridecon.graphql.exceptions",
    "AuthenticationError": "oridecon.graphql.exceptions",
    "AuthorizationError": "oridecon.graphql.exceptions",
    "ForbiddenError": "oridecon.graphql.exceptions",
    "NotFoundError": "oridecon.graphql.exceptions",
    "RateLimitError": "oridecon.graphql.exceptions",
    "QueryTooComplexError": "oridecon.graphql.exceptions",
    "QueryTooDeepError": "oridecon.graphql.exceptions",
    "SubscriptionError": "oridecon.graphql.exceptions",
    "GraphQLConnectionError": "oridecon.graphql.exceptions",
    # Provider
    "GraphQLProvider": "oridecon.graphql.di.provider",
    # Resolvers
    "ResolverAdapter": "oridecon.graphql.resolvers",
    # "resolver" is intentionally omitted here to avoid duplicate keys;
    # it can be imported directly from `oridecon.graphql.resolvers` if needed.
    # Directives
    "DirectiveRegistry": "oridecon.graphql.directives",
    "DeprecationDirectiveHandler": "oridecon.graphql.directives",
    # Pagination
    "Edge": "oridecon.graphql.pagination",
    "PageInfo": "oridecon.graphql.pagination",
    "CursorConnection": "oridecon.graphql.pagination",
    "encode_cursor": "oridecon.graphql.pagination",
    "decode_cursor": "oridecon.graphql.pagination",
    "encode_cursor_from_id": "oridecon.graphql.pagination",
    "decode_cursor_to_id": "oridecon.graphql.pagination",
    # Web Integration
    "GraphQLController": "oridecon.graphql.controllers",
    "GraphQLSubscriptionController": "oridecon.graphql.controllers",
    # APQ
    "PersistedQueryStore": "oridecon.graphql.core.persisted_queries",
    "InMemoryPersistedQueryStore": "oridecon.graphql.core.persisted_queries",
    "RedisPersistedQueryStore": "oridecon.graphql.core.persisted_queries",
    "CacheBackendPersistedQueryStore": "oridecon.graphql.core.persisted_queries",
    "APQResult": "oridecon.graphql.core.persisted_queries",
    "APQHandler": "oridecon.graphql.core.persisted_queries",
    "compute_query_hash": "oridecon.graphql.core.persisted_queries",
    # Hooks
    "GraphQLRequestReceivedHook": "oridecon.graphql.hooks",
    "GraphQLResponsePreparedHook": "oridecon.graphql.hooks",
    "GraphQLSchemaBuiltHook": "oridecon.graphql.hooks",
}


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib

        module_path = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__} has no attribute {name}")


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = list(_LAZY_IMPORTS.keys())
