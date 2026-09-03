---
title: "oridecon Configuration"
description: "How Oridecon loads configuration from multiple sources with an overlay model."
---
# Configuration

---

## Overview

Oridecon loads configuration from multiple sources with an overlay (later-wins) model. The `ConfigProvider` (priority `CRITICAL`) handles loading during the `register()` phase.

**Config sources** (in priority order, later wins):

1. In-code field defaults
2. `application.yaml` in the working directory
3. Custom file sources (via `ConfigLoader`)
4. Environment variables (`ORI_<KEY>`)
5. `.env` file
6. CLI arguments (via `CliConfigSource`)

---

## Config Section Key

Oridecon's config lives at the **root** of the config hierarchy (there is no outer section key). Extension packages use sub-keys under the root (e.g. `cache:`, `web:`, `db:`), which are accessed via `config.get_section("cache", CacheConfig)`.

---

## Options

### `OrideconConfig` — Root Configuration

| Key | Type | Default | Description | Env Var |
|-----|------|---------|-------------|---------|
| `app_name` | `str` | `"oridecon-app"` | Application name used in logging and telemetry | `ORI_APP__APP_NAME` |
| `debug` | `bool` | `False` | Enable debug mode (blocked in production) | `ORI_DEBUG` |
| `env` | `Environment` | `"development"` | Deployment environment | `ORI_ENV` |
| `logging.level` | `str` | `"INFO"` | Default log level | `ORI_LOGGING__LEVEL` |
| `logging.json_format` | `bool` | `false` | Render logs as JSON | `ORI_LOGGING__JSON_FORMAT` |
| `enabled_modules` | `list[str]` | `[]` | Enabled module names | `ORI_MODULEDISCOVERY__ENABLED_MODULES` |
| `discovery.auto_discover` | `bool` | `False` | Auto-discover modules | `ORI_MODULEDISCOVERY__AUTO_DISCOVER` |
| `discovery.entry_point_group` | `str` | `"oridecon.modules"` | Entry point group for module discovery | `ORI_MODULEDISCOVERY__ENTRY_POINT_GROUP` |
| `health.check_timeout` | `float` | `5.0` | Health check timeout (seconds) | `ORI_HEALTH__CHECK_TIMEOUT` |
| `health.include_details` | `bool` | `true` | Include detailed health output | `ORI_HEALTH__INCLUDE_DETAILS` |

### Environment Values

| Environment | String Value |
|-------------|-------------|
| `DEVELOPMENT` | `"development"` |
| `STAGING` | `"staging"` |
| `PRODUCTION` | `"production"` |
| `TEST` | `"test"` |

---

## Examples

### Minimal YAML (`application.yaml`)

```yaml
app_name: my-api
debug: false
env: development
logging:
  level: INFO
  json_format: true
```

### Production YAML

```yaml
app_name: my-api
debug: false
env: production
logging:
  level: WARN
  json_format: true
```

### Environment Variables

```bash
export ORI_APP__APP_NAME="my-api"
export ORI_DEBUG="false"
export ORI_ENV="production"
export ORI_LOGGING__LEVEL="WARN"
export ORI_LOGGING__JSON_FORMAT="true"
```

---

## Programmatic Usage

```python
from oridecon import OrideconConfig
from oridecon.config.di.provider import ConfigProvider

# Load from YAML + env
config = OrideconConfig.from_yaml("application.yaml")
print(config.app_name)   # "my-api"
print(config.is_production)  # True/False

# Provider section access
cache_cfg = config.get_section("cache", CacheConfig)

# Validation
issues = config.validate_for_environment()
for issue in issues:
    print(f"{issue.field}: {issue.message}")

# ConfigProvider for DI
provider = ConfigProvider()
```

---

## Best Practices

- **Never hardcode secrets** in YAML — use environment variables or a secret store
- **Use `ORI_` prefix** for all env var overrides
- **Section naming** uses double-underscore: `ORI_<SECTION>__<KEY>`
- **Validate with `config.validate_for_environment()`** in production to catch `debug=True`
- **Register secrets** via `app.register_secrets()` for boot-time validation
- **Pin config model types** by registering them in `ConfigRegistry` for extension packages
