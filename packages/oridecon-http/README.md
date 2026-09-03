# oridecon-http

Outbound HTTP client for the Oridecon Framework.

---

## Overview

Async outbound HTTP client for the Oridecon Framework. Provides a first-class
async HTTP client backed by `aiohttp`, with connection pooling, typed request/
response contexts, interceptor chains, base URL clients, streaming support, and
DI integration.

This package focuses on making **outbound** HTTP requests — for inbound web servers,
use `oridecon-web`. Resilience patterns (retry, circuit breaker) are layered in
through `oridecon-resilience`, not built in by default.


> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon-http
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module
from oridecon.http import HTTPModule, HTTPClientConfig


@module(imports=[HTTPModule.configure(HTTPClientConfig())])
class AppModule(Module):
    pass


async def main():
    async with Application.boot(modules=[AppModule]) as app:
        from oridecon.http import HTTPClient

        async with HTTPClient.session_context() as client:
            response = await client.get("https://api.example.com/users/123")
            if response.ok:
                user = await response.json()
                print(user)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## Configuration

> **Zero-config usage:** Call `HTTPModule.configure()` with no arguments to use defaults.

### Option 1 — YAML file

```yaml
# application.yaml
http:
  pool:
    max_connections: 100
    max_keepalive_connections: 50
    timeout: 30.0
  trust_env: true
  cookie_jar: true
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_HTTP__POOL__MAX_CONNECTIONS=100
export ORI_HTTP__POOL__TIMEOUT=30.0
export ORI_HTTP__TRUST_ENV=true
```

### Option 3 — Python

```python
from oridecon.http import HTTPModule, HTTPClientConfig, ConnectionPoolConfig

HTTPModule.configure(
    HTTPClientConfig(
        pool=ConnectionPoolConfig(
            max_connections=100,
            timeout=30.0,
        ),
        trust_env=True,
        cookie_jar=True,
    )
)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `pool.max_connections` | `10` | `ORI_HTTP__POOL__MAX_CONNECTIONS` | Total concurrent connections across all hosts |
| `pool.max_keepalive_connections` | `5` | `ORI_HTTP__POOL__MAX_KEEPALIVE_CONNECTIONS` | Keep-alive connections per host |
| `pool.max_connections_per_host` | `10` | `ORI_HTTP__POOL__MAX_CONNECTIONS_PER_HOST` | Max connections per individual host |
| `pool.timeout` | `30.0` | `ORI_HTTP__POOL__TIMEOUT` | Request timeout (seconds) |
| `pool.ttl_dns_cache` | `300` | `ORI_HTTP__POOL__TTL_DNS_CACHE` | DNS cache TTL (seconds) |
| `proxy` | `null` | `ORI_HTTP__PROXY` | HTTP/HTTPS proxy URL |
| `trust_env` | `True` | `ORI_HTTP__TRUST_ENV` | Read proxy settings from environment variables |
| `cookie_jar` | `True` | `ORI_HTTP__COOKIE_JAR` | Enable in-memory cookie jar |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `HTTPModule.configure(...)` | Configure with explicit HTTPClientConfig |
| `HTTPModule.stub()` | No-op HTTPModule for unit testing |

## Key Features

- **Connection pooling** — per-host limits, keepalive, DNS caching via aiohttp
- **Proxy support** — HTTP/HTTPS with environment variable auto-detection
- **Cookie jar** — optional, per-session in-memory cookie persistence
- **Streaming** — `StreamContext` for large file downloads
- **Interceptor chains** — composable auth, logging, metrics hooks
- **Type-safe contexts** — `RequestContext` and `ResponseContext` typed models

## Testing

```python
from oridecon.contracts.web import HTTPClientProtocol, HttpResponse


class FakeHTTPClient(HTTPClientProtocol):
    async def get(self, url: str, **kwargs) -> HttpResponse:
        return HttpResponse(status=200, headers={}, body=b'{"id": 123}')


# Inject into service under test
service = UserService(http_client=FakeHTTPClient())
```

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/http/module.py` | HTTPModule with factory methods |
| `src/oridecon/http/config.py` | HTTPClientConfig and ConnectionPoolConfig |
| `src/oridecon/http/di/provider.py` | HTTPProvider — wires HTTP client into DI container |
| `src/oridecon/http/client/` | HTTPClient and BaseURLHTTPClient |
| `src/oridecon/http/pool/` | ConnectionPool (aiohttp connector abstraction) |
| `src/oridecon/http/types.py` | RequestContext and ResponseContext typed models |
