"""MCP controller system — decorators, base class, and provider implementations."""

from __future__ import annotations

from oridecon.ai.mcp.controllers.base import MCPController
from oridecon.ai.mcp.controllers.decorators import prompt, resource, tool
from oridecon.ai.mcp.controllers.providers import (
    ControllerPromptProvider,
    ControllerResourceProvider,
    ControllerToolProvider,
    ModulePromptProvider,
    ModuleResourceProvider,
    ModuleToolProvider,
    ServiceToolProvider,
    _CombinedResourceProvider,
    _CombinedToolProvider,
)

__all__ = [
    "ControllerPromptProvider",
    "ControllerResourceProvider",
    "ControllerToolProvider",
    "MCPController",
    "ModulePromptProvider",
    "ModuleResourceProvider",
    "ModuleToolProvider",
    "ServiceToolProvider",
    "_CombinedResourceProvider",
    "_CombinedToolProvider",
    "prompt",
    "resource",
    "tool",
]
