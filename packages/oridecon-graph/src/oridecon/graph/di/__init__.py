"""DI provider for the graph sub-namespace of oridecon-nosql."""

from __future__ import annotations

from oridecon.graph.di.provider import GraphProvider
from oridecon.graph.module import GraphModule

__all__ = ["GraphModule", "GraphProvider"]
