---
title: "The oridecon CLI"
description: "Scaffold projects, run servers, manage migrations, and inspect your app from one command."
---

`oridecon-cli` ships the `oridecon` command — the day-to-day driver for every Oridecon project. It scaffolds new apps, runs the development server, drives database migrations, manages configuration, and exposes a plugin surface that lets installed extensions contribute their own subcommands.

For the full command reference, see the [`oridecon-cli` package docs](/packages/oridecon-cli/).

---

## 1. Install & Verify

```bash
pip install oridecon-cli       # or: uv add oridecon-cli
oridecon --version             # → oridecon <version>
oridecon --help                # full command list
```

The CLI is also pulled in transitively by most projects, so `uv sync` from a generated project is usually enough.

Global flags work on every subcommand:

| Flag | Effect |
| --- | --- |
| `--json` | machine-readable output where supported |
| `--quiet`, `-q` | suppress non-essential output |
| `--debug` | print tracebacks on error |
| `--no-color` | disable ANSI colour |
| `--config`, `-c` | path to `application.yaml` |

---

## 2. Scaffolding a New Project

`oridecon new project` renders a project from the canonical scaffold
(`oridecon/cli/scaffold.py`) — every template is generated from the same
generator→path map as `oridecon gen`:

```bash
oridecon new project my-app                      # default template: web-api
oridecon new project my-app --template api
oridecon new project my-platform --template full
```

| Flag | Default | Notes |
| --- | --- | --- |
| `--template`, `-t` | `web-api` | one of `minimal`, `api`, `web-api`, `graphql`, `worker`, `full`, `fullstack` |
| `--directory`, `-d` | `.` | parent directory for the new project |
| `--interactive`, `-i` | `false` | prompts for the template |

`oridecon new module <name>` creates a feature module
(`protocols.py`, `provider.py`, `services.py`) and registers it with the
composition root; `oridecon gen controller users --module auth` writes
module-local components (`auth/controllers/users_controller.py`) while
cross-cutting generators write into `src/<app>/shared/`.

To scaffold a reusable extension package instead of an application:

```bash
oridecon new package my-feature        # → oridecon-my-feature/ with src/ + provider stub
```

`oridecon init` writes a minimal `application.yaml` into an *existing* directory — useful when adopting Oridecon in a project that already has a `pyproject.toml`:

```bash
oridecon init --full          # full config (web/db/auth/cache/monitor sections)
oridecon init --minimal       # just project + logging (default)
oridecon init --force         # overwrite an existing application.yaml
```

See [Project Structure](/getting-started/project-structure/) for what the templates lay down.

---

## 3. Running Locally

Two commands launch your app — pick by intent:

```bash
oridecon run                  # production-shaped: --host 127.0.0.1, --reload on
oridecon dev                  # development server, --reload on, ORI_ENV=development
```

Both auto-detect your entry point (`src/main.py`, `create_app`, etc.) using `discover_entry_point` and pick the best available server backend (prefers `granian` → `uvicorn`, falls back to `hypercorn`).

`oridecon run` flags:

| Flag | Default | Notes |
| --- | --- | --- |
| `target` (positional) | auto-detected | `module:attr`, e.g. `my_app.app:create_app` |
| `--host`, `-h` | `127.0.0.1` | bind address |
| `--port`, `-p` | `8000` | bind port |
| `--reload/--no-reload` | `true` | hot reload |
| `--workers`, `-w` | `1` | worker processes |
| `--profile` | none | sets `ORI_PROFILE` for the run |
| `--server` | auto | `uvicorn`, `granian`, or `hypercorn` |
| `--mcp-port` | none | also serve MCP (SSE) on this port |

`oridecon dev` accepts `--entry`, `--host`, `--port`, `--reload/--no-reload`, `--env`, `--server`. For production, use `oridecon dev start` (binds `0.0.0.0`, no reload, takes `--workers`) or invoke an ASGI server directly — see [Deployment](/guides/deployment/).

:::note
The reloader watches `.py` files. Changes to `application.yaml` require a manual restart.
:::

---

## 4. Database Migrations

`oridecon db` wraps `oridecon-sql`'s migration runner. The most common flow:

```bash
oridecon db init migrations              # create migrations/ directory
oridecon db create add_users_table       # new empty migration file
oridecon db upgrade                      # apply pending migrations
oridecon db status                       # show current version + pending
oridecon db history --limit 20           # last N applied migrations
oridecon db downgrade                    # roll back the most recent
oridecon db downgrade 0003_seed          # roll back to a specific version
```

Inspection and maintenance:

```bash
oridecon db inspect                      # list tables + columns
oridecon db inspect --table users        # one table's columns + types
oridecon db shell                        # open psql / mysql / sqlite3 client
oridecon db validate                     # check applied migrations have files
oridecon db reset --force                # drop & re-migrate (SQLite-optimized)
oridecon db backup --output dump.sql
oridecon db restore dump.sql --force
```

Seed scripts in `seeds/*.py` (each exposing a `run(provider)` function) are applied by `oridecon db seed` or as part of `oridecon db reset --seed`.

All `db` commands read `DATABASE_URL` from the environment (default `sqlite:///./dev.db`). When `oridecon-sql` is installed, the runner is resolved through the DI container so connection pooling and observability hooks are active.

See the [Database guide](/guides/database/) for the repository pattern these migrations support.

---

## 5. Inspecting & Diagnosing

```bash
oridecon list                            # all available commands, grouped
oridecon list --group Database
oridecon version --all                   # versions of every installed oridecon-* package
oridecon system info                     # Python version, platform, config path
oridecon system health                   # project + contributor health checks
oridecon system doctor --fix             # diagnostics with auto-fix hints
oridecon system providers                # provider sections in application.yaml
```

Installed extensions register CLI **contributors** — discover them with:

```bash
oridecon contrib list                    # all contributors + their contributions
oridecon contrib inspect sql             # generators/commands/health checks for one
oridecon contrib check                   # verify every contributor loads
```

Code generation routes through contributors as well:

```bash
oridecon gen list                        # all discovered generators
oridecon gen provider MyProvider         # core generator: scaffolds a provider class
```

---

## 6. Configuration

The CLI looks for `application.yaml` in the current directory (and walks up to find one). Override with `--config /path/to/app.yaml`.

Profiles are environment-driven — set `ORI_PROFILE=production` and a matching `application.production.yaml` is overlaid on the base config. Any value can be overridden by a `ORI_`-prefixed env var with `__` for nesting:

```bash
export ORI_PROFILE=staging
export ORI_SQL__BACKEND__URL=postgresql+asyncpg://...
```

Useful config commands:

```bash
oridecon config show                     # current resolved config (secrets masked)
oridecon config show --reveal-secrets    # unmasked
oridecon config validate                 # schema + cross-field validation
oridecon config doctor --env production  # environment-specific diagnostics
oridecon config env                      # ${VAR} references and whether they're set
oridecon config env --missing            # exit 1 if any are unset
oridecon config env-example              # generate .env.example from config
oridecon config diff -c application.production.yaml
oridecon config schema                   # dump the JSON schema
```

See [Configuration](/getting-started/configuration/) and [YAML Configuration](/fundamentals/yaml-configuration/) for the full layering rules.

---

## 7. Adding Providers & Shell Completion

```bash
oridecon add database                    # add oridecon-sql + db: section to YAML
oridecon add auth                        # add oridecon-auth + auth: section
```

The `add` command edits `pyproject.toml` (via `uv add` when available) and patches `application.yaml` with the provider's default config block.

Generate shell completion:

```bash
oridecon completion --shell bash         # also: zsh, fish, powershell
eval "$(oridecon completion --shell zsh)"
```

---

## Next Steps

- [Your First App](/getting-started/first-app/) — the 60-second walkthrough using `oridecon new` and `oridecon run`
- [Database & Persistence](/guides/database/) — the repository pattern these migrations feed
- [Deployment & Infrastructure](/guides/deployment/) — running `oridecon` in production
- [`oridecon-cli` package](/packages/oridecon-cli/) — full flag-by-flag reference and the contributor API
