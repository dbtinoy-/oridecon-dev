"""Public protocol surface for ``oridecon.nosql``."""

from __future__ import annotations

from oridecon.contracts.data.graph.protocols import GraphProtocol, GraphStoreProtocol
from oridecon.contracts.data.nosql.nosql import (
    CollectionProtocol,
    DocumentStoreProtocol,
)

__all__ = [
    "CollectionProtocol",
    "DocumentStoreProtocol",
    "GraphProtocol",
    "GraphStoreProtocol",
]
