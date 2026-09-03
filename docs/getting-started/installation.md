---
title: Installation
description: Install the Oridecon framework and get your environment ready
sidebar:
  order: 1
---

:::note[What you'll learn]
- Install Oridecon using **uv** (recommended) or pip
- Choose the right packages for your project
- Verify your installation
:::

:::tip[Alpha]
Oridecon is **alpha (0.1.x)**. Pin versions in production and expect public APIs to evolve before 1.0.
:::

## Requirements

- **Python 3.11** or higher
- **uv** (recommended) or pip

---

## Quick Install

```bash
# uv (recommended — fast, deterministic)
uv add oridecon

# pip
pip install oridecon
```

The core `oridecon` package gives you:

| Feature | Import | Description |
|---------|--------|-------------|
| `Application` | `from oridecon import Application` | Composition root with lifecycle management |
| `Provider` | `from oridecon import Provider` | Two-phase `register` / `boot` service wiring |
| `Container` | `from oridecon import Container` | IoC container — `singleton`, `scoped`, `transient` bindings |
| DI decorators | `from oridecon import singleton, injectable, scoped, transient` | Mark classes for auto-registration |
| `OrideconConfig` | `from oridecon import OrideconConfig` | YAML + env vars + profile overlays |
| `Result` | `from oridecon.result import Result, Ok, Err` | Explicit error handling with `unwrap`, `map`, `and_then` |
| `module` | `from oridecon import module, Module` | `@module` decorator with import/export boundaries |

`oridecon-contracts` (the zero-dependency protocol layer, imported as `oridecon.contracts.*`) is installed automatically as a dependency of `oridecon`.

---

## Common Stacks

Install only what you need. Every extension depends only on `oridecon` (core) and `oridecon-contracts` — never on each other.

### Web API

```bash
uv add oridecon-web
```

ASGI web layer — controllers, routing, middleware, OpenAPI docs, CORS, CSRF, rate limiting.

### Database

```bash
uv add oridecon-sql
```

Async SQL for Postgres / MySQL / SQLite — repositories, migrations, query building.

### AI

```bash
uv add oridecon-ai oridecon-ai-llm
```

Multi-provider LLM client and the orchestration layer. Add `oridecon-ai-rag`, `oridecon-ai-agents`, and `oridecon-vector` as needed.

---

## All Packages

The open-source ecosystem is 35+ extensions across these areas. See **[The Ecosystem](/ecosystem/)** for the full, annotated list.

| Category | Packages |
|----------|----------|
| **Foundation** | `oridecon`, `oridecon-contracts` |
| **Web & API** | `oridecon-web`, `oridecon-http`, `oridecon-graphql` |
| **Data & Persistence** | `oridecon-sql`, `oridecon-nosql`, `oridecon-cache`, `oridecon-storage`, `oridecon-search`, `oridecon-vector`, `oridecon-graph` |
| **AI** | `oridecon-ai`, `oridecon-ai-llm`, `oridecon-ai-rag`, `oridecon-ai-agents`, `oridecon-ai-memory`, `oridecon-ai-skills`, `oridecon-ai-session`, `oridecon-ai-mcp`, `oridecon-ai-workers`, `oridecon-ai-feedback` |
| **Messaging & Workflow** | `oridecon-events`, `oridecon-queue`, `oridecon-notification`, `oridecon-webhook`, `oridecon-workflow` |
| **Background Work** | `oridecon-tasks` |
| **Observability & Reliability** | `oridecon-monitor`, `oridecon-resilience`, `oridecon-audit`, `oridecon-ai-observability` |
| **Security & Multi-Tenancy** | `oridecon-auth`, `oridecon-tenancy`, `oridecon-features` |
| **Developer Tooling** | `oridecon-cli`, `oridecon-testing` |

---

## Developer Tools

```bash
# CLI — project scaffolding, dev server, migrations
uv add oridecon-cli

# Testing — fakes, test clients, compliance suites
uv add --dev oridecon-testing
```

With `oridecon-cli` installed you get the `oridecon` command:

```bash
oridecon new project my-app   # scaffold a project (or: oridecon new package <name>)
oridecon run                  # auto-detect create_app() and serve
oridecon db upgrade           # run migrations
```

---

## Verify Installation

```bash
python -c "import oridecon; print(oridecon.__version__)"
```

---

## Next Steps

- [Your First App](/getting-started/first-app/) — Build a working API
- [Project Structure](/getting-started/project-structure/) — Recommended layouts
- [Core Concepts](/getting-started/core-concepts/) — Providers, DI, Result type, and modules
- [The Ecosystem](/ecosystem/) — Every package, grouped by purpose
