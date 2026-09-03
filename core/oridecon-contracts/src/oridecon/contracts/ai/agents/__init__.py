"""Agent contracts for the Oridecon framework.

Exceptions, types, and protocols for agents, tools, and strategies.
"""

from __future__ import annotations

from oridecon.contracts.ai.agents.exceptions import AgentError as AgentError
from oridecon.contracts.ai.agents.exceptions import StrategyError as StrategyError
from oridecon.contracts.ai.agents.exceptions import ToolError as ToolError
from oridecon.contracts.ai.agents.protocols import (
    AgentExecutorProtocol as AgentExecutorProtocol,
)
from oridecon.contracts.ai.agents.protocols import AgentProtocol as AgentProtocol
from oridecon.contracts.ai.agents.protocols import (
    AgentStrategyProtocol as AgentStrategyProtocol,
)
from oridecon.contracts.ai.agents.protocols import MemoryProtocol as MemoryProtocol
from oridecon.contracts.ai.agents.protocols import (
    RunnableAgentProtocol as RunnableAgentProtocol,
)
from oridecon.contracts.ai.agents.protocols import (
    SkillComposerProtocol as SkillComposerProtocol,
)
from oridecon.contracts.ai.agents.protocols import StrategyProtocol as StrategyProtocol
from oridecon.contracts.ai.agents.protocols import ToolProtocol as ToolProtocol
from oridecon.contracts.ai.agents.protocols import (
    ToolRegistryProtocol as ToolRegistryProtocol,
)
from oridecon.contracts.ai.agents.types import AgentEvent as AgentEvent
from oridecon.contracts.ai.agents.types import AgentEventType as AgentEventType
from oridecon.contracts.ai.agents.types import (
    AgentExecutionContext as AgentExecutionContext,
)
from oridecon.contracts.ai.agents.types import AgentResponse as AgentResponse
from oridecon.contracts.ai.agents.types import ToolDefinition as ToolDefinition
from oridecon.contracts.ai.agents.types import ToolResult as ToolResult

__all__ = [
    "AgentError",
    "AgentEvent",
    "AgentEventType",
    "AgentExecutionContext",
    "AgentExecutorProtocol",
    "AgentProtocol",
    "AgentResponse",
    "AgentStrategyProtocol",
    "MemoryProtocol",
    "RunnableAgentProtocol",
    "SkillComposerProtocol",
    "StrategyError",
    "StrategyProtocol",
    "ToolDefinition",
    "ToolError",
    "ToolProtocol",
    "ToolRegistryProtocol",
    "ToolResult",
]
