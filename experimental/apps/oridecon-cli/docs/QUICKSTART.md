---
title: oridecon-cli Quickstart
description: Install the Oridecon CLI and scaffold your first project in minutes
---

:::tip[Alpha]
Oridecon is **alpha (0.1.x)**. Pin versions in production and expect public APIs to evolve before 1.0.
:::

## Install

```bash
uv add oridecon-cli
```

Or install as a standalone tool:

```bash
uv tool install oridecon-cli
```

## Hello World

```bash
# Verify the CLI is available
oridecon --help

# Scaffold a new project
oridecon new project my-app --template web-api
cd my-app

# Start the dev server
oridecon dev --reload
```

## Primary Import + Provider Wiring

The CLI can be integrated into a DI container via `CLIModule`:

```python
from oridecon import Application
from oridecon.cli import CLIModule

app = Application(name="my-app")
app.add_module(CLIModule.configure())
```

Or using `CLIProvider` directly:

```python
from oridecon.cli import CLIConfig
from oridecon.cli.di.provider import CLIProvider

provider = CLIProvider(config=CLIConfig())
app.add_provider(provider)
```

## What Just Happened

- `oridecon new project` scaffolded a complete project structure with `pyproject.toml`, `src/`, `tests/`, and `application.yaml`
- `oridecon dev` auto-detected the `create_app()` factory and launched an ASGI dev server with hot-reload
- `CLIModule.configure()` registers the CLI provider and exports `CLIApplicationProtocol`

## Next Steps

- [Guide](./GUIDE.md) — full walkthrough of every CLI command
- [How-Tos](./HOWTOS.md) — task-oriented recipes
