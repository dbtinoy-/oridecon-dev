"""RAG (Retrieval-Augmented Generation) module.

Root ``__init__.py`` exposes only the core pipeline API.
All specialised symbols remain importable from their subpackage paths, e.g.::

    from oridecon.ai.rag.evaluation import HallucinationDetector
    from oridecon.ai.rag.chunking import SemanticChunker
    from oridecon.ai.rag.hyde import SingleHyDEGenerator
"""

from __future__ import annotations

import importlib.metadata
from typing import TYPE_CHECKING, Any

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from oridecon.ai.rag.constants import __version__ as __version__

_LAZY_IMPORTS = {
    # DI Provider
    "RAGModule": "oridecon.ai.rag.module",
    "RAGProvider": "oridecon.ai.rag.di.provider",
    # Events
    "RetrievalCompletedEvent": "oridecon.ai.rag.events",
    "SynthesisCompletedEvent": "oridecon.ai.rag.events",
    # Hooks
    "RAGAnswerSynthesizedHook": "oridecon.ai.rag.hooks",
    "RAGDocumentsRetrievedHook": "oridecon.ai.rag.hooks",
    "RAGPipelineStartedHook": "oridecon.ai.rag.hooks",
    # Core types
    "Chunk": "oridecon.ai.rag.types",
    "Context": "oridecon.ai.rag.types",
    "RAGError": "oridecon.ai.rag.types",
    # Pipeline
    "RAGPipeline": "oridecon.ai.rag.pipeline",
    "PipelineBuilder": "oridecon.ai.rag.pipeline.builder",
    # Config
    "RAGConfig": "oridecon.ai.rag.config",
    "RAGTenancyConfig": "oridecon.ai.rag.config",
    "PipelineConfig": "oridecon.ai.rag.config",
    "IngestionConfig": "oridecon.ai.rag.config",
    "RetrievalConfig": "oridecon.ai.rag.config",
    "SynthesisConfig": "oridecon.ai.rag.config",
    # Chunking — factory + primary types only
    "ChunkingConfig": "oridecon.ai.rag.chunking",
    "create_chunker": "oridecon.ai.rag.chunking",
    # Cache
    "RAGCache": "oridecon.ai.rag.cache",
    # Tenancy
    "TenantScopedRAGPipeline": "oridecon.ai.rag.tenancy",
    # Strategy registries
    "RerankingStrategyRegistry": "oridecon.ai.rag.reranking.strategy_registry",
    "RetrievalStrategyRegistry": "oridecon.ai.rag.retrieval.strategy_registry",
    # Types
    "RerankResult": "oridecon.ai.rag.reranking.types",
    # Contracts re-exports
    "ChunkerProtocol": "oridecon.contracts.ai.vector",
}

if TYPE_CHECKING:
    from oridecon.ai.rag.cache import RAGCache
    from oridecon.ai.rag.chunking import (
        ChunkingConfig,
        create_chunker,
    )
    from oridecon.ai.rag.config import (
        IngestionConfig,
        PipelineConfig,
        RAGConfig,
        RAGTenancyConfig,
        RetrievalConfig,
        SynthesisConfig,
    )
    from oridecon.ai.rag.di.provider import RAGProvider
    from oridecon.ai.rag.events import (
        RetrievalCompletedEvent,
        SynthesisCompletedEvent,
    )
    from oridecon.ai.rag.hooks import (
        RAGAnswerSynthesizedHook,
        RAGDocumentsRetrievedHook,
        RAGPipelineStartedHook,
    )
    from oridecon.ai.rag.pipeline import RAGPipeline
    from oridecon.ai.rag.pipeline.builder import PipelineBuilder
    from oridecon.ai.rag.reranking.strategy_registry import (
        RerankingStrategyRegistry,
    )
    from oridecon.ai.rag.reranking.types import RerankResult
    from oridecon.ai.rag.retrieval.strategy_registry import (
        RetrievalStrategyRegistry,
    )
    from oridecon.ai.rag.tenancy import TenantScopedRAGPipeline
    from oridecon.ai.rag.types import (
        Chunk,
        Context,
        RAGError,
    )
    from oridecon.contracts.ai.vector import ChunkerProtocol


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib

        module = importlib.import_module(_LAZY_IMPORTS[name])
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__} has no attribute {name}")


def __dir__() -> list[str]:
    return __all__


__all__ = [
    "Chunk",
    "ChunkerProtocol",
    "ChunkingConfig",
    "Context",
    "IngestionConfig",
    "PipelineBuilder",
    "PipelineConfig",
    "RAGAnswerSynthesizedHook",
    "RAGCache",
    "RAGConfig",
    "RAGDocumentsRetrievedHook",
    "RAGError",
    "RAGModule",
    "RAGPipeline",
    "RAGPipelineStartedHook",
    "RAGProvider",
    "RAGTenancyConfig",
    "RerankResult",
    "RerankingStrategyRegistry",
    "RetrievalCompletedEvent",
    "RetrievalConfig",
    "RetrievalStrategyRegistry",
    "SynthesisCompletedEvent",
    "SynthesisConfig",
    "TenantScopedRAGPipeline",
    "create_chunker",
]
