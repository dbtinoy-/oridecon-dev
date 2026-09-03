---
title: oridecon-cli Troubleshooting
description: Common CLI errors, their causes, and how to fix them
---

## `oridecon` Command Not Found

**Cause:** The package is not installed or the virtual environment is not activated.

**Solution:**
```bash
uv add oridecon-cli
# or run via uv without installing:
uv run oridecon --help
```

## `ConfigNotFoundError` — Configuration File Not Found

**Exception:** `oridecon.cli.ConfigNotFoundError`

**Cause:** A CLI command that needs project context (`run`, `dev`, `db`, `inspect`, `gen`) was run outside a project directory.

**Solution:**
```bash
# Create an application.yaml in the current directory
oridecon init

# Or run from the project root
cd my-project
```

## `ProviderNotInstalledError` — Provider Not Installed

**Exception:** `oridecon.cli.ProviderNotInstalledError`

**Cause:** A command requires a package that is not installed (e.g., `oridecon-sql` for `db` commands).

**Solution:**
```bash
uv add oridecon-sql    # for database commands
uv add oridecon-web    # for web-related generators
```

## Generator Not Found

**Cause:** The generator's contributing package is not installed.

**Solution:**
```bash
uv add oridecon-web    # or the relevant package
oridecon gen list      # verify it appears
```

## Entry Point Not Detected

**Cause:** `oridecon run` or `oridecon dev` could not find `create_app()` in the project.

**Solution:**
```bash
# Specify the entry point explicitly
oridecon run my_app.app:create_app

# Or ensure your app module defines create_app() or 'app' at module level
```

## Server Backend Not Available

**Cause:** The preferred server backend (Granian, Uvicorn) is not installed.

**Solution:**
```bash
uv add uvicorn
# or
uv add granian
```

The CLI auto-detects available backends and falls back gracefully.

## CLI config TOML parse error

```
Error: Failed to parse config file at ~/.config/oridecon/config.toml
```

**Cause:** The TOML config file contains syntax errors — missing quotes, invalid tables, or trailing commas.

**Fix:** Validate the TOML file:

```bash
uv run python -c "import tomllib; tomllib.load(open('~/.config/oridecon/config.toml', 'rb'))"
```

The default config is created by `ConfigManager.save()` and should be valid. If the file is corrupted, delete it and let the CLI recreate it:

```bash
rm ~/.config/oridecon/config.toml
```

## Generator fails with package import error

```
Error: Generator 'web-api' failed: No module named 'oridecon-web'
```

**Cause:** The generator's contributing package (`oridecon-web`, etc.) is not installed. Generators are discovered via entry points and may declare optional dependencies.

**Fix:** Install the required package:

```bash
uv add oridecon-web
oridecon gen list  # verify it appears
```

## Server backend detection fails

```
Warning: No ASGI server backend found. Install uvicorn or granian.
```

**Cause:** Neither `uvicorn` nor `granian` is installed in the current environment. `oridecon run` and `oridecon dev` require an ASGI server to serve the application.

**Fix:** Install a server backend:

```bash
uv add uvicorn
# or for better performance:
uv add granian
```

The CLI prefers Granian when available and falls back to Uvicorn.

## Output shows raw ANSI color codes

**Symptom:** Terminal output contains literal escape sequences like `[32m` instead of colored text.

**Cause:** The terminal does not support ANSI color codes (pipe/redirect, CI output, or `NO_COLOR` environment). The CLI detects terminal capabilities but may not disable color when output is piped.

**Fix:** Disable colors explicitly:

```bash
oridecon --no-color <command>
# or
ORI_CLI__COLOR=false oridecon <command>
```

For scripted output, use `--json` for machine-readable results:

```bash
oridecon system info --json
```
