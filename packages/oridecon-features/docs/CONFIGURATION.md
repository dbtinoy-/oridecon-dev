---
title: oridecon-features Configuration
description: Every configuration key for the feature-flag subsystem
---

Config section: `features`  
Env prefix: `ORI_FEATURES__`  
Config model: `FeatureFlagsConfig`

## FeatureFlagsConfig

| Key | Type | Default | Env var | Description |
|-----|------|---------|---------|-------------|
| `enabled` | `bool` | `True` | `ORI_FEATURES__ENABLED` | Enable the features subsystem |
| `cache_ttl` | `int` | `300` | `ORI_FEATURES__CACHE_TTL` | Cache TTL for flag evaluations (seconds; 0 = disabled) |
| `default_enabled` | `bool` | `False` | `ORI_FEATURES__DEFAULT_ENABLED` | Default when flag not found |
| `flag_env_prefix` | `str` | `"ORI_FLAG_"` | `ORI_FEATURES__FLAG_ENV_PREFIX` | Env prefix for `EnvProvider` |
| `initial_flags` | `dict[str, bool | Flag | mapping]` | `{}` | `ORI_FEATURES__INITIAL_FLAGS` | Seed boolean or rich flag definitions for `LocalProvider` |

## Example YAML

```yaml
features:
  enabled: true
  cache_ttl: 60
  default_enabled: false
  flag_env_prefix: ORI_FLAG_
  initial_flags:
    new_checkout: true
    dark_mode: false
    experimental_search:
      type: percentage
      enabled: true
      percentage: 25
    search_experiment:
      type: variant
      enabled: true
      variants:
        control: 50
        ranked: 50
      default_variant: control
```

Each `initial_flags` value may be a legacy boolean, a `Flag` instance in
Python configuration, or a YAML-friendly mapping with a `type`, `enabled`,
and type-specific fields such as `percentage`, `user_attributes`, or
`variants`.

Env var override form:

```bash
export ORI_FEATURES__CACHE_TTL=0
export ORI_FEATURES__INITIAL_FLAGS='{"new_checkout":true}'
```

## Environment variable flags

When using `EnvProvider`, flags are read from environment variables with the configured prefix:

```bash
export ORI_FLAG_NEW_CHECKOUT=true
export ORI_FLAG_DARK_MODE=false
```
