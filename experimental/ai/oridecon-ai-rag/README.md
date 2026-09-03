# oridecon-ai-rag

Retrieval-Augmented Generation (RAG) pipeline for the Oridecon Framework

---

## Overview

RAG (Retrieval-Augmented Generation) pipeline for the Oridecon Framework. Provides a multi-stage, fully configurable pipeline covering ingestion, query processing, retrieval, context optimisation, synthesis, quality assurance, and post-processing — all wired through the DI container via `RAGModule`. Zero-config usage starts with sensible defaults.


> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon-ai-rag
# Optional extras
uv add "oridecon-ai-rag[pdf,web]"
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module

from oridecon.ai.rag import RAGModule
from oridecon.ai.rag.config import RAGConfig


@module(
    imports=[
        RAGModule.configure(
            RAGConfig(
                vector_store_type="pgvector",
                collection_name="my_docs",
                top_k=5,
                enable_citations=True,
            )
        )
    ]
)
class AppModule(Module):
    pass


async with Application.boot(modules=[AppModule]) as app:
    # use app.container to resolve services
    ...
```

## Configuration

> **Zero-config usage:** Call `RAGModule.configure()` with no arguments to use defaults.

### Option 1 — YAML file

```yaml
# application.yaml
ai_rag:
  vector_store_type: "pgvector"
  collection_name: "my_docs"
  top_k: 5
  embedding_model: "text-embedding-ada-002"
  enable_citations: true
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_AI_RAG__VECTOR_STORE_TYPE=pgvector
# Environment variables for each field
```

### Option 3 — Python

```python
from oridecon.ai.rag.config import RAGConfig
from oridecon.ai.rag import RAGModule

config = RAGConfig(
    vector_store_type="pgvector",
    collection_name="my_docs",
    top_k=5,
)
RAGModule.configure(config)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `vector_store_type` | `pgvector` | `ORI_AI_RAG__VECTOR_STORE_TYPE` | Backend: `pgvector`, `chroma`, `qdrant`, `mock` |
| `collection_name` | `default` | `ORI_AI_RAG__COLLECTION_NAME` | Collection / index name |
| `vector_dimension` | `1536` | `ORI_AI_RAG__VECTOR_DIMENSION` | Embedding dimension |
| `top_k` | `5` | `ORI_AI_RAG__TOP_K` | Documents to retrieve per query |
| `similarity_threshold` | `0.7` | `ORI_AI_RAG__SIMILARITY_THRESHOLD` | Minimum similarity score to include |
| `use_hybrid_search` | `True` | `ORI_AI_RAG__USE_HYBRID_SEARCH` | Combine semantic + keyword search |
| `embedding_provider` | `openai` | `ORI_AI_RAG__EMBEDDING_PROVIDER` | Embedding provider |
| `embedding_model` | `None` | `ORI_AI_RAG__EMBEDDING_MODEL` | Embedding model |
| `chunking_strategy` | `recursive` | `ORI_AI_RAG__CHUNKING_STRATEGY` | `recursive`, `semantic`, or `token` |
| `chunk_size` | `512` | `ORI_AI_RAG__CHUNK_SIZE` | Tokens per chunk |
| `chunk_overlap` | `50` | `ORI_AI_RAG__CHUNK_OVERLAP` | Token overlap between chunks |
| `enable_citations` | `True` | `ORI_AI_RAG__ENABLE_CITATIONS` | Include source citations in responses |
| `citation_style` | `inline` | `ORI_AI_RAG__CITATION_STYLE` | `inline`, `footnote`, or `numbered` |
| `enable_query_expansion` | `True` | `ORI_AI_RAG__ENABLE_QUERY_EXPANSION` | Expand queries before retrieval |
| `enable_hyde` | `False` | `ORI_AI_RAG__ENABLE_HYDE` | Hypothetical Document Embeddings |
| `synthesis_strategy` | `hybrid` | `ORI_AI_RAG__SYNTHESIS_STRATEGY` | `direct`, `extractive`, `abstractive`, `hybrid` |
| `tenancy.enabled` | `False` | — | Enable per-tenant pipeline isolation |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `RAGModule.configure(config)` | Production pipeline |
| `RAGModule.stub()` | In-memory / no-op pipeline for tests |

## Key Features

- **Multi-stage pipeline**: Ingestion, query processing, retrieval, context optimization, synthesis, quality assurance, post-processing
- **Chunking strategies**: recursive, semantic, token, fixed_size, sliding_window
- **Retrieval**: Vector search with `top_k` / `similarity_threshold` controls
- **Reranking**: FlashRank cross-encoder reranker
- **Synthesis**: Direct, extractive, abstractive, and hybrid synthesizers
- **HyDE support**: Hypothetical Document Embeddings for query expansion
- **Citations**: Inline, footnote, or numbered citation styles
- **Quality assurance**: Faithfulness check and hallucination detection

## Testing

```python
async with Application.boot(modules=[RAGModule.stub()]) as app:
    # your test code
    ...
```

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/ai/rag/module.py` | `RAGModule.configure()` and `RAGModule.stub()` |
| `src/oridecon/ai/rag/config.py` | `RAGConfig`, `RAGTenancyConfig`, `PipelineConfig`, all stage configs |
| `src/oridecon/ai/rag/di/provider.py` | `RAGProvider` — registers pipeline and supporting services |
| `src/oridecon/ai/rag/pipeline/` | Stage executor and pipeline runner |
| `src/oridecon/ai/rag/tenancy/` | `TenantScopedRAGPipeline` factory + resolver |
| `src/oridecon/ai/rag/exceptions.py` | Full exception hierarchy |
| `src/oridecon/ai/rag/types.py` | RAG-specific domain types |

## Multi-Tenancy

`oridecon-ai-rag` supports per-tenant pipeline isolation. When tenancy is
enabled, the provider registers a `TenantScopedRAGPipeline` — a caching
wrapper that builds a dedicated `RAGPipelineProtocol` per tenant, with a
tenant-resolved `collection_name`.

> **Note:** Enabling tenancy requires the app-wide `Context` binding, which
> ships with the core bootstrap module (`CoreModule` / `StandardModule` from
> `oridecon.app`). A bare `Application.boot(modules=[RAGModule...])` without
> it fails with `UnresolvableDependencyError: Context`.

### Configuration

```python
from oridecon.ai.rag import RAGModule
from oridecon.ai.rag.config import RAGConfig, RAGTenancyConfig

config = RAGConfig(
    tenancy=RAGTenancyConfig(enabled=True),
    collection_name="my_docs",
)
RAGModule.configure(config)
```

### Per-Tenant Collection Name

Use `RAGConfig.with_collection()` to create configs scoped to different
collection names — handy for dynamic per-tenant pipeline construction:

```python
tenant_config = RAGConfig().with_collection("tenant_a_collection")
```

### Components

| Component | Role |
|-----------|------|
| `RAGTenancyConfig` | Dataclass with `enabled` flag |
| `TenantScopedRAGPipeline` | Caches per-tenant pipelines (LRU eviction) |
| `TemplatedTenantCollectionResolver` | Resolves logical → physical collection name per tenant |
