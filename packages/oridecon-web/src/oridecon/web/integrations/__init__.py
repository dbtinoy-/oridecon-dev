"""Framework integrations: authentication, debugging, GraphQL, rate limiting."""

from __future__ import annotations

from oridecon.web.integrations.auth import AuthIntegration
from oridecon.web.integrations.cache import CacheIntegration
from oridecon.web.integrations.debug import DebugIntegration
from oridecon.web.integrations.graphql import GraphQLIntegration
from oridecon.web.integrations.rate_limit import RateLimitIntegration
from oridecon.web.integrations.setup import lifespan
from oridecon.web.integrations.sql import SQLIntegration
from oridecon.web.integrations.throttle import RateLimitModule, throttle

__all__ = [
    "AuthIntegration",
    "CacheIntegration",
    "DebugIntegration",
    "GraphQLIntegration",
    "RateLimitIntegration",
    "RateLimitModule",
    "SQLIntegration",
    "lifespan",
    "throttle",
]
