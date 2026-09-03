# oridecon-ai-evaluation

AI Evaluation framework for the Oridecon Framework.

---

## Overview

AI Evaluation framework for the Oridecon Framework. Provides evaluators harness, and metrics — all wired through the DI container via `EvaluationModule`. Zero-config usage starts with sensible defaults.

## Install

```bash
uv add oridecon-ai-evaluation
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module

from oridecon.ai.evaluation import EvaluationModule
from oridecon.ai.evaluation.config import EvaluationConfig


@module(imports=[EvaluationModule.configure(EvaluationConfig(default_threshold=0.8))])
class AppModule(Module):
    pass


async with Application.boot(modules=[AppModule]) as app:
    # use app.container to resolve services
    ...
```

## Configuration

> **Zero-config usage:** Call `EvaluationModule.configure()` with no arguments to use defaults.

### Option 1 — YAML file

```yaml
# application.yaml
ai_evaluation:
  enabled: true
  default_threshold: 0.8
  embedding_model: "text-embedding-3-small"
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_AI_EVALUATION__DEFAULT_THRESHOLD=0.8
# Environment variables for each field
```

### Option 3 — Python

```python
from oridecon.ai.evaluation.config import EvaluationConfig
from oridecon.ai.evaluation import EvaluationModule

config = EvaluationConfig(
    default_threshold=0.8,
    embedding_model="text-embedding-3-small",
)
EvaluationModule.configure(config)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `enabled` | `True` | `ORI_AI_EVALUATION__ENABLED` | Enable the evaluation subsystem |
| `default_threshold` | `0.8` | `ORI_AI_EVALUATION__DEFAULT_THRESHOLD` | Score threshold for passing |
| `embedding_model` | `text-embedding-3-small` | `ORI_AI_EVALUATION__EMBEDDING_MODEL` | Model for embedding evaluations |
| `include_metadata` | `True` | `ORI_AI_EVALUATION__INCLUDE_METADATA` | Include metadata in reports |
| `max_samples` | `None` | `ORI_AI_EVALUATION__MAX_SAMPLES` | Max samples per run |
| `max_retries` | `3` | `ORI_AI_EVALUATION__MAX_RETRIES` | Max retries for failed evaluations |
| `timeout_seconds` | `30` | `ORI_AI_EVALUATION__TIMEOUT_SECONDS` | Execution timeout |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `EvaluationModule.configure(config)` | Configure with explicit settings |
| `EvaluationModule.stub()` | No-op for testing |

## Key Features

- **5 evaluator types**: Criteria, QA, Embedding Distance, String Distance, Trajectory
- **Evaluation harness**: Run datasets against models with configurable evaluators
- **Metrics**: Pass/fail, score-based, and threshold evaluation
- **Embedding support**: Semantic similarity via embeddings

## Testing

```python
async with Application.boot(modules=[EvaluationModule.stub()]) as app:
    # your test code
    ...
```

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/ai/evaluation/module.py` | `EvaluationModule.configure()` and `EvaluationModule.stub()` |
| `src/oridecon/ai/evaluation/config.py` | `EvaluationConfig` |
| `src/oridecon/ai/evaluation/di/provider.py` | `EvaluationProvider` — registers and boots |
| `src/oridecon/ai/evaluation/evaluators/` | Evaluator implementations |
| `src/oridecon/ai/evaluation/harness/` | Evaluation harness and runner |
| `src/oridecon/ai/evaluation/exceptions.py` | Full exception hierarchy |