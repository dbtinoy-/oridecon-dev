# oridecon-tenancy

Multi-tenant resolution, lifecycle, and isolation for the Oridecon Framework.

---

## Overview

`oridecon-tenancy` provides a composable resolver chain (JWT claim, header, subdomain, path) for tenant identification, ASGI enforcement middleware, three data-isolation strategies (row-level, schema, database), tenant lifecycle CRUD with domain event emission, and per-tenant config overrides — all wired through Oridecon's DI/IoC container.

---


> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon oridecon-tenancy

# With SQL tenant store
uv add "oridecon-tenancy[sql]"
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module
from oridecon.tenancy import TenancyModule
from oridecon.tenancy.config import ResolutionConfig, TenancyConfig
from oridecon.contracts.tenancy.protocols import TenantProviderProtocol


@module(
    imports=[
        TenancyModule.configure(
            TenancyConfig(
                resolution=ResolutionConfig(
                    resolvers=["jwt_claim", "header"],
                    header_name="x-tenant-id",
                    jwt_claim_key="tenant_id",
                    validator_cache_ttl=300,
                ),
            )
        )
    ]
)
class AppModule(Module):
    pass


async def main() -> None:
    async with Application.boot(modules=[AppModule]) as app:
        provider = await app.container.resolve(TenantProviderProtocol)
        tenants = await provider.list_tenants()
        print(f"Active tenants: {len(tenants)}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## Configuration

> **Zero-config usage:** Call `TenancyModule.configure()` with no arguments to use all defaults.

### Option 1 — YAML file

```yaml
# application.yaml
tenancy:
  resolution:
    resolvers: ["jwt_claim", "header"]
    header_name: "x-tenant-id"
    jwt_claim_key: "tenant_id"
  lifecycle:
    isolation_strategy: "row_level"
    auto_provision_isolation: true
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_TENANCY__ENABLED=true
export ORI_TENANCY__RESOLUTION__RESOLVERS=["jwt_claim", "header"]
```

### Option 3 — Python

```python
from oridecon.tenancy import TenancyModule
from oridecon.tenancy.config import TenancyConfig, ResolutionConfig, LifecycleConfig

TenancyModule.configure(
    TenancyConfig(
        resolution=ResolutionConfig(
            resolvers=["jwt_claim", "header"],
            header_name="x-tenant-id",
            jwt_claim_key="tenant_id",
        ),
        lifecycle=LifecycleConfig(isolation_strategy="schema"),
    )
)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `resolution.resolvers` | `["jwt_claim", "header", "subdomain", "path"]` | `ORI_TENANCY__RESOLUTION__RESOLVERS` | Ordered resolver list; first match wins |
| `resolution.header_name` | `"x-tenant-id"` | `ORI_TENANCY__RESOLUTION__HEADER_NAME` | HTTP header read by `HeaderTenantResolver` |
| `resolution.subdomain_pattern` | `null` | `ORI_TENANCY__RESOLUTION__SUBDOMAIN_PATTERN` | Base domain for subdomain extraction |
| `resolution.jwt_claim_key` | `"tenant_id"` | `ORI_TENANCY__RESOLUTION__JWT_CLAIM_KEY` | JWT payload claim key |
| `resolution.validator_cache_ttl` | `300` | `ORI_TENANCY__RESOLUTION__VALIDATOR_CACHE_TTL` | Seconds a validated `TenantInfo` is cached |
| `lifecycle.isolation_strategy` | `"row_level"` | `ORI_TENANCY__LIFECYCLE__ISOLATION_STRATEGY` | `"row_level"`, `"schema"`, or `"database"` |
| `lifecycle.auto_provision_isolation` | `true` | `ORI_TENANCY__LIFECYCLE__AUTO_PROVISION_ISOLATION` | Run isolation strategy on tenant creation |
| `overrides.cache_ttl` | `60` | `ORI_TENANCY__OVERRIDES__CACHE_TTL` | Seconds a tenant's config dict is cached |
| `integration.cache_key_prefix` | `true` | `ORI_TENANCY__INTEGRATION__CACHE_KEY_PREFIX` | Prefix cache keys with `t:{tenant_id}:` |
| `integration.sql_context_bridge` | `true` | `ORI_TENANCY__INTEGRATION__SQL_CONTEXT_BRIDGE` | Propagate `TENANT_ID` to oridecon-sql context |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `TenancyModule.configure(config)` | Configure with explicit `TenancyConfig` |
| `TenancyModule.stub()` | Minimal config for testing (exports `TenantProviderProtocol` and `TenantConfigProviderProtocol`) |

## Key Features

- **Resolver chain** — JWT claim, header, subdomain, and path resolvers in priority order
- **ASGI middleware** — `TenantContextMiddleware` resolves tenant on every HTTP/WebSocket request
- **Three isolation strategies** — row-level (default), schema-per-tenant, database-per-tenant
- **Tenant lifecycle CRUD** — create, activate, deactivate, suspend with domain event emission
- **Per-tenant config overrides** — key-value overrides with defaults and `TenantConfigChanged` events
- **Cache key prefixing** — wraps `CacheBackendProtocol` with tenant-prefixed keys automatically
- **oridecon-sql integration** — `TenantSQLContextBridge` enables `TenantScope` and `multi_tenant=True` filtering

## Testing

```python
import pytest
from oridecon import Application
from oridecon.tenancy import TenancyModule
from oridecon.contracts.tenancy.commands import CreateTenantCommand
from oridecon.tenancy.lifecycle.service import TenantLifecycleService


@pytest.mark.asyncio
async def test_tenant_lifecycle() -> None:
    async with Application.boot(modules=[TenancyModule.stub()]) as app:
        lifecycle = await app.container.resolve(TenantLifecycleService)

        result = await lifecycle.create_tenant(
            CreateTenantCommand(slug="acme", name="ACME Corp")
        )
        assert result.is_ok()
        assert result.unwrap().slug == "acme"
```

## Key Source Files

| File | What it contains |
|------|----------------|
| `src/oridecon/tenancy/module.py` | `TenancyModule.configure()`, `.stub()` |
| `src/oridecon/tenancy/config.py` | `TenancyConfig`, `ResolutionConfig`, `LifecycleConfig` |
| `src/oridecon/tenancy/di/provider.py` | `TenancyProvider` bundle and sub-providers |
| `src/oridecon/tenancy/resolution/chain.py` | `CompositeResolver` |
| `src/oridecon/tenancy/enforcement/middleware.py` | `TenantContextMiddleware` |
| `src/oridecon/tenancy/enforcement/guard.py` | `TenantGuard` |
| `src/oridecon/tenancy/lifecycle/service.py` | `TenantLifecycleService` |
| `src/oridecon/tenancy/isolation/registry.py` | `IsolationStrategyRegistry` |
| `src/oridecon/tenancy/config_overrides/service.py` | `TenantConfigService` |