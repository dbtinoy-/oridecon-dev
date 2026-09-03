---
title: oridecon-tenancy Configuration
description: Every configuration key for the tenancy subsystem
---

Config section: `tenancy`  
Env prefix: `ORI_TENANCY__`  
Config model: `TenancyConfig`

## Top-level

| Key | Type | Default | Env var | Description |
|-----|------|---------|---------|-------------|
| `resolution` | `ResolutionConfig` | — | `ORI_TENANCY__RESOLUTION__*` | Resolver chain configuration |
| `lifecycle` | `LifecycleConfig` | — | `ORI_TENANCY__LIFECYCLE__*` | Lifecycle and isolation |
| `overrides` | `ConfigOverridesConfig` | — | `ORI_TENANCY__OVERRIDES__*` | Per-tenant config overrides |
| `integration` | `IntegrationConfig` | — | `ORI_TENANCY__INTEGRATION__*` | Cross-package integration toggles |

## ResolutionConfig

| Key | Type | Default | Env var | Description |
|-----|------|---------|---------|-------------|
| `resolvers` | `list[str]` | `["jwt_claim", "header", "subdomain", "path"]` | `ORI_TENANCY__RESOLUTION__RESOLVERS` | Ordered resolver names |
| `header_name` | `str` | `"x-tenant-id"` | `ORI_TENANCY__RESOLUTION__HEADER_NAME` | Header name for `HeaderTenantResolver` |
| `subdomain_pattern` | `str \| None` | `None` | `ORI_TENANCY__RESOLUTION__SUBDOMAIN_PATTERN` | Base domain for subdomain extraction |
| `path_pattern` | `str \| None` | `"/tenants/{tenant_id}/"` | `ORI_TENANCY__RESOLUTION__PATH_PATTERN` | Path pattern for `PathTenantResolver` |
| `jwt_claim_key` | `str` | `"tenant_id"` | `ORI_TENANCY__RESOLUTION__JWT_CLAIM_KEY` | JWT claim key |
| `validator_cache_ttl` | `int` | `300` | `ORI_TENANCY__RESOLUTION__VALIDATOR_CACHE_TTL` | Cache TTL for validated tenants (seconds) |

## LifecycleConfig

| Key | Type | Default | Env var | Description |
|-----|------|---------|---------|-------------|
| `isolation_strategy` | `str` | `"row_level"` | `ORI_TENANCY__LIFECYCLE__ISOLATION_STRATEGY` | Name of isolation strategy |
| `auto_provision_isolation` | `bool` | `True` | `ORI_TENANCY__LIFECYCLE__AUTO_PROVISION_ISOLATION` | Auto-provision on tenant creation |

## ConfigOverridesConfig

| Key | Type | Default | Env var | Description |
|-----|------|---------|---------|-------------|
| `cache_ttl` | `int` | `60` | `ORI_TENANCY__OVERRIDES__CACHE_TTL` | Cache TTL for per-tenant config (seconds) |

## IntegrationConfig

| Key | Type | Default | Env var | Description |
|-----|------|---------|---------|-------------|
| `cache_key_prefix` | `bool` | `True` | `ORI_TENANCY__INTEGRATION__CACHE_KEY_PREFIX` | Prefix cache keys with tenant ID |
| `sql_context_bridge` | `bool` | `True` | `ORI_TENANCY__INTEGRATION__SQL_CONTEXT_BRIDGE` | Sync tenant context into SQL sessions |

## Example YAML

```yaml
tenancy:
  resolution:
    resolvers:
      - header
      - jwt_claim
    header_name: x-tenant-id
    jwt_claim_key: tenant_id
  lifecycle:
    isolation_strategy: row_level
    auto_provision_isolation: true
  overrides:
    cache_ttl: 120
  integration:
    cache_key_prefix: true
    sql_context_bridge: true
```

Env var override form:

```bash
export ORI_TENANCY__RESOLUTION__RESOLVERS='["header"]'
export ORI_TENANCY__LIFECYCLE__ISOLATION_STRATEGY=schema
```
