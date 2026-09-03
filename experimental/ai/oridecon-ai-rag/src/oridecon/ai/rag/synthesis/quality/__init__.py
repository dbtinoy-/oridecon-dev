"""Quality control components for response synthesis.

This package provides components for checking and ensuring response quality,
including faithfulness, relevance, hallucination detection, and confidence scoring.
"""

from __future__ import annotations

from oridecon.ai.rag.synthesis.quality.confidence import ConfidenceScorer
from oridecon.ai.rag.synthesis.quality.faithfulness import FaithfulnessChecker
from oridecon.ai.rag.synthesis.quality.hallucination import (
    HallucinationChecker,
)
from oridecon.ai.rag.synthesis.quality.relevance import RelevanceFilter

__all__ = [
    "ConfidenceScorer",
    "FaithfulnessChecker",
    "HallucinationChecker",
    "RelevanceFilter",
]
