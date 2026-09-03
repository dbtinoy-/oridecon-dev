"""Speculative execution module — draft-verify pattern and tool pre-fetching."""

from __future__ import annotations

from oridecon.ai.agents.speculation.draft_verify import DraftVerifyExecutor
from oridecon.ai.agents.speculation.predictor import KeywordToolCallPredictor
from oridecon.ai.agents.speculation.prefetcher import SpeculativeToolPreFetcher
from oridecon.ai.agents.speculation.protocols import ToolCallPredictorProtocol

__all__ = [
    "DraftVerifyExecutor",
    "KeywordToolCallPredictor",
    "SpeculativeToolPreFetcher",
    "ToolCallPredictorProtocol",
]
