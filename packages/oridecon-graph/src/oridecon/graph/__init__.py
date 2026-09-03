"""Oridecon Graph — Graph database backends for the Oridecon Framework.

Provides pluggable graph storage and traversal with Neo4j support.
Application code depends on ``GraphStoreProtocol`` from
``oridecon-contracts``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from oridecon.graph.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.contracts.data.graph.protocols import (
        GraphProtocol,
        GraphStoreProtocol,
    )
    from oridecon.graph.backends.base import BaseGraph, BaseGraphStore
    from oridecon.graph.backends.neo4j import Neo4jGraph, Neo4jGraphStore
    from oridecon.graph.config import GraphConfig, GraphTenancyConfig, Neo4jConfig
    from oridecon.graph.di.provider import GraphProvider
    from oridecon.graph.events import (
        GraphConnectedEvent,
        GraphDisconnectedEvent,
        GraphEdgeCreatedEvent,
        GraphNodeCreatedEvent,
        GraphQueryExecutedEvent,
    )
    from oridecon.graph.module import GraphModule

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # --- Base ---
    "BaseGraphStore": ("oridecon.graph.backends.base", "BaseGraphStore"),
    "BaseGraph": ("oridecon.graph.backends.base", "BaseGraph"),
    # --- Drivers ---
    "Neo4jGraphStore": ("oridecon.graph.backends.neo4j", "Neo4jGraphStore"),
    "Neo4jGraph": ("oridecon.graph.backends.neo4j", "Neo4jGraph"),
    # --- Events ---
    "GraphConnectedEvent": ("oridecon.graph.events", "GraphConnectedEvent"),
    "GraphDisconnectedEvent": ("oridecon.graph.events", "GraphDisconnectedEvent"),
    "GraphNodeCreatedEvent": ("oridecon.graph.events", "GraphNodeCreatedEvent"),
    "GraphEdgeCreatedEvent": ("oridecon.graph.events", "GraphEdgeCreatedEvent"),
    "GraphQueryExecutedEvent": ("oridecon.graph.events", "GraphQueryExecutedEvent"),
    # --- Framework ---
    "GraphConfig": ("oridecon.graph.config", "GraphConfig"),
    "GraphTenancyConfig": ("oridecon.graph.config", "GraphTenancyConfig"),
    "Neo4jConfig": ("oridecon.graph.config", "Neo4jConfig"),
    "GraphProvider": ("oridecon.graph.di.provider", "GraphProvider"),
    "GraphModule": ("oridecon.graph.module", "GraphModule"),
    # --- Protocols ---
    "GraphProtocol": ("oridecon.graph.protocols", "GraphProtocol"),
    "GraphStoreProtocol": ("oridecon.graph.protocols", "GraphStoreProtocol"),
    # --- Tenancy ---
    "TenantGraphStoreDecorator": (
        "oridecon.graph.tenancy.decorator",
        "TenantGraphStoreDecorator",
    ),
    "TenantPropertyFilterGraph": (
        "oridecon.graph.tenancy.decorator",
        "TenantPropertyFilterGraph",
    ),
}


def __getattr__(name: str) -> Any:
    """Lazy-load symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib  # noqa: PLC0415 — lazy-load pattern; heavy driver modules are deferred until first attribute access

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)


def __dir__() -> list[str]:
    """Enumerate available attributes for IDE support."""
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = [
    "BaseGraph",
    "BaseGraphStore",
    "GraphConfig",
    "GraphConnectedEvent",
    "GraphDisconnectedEvent",
    "GraphEdgeCreatedEvent",
    "GraphModule",
    "GraphNodeCreatedEvent",
    "GraphProtocol",
    "GraphProvider",
    "GraphQueryExecutedEvent",
    "GraphStoreProtocol",
    "GraphTenancyConfig",
    "Neo4jConfig",
    "Neo4jGraph",
    "Neo4jGraphStore",
    "TenantGraphStoreDecorator",
    "TenantPropertyFilterGraph",
]
