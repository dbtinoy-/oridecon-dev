# oridecon-secrets

Secret vaults with rotation, tenant isolation, and audit logging for the Oridecon Framework.
Supports HashiCorp Vault, AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, and in-memory
backends with automatic key rotation, version tracking, and tenant-scoped secret stores.

---

## Overview

oridecon-secrets provides a `RotatableSecretStoreProtocol`-based secret management system
with versioned rotation, tenant isolation, audit logging, and pluggable backends. All services
are wired via `SecretsProvider`, which registers the secret store and rotation decorator
with the DI container.

> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon-secrets
# Optional extras
uv add "oridecon-secrets[vault]"    # HashiCorp Vault backend
uv add "oridecon-secrets[aws]"      # AWS Secrets Manager backend
uv add "oridecon-secrets[gcp]"      # GCP Secret Manager backend
uv add "oridecon-secrets[azure]"    # Azure Key Vault backend
```

## Quick Start

```python
from oridecon import Application
from oridecon.secrets import SecretsModule
from oridecon.secrets.types import RotatableSecretStoreProtocol


async def main() -> None:
    async with Application.boot(modules=[SecretsModule.configure()]) as app:
        store = await app.container.resolve(RotatableSecretStoreProtocol)
        # ... work with the secret store ...


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## Configuration

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `name` | `"secrets"` | `ORI_SECRETS__NAME` | Configuration name |
| `enabled` | `true` | `ORI_SECRETS__ENABLED` | Enable the secrets subsystem |
| `backend_type` | `memory` | `ORI_SECRETS__BACKEND_TYPE` | Backend store type (`memory`, `vault`, `aws`, `gcp`, `azure`) |
| `backend_options` | `{}` | — | Keyword arguments forwarded to the backend constructor |
| `max_age_seconds` | `7776000` | `ORI_SECRETS__MAX_AGE_SECONDS` | Max age before automatic rotation |
| `warning_before_seconds` | `86400` | `ORI_SECRETS__WARNING_BEFORE_SECONDS` | Seconds before expiry to emit warnings |
| `tenant_id` | `null` | `ORI_SECRETS__TENANT_ID` | Optional tenant namespace |
| `audit_actor_id` | `"secrets-system"` | `ORI_SECRETS__AUDIT_ACTOR_ID` | Actor identifier for audit logs |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `SecretsModule.configure(config)` | Configure with explicit SecretsConfig |
| `SecretsModule.stub()` | Minimal config for testing (memory backend) |

## Key Features

- **Versioned secrets** — Every `set` and `rotate` creates a new version; full history retained
- **Automatic rotation** — `RotationDecorator` (`get_rotated`, `get_current_version`, `check_warnings`) serves a fresh secret when the current version is past `max_age_seconds`
- **Tenant isolation** — `TenantScopedSecretStore` prefixes keys per tenant for multi-tenant apps
- **Audit logging** — `SecretAuditDecorator` logs all store operations through `AuditLoggerProtocol`
- **Pluggable backends** — `HashicorpVaultStore` (KV v2) and in-memory (`FakeRotatableSecretStore`)
- **Bulk operations** — `get_bulk` for fetching multiple secrets at once
- **Version introspection** — `list_versions` and `get_version` for audit and rollback workflows

## Testing

```python
from oridecon.testing.fakes import FakeRotatableSecretStore
from oridecon.testing.compliance import StoreConformanceSuite


class TestMyStore(StoreConformanceSuite):
    @pytest.fixture
    def make_store(self):
        return FakeRotatableSecretStore
```

## Key Source Files

| File | What it contains |
|------|----------------|
| `src/oridecon/secrets/module.py` | `SecretsModule` class with factory methods |
| `src/oridecon/secrets/di/provider.py` | `SecretsProvider` — wires secret store into DI container |
| `src/oridecon/secrets/config.py` | `SecretsConfig` and backend selection |
| `src/oridecon/secrets/types.py` | `RotatableSecretStoreProtocol`, `VersionedSecret`, `SecretVersion` |
| `src/oridecon/secrets/rotation/` | `RotationDecorator` and `RotationSchedule` for automatic key rotation |
| `src/oridecon/secrets/tenancy/` | `TenantScopedSecretStore` for multi-tenant key isolation |
| `src/oridecon/secrets/audit/` | `SecretAuditDecorator` for operation audit logging |
| `src/oridecon/secrets/backends/` | Backend implementations (Vault, etc.) |
