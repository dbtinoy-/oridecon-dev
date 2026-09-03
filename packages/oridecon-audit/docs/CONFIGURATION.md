---
title: oridecon-audit Configuration
description: All config fields for oridecon-audit
sidebar:
  order: 4
---

The config section is `"audit"`. Environment variable prefix is `ORI_AUDIT__`.

## AuditConfig

```yaml
audit:
  store_backend: "sql"
  table_name: "audit_log"
  hmac_key: null
  retention_policy:
    name: "default"
    default_retention_days: 365
    severity_overrides:
      critical: 2555
      high: 1095
  verification_schedule: "0 * * * *"
  verification_batch_size: 100
  enable_admin: true
```

### Fields

| Key | Type | Default | Env Var | Description |
|-----|------|---------|---------|-------------|
| `store_backend` | `str` | `"sql"` | `ORI_AUDIT__STORE_BACKEND` | Backend type — `"sql"` or `"memory"` |
| `table_name` | `str` | `"audit_log"` | `ORI_AUDIT__TABLE_NAME` | SQL table name for the unified audit store |
| `hmac_key` | `bytes | None` | `None` | `ORI_AUDIT__HMAC_KEY` | HMAC key for checksum computation |
| `retention_policy` | `RetentionPolicy` | (see below) | — | Retention rules |
| `verification_schedule` | `str` | `"0 * * * *"` | `ORI_AUDIT__VERIFICATION_SCHEDULE` | Cron expression for scheduled verification |
| `verification_batch_size` | `int` | `100` | `ORI_AUDIT__VERIFICATION_BATCH_SIZE` | Entries to verify per run |
| `enable_admin` | `bool` | `True` | `ORI_AUDIT__ENABLE_ADMIN` | Register the admin panel contributor |

### RetentionPolicy sub-fields

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `name` | `str` | `"default"` | Policy identifier |
| `default_retention_days` | `int` | `365` | Default retention in days (0 = indefinite) |
| `severity_overrides` | `dict[str, int]` | `{"critical": 2555, "high": 1095}` | Per-severity retention days |
| `source_overrides` | `dict[str, int]` | `{}` | Per-source retention days |

## Example: application.yaml

```yaml
audit:
  store_backend: "sql"
  table_name: "audit_log"
  hmac_key: "c2VjdXJlLWhtYWMta2V5"
  retention_policy:
    name: "compliance"
    default_retention_days: 365
    severity_overrides:
      critical: 2555
      high: 1095
      medium: 730
  verification_schedule: "0 2 * * *"
  enable_admin: true
```

## Env var override form

```bash
export ORI_AUDIT__STORE_BACKEND=sql
export ORI_AUDIT__HMAC_KEY=c2VjdXJlLWhtYWMta2V5
export ORI_AUDIT__VERIFICATION_SCHEDULE="0 */6 * * *"
```

## Configuration via AuditModule

Use `AuditModule.configure()` for a Python-native approach without YAML:

```python
from oridecon.audit import AuditModule

app.add_module(AuditModule.configure(
    hmac_key=b"my-key",
    store_backend="sql",
    retention_days=730,
    enable_admin=True,
))
```
