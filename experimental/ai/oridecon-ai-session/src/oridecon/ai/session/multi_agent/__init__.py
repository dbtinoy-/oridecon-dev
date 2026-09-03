"""Multi-agent subpackage — group sessions with coordinated turn-taking."""

from __future__ import annotations

from oridecon.ai.session.multi_agent.group_session import GroupSession
from oridecon.ai.session.multi_agent.role_isolation import RoleIsolation
from oridecon.ai.session.multi_agent.turn_manager import (
    PriorityTurnManager,
    RoundRobinTurnManager,
    TopicBasedTurnManager,
    TurnManager,
)

__all__ = [
    "GroupSession",
    "PriorityTurnManager",
    "RoleIsolation",
    "RoundRobinTurnManager",
    "TopicBasedTurnManager",
    "TurnManager",
]
