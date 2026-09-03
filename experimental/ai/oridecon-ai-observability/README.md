# oridecon-ai-observability

AI observability for the Oridecon Framework — tracing, metrics, and monitoring

---

## Overview

AI-layer observability for the Oridecon Framework. Provides tracing, metrics, health monitoring, and decorator-based instrumentation for LLM calls, RAG operations, and vector store interactions — all wired through the DI container via `ObservabilityModule`. Zero-config usage starts with sensible defaults.


> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon-ai-observability
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module

from oridecon.ai.observability import ObservabilityModule
from oridecon.ai.observability.config import ObservabilityConfig


@module(
    imports=[
        ObservabilityModule.configure(
            ObservabilityConfig(
                enabled=True,
                metrics_enabled=True,
                tracing_enabled=True,
                health_checks_enabled=True,
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

## Trace Payload Redaction (recommended for production)

`AITracer` exports tool arguments, agent actions/finishes, and retriever queries to trace spans verbatim. To keep
secret-shaped keys (`token`, `password`, `api_key`, `secret`, `authorization`, ...) and oversized string values out of
your tracing backend, enable trace redaction — **off by default, strongly recommended in production**:

```python
config = ObservabilityConfig(
    enabled=True,
    trace_redaction_enabled=True,
    trace_max_attribute_length=4096,
)
```

- `trace_redaction_enabled` masks values whose keys match the framework's secret denylist (`"<redacted>"` sentinel,
  exact case-insensitive key match, recursing nested dicts/lists) in the four callback paths and in LLM audit metadata.
- `trace_max_attribute_length` truncates any string attribute value beyond the cap (characters), independently of redaction.
- No behavior changes when disabled: span attributes stay byte-identical to today's output.

## Configuration

> **Zero-config usage:** Call `ObservabilityModule.configure()` with no arguments to use defaults.

### Option 1 — YAML file

```yaml
# application.yaml
ai_observability:
  enabled: true
  metrics_enabled: true
  tracing_enabled: true
  health_checks_enabled: true
  trace_redaction_enabled: true
  trace_max_attribute_length: 4096
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_AI_OBSERVABILITY__ENABLED=true
export ORI_AI_OBSERVABILITY__TRACE_REDACTION_ENABLED=true
export ORI_AI_OBSERVABILITY__TRACE_MAX_ATTRIBUTE_LENGTH=4096
# Environment variables for each field
```

### Option 3 — Python

```python
from oridecon.ai.observability.config import ObservabilityConfig
from oridecon.ai.observability import ObservabilityModule

config = ObservabilityConfig(
    enabled=True,
    metrics_enabled=True,
    tracing_enabled=True,
    health_checks_enabled=True,
)
ObservabilityModule.configure(config)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `enabled` | `True` | `ORI_AI_OBSERVABILITY__ENABLED` | Master on/off switch for all observability |
| `metrics_enabled` | `True` | `ORI_AI_OBSERVABILITY__METRICS_ENABLED` | Enable metrics collection |
| `tracing_enabled` | `True` | `ORI_AI_OBSERVABILITY__TRACING_ENABLED` | Enable distributed tracing |
| `health_checks_enabled` | `True` | `ORI_AI_OBSERVABILITY__HEALTH_CHECKS_ENABLED` | Enable background health checking |
| `trace_redaction_enabled` | `False` | `ORI_AI_OBSERVABILITY__TRACE_REDACTION_ENABLED` | Redact secret-shaped keys from trace span attributes and audit metadata |
| `trace_max_attribute_length` | `0` | `ORI_AI_OBSERVABILITY__TRACE_MAX_ATTRIBUTE_LENGTH` | Cap on string attribute values written to trace spans (`0` = disabled) |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `ObservabilityModule.configure(config)` | Fully-configured observability module |
| `ObservabilityModule.stub()` | No-op observability for testing |

## Key Features

- **Tracing**: Distributed tracing for LLM calls, RAG pipeline stages, and vector store queries
- **Metrics**: Token usage, latency, error rates, and cache hit ratios
- **Health monitoring**: Background health checks for AI components
- **Decorators**: `@trace_llm`, `@trace_rag`, `@track_llm_call` for automatic instrumentation
- **Observable wrappers**: `ObservableLLMClient` and `ObservableVectorStore`
- **No-op default**: Tracing uses the framework `TracerProtocol` interface with a no-op tracer by default, compatible with `oridecon-monitor`'s `Tracer`

## Testing

```python
async with Application.boot(modules=[ObservabilityModule.stub()]) as app:
    # your test code
    ...
```

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/ai/observability/module.py` | Module factory — `configure()` and `stub()` |
| `src/oridecon/ai/observability/config.py` | `ObservabilityConfig` — environment-aware settings |
| `src/oridecon/ai/observability/di/provider.py` | `ObservabilityProvider` — registers observability services |
| `src/oridecon/ai/observability/tracing/` | `AITracer` — distributed tracing for AI operations |
| `src/oridecon/ai/observability/metrics/` | `AIMetrics` — token usage, latency, error rates |
| `src/oridecon/ai/observability/health/` | `AIHealthMonitor` — background health checks |
| `src/oridecon/ai/observability/decorators.py` | `@trace_llm`, `@trace_rag`, `@track_llm_call` |
| `src/oridecon/ai/observability/exceptions.py` | Typed exceptions |
