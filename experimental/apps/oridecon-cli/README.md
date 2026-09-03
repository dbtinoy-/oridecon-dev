# oridecon-cli

Command-line interface for the Oridecon Framework.

---

## Overview

The `oridecon` CLI provides project scaffolding, code generation, development tooling, and administrative commands for every stage of the application lifecycle. It uses a contributor-based plugin system so other packages can extend the CLI with new commands and generators.

> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon-cli
# or, as a standalone tool:
uv tool install oridecon-cli
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module

from oridecon.cli import CLIModule
from oridecon.cli.config import CLIConfig


@module(imports=[CLIModule.configure(CLIConfig())])
class AppModule(Module):
    pass


async with Application.boot(modules=[AppModule]) as app:
    # use app.container to resolve services
    ...
```

Or use the CLI directly:

```bash
# Create a new web API project
oridecon new project my-api --template web-api

# Scaffold a new extension package
oridecon new package my-feature

# Generate a provider (providers and tests are the built-in generators)
oridecon gen provider MyProvider

# Add the database package to an existing project
oridecon add database

# Start the dev server with hot-reload
oridecon dev start
```

## Configuration

> **Zero-config usage:** Call `CLIModule.configure()` with no arguments to use all defaults.

### Option 1 — YAML file

```yaml
# application.yaml
cli:
  default_template: "web-api"
  default_database: "postgres"
  color: true
  verbose: false
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_CLI__DEFAULT_TEMPLATE=web-api
export ORI_CLI__COLOR=true
export ORI_CLI__VERBOSE=false
```

### Option 3 — Python

```python
from oridecon.cli.config import CLIConfig
from oridecon.cli import CLIModule

config = CLIConfig.from_env_profile()
CLIModule.configure(config)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `default_template` | `"web-api"` | `ORI_CLI__DEFAULT_TEMPLATE` | Template used by `oridecon new` |
| `default_database` | `"postgres"` | `ORI_CLI__DEFAULT_DATABASE` | Database driver used by scaffolding |
| `color` | `true` | `ORI_CLI__COLOR` | Enable coloured terminal output |
| `verbose` | `false` | `ORI_CLI__VERBOSE` | Print verbose/debug output |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `CLIModule.configure(config)` | Register the CLI module and its contributor-based commands |
| `CLIModule.stub()` | Minimal module for tests |

## Key Features

- **Project scaffolding** — `web-api`, `api`, and `full` templates
- **Package generation** — scaffold new `oridecon-*` extension packages
- **Code generators** — `provider` and `test` generators built in; more generators ship as CLI contributors from ecosystem packages (e.g. controllers via `oridecon-web`)
- **Contributor system** — extensible plugin architecture for new commands
- **Shell completion** — bash, zsh, and fish completion scripts

## Testing

```python
from oridecon import Application
from oridecon.cli import CLIModule


async def test_cli_module():
    async with Application.boot(modules=[CLIModule.stub()]) as app:
        # No-op CLI module for tests
        ...
```

## Key Source Files

| File | What it contains |
|------|----------------|
| `src/oridecon/cli/config.py` | `CLIConfig` configuration dataclass |
| `src/oridecon/cli/module.py` | CLI module assembly |
| `src/oridecon/cli/commands/` | All CLI command implementations |
| `src/oridecon/cli/generators/` | Code generation logic |
| `src/oridecon/cli/registry/` | Registry subsystems |
| `src/oridecon/cli/contributors/` | Plugin contributor system |