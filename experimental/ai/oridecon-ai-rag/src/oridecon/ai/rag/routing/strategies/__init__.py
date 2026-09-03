"""Routing strategies for query routing."""

from __future__ import annotations

from oridecon.ai.rag.routing.strategies.base import RoutingStrategy
from oridecon.ai.rag.routing.strategies.hybrid import HybridRouter
from oridecon.ai.rag.routing.strategies.llm import LLMRouter
from oridecon.ai.rag.routing.strategies.rule_based import RuleBasedRouter
from oridecon.ai.rag.routing.strategies.semantic import SemanticRouter

__all__ = [
    "HybridRouter",
    "LLMRouter",
    "RoutingStrategy",
    "RuleBasedRouter",
    "SemanticRouter",
]
