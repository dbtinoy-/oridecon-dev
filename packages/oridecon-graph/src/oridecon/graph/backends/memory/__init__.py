"""In-memory graph backend."""

from __future__ import annotations

from oridecon.graph.backends.memory.backend import InMemoryGraphStore
from oridecon.graph.backends.memory.graph import InMemoryGraph

__all__ = ["InMemoryGraph", "InMemoryGraphStore"]
