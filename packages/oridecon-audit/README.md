# oridecon-audit

Unified audit trail for the Oridecon Framework — append-only, HMAC-verified, retention-managed.

---

## Overview

`oridecon-audit` provides a unified, append-only audit trail with HMAC-SHA256 tamper detection, configurable per-severity retention policies, and scheduled integrity verification batches. The `AuditLogger` is fire-tolerant — audit failures never interrupt business logic.

---


> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon oridecon-audit

# For the SQL backend (recommended for production)
uv add oridecon-sql
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module
from oridecon.audit import AuditModule
from oridecon.audit.protocols import AuditLoggerProtocol
from oridecon.contracts.audit import AuditEntry, AuditEventSeverity


@module(
    imports=[
        AuditModule.configure(
            store_backend="memory",
            hmac_key=b"your-hmac-secret",
        )
    ]
)
class AppModule(Module):
    pass


async def main() -> None:
    async with Application.boot(modules=[AppModule]) as app:
        audit = await app.container.resolve(AuditLoggerProtocol)

        await audit.log(
            AuditEntry(
                action="user.deleted",
                actor_id="user-123",
                resource_type="user",
                resource_id="user-42",
                severity=AuditEventSeverity.HIGH,
            )
        )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

> The `"sql"` backend (default) requires `oridecon-sql` with a `DatabaseModule` registered; `"memory"` is an in-process store for development and tests.

## Configuration

> **Zero-config usage:** Call `AuditModule.configure()` with no arguments to use all defaults.

### Option 1 — YAML file

```yaml
# application.yaml
audit:
  store_backend: "sql"
  hmac_key: null
  retention_policy:
    default_retention_days: 365
  enable_admin: true
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_AUDIT__STORE_BACKEND=sql
export ORI_AUDIT__HMAC_KEY=your-hex-encoded-key
export ORI_AUDIT__RETENTION_POLICY__DEFAULT_RETENTION_DAYS=365
```

### Option 3 — Python

```python
from oridecon.audit import AuditModule

AuditModule.configure(
    store_backend="sql",
    hmac_key=b"your-hmac-secret",
    table_name="audit_log",
    retention_days=365,
    enable_admin=True,
)
```

For full control (e.g. per-severity retention overrides), build an `AuditConfig` directly and configure `retention_policy` with a `RetentionPolicy` from `oridecon.contracts.audit`:

```python
from oridecon.audit.config import AuditConfig
from oridecon.contracts.audit import RetentionPolicy

AuditConfig(
    store_backend="sql",
    hmac_key=b"your-hmac-secret",
    retention_policy=RetentionPolicy(
        default_retention_days=365,
        severity_overrides={"critical": 2555, "high": 1095},
    ),
    enable_admin=True,
)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `store_backend` | `"sql"` | `ORI_AUDIT__STORE_BACKEND` | Storage backend: `"sql"` or `"memory"` |
| `table_name` | `"audit_log"` | `ORI_AUDIT__TABLE_NAME` | SQL table name (SQL backend only) |
| `hmac_key` | `null` | `ORI_AUDIT__HMAC_KEY` | HMAC-SHA256 secret key (bytes; strings are used as UTF-8 bytes, not hex-decoded); `null` disables tamper detection |
| `retention_policy.default_retention_days` | `365` | `ORI_AUDIT__RETENTION_POLICY__DEFAULT_RETENTION_DAYS` | Default retention in days (0 = indefinite) |
| `retention_policy.severity_overrides` | `{"critical": 2555, "high": 1095}` | — | Per-severity retention overrides (days) |
| `verification_schedule` | `"0 * * * *"` | `ORI_AUDIT__VERIFICATION_SCHEDULE` | Cron expression for HMAC verification runs |
| `verification_batch_size` | `100` | `ORI_AUDIT__VERIFICATION_BATCH_SIZE` | Entries verified per scheduled run |
| `enable_admin` | `true` | `ORI_AUDIT__ENABLE_ADMIN` | Enable admin dashboard integration |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `AuditModule.configure(*, hmac_key=None, store_backend="sql", table_name="audit_log", retention_days=365, enable_admin=True)` | Configure the audit module (keyword arguments only) |

## Key Features

- **Fire-tolerant logging** — `AuditLogger.log()` never blocks calling code; errors are logged at WARNING and swallowed
- **HMAC-SHA256 checksums** — per-entry tamper detection verified on schedule or on-demand
- **Per-severity retention** — `PolicyBasedRetention` applies different retention periods per severity level
- **SQL backend** — append-only `SqlAuditStore` backed by `oridecon-sql`
- **Memory backend** — bounded in-process store for development and testing
- **Admin dashboard** — `AuditAdminContributor` adds an Audit Log panel
- **Scheduled verification** — hourly HMAC batch verification when a task scheduler is present

## Testing

```python
import pytest
from oridecon import Application
from oridecon.audit import AuditModule
from oridecon.audit.protocols import AuditLoggerProtocol, AuditStoreProtocol
from oridecon.contracts.audit import AuditEntry, AuditQuery


@pytest.mark.asyncio
async def test_audit_log_records_entry() -> None:
    async with Application.boot(
        modules=[AuditModule.configure(store_backend="memory")]
    ) as app:
        audit = await app.container.resolve(AuditLoggerProtocol)
        store = await app.container.resolve(AuditStoreProtocol)

        await audit.log(
            AuditEntry(
                action="user.created",
                actor_id="actor-1",
                resource_type="user",
                resource_id="user-42",
            )
        )

        entries = await store.query(AuditQuery(action="user.created"))
        assert len(entries) == 1
        assert entries[0].actor_id == "actor-1"
```

## Key Source Files

| File | What it contains |
|------|----------------|
| `src/oridecon/audit/module.py` | `AuditModule.configure()`, `.stub()` |
| `src/oridecon/audit/config.py` | `AuditConfig`, `RetentionPolicyConfig` |
| `src/oridecon/audit/di/bundle_provider.py` | `AuditBundleProvider` boot and registration |
| `src/oridecon/audit/logging/logger.py` | `AuditLogger` (fire-tolerant entry point) |
| `src/oridecon/audit/store/memory.py` | `InMemoryAuditStore` |
| `src/oridecon/audit/store/sql.py` | `SqlAuditStore` |
| `src/oridecon/audit/verification/checksum.py` | HMAC-SHA256 checksum logic |
| `src/oridecon/audit/retention/policy.py` | `PolicyBasedRetention` |
| `src/oridecon/audit/admin/contributor.py` | `AuditAdminContributor` |