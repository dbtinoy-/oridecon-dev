"""LLM multi-provider routing package.

Provides a cascade-style router that tries providers in priority order
and records every attempt via a pluggable quota backend and inference logger.

Quick start::

    from oridecon.ai.llm.routing import (
        LLMRouter,
        LLMConfig,
        ProviderConfig,
        InferenceResult,
        InferenceError,
        InferenceLog,
        InMemoryQuotaBackend,
        InMemoryInferenceLogger,
    )

    config = LLMConfig.from_env()
    router = LLMRouter(
        config=config,
        clients={},
        quota_backend=InMemoryQuotaBackend(),
        inference_logger=InMemoryInferenceLogger(),
    )
    result = await router.route(messages=[{"role": "user", "content": "Hello"}])
"""

from __future__ import annotations

from oridecon.ai.llm.routing.ab_split import ABSplitConfig, ABSplitStrategy
from oridecon.ai.llm.routing.backends.database import DatabaseQuotaBackend
from oridecon.ai.llm.routing.backends.memory import InMemoryQuotaBackend
from oridecon.ai.llm.routing.config import (
    GenerationDefaults,
    LLMConfig,
    LogConfig,
    ProviderConfig,
    QuotaConfig,
)
from oridecon.ai.llm.routing.loggers.database import DatabaseInferenceLogger
from oridecon.ai.llm.routing.loggers.memory import InMemoryInferenceLogger
from oridecon.ai.llm.routing.orchestrator import (
    LLMOrchestrator,
    NoSuitableModelError,
    OrchestratorError,
)
from oridecon.ai.llm.routing.router import LLMRouter
from oridecon.ai.llm.routing.strategies import (
    CostOptimizedStrategy,
    LatencyOptimizedStrategy,
    ParallelRaceStrategy,
    RoutingStrategyProtocol,
    SequentialCascadeStrategy,
)
from oridecon.ai.llm.routing.types import (
    InferenceError,
    InferenceLog,
    InferenceResult,
    ProviderUsage,
)

__all__ = [
    "ABSplitConfig",
    "ABSplitStrategy",
    "CostOptimizedStrategy",
    "DatabaseInferenceLogger",
    "DatabaseQuotaBackend",
    "GenerationDefaults",
    "InMemoryInferenceLogger",
    "InMemoryQuotaBackend",
    "InferenceError",
    "InferenceLog",
    "InferenceResult",
    "LLMConfig",
    "LLMOrchestrator",
    "LLMRouter",
    "LatencyOptimizedStrategy",
    "LogConfig",
    "NoSuitableModelError",
    "OrchestratorError",
    "ParallelRaceStrategy",
    "ProviderConfig",
    "ProviderUsage",
    "QuotaConfig",
    "RoutingStrategyProtocol",
    "SequentialCascadeStrategy",
]
