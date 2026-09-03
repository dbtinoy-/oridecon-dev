---
title: oridecon-cli How-Tos
description: Task-oriented recipes for the Oridecon CLI
---

## Scaffold a Full-Stack Project

```bash
oridecon new project my-app --template full -d ./workspace
cd ./workspace/my-app
ls src/my_app/
```

The `full` template includes `application.yaml`, `app.py`, modules structure, tests, and `pyproject.toml`.

## Create a New Extension Package

```bash
oridecon new package my-feature -d ./extensions
cd ./extensions/oridecon-my-feature
uv sync
uv run pytest
```

Scaffolds `oridecon-my-feature/` with `pyproject.toml`, `src/oridecon/my_feature/`, `di/provider.py`, and a unit test scaffold.

## List All Available Generators

```bash
oridecon gen list
```

Generators are contributed by installed packages. Each entry shows the generator name and description.

## Generate a Model, Service, and Controller

```bash
oridecon gen model Product
oridecon gen service ProductService
oridecon gen repository ProductRepository
oridecon gen controller ProductController
```

Generated files are placed in the project's `src/` tree, following framework conventions.

## Run Database Migrations

```bash
oridecon db init          # create initial migration
oridecon db migrate -m "add email field"
oridecon db upgrade       # apply pending
oridecon db rollback      # revert last
oridecon db status        # check state
oridecon db list          # show history
```

Requires `oridecon-sql` to be installed in the project.

## Inspect the Runtime

```bash
oridecon inspect providers    # list DI providers
oridecon inspect routes       # show HTTP routes
oridecon inspect health       # run health checks
oridecon inspect container    # show container bindings
```

## Start an Interactive Shell

```bash
oridecon shell                # REPL with app context
oridecon shell --ipython      # use IPython if available
oridecon shell --no-app       # plain Python REPL
```

The context-loaded shell provides `app`, `container`, `config`, `db`, `cache`, and `events`.

## Run Project Checks as a Pre-Commit Gate

```bash
oridecon test                 # run pytest
oridecon lint                 # run ruff
oridecon project typecheck    # run mypy
oridecon project run-all      # all checks
```

## Notes

- Use `--json` flag on any command for machine-readable output
- Generators create files relative to the project root; run from the project directory
- Migration files are timestamped and stored in the project's migrations directory
- The dev server and run command auto-discover `create_app()`; use `module:attr` syntax to override
