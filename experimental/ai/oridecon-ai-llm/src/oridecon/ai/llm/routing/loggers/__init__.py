"""Inference logger implementations for LLM routing."""

from __future__ import annotations

from oridecon.ai.llm.routing.loggers.database import DatabaseInferenceLogger
from oridecon.ai.llm.routing.loggers.memory import InMemoryInferenceLogger

__all__ = [
    "DatabaseInferenceLogger",
    "InMemoryInferenceLogger",
]
