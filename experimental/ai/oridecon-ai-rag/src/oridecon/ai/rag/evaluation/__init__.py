"""
RAG Evaluation Framework

This module provides comprehensive evaluation metrics for RAG systems
to measure retrieval quality, answer relevance, faithfulness, and overall performance.
"""

from __future__ import annotations

from oridecon.ai.rag.evaluation.answer import (
    AnswerFaithfulnessEvaluator,
    AnswerRelevanceEvaluator,
)
from oridecon.ai.rag.evaluation.base import EvaluatorBase
from oridecon.ai.rag.evaluation.context import ContextRelevanceEvaluator
from oridecon.ai.rag.evaluation.convenience import evaluate_rag
from oridecon.ai.rag.evaluation.evaluator import RAGEvaluator
from oridecon.ai.rag.evaluation.hallucination import HallucinationDetector
from oridecon.ai.rag.evaluation.harness import (
    BenchmarkReport,
    EvalExample,
    PipelineResult,
    RAGBenchmark,
)
from oridecon.ai.rag.evaluation.retrieval import (
    RetrievalPrecisionEvaluator,
    RetrievalRecallEvaluator,
)
from oridecon.ai.rag.evaluation.types import (
    EvaluationResult,
    MetricType,
    RAGEvaluationReport,
)

__all__ = [
    "AnswerFaithfulnessEvaluator",
    "AnswerRelevanceEvaluator",
    "BenchmarkReport",
    "ContextRelevanceEvaluator",
    "EvalExample",
    "EvaluationResult",
    "EvaluatorBase",
    "HallucinationDetector",
    "MetricType",
    "PipelineResult",
    "RAGBenchmark",
    "RAGEvaluationReport",
    "RAGEvaluator",
    "RetrievalPrecisionEvaluator",
    "RetrievalRecallEvaluator",
    "evaluate_rag",
]
