---
title: oridecon-cli Commands
description: Complete command reference for `oridecon` CLI — every command with arguments, flags, and examples.
---

> **Alpha (0.1.x)** — MIT licensed. Commands and flags may change before 1.0.

## Overview

The `oridecon` CLI is the primary developer tool for scaffolding, running, and managing Oridecon projects. Commands are organised into categories.

## Built-in commands

### `oridecon new`

Scaffold a new project or package.

```
oridecon new project <name> [--template web-api] [--directory .]
oridecon new module <name> [--directory .]
oridecon new package <name> [--output-dir packages/]
```

| Flag | Default | Description |
|------|---------|-------------|
| `--template`, `-t` | `web-api` | Project template (`minimal`, `api`, `web-api`, `graphql`, `worker`, `full`, `fullstack`) |
| `--directory`, `-d` | `.` | Output directory |

**Examples:**

```bash
oridecon new project my-api --template web-api
oridecon new project my-app --template api
oridecon new project my-platform --template full
```

`oridecon new module <name>` adds a bounded context to a project
(`src/<app>/modules/<name>/` with a `@module` boundary, `protocols.py`,
`provider.py` and `services.py`, registered in `modules/__init__.py`).

`oridecon gen <generator> <name> --module <feature>` writes module-local
components into the matching bounded context; cross-cutting generators
(`errors`, `filters`, `health`, `schema`, ...) write into `shared/`.

### `oridecon run`

Smart runner — auto-detects `create_app()` factory and starts the ASGI server.

```
oridecon run [target] [--host 0.0.0.0] [--port 8000] [--server uvicorn]
```

| Flag | Default | Description |
|------|---------|-------------|
| `target` | Auto-detected | `module:attr` factory path |
| `--host`, `-h` | `0.0.0.0` | Bind address |
| `--port`, `-p` | `8000` | Port |
| `--server` | Auto-detected | Server backend (`uvicorn`, `hypercorn`, `granian`) |

**Example:** `oridecon run my_app.app:create_app --port 8080`

### `oridecon dev`

Development server with hot reload.

```
oridecon dev [--entry src/main.py] [--host 127.0.0.1] [--port 8000] [--reload] [--env development]
```

| Flag | Default | Description |
|------|---------|-------------|
| `--entry` | Auto-detected | Entry point file |
| `--reload/--no-reload` | `True` | Hot reload on file changes |
| `--env` | `development` | Environment profile |

**Example:** `oridecon dev --entry app.py --port 9000 --no-reload`

### `oridecon db`

Database management commands.

```
oridecon db init [--reset] [--seed]
oridecon db migrate [--name <migration>] [--auto]
oridecon db seed [--file seeds.py]
oridecon db shell
```

### `oridecon gen`

Code generation commands.

```
oridecon gen provider <name> [--output src/providers/]
oridecon gen module <name> [--output src/modules/]
oridecon gen migration [--auto-detect]
```

### `oridecon inspect`

Inspect runtime state of a running application or configuration.

```
oridecon inspect providers [--json]
oridecon inspect config [--section <section>]
oridecon inspect routes
oridecon inspect health
```

| Flag | Description |
|------|-------------|
| `--json` | Output as JSON |
| `--section` | Filter config to a specific section |

### `oridecon shell`

Open an interactive Python REPL with the Oridecon application loaded.

```
oridecon shell [target]
```

### `oridecon init`

Initialize Oridecon in an existing project.

```
oridecon init [--force]
```

Creates `application.yaml`, project scaffold, and optional `pyproject.toml` updates.

### `oridecon add`

Add a provider or extension to the project.

```
oridecon add <package> [--version <version>]
oridecon add provider <name>
```

### `oridecon config`

Configuration management.

```
oridecon config view [--section <section>]
oridecon config validate [--file application.yaml]
```

### `oridecon contrib`

Discover and inspect installed contributors (plugins).

```
oridecon contrib list [--json]
oridecon contrib info <name>
```

| Flag | Description |
|------|-------------|
| `--json` | Machine-readable output |

### `oridecon project`

Project management utilities.

```
oridecon project test [path] [--coverage] [--verbose] [--runner pytest]
oridecon project lint [path] [--fix] [--check]
oridecon project routes
```

### `oridecon system`

System information and diagnostics.

```
oridecon system info
oridecon system diagnostics
oridecon system check
```

### `oridecon version`

Show framework and package versions.

```
oridecon version [--all]
```

| Flag | Description |
|------|-------------|
| `--all` | List versions of all installed Oridecon packages |

### `oridecon list`

List all available commands.

```
oridecon list [--group <group>] [--json]
```

| Flag | Description |
|------|-------------|
| `--group`, `-g` | Filter by category |
| `--json` | Machine-readable output |

### `oridecon completion`

Generate shell completion script.

```
oridecon completion --shell <bash|zsh|fish|powershell>
```

Install with: `eval "$(oridecon completion --shell bash)"`

### `oridecon test`

Run project tests (delegates to `oridecon project test`).

```
oridecon test [path] [--coverage] [--verbose]
```

### `oridecon lint`

Run project linting (delegates to `oridecon project lint`).

```
oridecon lint [path] [--fix]
```

### `oridecon events`

Event schema management.

```
oridecon events schema validate
oridecon events schema migrate
```

## Plugin/contributor commands

Packages can register commands via the `oridecon.cli.commands` entry point. Contributor commands appear under their own category in `oridecon list`. Register in `pyproject.toml`:

```toml
[project.entry-points."oridecon.cli.commands"]
my_contrib = "my_package.cli:app"
```

## See also

- `CLIModule` — DI integration for CLI commands
- `CommandRegistry` — programmatic command registration
- `ContributorRuntime` — plugin discovery at runtime
- `PUBLIC_PACKAGE_CLI_MATRIX.md` — per-package command ownership
