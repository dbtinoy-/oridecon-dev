"""User-facing decorators for oridecon-ai-mcp.

Applied by application developers when defining MCP tools, resources,
and prompts for model context protocol servers.
"""

from __future__ import annotations

from oridecon.ai.mcp.controllers.decorators import (
    prompt as prompt,
)
from oridecon.ai.mcp.controllers.decorators import (
    resource as resource,
)
from oridecon.ai.mcp.controllers.decorators import (
    tool as tool,
)

__all__ = ["prompt", "resource", "tool"]
