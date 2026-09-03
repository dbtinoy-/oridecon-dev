"""MCP adapters for integrating with other Oridecon components."""

from __future__ import annotations

from oridecon.ai.mcp.adapters.skill_adapter import SkillToolAdapter
from oridecon.ai.mcp.adapters.tool_adapter import ToolRegistryAdapter

__all__ = ["SkillToolAdapter", "ToolRegistryAdapter"]
