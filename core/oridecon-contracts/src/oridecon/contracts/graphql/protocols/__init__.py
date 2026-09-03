"""GraphQL protocol definitions.

Protocols for GraphQL execution, schema building, data loading,
resolvers, and subscriptions.
"""

from __future__ import annotations

from oridecon.contracts.graphql.protocols.execution import (
    DEFAULT_SUBSCRIPTIONS_PATH as DEFAULT_SUBSCRIPTIONS_PATH,
)
from oridecon.contracts.graphql.protocols.execution import (
    DataLoaderProtocol as DataLoaderProtocol,
)
from oridecon.contracts.graphql.protocols.execution import (
    EntityResolverProtocol as EntityResolverProtocol,
)
from oridecon.contracts.graphql.protocols.execution import (
    GraphQLControllerProtocol as GraphQLControllerProtocol,
)
from oridecon.contracts.graphql.protocols.execution import (
    GraphQLExecutorProtocol as GraphQLExecutorProtocol,
)
from oridecon.contracts.graphql.protocols.execution import (
    ResolverProtocol as ResolverProtocol,
)
from oridecon.contracts.graphql.protocols.execution import (
    SchemaBuilderProtocol as SchemaBuilderProtocol,
)
from oridecon.contracts.graphql.protocols.subscription import (
    DirectiveHandlerProtocol as DirectiveHandlerProtocol,
)
from oridecon.contracts.graphql.protocols.subscription import (
    MutationHandlerProtocol as MutationHandlerProtocol,
)
from oridecon.contracts.graphql.protocols.subscription import (
    SubscriptionAuthHandlerProtocol as SubscriptionAuthHandlerProtocol,
)
from oridecon.contracts.graphql.protocols.subscription import (
    SubscriptionHandlerProtocol as SubscriptionHandlerProtocol,
)
from oridecon.contracts.graphql.protocols.subscription import (
    WebSocketTransportProtocol as WebSocketTransportProtocol,
)
from oridecon.contracts.graphql.protocols.types import (
    ErrorFormatterProtocol as ErrorFormatterProtocol,
)
from oridecon.contracts.graphql.protocols.types import (
    GraphQLPrincipalResolverProtocol as GraphQLPrincipalResolverProtocol,
)
from oridecon.contracts.graphql.protocols.types import (
    GraphQLRequestProtocol as GraphQLRequestProtocol,
)
from oridecon.contracts.graphql.protocols.types import (
    IntrospectionHandlerProtocol as IntrospectionHandlerProtocol,
)
from oridecon.contracts.graphql.protocols.types import (
    ValidationRuleProtocol as ValidationRuleProtocol,
)

__all__ = [
    "DEFAULT_SUBSCRIPTIONS_PATH",
    "DataLoaderProtocol",
    "DirectiveHandlerProtocol",
    "EntityResolverProtocol",
    "ErrorFormatterProtocol",
    "GraphQLControllerProtocol",
    "GraphQLExecutorProtocol",
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
