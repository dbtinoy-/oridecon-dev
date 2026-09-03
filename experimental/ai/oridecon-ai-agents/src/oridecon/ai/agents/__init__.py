"""oridecon-ai-agents — Agent system for Oridecon Framework.

Canonical import paths
-----------------------
AgentBase class:     from oridecon.ai.agents import AgentBase
Tool decorator:      from oridecon.ai.agents import tool
Tool registry:       from oridecon.ai.agents import ToolRegistryImpl
Agent executor:      from oridecon.ai.agents import AgentExecutorImpl
ReAct strategy:      from oridecon.ai.agents import ReActStrategy
Crew:                from oridecon.ai.agents import Crew
CrewTask:            from oridecon.ai.agents import CrewTask
CrewBuilder:         from oridecon.ai.agents import CrewBuilder
Process:             from oridecon.ai.agents import Process

Quick Start
-----------

    from oridecon.ai.agents import AgentBase, tool

    @tool
    async def lookup_order(order_id: str) -> dict:
        \"\"\"Look up an order by its ID.\"\"\"
        return {"order_id": order_id, "status": "shipped"}

    class OrderAgent(AgentBase):
        name = "order_agent"
        system_prompt = "You are a helpful order support agent."

        @property
        def tools(self):
            return [lookup_order]
"""

from __future__ import annotations

import importlib.metadata
import pkgutil
from typing import TYPE_CHECKING, Any

__path__ = pkgutil.extend_path(__path__, __name__)

from oridecon.ai.agents.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.ai.agents.agent import AgentBase, AgentBuilder
    from oridecon.ai.agents.config import AgentConfig
    from oridecon.ai.agents.crew import (
        Crew,
        CrewBuilder,
        CrewExecutionResult,
        CrewRunner,
        CrewTask,
        Process,
        TaskResult,
    )
    from oridecon.ai.agents.decorators import strategy
    from oridecon.ai.agents.delegation import AgentAsToolAdapter
    from oridecon.ai.agents.di.provider import AgentsProvider
    from oridecon.ai.agents.events import (
        AgentRunCompletedEvent,
        ToolExecutionCompletedEvent,
    )
    from oridecon.ai.agents.exceptions import (
        AgentConfigurationError,
        AgentError,
        AgentExecutionError,
        BudgetExceededError,
        MaxIterationsExceededError,
        StrategyError,
        ToolAccessDeniedError,
        ToolError,
        ToolExecutionError,
        ToolNotFoundError,
    )
    from oridecon.ai.agents.executor import AgentExecutorImpl
    from oridecon.ai.agents.hooks import (
        AgentCompletedHook,
        AgentStartedHook,
        AgentToolCalledHook,
    )
    from oridecon.ai.agents.module import AgentsModule
    from oridecon.ai.agents.protocols import ObserverProtocol, PlannerProtocol
    from oridecon.ai.agents.strategies import (
        AbstractStrategy,
        PlanAndExecuteStrategy,
        PlanStepStatus,
        ReActStrategy,
        ReflexionStrategy,
        SupervisorStrategy,
    )
    from oridecon.ai.agents.strategies.strategy_registry import AgentStrategyRegistry
    from oridecon.ai.agents.tools import AbstractTool, ToolRegistryImpl, tool
    from oridecon.ai.agents.types import (
        AgentResponse,
        ReasoningStep,
        ToolExecutionRecord,
    )

_LAZY_IMPORTS: dict[str, str] = {
    # Events
    "AgentRunCompletedEvent": "oridecon.ai.agents.events",
    # Hooks
    "AgentCompletedHook": "oridecon.ai.agents.hooks",
    "AgentStartedHook": "oridecon.ai.agents.hooks",
    "AgentToolCalledHook": "oridecon.ai.agents.hooks",
    "AbstractStrategy": "oridecon.ai.agents.strategies",
    "AbstractTool": "oridecon.ai.agents.tools",
    "AgentAsToolAdapter": "oridecon.ai.agents.delegation",
    "AgentBase": "oridecon.ai.agents.agent",
    "AgentBuilder": "oridecon.ai.agents.agent",
    "AgentConfig": "oridecon.ai.agents.config",
    "AgentStrategyRegistry": "oridecon.ai.agents.strategies.strategy_registry",
    "Crew": "oridecon.ai.agents.crew",
    "CrewBuilder": "oridecon.ai.agents.crew",
    "CrewExecutionResult": "oridecon.ai.agents.crew",
    "CrewRunner": "oridecon.ai.agents.crew",
    "CrewTask": "oridecon.ai.agents.crew",
    "Process": "oridecon.ai.agents.crew",
    "TaskResult": "oridecon.ai.agents.crew",
    "AgentConfigurationError": "oridecon.ai.agents.exceptions",
    "AgentError": "oridecon.ai.agents.exceptions",
    "AgentExecutionError": "oridecon.ai.agents.exceptions",
    "AgentExecutorImpl": "oridecon.ai.agents.executor",
    "AgentResponse": "oridecon.ai.agents.types",
    "AgentsModule": "oridecon.ai.agents.module",
    "AgentsProvider": "oridecon.ai.agents.di.provider",
    "BudgetExceededError": "oridecon.ai.agents.exceptions",
    "MaxIterationsExceededError": "oridecon.ai.agents.exceptions",
    "PlanAndExecuteStrategy": "oridecon.ai.agents.strategies",
    "PlanStepStatus": "oridecon.ai.agents.strategies",
    "ReActStrategy": "oridecon.ai.agents.strategies",
    "ReflexionStrategy": "oridecon.ai.agents.strategies",
    "SupervisorStrategy": "oridecon.ai.agents.strategies",
    "ReasoningStep": "oridecon.ai.agents.types",
    "strategy": "oridecon.ai.agents.decorators",
    "StrategyError": "oridecon.ai.agents.exceptions",
    "ToolAccessDeniedError": "oridecon.ai.agents.exceptions",
    "ToolExecutionCompletedEvent": "oridecon.ai.agents.events",
    "ToolExecutionRecord": "oridecon.ai.agents.types",
    "ToolError": "oridecon.ai.agents.exceptions",
    "ToolExecutionError": "oridecon.ai.agents.exceptions",
    "ToolNotFoundError": "oridecon.ai.agents.exceptions",
    "ToolRegistryImpl": "oridecon.ai.agents.tools",
    "tool": "oridecon.ai.agents.tools",
    # Internal protocols
    "PlannerProtocol": "oridecon.ai.agents.protocols",
    "ObserverProtocol": "oridecon.ai.agents.protocols",
}


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib as _importlib

        module = _importlib.import_module(_LAZY_IMPORTS[name])
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = [
    "AbstractStrategy",
    "AbstractTool",
    "AgentAsToolAdapter",
    "AgentBase",
    "AgentBuilder",
    "AgentCompletedHook",
    "AgentConfig",
    "AgentConfigurationError",
    "AgentError",
    "AgentExecutionError",
    "AgentExecutorImpl",
    "AgentResponse",
    "AgentRunCompletedEvent",
    "AgentStartedHook",
    "AgentStrategyRegistry",
    "AgentToolCalledHook",
    "AgentsModule",
    "AgentsProvider",
    "BudgetExceededError",
    "Crew",
    "CrewBuilder",
    "CrewExecutionResult",
    "CrewRunner",
    "CrewTask",
    "MaxIterationsExceededError",
    "ObserverProtocol",
    "PlanAndExecuteStrategy",
    "PlanStepStatus",
    "PlannerProtocol",
    "Process",
    "ReActStrategy",
    "ReasoningStep",
    "ReflexionStrategy",
    "StrategyError",
    "SupervisorStrategy",
    "TaskResult",
    "ToolAccessDeniedError",
    "ToolError",
    "ToolExecutionCompletedEvent",
    "ToolExecutionError",
    "ToolExecutionRecord",
    "ToolNotFoundError",
    "ToolRegistryImpl",
    "strategy",
    "tool",
]
