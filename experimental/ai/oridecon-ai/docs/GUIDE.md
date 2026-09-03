---
title: oridecon-ai Guide
description: Mental model, core concepts, and typical usage of `oridecon-ai`.
---

## Requirements

| Package | Required | Purpose |
|---------|----------|---------|
| `oridecon` | Yes | Core framework |
| `oridecon-contracts` | Yes | Protocol definitions |
| `oridecon-ai-llm` | Yes | LLM client integration |
| `oridecon-ai-rag` | Yes | RAG pipeline integration |
| `oridecon-ai-feedback` | Yes | Feedback collection |
| `oridecon-ai-observability` | Yes | Observability |
| `oridecon-ai-agents` | Optional | Agent system (runtime discovery) |
| `oridecon-ai-skills` | Optional | Skills system (runtime discovery) |
| `oridecon-ai-memory` | Optional | Memory system (runtime discovery) |
| `oridecon-ai-session` | Optional | Session management (runtime discovery) |
| `oridecon-ai-mcp` | Optional | MCP protocol (runtime discovery) |
| `oridecon-ai-workers` | Optional | Background workers (runtime discovery) |

## What problem does it solve?

`oridecon-ai` is the **orchestration layer** for the AI subsystem. Instead of wiring LLM clients, vector stores, RAG pipelines, and observability providers individually, you configure a single `AIConfig` and `AIModule` wires everything through the DI container.

It discovers sub-packages via Python entry points (`oridecon.ai.subsystems`), so installing a supported extension (e.g., `oridecon-ai-llm`) is enough — no manual registration.

## Mental model

```
AIConfig ──► AIModule.configure()
                  │
           AIProvider (register)
           ├── LLMProvider        (oridecon-ai-llm)
           ├── VectorProvider     (oridecon-vector, optional)
           ├── RAGProvider        (oridecon-ai-rag, optional)
           ├── Observability      (always on: metrics, tracing, health)
           ├── Governance         (optional)
           └── Entry-point discovery (any subsystem with ep group)
```

`AIModule` is the **public entrypoint**. `AIProvider` is the internal orchestrator that delegates to sub-providers.

## Core concepts

### AIConfig

The single config object that drives the entire AI subsystem. It nests sub-configs for each subsystem:

```python
from oridecon.ai.config import AIConfig
from oridecon.ai.llm import ClientConfig

config = AIConfig(
    enabled=True,
    llm=ClientConfig(provider="openai", model="gpt-4o"),
    # vector=VectorConfig(...),
    # rag=RAGConfig(...),
)
```

Config is read from `ORI_AI__*` environment variables or the `ai:` section of `application.yaml`.

### AIProvider

The provider class that orchestrates sub-providers. In `register()` it:
1. Registers monitoring singletons (`AIHealthMonitor`, `AIMetrics`, `AITracer`, `CallbackManagerProtocol`)
2. Delegates LLM, Vector, and RAG to their respective sub-providers
3. Discovers additional subsystems via `oridecon.ai.subsystems` entry points
4. Wires governance and RAG cache when the relevant config is present

```python
from oridecon.ai.di.provider import AIProvider

provider = AIProvider(config=AIConfig(llm=ClientConfig(provider="openai")))
# Used internally by AIModule — you normally don't instantiate it directly
```

### Entry-point discovery

Any installed package declaring the `oridecon.ai.subsystems` entry-point group is automatically discovered:

```toml
# pyproject.toml of a subsystem package
[project.entry-points."oridecon.ai.subsystems"]
llm = "oridecon.ai.llm.di.provider:LLMProvider"
```

The `AIProvider.register()` method loads each entry point and calls `sub_provider.register(container)`.

## Typical usage

### 1. Basic LLM access

```python
from oridecon import Application
from oridecon.ai.module import AIModule
from oridecon.ai.llm import ClientConfig
from oridecon.contracts.ai import LLMClientProtocol


async def main() -> None:
    config = AIConfig(llm=ClientConfig(provider="openai", model="gpt-4o"))
    async with Application.boot(
        name="ai-demo",
        modules=[AIModule.configure(config)],
    ) as app:
        llm = await app.container.resolve(LLMClientProtocol)
        result = await llm.complete([{"role": "user", "content": "Hello!"}])
        if result.is_ok():
            print(result.unwrap().content)
```

### 2. Health check

```python
from oridecon.contracts.core import HealthStatus

health = await app.health_check()
print(health.status)  # HealthStatus.HEALTHY or .DEGRADED
```

### 3. Manual provider wiring (no module)

```python
from oridecon import Application
from oridecon.ai.di.provider import AIProvider
from oridecon.ai.config import AIConfig

app = Application(name="ai-demo")
app.add_provider(AIProvider(config=AIConfig(llm=ClientConfig(provider="openai"))))
await app.start()
```

## Best practices

- **Start with `AIModule.configure()`** — it's the intended public API. Only drop to `AIProvider` directly when you need fine-grained control over sub-provider configuration.
- **One AIConfig per app** — the AI subsystem is designed as a singleton. Creating multiple instances will register duplicate bindings.
- **Use env vars for secrets** — set `ORI_AI_LLM__API_KEY` instead of hardcoding API keys. `AIConfig` reads environment variables automatically.
- **Enable governance in production** — `AIConfig(governance=GovernanceConfig(enabled=True))` provides an audit trail for AI operations.
- **Don't import sub-packages directly** — resolve `LLMClientProtocol` through the container instead of importing `LLMProvider` or individual clients.

## Next steps

- [Architecture](/packages/oridecon-ai/architecture/) — provider lifecycle and entry-point discovery
- [Configuration](/packages/oridecon-ai/configuration/) — every config key
- [How-tos](/packages/oridecon-ai/howtos/) — common recipes
- [LLM Package](/packages/oridecon-ai-llm/) — the LLM client layer in depth
