"""Oridecon Vector — Vector store backends for the Oridecon Framework."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from typing import TYPE_CHECKING, Any

try:
    __version__ = version("oridecon-vector")
except PackageNotFoundError:
    __version__ = "0.0.0"

if TYPE_CHECKING:
    from oridecon.vector.adapters.document_store import DocumentVectorStoreAdapter
    from oridecon.vector.adapters.vector_store import VectorStoreAdapter
    from oridecon.vector.backends.base import BaseVectorCollection, BaseVectorStore
    from oridecon.vector.backends.chroma import ChromaStore
    from oridecon.vector.backends.memory import MemoryVectorStore
    from oridecon.vector.backends.pgvector import PgVectorStore
    from oridecon.vector.backends.pinecone import PineconeStore
    from oridecon.vector.backends.qdrant import QdrantStore
    from oridecon.vector.config import (
        MemoryConfig,
        NamedVectorConfig,
        PgVectorConfig,
        PineconeConfig,
        QdrantConfig,
        VectorConfig,
    )
    from oridecon.vector.di.factories import create_vector_store
    from oridecon.vector.di.provider import VectorProvider
    from oridecon.vector.embedding.cache import EmbeddingCache, InMemoryEmbeddingCache
    from oridecon.vector.embedding.client import OpenAICompatibleEmbeddingClient
    from oridecon.vector.embedding.config import EmbeddingClientConfig
    from oridecon.vector.events import (
        VectorDeletedEvent,
        VectorIndexedEvent,
        VectorSearchedEvent,
    )
    from oridecon.vector.exceptions import (
        CollectionAlreadyExistsError,
        CollectionNotFoundError,
        DimensionMismatchError,
        FilterCompilationError,
        VectorConfigError,
        VectorConnectionError,
        VectorDeleteError,
        VectorError,
        VectorSearchError,
        VectorTimeoutError,
        VectorUpsertError,
    )
    from oridecon.vector.module import VectorModule
    from oridecon.vector.search.hybrid import (
        BM25Retriever,
        HybridRetriever,
        HybridSearchConfig,
        RRFReranker,
        create_hybrid_retriever,
    )
    from oridecon.vector.search.reranking import (
        CrossEncoderReranker,
        DiversityReranker,
        RerankerPipeline,
        RerankingConfig,
        RerankingStrategy,
        SimilarityReranker,
        create_reranker,
    )
    from oridecon.vector.testing.mocks import (
        MockVectorStore,
        MockVectorStoreWithErrors,
        MockVectorStoreWithSimilarity,
    )
    from oridecon.vector.types import Embedding

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "BaseVectorCollection": ("oridecon.vector.backends.base", "BaseVectorCollection"),
    "BaseVectorStore": ("oridecon.vector.backends.base", "BaseVectorStore"),
    "BM25Retriever": ("oridecon.vector.search.hybrid", "BM25Retriever"),
    "ChromaStore": ("oridecon.vector.backends.chroma", "ChromaStore"),
    "CollectionAlreadyExistsError": (
        "oridecon.vector.exceptions",
        "CollectionAlreadyExistsError",
    ),
    "CollectionNotFoundError": (
        "oridecon.vector.exceptions",
        "CollectionNotFoundError",
    ),
    "CrossEncoderReranker": (
        "oridecon.vector.search.reranking",
        "CrossEncoderReranker",
    ),
    "DimensionMismatchError": ("oridecon.vector.exceptions", "DimensionMismatchError"),
    "DiversityReranker": ("oridecon.vector.search.reranking", "DiversityReranker"),
    "DocumentVectorStoreAdapter": (
        "oridecon.vector.adapters.document_store",
        "DocumentVectorStoreAdapter",
    ),
    "Embedding": ("oridecon.vector.types", "Embedding"),
    "EmbeddingCache": ("oridecon.vector.embedding.cache", "EmbeddingCache"),
    "EmbeddingClientConfig": (
        "oridecon.vector.embedding.config",
        "EmbeddingClientConfig",
    ),
    "FilterCompilationError": ("oridecon.vector.exceptions", "FilterCompilationError"),
    "HybridRetriever": ("oridecon.vector.search.hybrid", "HybridRetriever"),
    "HybridSearchConfig": ("oridecon.vector.search.hybrid", "HybridSearchConfig"),
    "InMemoryEmbeddingCache": (
        "oridecon.vector.embedding.cache",
        "InMemoryEmbeddingCache",
    ),
    "MemoryConfig": ("oridecon.vector.config", "MemoryConfig"),
    "MemoryVectorStore": ("oridecon.vector.backends.memory", "MemoryVectorStore"),
    "MockVectorStore": ("oridecon.vector.testing.mocks", "MockVectorStore"),
    "MockVectorStoreWithErrors": (
        "oridecon.vector.testing.mocks",
        "MockVectorStoreWithErrors",
    ),
    "MockVectorStoreWithSimilarity": (
        "oridecon.vector.testing.mocks",
        "MockVectorStoreWithSimilarity",
    ),
    "NamedVectorConfig": ("oridecon.vector.config", "NamedVectorConfig"),
    "OpenAICompatibleEmbeddingClient": (
        "oridecon.vector.embedding.client",
        "OpenAICompatibleEmbeddingClient",
    ),
    "PgVectorConfig": ("oridecon.vector.config", "PgVectorConfig"),
    "PgVectorStore": ("oridecon.vector.backends.pgvector", "PgVectorStore"),
    "PineconeConfig": ("oridecon.vector.config", "PineconeConfig"),
    "PineconeStore": ("oridecon.vector.backends.pinecone", "PineconeStore"),
    "QdrantConfig": ("oridecon.vector.config", "QdrantConfig"),
    "QdrantStore": ("oridecon.vector.backends.qdrant", "QdrantStore"),
    "RRFReranker": ("oridecon.vector.search.hybrid", "RRFReranker"),
    "RerankingConfig": ("oridecon.vector.search.reranking", "RerankingConfig"),
    "RerankingStrategy": ("oridecon.vector.search.reranking", "RerankingStrategy"),
    "RerankerPipeline": ("oridecon.vector.search.reranking", "RerankerPipeline"),
    "SimilarityReranker": ("oridecon.vector.search.reranking", "SimilarityReranker"),
    "VectorConfig": ("oridecon.vector.config", "VectorConfig"),
    "VectorConfigError": ("oridecon.vector.exceptions", "VectorConfigError"),
    "VectorConnectionError": ("oridecon.vector.exceptions", "VectorConnectionError"),
    "VectorDeletedEvent": ("oridecon.vector.events", "VectorDeletedEvent"),
    "VectorDeleteError": ("oridecon.vector.exceptions", "VectorDeleteError"),
    "VectorError": ("oridecon.vector.exceptions", "VectorError"),
    "VectorIndexedEvent": ("oridecon.vector.events", "VectorIndexedEvent"),
    "VectorModule": ("oridecon.vector.module", "VectorModule"),
    "VectorProvider": ("oridecon.vector.di.provider", "VectorProvider"),
    "VectorSearchedEvent": ("oridecon.vector.events", "VectorSearchedEvent"),
    "VectorSearchError": ("oridecon.vector.exceptions", "VectorSearchError"),
    "VectorStoreAdapter": (
        "oridecon.vector.adapters.vector_store",
        "VectorStoreAdapter",
    ),
    "VectorTenancyConfig": ("oridecon.vector.config", "VectorTenancyConfig"),
    "VectorTimeoutError": ("oridecon.vector.exceptions", "VectorTimeoutError"),
    "VectorUpsertError": ("oridecon.vector.exceptions", "VectorUpsertError"),
    # Tenancy
    "TemplatedTenantCollectionResolver": (
        "oridecon.vector.tenancy.resolver",
        "TemplatedTenantCollectionResolver",
    ),
    "PineconeNamespaceTenantResolver": (
        "oridecon.vector.tenancy.pinecone_namespace",
        "PineconeNamespaceTenantResolver",
    ),
    "TenantVectorStoreDecorator": (
        "oridecon.vector.tenancy.decorator",
        "TenantVectorStoreDecorator",
    ),
    "create_hybrid_retriever": (
        "oridecon.vector.search.hybrid",
        "create_hybrid_retriever",
    ),
    "create_reranker": ("oridecon.vector.search.reranking", "create_reranker"),
    "create_vector_store": ("oridecon.vector.di.factories", "create_vector_store"),
    # Hooks
    "VectorIndexedHook": ("oridecon.vector.hooks", "VectorIndexedHook"),
    "VectorSearchedHook": ("oridecon.vector.hooks", "VectorSearchedHook"),
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


__all__ = [
    "BM25Retriever",
    "BaseVectorCollection",
    "BaseVectorStore",
    "ChromaStore",
    "CollectionAlreadyExistsError",
    "CollectionNotFoundError",
    "CrossEncoderReranker",
    "DimensionMismatchError",
    "DiversityReranker",
    "DocumentVectorStoreAdapter",
    "Embedding",
    "EmbeddingCache",
    "EmbeddingClientConfig",
    "FilterCompilationError",
    "HybridRetriever",
    "HybridSearchConfig",
    "InMemoryEmbeddingCache",
    "MemoryConfig",
    "MemoryVectorStore",
    "MockVectorStore",
    "MockVectorStoreWithErrors",
    "MockVectorStoreWithSimilarity",
    "NamedVectorConfig",
    "OpenAICompatibleEmbeddingClient",
    "PgVectorConfig",
    "PgVectorStore",
    "PineconeConfig",
    "PineconeNamespaceTenantResolver",
    "PineconeStore",
    "QdrantConfig",
    "QdrantStore",
    "RRFReranker",
    "RerankerPipeline",
    "RerankingConfig",
    "RerankingStrategy",
    "SimilarityReranker",
    "TemplatedTenantCollectionResolver",
    "TenantVectorStoreDecorator",
    "VectorConfig",
    "VectorConfigError",
    "VectorConnectionError",
    "VectorDeleteError",
    "VectorDeletedEvent",
    "VectorError",
    "VectorIndexedEvent",
    "VectorIndexedHook",
    "VectorModule",
    "VectorProvider",
    "VectorSearchError",
    "VectorSearchedEvent",
    "VectorSearchedHook",
    "VectorStoreAdapter",
    "VectorTenancyConfig",
    "VectorTimeoutError",
    "VectorUpsertError",
    "create_hybrid_retriever",
    "create_reranker",
    "create_vector_store",
]
