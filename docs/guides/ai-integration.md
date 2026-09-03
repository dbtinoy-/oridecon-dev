---
title: "AI Integration"
description: "Build intelligent applications with the Oridecon AI packages — LLMs, RAG, agents, and memory."
---

Oridecon ships a modular AI stack built on the same contract-first foundation as the rest of the framework. You program against protocols (`LLMClientProtocol`, `RAGPipelineProtocol`, …), so providers and models are swappable through configuration alone.

The AI layer is composed of focused, independently installable packages:

| Package | Purpose |
|---------|---------|
| `oridecon-ai` | Orchestration layer — discovers and wires the AI subsystems below |
| `oridecon-ai-llm` | Multi-provider LLM client (OpenAI, Anthropic, Gemini, Ollama, Groq, Mistral, …) |
| `oridecon-ai-rag` | Retrieval-augmented generation pipeline |
| `oridecon-vector` | Vector store backends (pgvector, Qdrant, Pinecone, in-memory) |
| `oridecon-ai-agents` | Agents with tools and strategies (ReAct, plan-and-execute) |
| `oridecon-ai-memory` | Episodic, semantic, and working memory |
| `oridecon-ai-session` | Conversation sessions — branching, checkpointing, multi-agent |
| `oridecon-ai-skills` | Skill/tool registry and executor |
| `oridecon-ai-mcp` | Model Context Protocol server and client |
| `oridecon-ai-workers` | Background AI work — batch embedding, document ingestion |
| `oridecon-ai-observability` | Tracing, metrics, and health checks for AI calls |
| `oridecon-ai-feedback` | Feedback collection and processing |
| `oridecon-ai-evaluation` | LLM output evaluation (Q&A, string/embedding distance, trajectory, criteria) and reproducible experiment tracking |

---

## 1. Configuring the LLM Client

`oridecon-ai-llm` exposes a single `LLMClientProtocol` and selects the concrete provider from configuration. Wire it through the AI module:

```python
from oridecon import Application
from oridecon.ai import AIModule, AIConfig
from oridecon.ai.llm import ClientConfig


def create_app() -> Application:
    app = Application(name="my-ai-app")
    app.add_module(
        AIModule.configure(
            AIConfig(llm=ClientConfig(provider="anthropic", model="claude-sonnet-4-6"))
        )
    )
    return app
```

Equivalent YAML — providers are an ordered list under the `ai_llm` section (the first is highest priority):

```yaml title="application.yaml"
ai_llm:
  enabled: true
  strategy: sequential          # sequential | parallel_race | cost_optimized | latency_optimized
  providers:
    - name: primary
      model: claude-sonnet-4-6
      api_key: "${ANTHROPIC_API_KEY}"
  defaults:
    temperature: 0.2
```

:::tip
Prefer environment variables for secrets. Any config key maps to an env var with the `ORI_` prefix and `__` for nesting, e.g. `ORI_AI_LLM__PROVIDERS__PRIMARY__API_KEY` (providers are keyed by name).
:::

---

## 2. Calling the LLM

Inject `LLMClientProtocol` and call `complete()`. It returns a `Result` — there are no exceptions for expected failures (rate limits, provider errors):

```python
from oridecon.contracts.ai.llm import LLMClientProtocol
from oridecon.result import Result


class ChatService:
    def __init__(self, llm: LLMClientProtocol) -> None:
        self._llm = llm

    async def reply(self, prompt: str) -> str:
        result = await self._llm.complete(
            messages=[{"role": "user", "content": prompt}],
        )
        if result.is_err():
            return f"LLM error: {result.unwrap_err()}"
        return result.unwrap().content
```

`complete()` accepts a plain message list and supports `model`, `temperature`, `max_tokens`, `tools`, and `stop_sequences` overrides. For token-by-token output, use `stream_chat(...)`, which returns an async stream of chunks.

---

## 3. Thinking Suppression

Some models (Qwen3, Gemma, and other reasoning models served via LM Studio / vLLM / SGLang) emit chain-of-thought tokens by default, adding 20–30s of latency. Oridecon can suppress this at the provider level via `ThinkingConfig`:

```python
from oridecon.contracts.ai.thinking import ThinkingConfig
from oridecon.ai.llm import ClientConfig

ClientConfig(
    provider="lmstudio",
    model="qwen3",
    thinking=ThinkingConfig(suppress=True),   # inject `enable_thinking: false`
)
```

Or per provider in the routing config / via env var:

```bash
ORI_AI_LLM__PROVIDERS__PRIMARY__SUPPRESS_THINKING=true
```

`ThinkingConfig` also exposes `budget_tokens` (Anthropic, Gemini 2.5), `effort` (OpenAI o-series), and `level` (Gemini 3) for models where you *want* reasoning but with a bound.

---

## 4. Retrieval-Augmented Generation (RAG)

`oridecon-ai-rag` coordinates chunking, embedding, vector retrieval, and synthesis behind `RAGPipelineProtocol`. Configure it with `RAGModule`:

```python
from oridecon.ai.rag import RAGModule, RAGConfig

app.add_module(
    RAGModule.configure(
        RAGConfig(
            chunk_size=512,
            top_k=5,
            embedding_provider="openai",
            embedding_model="text-embedding-3-small",
        )
    )
)
```

Then query through the injected pipeline:

```python
from oridecon.contracts.ai.rag import RAGPipelineProtocol, RAGContext


class DocsService:
    def __init__(self, rag: RAGPipelineProtocol) -> None:
        self._rag = rag

    async def ask(self, question: str) -> str:
        result = await self._rag.execute(RAGContext(query=question))
        answer = result.unwrap()
        return answer.answer  # plus citations / sources when enabled
```

The vector backend (pgvector, Qdrant, Pinecone, or in-memory for tests) is provided by `oridecon-vector` and selected via the `vector` config section — your RAG code never changes when you switch stores.

---

## 5. Agents, Memory & Sessions

For multi-step reasoning, `oridecon-ai-agents` provides agents that call **tools** and follow strategies such as **ReAct** and **plan-and-execute**. Pair them with:

- `oridecon-ai-skills` — a registry of callable tools the agent can invoke.
- `oridecon-ai-memory` — episodic / semantic / working memory across turns.
- `oridecon-ai-session` — durable conversations with branching and checkpointing.

These compose through the container like any other Oridecon services. See the per-package guides under [the ecosystem](/ecosystem/) for the exact tool-registration and executor APIs.

---

## 6. Observability

`oridecon-ai-observability` adds tracing, metrics, and health checks around AI calls — giving you visibility into latency, token usage, and retrieval steps without changing your service code:

```yaml title="application.yaml"
ai_observability:
  enabled: true
  metrics_enabled: true
  tracing_enabled: true
  health_checks_enabled: true
```

---

## Next Steps

- [The Ecosystem](/ecosystem/) — every public package at a glance
- [Configuration](/getting-started/configuration/) — sections, profiles, and env-var overrides
- [Result Pattern](/fundamentals/result-pattern/) — how `complete()` and `query()` report failures
