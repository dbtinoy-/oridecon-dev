"""MCP exceptions - re-exported from contracts.

This module re-exports the MCP error hierarchy from oridecon-contracts
for convenient access within the oridecon-mcp package.

Extensions that need to add package-specific exceptions can extend
the base classes from oridecon.contracts.mcp.exceptions.
"""

from __future__ import annotations

from oridecon.contracts.mcp.exceptions import (
    MCPError,
    MCPInitializationError,
    MCPMethodNotFoundError,
    MCPPromptError,
    MCPProtocolError,
    MCPResourceError,
    MCPToolCallError,
    MCPTransportError,
)

__all__ = [
    "MCPError",
    "MCPInitializationError",
    "MCPMethodNotFoundError",
    "MCPPromptError",
    "MCPProtocolError",
    "MCPResourceError",
    "MCPToolCallError",
    "MCPTransportError",
]
