---
title: oridecon-ai Quickstart
description: Install `oridecon-ai`, configure providers, and make your first AI call.
---

:::note[Maturity]
Alpha (0.1.x) — public APIs may change before 1.0.
:::

## Install

```bash
uv add oridecon-ai
# Or with pip
pip install oridecon-ai
```

`oridecon-ai` depends on `oridecon`, `oridecon-contracts`, `oridecon-ai-llm`, `oridecon-ai-rag`, `oridecon-ai-feedback`, and `oridecon-ai-observability`.

## Minimal wiring

```python
import asyncio
from oridecon import Application
from oridecon.ai.module import AIModule
from oridecon.ai.llm import ClientConfig


async def main() -> None:
    config = AIConfig(
        llm=ClientConfig(
            provider="openai",
            model="gpt-4o",
            api_key="sk-...",
        ),
    )

    async with Application.boot(
        name="ai-demo",
        modules=[AIModule.configure(config)],
    ) as app:
        # LLMClientProtocol is now injectable
        from oridecon.contracts.ai import LLMClientProtocol

        llm = await app.container.resolve(LLMClientProtocol)
        result = await llm.complete([{"role": "user", "content": "Say hello!"}])

        if result.is_ok():
            print(result.unwrap().content)
        else:
            print(f"Error: {result.unwrap_err()}")


asyncio.run(main())
```

## What you get

`AIModule.configure(config)` registers the **AIProvider** which wires:
- **LLM** — multi-provider client (OpenAI, Anthropic, Ollama, Groq, Mistral, …)
- **Vector** — vector store backends (optional, requires `oridecon-vector`)
- **RAG** — retrieval-augmented generation pipelines (optional)
- **Observability** — AI tracing, metrics, and health monitoring
- **Governance** — audit logging and policy enforcement (optional)

## Next steps

- [Guide](/packages/oridecon-ai/guide/) — mental model, core concepts, end-to-end workflows
- [Architecture](/packages/oridecon-ai/architecture/) — provider composition and entry-point discovery
- [Configuration](/packages/oridecon-ai/configuration/) — all config keys and env-var overrides
- [Ecosystem](/ecosystem/) — related AI packages
