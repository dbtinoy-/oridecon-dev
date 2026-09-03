"""oridecon-ai-memory — three-tier AI memory for the Oridecon Framework.

Provides working, episodic, and semantic memory tiers with pluggable
backends, consolidation scheduling, and multi-source retrieval.
"""

from __future__ import annotations

import importlib.metadata
from typing import TYPE_CHECKING

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from oridecon.ai.memory.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.ai.memory.config import MemoryConfig
    from oridecon.ai.memory.di.provider import MemoryProvider
    from oridecon.ai.memory.events import (
        MemoryRetrievedEvent,
        MemoryStoredEvent,
    )
    from oridecon.ai.memory.hooks import (
        MemoryConsolidatedHook,
        MemoryRetrievedHook,
        MemoryWrittenHook,
    )
    from oridecon.ai.memory.module import MemoryModule
    from oridecon.ai.memory.protocols import (
        ConsolidationStrategyProtocol,
        MemoryIndexProtocol,
    )
    from oridecon.ai.memory.pruning.pruner import DynamicContextPruner
    from oridecon.ai.memory.retrieval.retriever import MemoryRetriever
    from oridecon.ai.memory.working.conversation_buffer import ConversationBuffer

_LAZY_IMPORTS: dict[str, str] = {
    # --- Events ---
    "MemoryRetrievedEvent": "oridecon.ai.memory.events",
    "MemoryStoredEvent": "oridecon.ai.memory.events",
    # --- Hooks ---
    "MemoryConsolidatedHook": "oridecon.ai.memory.hooks",
    "MemoryRetrievedHook": "oridecon.ai.memory.hooks",
    "MemoryWrittenHook": "oridecon.ai.memory.hooks",
    # --- Backends ---
    "CacheMemoryBackend": "oridecon.ai.memory.backends.cache",
    "DatabaseMemoryBackend": "oridecon.ai.memory.backends.database",
    "InMemoryMemoryBackend": "oridecon.ai.memory.backends.in_memory",
    "VectorMemoryBackend": "oridecon.ai.memory.backends.vector",
    # --- Config ---
    "ConsolidationConfig": "oridecon.ai.memory.config",
    "EpisodicMemoryConfig": "oridecon.ai.memory.config",
    "MemoryConfig": "oridecon.ai.memory.config",
    "SemanticMemoryConfig": "oridecon.ai.memory.config",
    "WorkingMemoryConfig": "oridecon.ai.memory.config",
    # --- Consolidation ---
    "MemoryConsolidator": "oridecon.ai.memory.consolidation.consolidator",
    "ConsolidationScheduler": "oridecon.ai.memory.consolidation.scheduler",
    "AccessFrequencyStrategy": "oridecon.ai.memory.consolidation.strategies",
    "DeduplicationStrategy": "oridecon.ai.memory.consolidation.strategies",
    "RecencyDecayStrategy": "oridecon.ai.memory.consolidation.strategies",
    # --- DI ---
    "MemoryModule": "oridecon.ai.memory.module",
    "MemoryProvider": "oridecon.ai.memory.di.provider",
    # --- Episodic ---
    "EpisodicCompressor": "oridecon.ai.memory.episodic.compressor",
    "EpisodicMemoryStore": "oridecon.ai.memory.episodic.store",
    # --- Exceptions ---
    "ConsolidationError": "oridecon.ai.memory.exceptions",
    "EmbeddingError": "oridecon.ai.memory.exceptions",
    "FactExtractionError": "oridecon.ai.memory.exceptions",
    "MemoryCapacityError": "oridecon.ai.memory.exceptions",
    "MemoryStoreError": "oridecon.ai.memory.exceptions",
    "MemorySystemError": "oridecon.ai.memory.exceptions",
    # --- Retrieval ---
    "RelevanceRanker": "oridecon.ai.memory.retrieval.ranking",
    "MemoryRetriever": "oridecon.ai.memory.retrieval.retriever",
    # --- Semantic ---
    "EntityExtractor": "oridecon.ai.memory.semantic.entity_extractor",
    "FactStore": "oridecon.ai.memory.semantic.fact_store",
    "SemanticMemoryStore": "oridecon.ai.memory.semantic.store",
    # --- Stores ---
    "BufferMemoryStore": "oridecon.ai.memory.stores.buffer",
    "ConversationMemoryStore": "oridecon.ai.memory.stores.conversation",
    "EntityMemoryStore": "oridecon.ai.memory.stores.entity",
    "SummaryMemoryStore": "oridecon.ai.memory.stores.summary",
    # --- Pruning ---
    "DynamicContextPruner": "oridecon.ai.memory.pruning.pruner",
    "HybridScorerImpl": "oridecon.ai.memory.pruning.scorer",
    "RecencyScorerImpl": "oridecon.ai.memory.pruning.scorer",
    "RelevanceScorerProtocol": "oridecon.ai.memory.pruning.scorer",
    "PruningResult": "oridecon.ai.memory.pruning.types",
    "PruningStrategy": "oridecon.ai.memory.pruning.types",
    # --- Working ---
    "ConversationBuffer": "oridecon.ai.memory.working.conversation_buffer",
    "WorkingMemoryManager": "oridecon.ai.memory.working.manager",
    "TokenBudgetAllocator": "oridecon.ai.memory.working.token_budget",
    # Internal protocols
    "MemoryIndexProtocol": "oridecon.ai.memory.protocols",
    "ConsolidationStrategyProtocol": "oridecon.ai.memory.protocols",
}


def __getattr__(name: str) -> object:
    if name in _LAZY_IMPORTS:
        import importlib

        module = importlib.import_module(_LAZY_IMPORTS[name])
        value = getattr(module, name)
        globals()[name] = value
        return value
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = list(_LAZY_IMPORTS.keys())
