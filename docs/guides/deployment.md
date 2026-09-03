---
title: "Deployment & Infrastructure"
description: "Going from local development to a production Oridecon deployment."
---

Oridecon applications are ordinary ASGI apps with a clean lifecycle, so they deploy like any modern Python service. This guide covers running, packaging, and configuring for production.

For the full command reference, see the [`oridecon-cli` package](/packages/oridecon-cli/).

---

## 1. Running the Application

A Oridecon `Application` is an ASGI callable (it auto-starts on first request), so you have several ways to run it.

### During development

```bash
# Auto-detects create_app() and serves with reload
oridecon run

# Pick the entry point, server, and port explicitly
oridecon run my_app.app:create_app --server uvicorn --port 8000
```

`oridecon run` supports `--host`, `--port`, `--workers`, `--reload/--no-reload`, `--profile` (sets `ORI_PROFILE`), and `--server` (`uvicorn`, `granian`, or `hypercorn`).

### In production

Point any ASGI server at your factory or app object:

```bash
uvicorn my_app.app:create_app --factory --host 0.0.0.0 --port 8000
# or
granian --interface asgi my_app.app:create_app --factory
```

### Non-web apps (workers, CLIs)

For applications without an HTTP server, run the lifecycle directly — `run_application` starts the app and shuts down cleanly on SIGINT/SIGTERM:

```python
import asyncio
from oridecon import Application, run_application
from my_app.app import create_app

asyncio.run(run_application(create_app()))
```

---

## 2. Configuration in Production

Drive everything through profiles and environment variables — never commit secrets.

```bash
export ORI_PROFILE=production         # loads application.production.yaml over the base
export ORI_SQL__BACKEND__URL=postgresql+asyncpg://...
export ORI_AUTH__SECRET_KEY=...
```

Any config key can be overridden with a `ORI_`-prefixed env var using `__` for nesting (see [YAML Configuration](/fundamentals/yaml-configuration/)). Set `ORI_QUIET=true` to suppress the startup banner in container logs.

---

## 3. Health Checks

`oridecon-monitor` exposes liveness/readiness endpoints (default `/health`), and `Application` provides programmatic probes for orchestrators:

```python
await app.liveness()       # is the process alive?
await app.readiness()      # ready to serve traffic?
await app.startup_check()  # finished booting?
await app.health_check()   # aggregated provider health
```

Wire these to your Kubernetes `livenessProbe` / `readinessProbe`.

---

## 4. Production Dockerfile

A multi-stage build with `uv` keeps images small:

```dockerfile
FROM python:3.12-slim-bookworm AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

FROM python:3.12-slim-bookworm
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY . .
ENV PATH="/app/.venv/bin:$PATH"
ENV ORI_PROFILE=production
EXPOSE 8000
CMD ["oridecon", "run", "--no-reload", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 5. Docker Compose (Local Dev)

```yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      ORI_PROFILE: development
      ORI_SQL__BACKEND__URL: postgresql+asyncpg://app:secret_pass@db/app_db
    depends_on:
      - db

  db:
    image: postgres:16
    environment:
      POSTGRES_DB: app_db
      POSTGRES_USER: app
      POSTGRES_PASSWORD: secret_pass
```

---

## 6. Pre-Deploy Checklist

- `ORI_PROFILE=production` and all secrets supplied via env vars.
- `debug: false` (validated by `config.validate_for_environment(Environment.PRODUCTION)`).
- Database `pool` sizes and `web.server.workers` tuned for your instance.
- Liveness/readiness probes wired to the health endpoints.
- Migrations applied: `oridecon db upgrade`.

---

## Next Steps

- [Configuration](/getting-started/configuration/) — profiles and env-var overrides
- [Project Structure](/getting-started/project-structure/) — the layouts referenced above
- [The Ecosystem](/ecosystem/) — observability and reliability packages
