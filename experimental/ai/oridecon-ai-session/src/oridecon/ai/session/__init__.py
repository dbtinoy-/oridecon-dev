"""oridecon-ai-session — stateful conversation session management.

Provides tools for managing conversation history, branching,
checkpointing, and multi-agent group sessions.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from typing import TYPE_CHECKING, Any

try:
    __version__ = version("oridecon-ai-session")
except PackageNotFoundError:
    __version__ = "0.0.0"

if TYPE_CHECKING:
    from oridecon.ai.session.analytics.core import SessionAnalytics
    from oridecon.ai.session.branching.branch_manager import BranchManager
    from oridecon.ai.session.branching.merge import (
        AppendMerge,
        MergeStrategy,
        SelectiveMerge,
    )
    from oridecon.ai.session.checkpointing.checkpoint_manager import CheckpointManager
    from oridecon.ai.session.checkpointing.diff import StateDiff
    from oridecon.ai.session.config import SessionConfig
    from oridecon.ai.session.context import RelevanceContextPruner, SessionContext
    from oridecon.ai.session.di.provider import SessionProvider
    from oridecon.ai.session.exceptions import (
        CheckpointNotFoundError,
        SessionCapacityError,
        SessionClosedError,
        SessionError,
        SessionExpiredError,
        SessionNotFoundError,
        SessionTransitionError,
    )
    from oridecon.ai.session.hooks import (
        SessionCheckpointCreatedHook,
        SessionClosedHook,
        SessionStartedHook,
    )
    from oridecon.ai.session.manager import SessionManagerImpl
    from oridecon.ai.session.middleware.session_middleware import SessionMiddleware
    from oridecon.ai.session.module import SessionModule
    from oridecon.ai.session.multi_agent.group_session import GroupSession
    from oridecon.ai.session.multi_agent.role_isolation import RoleIsolation
    from oridecon.ai.session.multi_agent.turn_manager import (
        PriorityTurnManager,
        RoundRobinTurnManager,
        TopicBasedTurnManager,
        TurnManager,
    )
    from oridecon.ai.session.state import SessionStateMachine
    from oridecon.ai.session.stores.cache import CacheSessionStore
    from oridecon.ai.session.stores.database import DatabaseSessionStore
    from oridecon.ai.session.stores.in_memory import InMemorySessionStore
    from oridecon.ai.session.types import Metadata, SessionId, TurnId

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # --- Branching ---
    "BranchManager": ("oridecon.ai.session.branching.branch_manager", "BranchManager"),
    "AppendMerge": ("oridecon.ai.session.branching.merge", "AppendMerge"),
    "MergeStrategy": ("oridecon.ai.session.branching.merge", "MergeStrategy"),
    "SelectiveMerge": ("oridecon.ai.session.branching.merge", "SelectiveMerge"),
    # --- Checkpointing ---
    "CheckpointManager": (
        "oridecon.ai.session.checkpointing.checkpoint_manager",
        "CheckpointManager",
    ),
    "StateDiff": ("oridecon.ai.session.checkpointing.diff", "StateDiff"),
    # --- Config ---
    "SessionConfig": ("oridecon.ai.session.config", "SessionConfig"),
    # --- Context ---
    "SessionContext": ("oridecon.ai.session.context", "SessionContext"),
    "RelevanceContextPruner": ("oridecon.ai.session.context", "RelevanceContextPruner"),
    # --- DI ---
    "SessionProvider": ("oridecon.ai.session.di.provider", "SessionProvider"),
    # --- Analytics ---
    "SessionAnalytics": ("oridecon.ai.session.analytics.core", "SessionAnalytics"),
    # --- Exceptions ---
    "CheckpointNotFoundError": (
        "oridecon.ai.session.exceptions",
        "CheckpointNotFoundError",
    ),
    "SessionCapacityError": ("oridecon.ai.session.exceptions", "SessionCapacityError"),
    "SessionClosedError": ("oridecon.ai.session.exceptions", "SessionClosedError"),
    "SessionError": ("oridecon.ai.session.exceptions", "SessionError"),
    "SessionExpiredError": ("oridecon.ai.session.exceptions", "SessionExpiredError"),
    "SessionNotFoundError": ("oridecon.ai.session.exceptions", "SessionNotFoundError"),
    "SessionTransitionError": (
        "oridecon.ai.session.exceptions",
        "SessionTransitionError",
    ),
    # --- Hooks ---
    "SessionCheckpointCreatedHook": (
        "oridecon.ai.session.hooks",
        "SessionCheckpointCreatedHook",
    ),
    "SessionClosedHook": ("oridecon.ai.session.hooks", "SessionClosedHook"),
    "SessionStartedHook": ("oridecon.ai.session.hooks", "SessionStartedHook"),
    # --- Manager ---
    "SessionManager": ("oridecon.ai.session.manager", "SessionManagerImpl"),
    "SessionManagerImpl": ("oridecon.ai.session.manager", "SessionManagerImpl"),
    # --- Middleware ---
    "SessionMiddleware": (
        "oridecon.ai.session.middleware.session_middleware",
        "SessionMiddleware",
    ),
    # --- Module ---
    "SessionModule": ("oridecon.ai.session.module", "SessionModule"),
    # --- Multi-Agent ---
    "GroupSession": ("oridecon.ai.session.multi_agent.group_session", "GroupSession"),
    "RoleIsolation": (
        "oridecon.ai.session.multi_agent.role_isolation",
        "RoleIsolation",
    ),
    "PriorityTurnManager": (
        "oridecon.ai.session.multi_agent.turn_manager",
        "PriorityTurnManager",
    ),
    "RoundRobinTurnManager": (
        "oridecon.ai.session.multi_agent.turn_manager",
        "RoundRobinTurnManager",
    ),
    "TopicBasedTurnManager": (
        "oridecon.ai.session.multi_agent.turn_manager",
        "TopicBasedTurnManager",
    ),
    "TurnManager": ("oridecon.ai.session.multi_agent.turn_manager", "TurnManager"),
    # --- State ---
    "SessionStateMachine": ("oridecon.ai.session.state", "SessionStateMachine"),
    # --- Stores ---
    "CacheSessionStore": ("oridecon.ai.session.stores.cache", "CacheSessionStore"),
    "DatabaseSessionStore": (
        "oridecon.ai.session.stores.database",
        "DatabaseSessionStore",
    ),
    "InMemorySessionStore": (
        "oridecon.ai.session.stores.in_memory",
        "InMemorySessionStore",
    ),
    # --- Types ---
    "Metadata": ("oridecon.ai.session.types", "Metadata"),
    "SessionId": ("oridecon.ai.session.types", "SessionId"),
    "TurnId": ("oridecon.ai.session.types", "TurnId"),
    # --- Events ---
    "SessionCreatedEvent": ("oridecon.ai.session.events", "SessionCreatedEvent"),
    "SessionClosedEvent": ("oridecon.ai.session.events", "SessionClosedEvent"),
    # --- Protocols ---
    "ContextPrunerProtocol": ("oridecon.ai.session.protocols", "ContextPrunerProtocol"),
    "SessionContextProtocol": (
        "oridecon.ai.session.protocols",
        "SessionContextProtocol",
    ),
    "SessionManagerProtocol": (
        "oridecon.ai.session.protocols",
        "SessionManagerProtocol",
    ),
    "SessionStoreProtocol": ("oridecon.ai.session.protocols", "SessionStoreProtocol"),
}


def __getattr__(name: str) -> Any:
    """Lazy-load symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """Enumerate available attributes for IDE support."""
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = list(_LAZY_IMPORTS)
