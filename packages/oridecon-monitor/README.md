# oridecon-monitor

Observability, health checks, and metrics for the Oridecon Framework.
Supports Prometheus, OpenTelemetry, structured log export, and `/health` endpoints
that integrate with Kubernetes probes and load-balancer health checks.

---

## Overview

oridecon-monitor provides metrics collection, distributed tracing, health checks, and alerting for Oridecon applications. It integrates with Prometheus and OpenTelemetry backends, supports composable health checks with liveness and readiness flavours, and includes decorators for instrumenting services with custom metrics and traces. All services are wired via `MonitorProvider`, which registers monitoring protocols with the DI container.

> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon-monitor
# Optional extras
uv add "oridecon-monitor[prometheus]"    # Prometheus + Grafana
uv add "oridecon-monitor[opentelemetry]" # OTLP / Jaeger / Zipkin
```

## Quick Start

```python
from oridecon import Application
from oridecon.monitor import MonitorModule


async def main() -> None:
    async with Application.boot(modules=[MonitorModule.configure()]) as app:
        # ... metrics, health checks and /health endpoints active ...
        ...


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## Configuration

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `prometheus.enable_default_metrics` | `true` | `ORI_MONITOR__PROMETHEUS__ENABLE_DEFAULT_METRICS` | Enable default process metrics |
| `prometheus.port` | `8000` | `ORI_MONITOR__PROMETHEUS__PORT` | Port for the Prometheus metrics endpoint |
| `prometheus.path` | `/metrics` | `ORI_MONITOR__PROMETHEUS__PATH` | URL path for metrics scraping |
| `tracing.enabled` | `true` | `ORI_MONITOR__TRACING__ENABLED` | Enable distributed tracing via OTLP |
| `tracing.sample_rate` | `1.0` | `ORI_MONITOR__TRACING__SAMPLE_RATE` | Trace sampling rate (0.0–1.0; use 0.1 in production) |
| `health.path` | `/health` | `ORI_MONITOR__HEALTH__PATH` | Base path for health check endpoints |
| `health.interval` | `30` | `ORI_MONITOR__HEALTH__INTERVAL` | Seconds between background health polls |
| `health.timeout` | `5` | `ORI_MONITOR__HEALTH__TIMEOUT` | Per-check timeout in seconds |
| `slo.enabled` | `true` | `ORI_MONITOR__SLO__ENABLED` | Enable periodic SLO evaluation worker |
| `slo.evaluation_interval` | `60` | `ORI_MONITOR__SLO__EVALUATION_INTERVAL` | Seconds between SLO evaluation cycles |
| `slo.suppression_window_seconds` | `300` | `ORI_MONITOR__SLO__SUPPRESSION_WINDOW_SECONDS` | Min seconds between duplicate alerts |

Structured logging is not configured here. Use the core `ORI_ORIDECON__LOGGING__*` variables (via `oridecon.config.LoggingConfig`) to set log level, JSON format, per-logger levels, redaction, and sampling.

## Endpoint protection

`HealthCheckProvider` and `PrometheusMiddleware` expose their endpoints
(`/health` and `/metrics` by default) **without authentication** — the
intentional default, because Kubernetes probes and Prometheus scrapers
usually run inside a trusted network and cannot always carry credentials.

If these endpoints are reachable from outside that boundary, pass an
`auth_token` to require `Authorization: Bearer <token>` on every request:

```python
from oridecon.monitor.middleware import HealthCheckProvider, PrometheusMiddleware

app = HealthCheckProvider(path="/health", auth_token=os.environ["HEALTH_TOKEN"])
app = PrometheusMiddleware(app, path="/metrics", auth_token=os.environ["METRICS_TOKEN"])
```

Requests without the matching token receive `401` with
`WWW-Authenticate: Bearer`. Configure the same token on the scraper side
(e.g. Prometheus `scrape_configs` → `authorization.credentials`).

Failed dependency checks never echo the raw driver message into the JSON
health payload — the response carries only the exception type name
(`"ConnectionError: connection check failed"`), while the full message is
written to the application logs.

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `MonitorModule.configure(backend, config)` | Configure with explicit backend and optional MonitorConfig |
| `MonitorModule.stub()` | Minimal config for testing |
| `MonitorModule.with_slo(backend, config)` | Configure with SLO exports for the DI container |

## Key Features

- **Prometheus** — Auto `/metrics` endpoint; request counters, histograms, gauges
- **OpenTelemetry** — Distributed tracing via OTLP exporter to Jaeger / Honeycomb
- **Health checks** — Composable checks with liveness + readiness flavours
- **Cached checks** — Per-check TTL to avoid thundering-herd on slow dependencies
- **DB instrumentation** — Automatic query timing and error tagging
- **HTTP instrumentation** — Outbound request tracking for `oridecon-http`
- **Messaging instrumentation** — Kafka / RabbitMQ consumer lag, publish rate
- **Alerting** — Configurable alert rules with tier-aware webhook delivery
- **SLO Monitoring** — Burn-rate evaluation with configurable suppression window
- **Tiered alerts** — P0 (PagerDuty) / P1 (business hours Slack) / P2 (weekly digest) routing
- **Structured logging** — `json` / `text` log output via `logging.level` / `logging.format`
- **Grafana dashboards** — Pre-built dashboard JSON in `oridecon-monitor/dashboards/`

## Testing

```python
async with Application.boot(modules=[MonitorModule.stub()]) as app:
    # your test code
    ...
```

## Key Source Files

| File | What it contains |
|------|----------------|
| `src/oridecon/monitor/module.py` | `MonitorModule` class with factory methods |
| `src/oridecon/monitor/di/provider.py` | `MonitorProvider` — wires monitoring protocols into DI container |
| `src/oridecon/monitor/config.py` | `MonitorConfig` and sub-config dataclasses |
| `src/oridecon/monitor/health/` | Health check registration and registry (`base.py`, `checker.py`, `registry.py`, ...) |
| `src/oridecon/monitor/instrumentation/decorators.py` | `@metered` and `@traced` decorators |
| `src/oridecon/monitor/slo/` | SLO evaluation, tiered alert dispatchers, channel implementations |
| `src/oridecon/monitor/alerts/` | Alert dispatcher protocols and tier routing |
| `dashboards/projection-health.json` | Grafana dashboard for SLO health and alerting |

## SLO Monitoring

Service Level Objectives are evaluated on a configurable interval. Each SLO tracks a
metric percentile against a threshold and fires alerts on budget exhaustion.

### Defining an SLO

```python
from datetime import timedelta
from oridecon.contracts.monitor import ProjectionTier
from oridecon.monitor.slo import SLO, SLOMonitor

monitor = SLOMonitor()

slo = SLO(
    name="api.p99_latency",
    metric="http.request.duration",
    percentile=0.99,
    threshold_ms=200.0,
    window=timedelta(hours=1),
    tier=ProjectionTier.P1_BUSINESS_HOURS,
    owner="team-api",
    runbook_url="https://ops.runbook/api-slo",
)
monitor.register(slo)
```

### Recording Samples

```python
monitor.record_sample("http.request.duration", 150.0)
monitor.record_sample("http.request.duration", 350.0)
```

### Evaluating and Dispatching

```python
violations = await monitor.evaluate_and_dispatch()
```

Violations are routed through the configured `AlertDispatcherProtocol`. Alerts for the
same SLO are suppressed within the suppression window (default 300s) to avoid storms.

### Projection Tiers

| Tier | Enum Value | Behaviour |
|------|------------|-----------|
| P0 — Page | `ProjectionTier.P0_PAGE` | Routes to PagerDuty (or equivalent paging channel) immediately |
| P1 — Business Hours | `ProjectionTier.P1_BUSINESS_HOURS` | Queues outside business hours, flushes on schedule |
| P2 — Digest | `ProjectionTier.P2_DIGEST` | Accumulates in a weekly digest buffer |

### Worker Configuration

Enable periodic evaluation via config:

```yaml
# application.yaml
monitor:
  slo:
    enabled: true
    evaluation_interval: 60
    suppression_window_seconds: 300
```

Or via environment variables:

```bash
export ORI_MONITOR__SLO__ENABLED=true
export ORI_MONITOR__SLO__EVALUATION_INTERVAL=60
export ORI_MONITOR__SLO__SUPPRESSION_WINDOW_SECONDS=300
```
