"""GraphQL protocols."""

from __future__ import annotations

from oridecon.contracts.graphql.protocols import (
    DataLoaderProtocol,
    DirectiveHandlerProtocol,
    EntityResolverProtocol,
    ErrorFormatterProtocol,
    GraphQLExecutorProtocol,
    GraphQLPrincipalResolverProtocol,
    GraphQLRequestProtocol,
    IntrospectionHandlerProtocol,
    MutationHandlerProtocol,
    ResolverProtocol,
    SchemaBuilderProtocol,
    SubscriptionAuthHandlerProtocol,
    SubscriptionHandlerProtocol,
    ValidationRuleProtocol,
    WebSocketTransportProtocol,
)
from oridecon.contracts.graphql.types import GraphQLPrincipal

__all__ = [
    "DataLoaderProtocol",
    "DirectiveHandlerProtocol",
    "EntityResolverProtocol",
    "ErrorFormatterProtocol",
    "GraphQLExecutorProtocol",
    "GraphQLPrincipal",
    "GraphQLPrincipalResolverProtocol",
    "GraphQLRequestProtocol",
    "IntrospectionHandlerProtocol",
    "MutationHandlerProtocol",
    "ResolverProtocol",
    "SchemaBuilderProtocol",
    "SubscriptionAuthHandlerProtocol",
    "SubscriptionHandlerProtocol",
    "ValidationRuleProtocol",
    "WebSocketTransportProtocol",
]
