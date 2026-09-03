"""Oridecon AI Skills — composable, registry-based skill execution platform."""

from __future__ import annotations

import importlib.metadata
from typing import TYPE_CHECKING

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from oridecon.ai.skills.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.ai.skills.base import AbstractSkill
    from oridecon.ai.skills.executor import SkillExecutor
    from oridecon.ai.skills.hooks import (
        SkillExecutedHook,
        SkillExecutionFailedHook,
        SkillRegisteredHook,
    )
    from oridecon.ai.skills.registry import SkillRegistry

_LAZY_IMPORTS: dict[str, str] = {
    # --- Base ---
    "AbstractSkill": "oridecon.ai.skills.base",
    "FunctionSkill": "oridecon.ai.skills.base",
    "ToolSkillAdapter": "oridecon.ai.skills.base",
    # --- Hooks ---
    "SkillExecutedHook": "oridecon.ai.skills.hooks",
    "SkillExecutionFailedHook": "oridecon.ai.skills.hooks",
    "SkillRegisteredHook": "oridecon.ai.skills.hooks",
    # --- Builtin ---
    "CodeExecutionSkill": "oridecon.ai.skills.builtin.code_execution",
    "DatabaseQuerySkill": "oridecon.ai.skills.builtin.database_query",
    "DateTimeSkill": "oridecon.ai.skills.builtin.datetime_skill",
    "FileReadSkill": "oridecon.ai.skills.builtin.file_operations",
    "FileWriteSkill": "oridecon.ai.skills.builtin.file_operations",
    "HTTPRequestSkill": "oridecon.ai.skills.builtin.http_request",
    "MathSkill": "oridecon.ai.skills.builtin.math_skill",
    "TextSummarizeSkill": "oridecon.ai.skills.builtin.text_processing",
    "TextTranslateSkill": "oridecon.ai.skills.builtin.text_processing",
    "WebSearchSkill": "oridecon.ai.skills.builtin.web_search",
    # --- Caching ---
    "SkillResultCache": "oridecon.ai.skills.caching.skill_cache",
    # --- Composition ---
    "SkillChain": "oridecon.ai.skills.composition.chain",
    "ParallelSkills": "oridecon.ai.skills.composition.parallel",
    "SkillPipeline": "oridecon.ai.skills.composition.pipeline",
    "SkillRouter": "oridecon.ai.skills.composition.router",
    # --- Config ---
    "SkillsConfig": "oridecon.ai.skills.config",
    # --- Decorators ---
    "skill": "oridecon.ai.skills.decorators",
    "skill_param": "oridecon.ai.skills.decorators",
    # --- DI ---
    "SkillsProvider": "oridecon.ai.skills.di.provider",
    # --- Discovery ---
    "MCPSkillBridge": "oridecon.ai.skills.discovery.mcp_bridge",
    "ModuleScanner": "oridecon.ai.skills.discovery.module_scanner",
    "SkillSourceScanner": "oridecon.ai.skills.discovery.skill_source_scanner",
    "SkillLoader": "oridecon.ai.skills.discovery.skill_loader",
    # --- Exceptions ---
    "SkillAlreadyRegisteredError": "oridecon.ai.skills.exceptions",
    "SkillExecutionError": "oridecon.ai.skills.exceptions",
    "SkillNotFoundError": "oridecon.ai.skills.exceptions",
    "SkillPermissionDeniedError": "oridecon.ai.skills.exceptions",
    "SkillRoutingError": "oridecon.ai.skills.exceptions",
    "SkillTimeoutError": "oridecon.ai.skills.exceptions",
    "SkillValidationError": "oridecon.ai.skills.exceptions",
    # --- Executor ---
    "SkillExecutor": "oridecon.ai.skills.executor",
    # --- Module ---
    "SkillsModule": "oridecon.ai.skills.module",
    # --- Permissions ---
    "PermissionChecker": "oridecon.ai.skills.permissions.permission_checker",
    # --- Registry ---
    "SkillRegistry": "oridecon.ai.skills.registry",
    # --- Validation ---
    "validate_params": "oridecon.ai.skills.validation.schema",
    "validate_non_empty_string": "oridecon.ai.skills.validation.validators",
    "validate_positive_int": "oridecon.ai.skills.validation.validators",
    "validate_range": "oridecon.ai.skills.validation.validators",
    # --- Contracts ---
    "SkillDefinition": "oridecon.contracts.ai.skills",
    "SkillError": "oridecon.contracts.ai.skills",
    "SkillExecutorProtocol": "oridecon.contracts.ai.skills",
    "SkillProtocol": "oridecon.contracts.ai.skills",
    "SkillRegistryProtocol": "oridecon.contracts.ai.skills",
    "SkillResult": "oridecon.contracts.ai.skills",
    # --- Events ---
    "SkillExecutedEvent": "oridecon.ai.skills.events",
}


def __getattr__(name: str) -> object:
    if name in _LAZY_IMPORTS:
        import importlib

        module = importlib.import_module(_LAZY_IMPORTS[name])
        value = getattr(module, name)
        globals()[name] = value
        return value
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = list(_LAZY_IMPORTS.keys())
