---
title: Configuration
description: YAML config, environment profiles, and auto-injection
sidebar:
  order: 5
---

:::note[What you'll learn]
- Structure of `application.yaml`
- Environment-variable substitution and overrides
- Profile overlays (`production`, `staging`, `test`)
- How providers auto-read their config sections via `config_key` / `config_model`
:::

## Configuration File

Create `application.yaml` in your project root. Top-level keys are core settings; each extension reads its **own section** (the section name is the provider's `config_key`):

```yaml title="application.yaml"
app_name: my-app
debug: false
env: development          # development | staging | production | test

logging:
  level: INFO
  json_format: true         # true | false

# oridecon-web  (name: "web")
web:
  server:
    host: "0.0.0.0"
    port: 8000
  cors:
    enabled: true
    allow_origins: ["https://myapp.com"]

# oridecon-sql  (config_key: "sql")
sql:
  backend:
    url: "${DATABASE_URL}"
  pool:
    min_size: 2
    max_size: 10

# oridecon-cache  (config_key: "cache")
cache:
  backends:
    - name: memory
      type: memory        # memory | redis | memcached
      default: true
```

:::tip
The shape of each section matches the package's config model exactly. The repository ships an `application.example.yaml` with the full, annotated reference for every section.
:::

### Loading Config

```python
from oridecon import OrideconConfig

# Auto-discovers application.yaml in the project root
config = OrideconConfig.from_yaml()

# Or from a specific path
config = OrideconConfig.from_yaml("path/to/application.yaml")
```

`Application` loads configuration for you when you don't pass one — it calls `OrideconConfig.from_env_profile()` by default.

`OrideconConfig` has typed top-level fields:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `app_name` | `str` | `"oridecon-app"` | Application name |
| `debug` | `bool` | `False` | Debug mode |
| `env` | `Environment` | `development` | Deployment environment |
| `logging` | `LoggingConfig` | — | Structured logging settings |
| `modules` | `list[str]` | `[]` | Enabled modules |

All extension sections (`web:`, `db:`, `cache:`, …) are accessed via `config.get_section()`.

---

## Environment Variables

There are two complementary mechanisms.

### 1. Interpolation inside YAML

Use `${VAR}` for secrets and deployment values, with optional defaults via `${VAR:default}`:

```yaml title="application.yaml"
sql:
  backend:
    url: "${DATABASE_URL:sqlite+aiosqlite:///./dev.db}"
auth:
  secret_key: "${ORI_AUTH__SECRET_KEY}"
```

### 2. Override any key with `ORI_` env vars

Any configuration key can be overridden by an environment variable using the `ORI_` prefix and **double underscores** for nesting. Env vars win over YAML:

```bash
ORI_WEB__SERVER__PORT=9000          # web.server.port = 9000
ORI_SQL__BACKEND__URL=postgresql+asyncpg://...   # db backend url
ORI_AI_LLM__PROVIDERS__0__API_KEY=sk-...         # list items use numeric indices
```

### Standard variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `ORI_PROFILE` | Active configuration profile | _(none)_ |
| `ORI_DEBUG` | Enable debug mode | `false` |
| `ORI_QUIET` | Suppress startup banner | `false` |
| `ORI_ENV` | Deployment environment | `development` |

---

## Profile Overlays

Oridecon merges a profile-specific YAML over the base config. Set `ORI_PROFILE` to activate it:

```
application.yaml                 # Base config (always loaded)
application.development.yaml     # Merged when ORI_PROFILE=development
application.staging.yaml         # Merged when ORI_PROFILE=staging
application.production.yaml      # Merged when ORI_PROFILE=production
application.test.yaml            # Merged when ORI_PROFILE=test
```

### Example profiles

```yaml title="application.development.yaml"
debug: true
logging:
  level: DEBUG
  json_format: false
sql:
  backend:
    url: "sqlite+aiosqlite:///./dev.db"
```

```yaml title="application.production.yaml"
debug: false
logging:
  level: WARNING
  json_format: true
cache:
  backends:
    - name: redis
      type: redis
      default: true
      redis_url: "${REDIS_URL}"
```

### Loading with a profile

```python
from oridecon import OrideconConfig

# Reads ORI_PROFILE from the environment
config = OrideconConfig.from_env_profile()

# Explicit profile
config = OrideconConfig.from_env_profile("production")

# With a custom base path
config = OrideconConfig.from_env_profile("staging", base_path="./config")
```

### Environment validation

`validate_for_environment()` checks environment-specific constraints (for example, `debug=True` in production):

```python
from oridecon.contracts.core.config import Environment

issues = config.validate_for_environment(Environment.PRODUCTION)
```

---

## Provider Config Auto-Injection

A provider declares `config_key` and `config_model` to automatically receive its typed config section — no manual parsing:

```python
from dataclasses import dataclass
from oridecon import Provider
from oridecon.contracts.core.di import ContainerRegistrarProtocol


@dataclass
class BillingConfig:
    stripe_key: str = ""
    currency: str = "usd"


class BillingProvider(Provider):
    name = "billing"
    config_key = "billing"          # reads "billing:" from application.yaml
    config_model = BillingConfig    # coerces it into BillingConfig

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        cfg = self.config or BillingConfig()   # self.config is a typed BillingConfig
        container.singleton(StripeClient, StripeClient(cfg.stripe_key))
```

Before calling `register()`, the framework reads the matching section via `OrideconConfig.get_section(config_key, config_model)` and assigns it to `provider.config`. Built-in providers use the same mechanism:

| Provider | `config_key` |
|----------|-------------|
| `DatabaseProvider` | `"sql"` |
| `CacheProvider` | `"cache"` |
| `AuthProvider` | `"auth"` |

---

## Unknown-Key Protection (Strict Sections)

When a section is bound to a model via `get_section(name, ModelClass)`,
keys the model does not define raise `UnknownConfigKeysError` at load
time — with the dotted path and a did-you-mean suggestion:

```python title="application.yaml"
web:
  server:
    prot: 9999        # typo: should be port
```

```python
config.get_section("web", WebConfig)
# UnknownConfigKeysError: Unknown configuration key(s) in section
# 'web': server.prot — did you mean 'port'?  [ORI_ERR_CFG_006]
```

Typos die at startup with the exact key name instead of silently falling
back to defaults. Nested keys report their full dotted path
(`server.prot`).

**Escape hatch** (legacy files, forward-declared keys):

```bash
ORI_CONFIG_ALLOW_UNKNOWN=true   # warn + prune instead of raising
```

Untyped access (`get_section("web")` without a model) stays permissive —
strictness applies only where a model defines the contract.

---

## Config API

```python
config = OrideconConfig.from_yaml()

# Typed top-level access
config.app_name         # "my-app"
config.debug            # False
config.environment      # Environment.DEVELOPMENT

# Section access (extension config)
db_config = config.get_section("sql", DatabaseConfig)
rag_config = config.get_section("ai_rag", RAGConfig)   # dotted paths also supported

# Existence + serialization (secrets redacted by default)
config.has_section("web")               # True
config.to_dict()                        # {"app_name": "...", "auth": {"secret_key": "***"}}
config.to_dict(redact_secrets=False)    # full values
```

---

## Next Steps

- [YAML Configuration](/fundamentals/yaml-configuration/) — interpolation, precedence, and profiles in depth
- [Core Concepts](/getting-started/core-concepts/) — Providers, DI, and the Result type
- [Your First App](/getting-started/first-app/) — Build a working API
