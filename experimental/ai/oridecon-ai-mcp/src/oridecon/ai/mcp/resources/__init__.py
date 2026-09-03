"""Built-in MCP resource providers."""

from __future__ import annotations

from oridecon.ai.mcp.resources.config import ConfigResourceProvider
from oridecon.ai.mcp.resources.database import DatabaseResourceProvider
from oridecon.ai.mcp.resources.search import SearchResourceProvider

__all__ = [
    "ConfigResourceProvider",
    "DatabaseResourceProvider",
    "SearchResourceProvider",
]
