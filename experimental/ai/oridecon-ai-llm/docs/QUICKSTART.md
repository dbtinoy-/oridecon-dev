---
title: oridecon-ai-llm Quickstart
description: Install `oridecon-ai-llm`, configure a provider, and make your first LLM call.
---

:::note[Maturity]
Alpha (0.1.x) — public APIs may change before 1.0.
:::

## Install

```bash
uv add oridecon-ai-llm
# Or with pip
pip install oridecon-ai-llm
```

Install a provider extra (at least one is required):

```bash
uv add "oridecon-ai-llm[openai]"
# or: uv add "oridecon-ai-llm[anthropic]"
# or: uv add "oridecon-ai-llm[ollama]"
```

## Minimal LLM call

```python
import asyncio
from oridecon import Application
from oridecon.ai.llm import LLMModule, ClientConfig


async def main() -> None:
    config = ClientConfig(
        provider="openai",
        model="gpt-4o",
        api_key="sk-...",
    )

    async with Application.boot(
        name="llm-demo",
        modules=[LLMModule.configure(config)],
    ) as app:
        from oridecon.contracts.ai import LLMClientProtocol

        llm = await app.container.resolve(LLMClientProtocol)
        result = await llm.complete([
            {"role": "user", "content": "What is the capital of France?"},
        ])

        if result.is_ok():
            print(result.unwrap().content)  # "Paris"
        else:
            print(f"Error: {result.unwrap_err()}")


asyncio.run(main())
```

## How it works

1. `LLMModule.configure(config)` creates a `DynamicModule` with an `LLMProvider`
2. The provider creates a client via `create_llm_client()` using the `ProviderRegistry`
3. `LLMClientProtocol` is registered in the container — resolve it anywhere
4. `llm.complete()` returns `Result[CompletionProtocol, LLMError]`

## Next steps

- [Guide](/packages/oridecon-ai-llm/guide/) — mental model, conversations, streaming, structured output
- [Architecture](/packages/oridecon-ai-llm/architecture/) — client layers, cache, model management
- [Configuration](/packages/oridecon-ai-llm/configuration/) — every config key
- [How-tos](/packages/oridecon-ai-llm/howtos/) — common recipes
