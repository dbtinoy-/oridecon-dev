---
title: oridecon-cli Configuration
description: CLIConfig options, environment variables, and YAML setup
---

## Overview

`CLIConfig` extends `BaseConfig` from `oridecon.config` with a `config_section = "cli"`. It reads from the `[cli]` section of `application.yaml` or environment variables prefixed with `ORI_CLI__`.

```python
from oridecon.cli import CLIConfig

# From YAML (reads [cli] section)
config = CLIConfig.from_yaml("application.yaml")

# Defaults
config = CLIConfig()
```

## Options

| Key | Type | Default | Env Var | Description |
|-----|------|---------|---------|-------------|
| `default_template` | `str` | `"web-api"` | `ORI_CLI__DEFAULT_TEMPLATE` | Project template used by `oridecon new project` |
| `default_database` | `str` | `"postgres"` | `ORI_CLI__DEFAULT_DATABASE` | Default database driver for scaffolding |
| `color` | `bool` | `True` | `ORI_CLI__COLOR` | Enable coloured terminal output |
| `verbose` | `bool` | `False` | `ORI_CLI__VERBOSE` | Print verbose/debug output |

## YAML Example

```yaml
# application.yaml
cli:
  default_template: "full"
  default_database: "sqlite"
  color: true
  verbose: false
```

## Environment Variables

```bash
export ORI_CLI__DEFAULT_TEMPLATE=full
export ORI_CLI__DEFAULT_DATABASE=sqlite
export ORI_CLI__COLOR=true
export ORI_CLI__VERBOSE=true
```

Environment variable overrides take precedence over values in `application.yaml`.

## Best Practices

- Use `application.yaml` for project-wide defaults checked into version control
- Use environment variables for CI/CD and per-deployment overrides
- Set `ORI_CLI__VERBOSE=true` during troubleshooting for detailed output
