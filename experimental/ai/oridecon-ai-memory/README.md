# oridecon-ai-memory

AI memory system for the Oridecon Framework — episodic, semantic, and working memory

---

## Overview

Three-tier AI memory system for the Oridecon Framework. Provides working, episodic, and semantic memory with pluggable backends, automatic consolidation scheduling, token-aware context assembly, and multi-source retrieval — all wired through the DI container via `MemoryModule`. Zero-config usage starts with sensible defaults.


> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon-ai-memory
# Optional extras
uv add "oridecon-ai-memory[redis]"
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module

from oridecon.ai.memory import MemoryModule
from oridecon.ai.memory.config import MemoryConfig


@module(imports=[MemoryModule.configure(MemoryConfig(default_backend="in_memory"))])
class AppModule(Module):
    pass


async with Application.boot(modules=[AppModule]) as app:
    # use app.container to resolve services
    ...
```

## Configuration

> **Zero-config usage:** Call `MemoryModule.configure()` with no arguments to use defaults.

### Option 1 — YAML file

```yaml
# application.yaml
ai_memory:
  default_backend: "vector"
  ttl_seconds: 2592000
  consolidation:
    enabled: true
    interval_seconds: 3600.0
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_AI_MEMORY__DEFAULT_BACKEND=vector
# Environment variables for each field
```

### Option 3 — Python

```python
from oridecon.ai.memory.config import MemoryConfig
from oridecon.ai.memory import MemoryModule

config = MemoryConfig(
    default_backend="vector",
)
MemoryModule.configure(config)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `enabled` | `True` | `ORI_AI_MEMORY__ENABLED` | Enable the AI memory subsystem |
| `default_backend` | `"in_memory"` | `ORI_AI_MEMORY__DEFAULT_BACKEND` | Backend type: `in_memory`, `cache`, `database`, `vector` |
| `ttl_seconds` | `2592000` | `ORI_AI_MEMORY__TTL_SECONDS` | Default entry TTL in seconds (0 = never expire) |
| `working.system_prompt_tokens` | `512` | `ORI_AI_MEMORY__WORKING__SYSTEM_PROMPT_TOKENS` | Fixed token allocation for system prompt |
| `working.recent_turns_fraction` | `0.4` | `ORI_AI_MEMORY__WORKING__RECENT_TURNS_FRACTION` | Fraction of remaining budget for recent turns |
| `episodic.default_top_k` | `10` | `ORI_AI_MEMORY__EPISODIC__DEFAULT_TOP_K` | Default number of episodes to retrieve |
| `semantic.min_confidence` | `0.5` | `ORI_AI_MEMORY__SEMANTIC__MIN_CONFIDENCE` | Minimum confidence score for stored facts |
| `consolidation.enabled` | `True` | `ORI_AI_MEMORY__CONSOLIDATION__ENABLED` | Whether automatic background consolidation is active |
| `consolidation.interval_seconds` | `3600.0` | `ORI_AI_MEMORY__CONSOLIDATION__INTERVAL_SECONDS` | How often to run a consolidation pass |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `MemoryModule.configure(config, enable_consolidation)` | Production-ready module with full consolidation pipeline |
| `MemoryModule.stub(config)` | Test-friendly module with in-memory backends |

## Key Features

- **Three-tier memory**: Working (context assembly), Episodic (conversation episodes), Semantic (entity facts)
- **Pluggable backends**: In-memory, Redis, SQLAlchemy, Qdrant/Chroma/PGVector
- **Token budget allocation**: Distributes available tokens across memory sources
- **Automatic consolidation**: Background scheduler promotes episodic to semantic storage
- **Multi-source retrieval**: Unified `MemoryRetriever` queries all tiers with relevance ranking
- **Dynamic pruning**: `DynamicContextPruner` fits context into hard token limits

## Testing

```python
async with Application.boot(modules=[MemoryModule.stub()]) as app:
    # your test code
    ...
```

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/ai/memory/module.py` | `MemoryModule` — DI module factory methods |
| `src/oridecon/ai/memory/config.py` | `MemoryConfig` and tier-specific config classes |
| `src/oridecon/ai/memory/di/provider.py` | `MemoryProvider` — wires all protocols and services |
| `src/oridecon/ai/memory/working/manager.py` | `WorkingMemoryManager` — context assembly |
| `src/oridecon/ai/memory/episodic/store.py` | `EpisodicMemoryStore` — episode storage |
| `src/oridecon/ai/memory/semantic/store.py` | `SemanticMemoryStore` — fact storage |
| `src/oridecon/ai/memory/consolidation/consolidator.py` | `MemoryConsolidator` — consolidation pipeline |
| `src/oridecon/ai/memory/retrieval/retriever.py` | `MemoryRetriever` — multi-source retrieval |
