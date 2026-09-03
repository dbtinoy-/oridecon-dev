# oridecon-ai-governance

AI governance for the Oridecon Framework — policy enforcement, audit trails, budget tracking

---

## Overview

AI usage governance for the Oridecon Framework. Enforces budget caps, rate limits, and model access policies on LLM requests — with a full audit trail, soft-limit callbacks, TPM/cost sliding windows, and hot-reloadable configuration. Zero-config usage starts with sensible defaults.

## Install

```bash
uv add oridecon-ai-governance
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module

from oridecon.ai.governance import GovernanceModule
from oridecon.ai.governance.config import GovernanceConfig


@module(
    imports=[
        GovernanceModule.configure(
            GovernanceConfig(
                monthly_budget=50.0,
                enforce_budget=True,
                soft_limit_pct=0.8,
                rpm_limit=60,
                restricted_models=["gpt-4o"],
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

> **Zero-config usage:** Call `GovernanceModule.configure()` with no arguments to use defaults.

### Option 1 — YAML file

```yaml
# application.yaml
ai_governance:
  enabled: true
  monthly_budget: 100.0
  enforce_budget: true
  soft_limit_pct: 0.8
  rpm_limit: 60
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_AI_GOVERNANCE__MONTHLY_BUDGET=100.0
# Environment variables for each field
```

### Option 3 — Python

```python
from oridecon.ai.governance.config import GovernanceConfig
from oridecon.ai.governance import GovernanceModule

config = GovernanceConfig(
    monthly_budget=100.0,
    enforce_budget=True,
    soft_limit_pct=0.8,
    rpm_limit=60,
)
GovernanceModule.configure(config)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `enabled` | `True` | `ORI_AI_GOVERNANCE__ENABLED` | Master on/off switch for governance enforcement |
| `monthly_budget` | `None` | `ORI_AI_GOVERNANCE__MONTHLY_BUDGET` | Monthly budget cap in dollars |
| `enforce_budget` | `True` | `ORI_AI_GOVERNANCE__ENFORCE_BUDGET` | Hard-block requests when budget is reached |
| `soft_limit_pct` | `None` | `ORI_AI_GOVERNANCE__SOFT_LIMIT_PCT` | Warn at this fraction of budget |
| `max_request_cost` | `None` | `ORI_AI_GOVERNANCE__MAX_REQUEST_COST` | Per-request cost cap in dollars |
| `rpm_limit` | `None` | `ORI_AI_GOVERNANCE__RPM_LIMIT` | Requests per minute cap |
| `tpm_limit` | `None` | `ORI_AI_GOVERNANCE__TPM_LIMIT` | Tokens per minute cap |
| `max_tokens_per_request` | `None` | `ORI_AI_GOVERNANCE__MAX_TOKENS_PER_REQUEST` | Hard token ceiling per request |
| `restricted_models` | `[]` | `ORI_AI_GOVERNANCE__RESTRICTED_MODELS` | Models blocked for all users |
| `model_allowlist` | `{}` | `ORI_AI_GOVERNANCE__MODEL_ALLOWLIST` | Per-user/role allowlist with glob patterns |
| `model_denylist` | `{}` | `ORI_AI_GOVERNANCE__MODEL_DENYLIST` | Per-user/role denylist |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `GovernanceModule.configure(config)` | Configure with explicit config |
| `GovernanceModule.stub(config)` | Minimal config for testing |

## Key Features

- **Budget enforcement**: Monthly budget caps with soft-limit callbacks
- **Rate limiting**: RPM and TPM sliding windows via `BudgetTracker`
- **Model access control**: Per-user and per-role allowlist/denylist with glob patterns
- **Audit trail**: Full governance decision recording via `AIAuditStore`
- **Hot reload**: Update limits at runtime without restarting
- **Persistence backends**: In-memory, Redis, and database backends

## Testing

```python
async with Application.boot(
    modules=[GovernanceModule.stub(GovernanceConfig(restricted_models=["gpt-4o"]))]
) as app:
    # your test code
    ...
```

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/ai/governance/module.py` | `GovernanceModule.configure()`, `.stub()` |
| `src/oridecon/ai/governance/config.py` | `GovernanceConfig` |
| `src/oridecon/ai/governance/services/manager.py` | `AIGovernanceManager` core logic |
| `src/oridecon/ai/governance/budget/tracker.py` | `BudgetTracker` TPM / cost enforcement |
| `src/oridecon/ai/governance/audit/` | `AIAuditStore`, `AIAuditEvent`, query models |
| `src/oridecon/ai/governance/persistence/persistence.py` | Persistence backends |
| `src/oridecon/ai/governance/di/provider.py` | `GovernanceProvider` boot and registration |
