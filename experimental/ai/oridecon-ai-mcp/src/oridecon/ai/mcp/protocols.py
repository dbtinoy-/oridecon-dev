"""Re-export MCP protocols for consumer convenience.

Consumers use these contracts to depend on MCP abstractions without
importing the full oridecon-ai-mcp implementation.
"""

from __future__ import annotations

from oridecon.contracts.mcp.protocols import (
    MCPAuthorizerProtocol as MCPAuthorizerProtocol,
)
from oridecon.contracts.mcp.protocols import (
    MCPPromptHandlerProtocol as MCPPromptHandlerProtocol,
)
from oridecon.contracts.mcp.protocols import (
    MCPPromptProviderProtocol as MCPPromptProviderProtocol,
)
from oridecon.contracts.mcp.protocols import (
    MCPResourceHandlerProtocol as MCPResourceHandlerProtocol,
)
from oridecon.contracts.mcp.protocols import (
    MCPResourceProviderProtocol as MCPResourceProviderProtocol,
)
from oridecon.contracts.mcp.protocols import (
    MCPServerProtocol as MCPServerProtocol,
)
from oridecon.contracts.mcp.protocols import (
    MCPToolHandlerProtocol as MCPToolHandlerProtocol,
)
from oridecon.contracts.mcp.protocols import (
    MCPToolProviderProtocol as MCPToolProviderProtocol,
)
from oridecon.contracts.mcp.protocols import (
    MCPTransportProtocol as MCPTransportProtocol,
)

__all__ = [
    "MCPAuthorizerProtocol",
    "MCPPromptHandlerProtocol",
    "MCPPromptProviderProtocol",
    "MCPResourceHandlerProtocol",
    "MCPResourceProviderProtocol",
    "MCPServerProtocol",
    "MCPToolHandlerProtocol",
    "MCPToolProviderProtocol",
    "MCPTransportProtocol",
]
