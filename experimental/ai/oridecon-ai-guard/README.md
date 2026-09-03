# oridecon-ai-guard

AI input/output guard pipeline for the Oridecon Framework — LLM safety and content filtering

---

## Overview

Content safety and guardrails for the Oridecon Framework. Runs an ordered pipeline of input and output guards against every LLM call — blocking prompt injections, redacting PII, enforcing length limits, restricting topics, and optionally using an LLM classifier for advanced jailbreak detection. Zero-config usage starts with sensible defaults.

## Install

```bash
uv add oridecon-ai-guard
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module

from oridecon.ai.guard import GuardModule
from oridecon.ai.guard.config import GuardConfig


@module(
    imports=[
        GuardModule.configure(
            GuardConfig(
                injection_detection=True,
                pii_detection=True,
                pii_action="redact",
                max_input_chars=8000,
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

> **Zero-config usage:** Call `GuardModule.configure()` with no arguments to use defaults.

### Option 1 — YAML file

```yaml
# application.yaml
ai_guard:
  injection_detection: true
  pii_detection: true
  pii_action: "redact"
  max_input_chars: 8000
  restricted_topics: []
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_AI_GUARD__PII_ACTION=redact
# Environment variables for each field
```

### Option 3 — Python

```python
from oridecon.ai.guard.config import GuardConfig
from oridecon.ai.guard import GuardModule

config = GuardConfig(
    injection_detection=True,
    pii_action="redact",
    max_input_chars=8000,
    restricted_topics=["violence", "adult_content"],
)
GuardModule.configure(config)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `enabled` | `True` | `ORI_AI_GUARD__ENABLED` | Master on/off switch |
| `injection_detection` | `True` | `ORI_AI_GUARD__INJECTION_DETECTION` | Enable heuristic prompt injection detector |
| `injection_action` | `"block"` | `ORI_AI_GUARD__INJECTION_ACTION` | Action on injection: `"block"` or `"warn"` |
| `pii_detection` | `True` | `ORI_AI_GUARD__PII_DETECTION` | Enable PII detection on user inputs |
| `pii_action` | `"redact"` | `ORI_AI_GUARD__PII_ACTION` | Action on PII: `"redact"`, `"block"`, or `"warn"` |
| `pii_entities` | `[]` | `ORI_AI_GUARD__PII_ENTITIES` | PII entity types to scan |
| `pii_redaction_output` | `True` | `ORI_AI_GUARD__PII_REDACTION_OUTPUT` | Apply PII redaction to LLM outputs |
| `max_input_chars` | `0` | `ORI_AI_GUARD__MAX_INPUT_CHARS` | Maximum input character count |
| `max_output_chars` | `0` | `ORI_AI_GUARD__MAX_OUTPUT_CHARS` | Maximum output character count |
| `length_action` | `"block"` | `ORI_AI_GUARD__LENGTH_ACTION` | Action when a length limit is exceeded |
| `restricted_topics` | `[]` | `ORI_AI_GUARD__RESTRICTED_TOPICS` | Topic keywords to block |
| `enable_llm_guards` | `False` | `ORI_AI_GUARD__ENABLE_LLM_GUARDS` | Use LLM for advanced injection/jailbreak detection |
| `guard_model` | `"gpt-4o-mini"` | `ORI_AI_GUARD__GUARD_MODEL` | Model used for LLM-based guards |
| `llm_guard_threshold` | `0.7` | `ORI_AI_GUARD__LLM_GUARD_THRESHOLD` | Confidence threshold for LLM guard action |
| `sensitivity_level` | `"medium"` | `ORI_AI_GUARD__SENSITIVITY_LEVEL` | Guard aggressiveness: `"low"`, `"medium"`, `"high"` |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `GuardModule.configure(config)` | Configure with explicit config |
| `GuardModule.stub(config)` | Minimal config for testing |

## Key Features

- **Input guards**: PromptInjectionDetector, PIIDetector, TopicRestrictor, InputLengthGuard
- **Output guards**: PIIRedactor, OutputLengthGuard
- **LLM-based guards**: Optional LLMInjectionDetector and LLMJailbreakDetector
- **Guard results**: `AggregateGuardResult` with passed, blocked, redacted, warned states
- **`@guarded` decorator**: Function-level guard attachment
- **Lifecycle hooks**: GuardInputCheckedHook, GuardOutputCheckedHook, GuardPipelineCompletedHook

## Testing

```python
async with Application.boot(
    modules=[
        GuardModule.stub(
            GuardConfig(
                injection_detection=True,
                injection_action="block",
            )
        )
    ]
) as app:
    # your test code
    ...
```

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/ai/guard/module.py` | `GuardModule.configure()`, `.stub()` |
| `src/oridecon/ai/guard/config.py` | `GuardConfig` |
| `src/oridecon/ai/guard/pipeline/guard_pipeline.py` | `GuardPipeline` orchestrator |
| `src/oridecon/ai/guard/pipeline/result.py` | `GuardCheckResult`, `AggregateGuardResult`, `GuardAction` |
| `src/oridecon/ai/guard/input/injection.py` | `PromptInjectionDetector` heuristics |
| `src/oridecon/ai/guard/input/pii.py` | `PIIDetector` regex patterns |
| `src/oridecon/ai/guard/output/pii_redactor.py` | `PIIRedactor` |
| `src/oridecon/ai/guard/di/provider.py` | `GuardProvider` boot and registration |
