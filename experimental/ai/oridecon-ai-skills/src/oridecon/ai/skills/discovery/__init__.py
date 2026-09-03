"""Discovery utilities for auto-registration of skills from modules and MCP."""

from __future__ import annotations

from oridecon.ai.skills.discovery.mcp_bridge import MCPSkillBridge
from oridecon.ai.skills.discovery.module_scanner import ModuleScanner
from oridecon.ai.skills.discovery.skill_loader import SkillLoader
from oridecon.ai.skills.discovery.skill_source_scanner import SkillSourceScanner

__all__ = [
    "MCPSkillBridge",
    "ModuleScanner",
    "SkillLoader",
    "SkillSourceScanner",
]
