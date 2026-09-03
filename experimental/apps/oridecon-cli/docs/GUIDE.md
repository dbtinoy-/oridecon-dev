---
title: oridecon-cli Guide
description: Full walkthrough of project scaffolding, code generation, database management, and runtime inspection
---

## Requirements

| Package | Required | Purpose |
|---------|----------|---------|
| `oridecon` | Yes | Core framework |
| `oridecon-contracts` | Yes | Protocol definitions |
| `oridecon-web` | Yes | Web UI support |

## The Problem `oridecon-cli` Solves

Building a Oridecon application involves repeated setup: project scaffolding, code generation, database migrations, and runtime inspection. `oridecon-cli` automates these tasks through a single `oridecon` command, using a **contributor-based plugin system** where packages extend the CLI via `oridecon.cli.contributors` entry points.

**Mental model:** Think of `oridecon-cli` as the framework's toolbox — one command to create, build, run, and introspect your application.

---

## Core Concepts

- **Command groups** — commands are organized as sub-Typer apps (`new`, `run`, `dev`, `db`, `gen`, `inspect`, `shell`, etc.)
- **Contributors** — packages advertise commands, generators, health checks, shell context, and hooks via `oridecon.cli.contributors`; discovered at import with automatic conflict resolution
- **CLIContext** — per-invocation shared state holding config, output mode (Rich/JSON/Quiet), and flags
- **`OutputManager`** — centralized output with support for Rich formatting, JSON serialization, and debug modes

---

## Full Command Walkthrough

### Scaffolding (`new`, `add`)

```bash
# Create a new project from a template
oridecon new project my-app --template web-api -d ./projects

# Create a project interactively
oridecon new project my-app -i

# Scaffold a new oridecon-* extension package
oridecon new package my-feature

# Add a provider to an existing project
oridecon add web
oridecon add sql
```

Available templates: `web-api`, `full`, `api`.

### Dev Server (`run`, `dev`)

```bash
# Auto-detect create_app() and start the server
oridecon run

# Explicit entry point
oridecon run my_app.app:create_app --port 9000 --no-reload

# Development server with hot-reload
oridecon dev --entry src/main.py --port 8000 --env development

# Use a specific server backend
oridecon run --server granian

# Run with an MCP SSE server alongside
oridecon run --mcp-port 8080
```

The CLI auto-detects the server backend, preferring Granian → Uvicorn → Hypercorn based on availability.

### Database Management (`db`)

```bash
# Create/upgrade a database and generate an initial migration
oridecon db init

# Auto-generate a migration from schema changes
oridecon db migrate -m "add email to users"

# Apply pending migrations
oridecon db upgrade

# Rollback the last migration
oridecon db rollback

# View migration status
oridecon db status

# Seed test data
oridecon db seed

# View migration history
oridecon db list
```

Database commands require `oridecon-sql` to be installed:

```bash
uv add oridecon-sql
```

### Code Generation (`gen`)

```bash
# List all available generators
oridecon gen list

# Generate code
oridecon gen model User
oridecon gen service UserService
oridecon gen repository UserRepository
oridecon gen controller UserController
```

Generators are contributed by installed packages. Each generator creates files in the current project's source tree.

### Runtime Inspection (`inspect`)

```bash
# List registered container providers
oridecon inspect providers

# Show HTTP routes
oridecon inspect routes

# Display container bindings
oridecon inspect container

# Run health checks
oridecon inspect health

# View service list
oridecon inspect services
```

### Interactive Shell (`shell`)

```bash
# Start a REPL with the application context pre-loaded
oridecon shell

# Plain Python REPL without app bootstrap
oridecon shell --no-app

# Use IPython if available
oridecon shell --ipython
```

The shell provides `app`, `container`, `config`, `db`, `cache`, and `events` as pre-loaded objects.

### Other Commands

```bash
# System information
oridecon system info
oridecon version

# Configuration management
oridecon config show
oridecon config set default_template=full

# Contributor discovery
oridecon contrib check
oridecon contrib list

# Meta commands
oridecon list         # list all commands
oridecon completion   # generate shell completion
oridecon test         # run project tests
oridecon lint         # run project linters
```

---

## Integration with the DI Container

```python
from oridecon import Application
from oridecon.cli import CLIModule, CLIConfig
from oridecon.cli.di.provider import CLIProvider

# Via module (recommended)
app = Application(name="my-app")
app.add_module(CLIModule.configure(CLIConfig(default_template="full")))

# Via provider directly
provider = CLIProvider(config=CLIConfig(verbose=True))
app.add_provider(provider)
```

The `CLIProvider` has priority `APPLICATION` (40) — it boots after infrastructure but before domain services.

---

## Best Practices

- ✅ Run `oridecon gen list` to see all available generators from installed packages
- ✅ Use `oridecon project test/lint` as a pre-commit gate
- ✅ Run `oridecon contrib check` to verify contributors load cleanly after adding packages
- ✅ Use `--json` flag for machine-readable output (useful in CI scripts)
- ❌ Don't manually edit generated file headers — re-run the generator instead
- ❌ Don't use `oridecon run` in production — deploy through your ASGI server directly
