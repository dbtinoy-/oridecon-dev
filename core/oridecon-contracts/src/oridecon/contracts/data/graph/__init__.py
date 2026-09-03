"""Graph store contracts — protocols, types, and filter primitives."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from oridecon.contracts.data.graph.enums import (
        ConstraintKind,
        EdgeDirection,
        IndexKind,
        MergeAction,
        ReturnType,
    )
    from oridecon.contracts.data.graph.filters import (
        Prop,
        PropertyCondition,
        PropertyConditionGroup,
        PropertyFilter,
        PropertyOperator,
    )
    from oridecon.contracts.data.graph.protocols import (
        GraphProtocol,
        GraphStoreProtocol,
    )
    from oridecon.contracts.data.graph.tenancy import (
        GraphTenancyStrategy,
    )
    from oridecon.contracts.data.graph.types import (
        BulkEdgeResult,
        BulkNodeResult,
        ConstraintSpec,
        EdgeResult,
        EdgeSpec,
        GraphEdge,
        GraphInfo,
        GraphNode,
        GraphPath,
        IndexSpec,
        NodeResult,
        NodeSpec,
        StartSpec,
        TraversalQuery,
        TraversalStep,
    )
    from oridecon.contracts.data.types import LogicalOperator

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # --- Protocols ---
    "GraphStoreProtocol": (
        "oridecon.contracts.data.graph.protocols",
        "GraphStoreProtocol",
    ),
    "GraphProtocol": (
        "oridecon.contracts.data.graph.protocols",
        "GraphProtocol",
    ),
    # --- Types ---
    "GraphNode": ("oridecon.contracts.data.graph.types", "GraphNode"),
    "GraphEdge": ("oridecon.contracts.data.graph.types", "GraphEdge"),
    "GraphPath": ("oridecon.contracts.data.graph.types", "GraphPath"),
    "NodeSpec": ("oridecon.contracts.data.graph.types", "NodeSpec"),
    "EdgeSpec": ("oridecon.contracts.data.graph.types", "EdgeSpec"),
    "NodeResult": ("oridecon.contracts.data.graph.types", "NodeResult"),
    "EdgeResult": ("oridecon.contracts.data.graph.types", "EdgeResult"),
    "BulkNodeResult": ("oridecon.contracts.data.graph.types", "BulkNodeResult"),
    "BulkEdgeResult": ("oridecon.contracts.data.graph.types", "BulkEdgeResult"),
    "GraphInfo": ("oridecon.contracts.data.graph.types", "GraphInfo"),
    "StartSpec": ("oridecon.contracts.data.graph.types", "StartSpec"),
    "TraversalStep": ("oridecon.contracts.data.graph.types", "TraversalStep"),
    "TraversalQuery": ("oridecon.contracts.data.graph.types", "TraversalQuery"),
    "IndexSpec": ("oridecon.contracts.data.graph.types", "IndexSpec"),
    "ConstraintSpec": ("oridecon.contracts.data.graph.types", "ConstraintSpec"),
    # --- Enums ---
    "EdgeDirection": ("oridecon.contracts.data.graph.enums", "EdgeDirection"),
    "ReturnType": ("oridecon.contracts.data.graph.enums", "ReturnType"),
    "IndexKind": ("oridecon.contracts.data.graph.enums", "IndexKind"),
    "ConstraintKind": ("oridecon.contracts.data.graph.enums", "ConstraintKind"),
    "MergeAction": ("oridecon.contracts.data.graph.enums", "MergeAction"),
    # --- Tenancy ---
    "GraphTenancyStrategy": (
        "oridecon.contracts.data.graph.tenancy",
        "GraphTenancyStrategy",
    ),
    # --- Filters ---
    "Prop": ("oridecon.contracts.data.graph.filters", "Prop"),
    "PropertyFilter": ("oridecon.contracts.data.graph.filters", "PropertyFilter"),
    "PropertyCondition": ("oridecon.contracts.data.graph.filters", "PropertyCondition"),
    "PropertyConditionGroup": (
        "oridecon.contracts.data.graph.filters",
        "PropertyConditionGroup",
    ),
    "PropertyOperator": ("oridecon.contracts.data.graph.filters", "PropertyOperator"),
    "LogicalOperator": ("oridecon.contracts.data.types", "LogicalOperator"),
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
    "BulkEdgeResult",
    "BulkNodeResult",
    "ConstraintKind",
    "ConstraintSpec",
    "EdgeDirection",
    "EdgeResult",
    "EdgeSpec",
    "GraphEdge",
    "GraphInfo",
    "GraphNode",
    "GraphPath",
    "GraphProtocol",
    "GraphStoreProtocol",
    "GraphTenancyStrategy",
    "IndexKind",
    "IndexSpec",
    "LogicalOperator",
    "MergeAction",
    "NodeResult",
    "NodeSpec",
    "Prop",
    "PropertyCondition",
    "PropertyConditionGroup",
    "PropertyFilter",
    "PropertyOperator",
    "ReturnType",
    "StartSpec",
    "TraversalQuery",
    "TraversalStep",
]
