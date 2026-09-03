# oridecon-features

Feature flag evaluation and runtime gating for the Oridecon Framework.

---

## Overview

Feature flag evaluation and runtime gating for the Oridecon Framework. Provides a DI-friendly `FeatureFlagsModule`, multiple evaluation backends (in-memory, environment variables, chained, cache-backed, testing), decorator-based gates, and a `FlagManager` with TTL caching, runtime overrides, variant flags, and an audit log.

> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)

## Install

```bash
uv add oridecon-features
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module

from oridecon.features.config import FeatureFlagsConfig
from oridecon.features.manager import FlagManager
from oridecon.features.module import FeatureFlagsModule


@module(
    imports=[
        FeatureFlagsModule.configure(
            FeatureFlagsConfig(
                initial_flags={"beta_dashboard": True},
                cache_ttl=60,
            )
        )
    ]
)
class AppModule(Module):
    pass


class DashboardService:
    def __init__(self, flags: FlagManager) -> None:
        self._flags = flags

    async def show_beta(self) -> bool:
        return await self._flags.is_enabled("beta_dashboard")
```

## Configuration

> **Zero-config usage:** Call `FeatureFlagsModule.configure()` with no arguments to start
> with all built-in defaults — no config file or environment variables needed.
> See the [Config reference](#config-reference) below for all default values.

### Option 1 — YAML file *(use when config lives in a single explicit file)*

Declare config in a YAML file loaded at a fixed, explicit path. `ORI_*`
environment variables override YAML values at startup.

`config_section = "features"` is already set on this class — `section=` can be
omitted in all calls. Pass an explicit `section=` only to override the
default (e.g. when this config is nested under a non-standard key).

```yaml
# application.yaml — copy example.yaml for a fully-annotated starting point
features:
  enabled: true
  cache_ttl: 300
  default_enabled: false
  flag_env_prefix: "ORI_FLAG_"
```

Then load and wire it in your composition root:

```python
from oridecon.features.config import FeatureFlagsConfig
from oridecon.features.module import FeatureFlagsModule

config = FeatureFlagsConfig.from_yaml("application.yaml")
app.add_module(FeatureFlagsModule.configure(config))
```

Environment variables override YAML values and use the `ORI_FEATURES__` prefix:

```bash
ORI_FEATURES__CACHE_TTL=60
ORI_FEATURES__DEFAULT_ENABLED=false
ORI_FEATURES__FLAG_ENV_PREFIX=ORI_FLAG_
```

### Option 2 — Profiles + Environment Variables *(recommended for production, staging, Docker, CI/CD)*

Loads a base `application.yaml`, then overlays an environment-specific
file (`application.production.yaml`, `application.staging.yaml`, etc.)
based on the `ORI_PROFILE` environment variable. `ORI_*` env vars are
applied last as the final override layer.

```bash
# Set ORI_FEATURES__* env vars before starting the process
export ORI_FEATURES__ENABLED=true
```

```python
from oridecon.features.config import FeatureFlagsConfig
from oridecon.features.module import FeatureFlagsModule

config = FeatureFlagsConfig.from_env_profile()
app.add_module(FeatureFlagsModule.configure(config))
```

> **Loading order:** `application.yaml` (base) →
> `application.{profile}.yaml` (overlay, if `ORI_PROFILE` is set) →
> `ORI_*` environment variables (final override). Missing files are
> silently skipped so this is safe to call in all environments.

### Option 3 — Python *(use when config is dynamic or computed at boot)*

Build config in code at boot time. Use this when settings are **derived at
runtime** — e.g. secrets fetched from a vault, per-tenant configurations,
or when you need multiple module instances with different settings.

```python
from oridecon.features.module import FeatureFlagsModule
from oridecon.features.config import FeatureFlagsConfig

app.add_module(
    FeatureFlagsModule.configure(
        FeatureFlagsConfig(
            cache_ttl=60,
            initial_flags={"beta_dashboard": True},
        )
    )
)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `enabled` | `true` | `ORI_FEATURES__ENABLED` | Enable the feature flags subsystem |
| `cache_ttl` | `300` | `ORI_FEATURES__CACHE_TTL` | Seconds to cache flag evaluations (0 = disabled) |
| `default_enabled` | `false` | `ORI_FEATURES__DEFAULT_ENABLED` | Fallback result when a flag is not found in the provider |
| `flag_env_prefix` | `"ORI_FLAG_"` | `ORI_FEATURES__FLAG_ENV_PREFIX` | Env var prefix used by `EnvProvider` when reading flag values |
| `initial_flags` | `{}` | — | Seed flags for the in-memory provider (`name → enabled`) |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `FeatureFlagsModule.configure(config)` | Features subsystem with an explicit `FeatureFlagsConfig` |
| `FeatureFlagsModule.stub()` | In-memory module for tests, all flags disabled unless overridden |

## Key Features

- **DI-friendly registration**: `FeatureFlagsModule` wires the subsystem with one call
- **Multiple backends**: `LocalProvider`, `EnvProvider`, `ChainedProvider`, `MemoryProvider`, and `CacheBackendFlagProvider`
- **Runtime gating**: `feature_flag`, `require_flag`, `feature_flag_sync`, and `require_flag_sync` decorators
- **Evaluation primitives**: `Flag`, `FlagContext`, `FlagEvaluation`, and `FlagType`
- **TTL caching**: flag evaluations cached in-process with a configurable TTL
- **Runtime overrides**: `enable()`, `disable()`, `set_override()`, and `clear_override()` win over provider results
- **Variant flags**: available through `get_variant()` and `FlagType.VARIANT`
- **Audit trail**: `get_audit_log()` exposes override history

## Testing

```python
async with Application.boot(modules=[FeatureFlagsModule.stub()]) as app:
    # your test code
    ...
```

- `FeatureFlagsModule.stub()` is the fastest way to import the package in tests.
- `MemoryProvider` is the purpose-built test backend.
- `FlagManager.enable()`, `disable()`, `set_override()`, and `clear_override()` let you force runtime behavior without changing stored definitions.
- `get_audit_log()` is available when you need to inspect override history.

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/features/module.py` | `FeatureFlagsModule.configure()` and `FeatureFlagsModule.stub()` |
| `src/oridecon/features/config.py` | `FeatureFlagsConfig` |
| `src/oridecon/features/di/provider.py` | `FeatureFlagsProvider` — registers config, backends, and `FlagManager` |
| `src/oridecon/features/backends/` | `LocalProvider`, `EnvProvider`, `ChainedProvider`, `MemoryProvider`, `CacheBackendFlagProvider` |
| `src/oridecon/features/manager/` | `FlagManager` — evaluation, caching, overrides, audit log |
| `src/oridecon/features/decorators/` | `feature_flag`, `require_flag` and sync variants |

## Backends and Evaluation Flow

The shipped backends cover local development, environment-driven rollout, layered lookup, tests, and cache-backed storage:

- `LocalProvider`: in-memory definitions and sync evaluation support.
- `EnvProvider`: reads flags from environment variables.
- `ChainedProvider`: queries multiple providers in order.
- `MemoryProvider`: lightweight testing backend with explicit overrides.
- `CacheBackendFlagProvider`: stores flag definitions in a cache backend.

Evaluation flows through the provider into `FlagManager`, which applies TTL caching, supports `FlagContext`, and returns `FlagEvaluation` data. Runtime overrides win before provider results, and variant flags are available through `get_variant()` and `FlagType.VARIANT`.

## Decorators and Runtime Gates

Use decorators when you want feature checks close to the callable being guarded.

```python
from oridecon.features.decorators import feature_flag, require_flag


@feature_flag("beta_dashboard", manager=flags, fallback=lambda *_args, **_kwargs: None)
async def render_beta() -> None: ...


@require_flag("admin_reports", manager=flags)
async def export_report() -> bytes: ...
```

Use the sync variants only when the active backend supports synchronous in-memory evaluation.