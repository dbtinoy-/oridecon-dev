# Configuration

Configuration options for `oridecon-admin`.

## Overview

Configuration is loaded through `AdminConfig`, passed to `AdminModule.configure()`.
It can also be set via environment variables (recommended for production) or a YAML
file.

## Basic Example

```python
from oridecon.admin.config import AdminConfig

config = AdminConfig(
    prefix="/admin",
    title="My App Admin",
    features=AdminFeaturesConfig(audit_logging=True),
)
module = AdminModule.configure(config)
```

## AdminConfig Reference

| Field | Type | Default | Env var | Description |
|-------|------|---------|---------|-------------|
| `prefix` | `str` | `/admin` | `ORI_ADMIN__PREFIX` | URL prefix for all admin routes |
| `title` | `str` | `Oridecon Admin` | `ORI_ADMIN__TITLE` | Panel title shown in browser and header |
| `contributor_collision_mode` | `Literal["warn", "error"]` | `"warn"` | `ORI_ADMIN__CONTRIBUTOR_COLLISION_MODE` | How to handle name collisions between contributors |
| `features.audit_logging` | `bool` | `True` | `ORI_ADMIN__FEATURES__AUDIT_LOGGING` | Log every write action with user and diff |
| `features.enabled` | `bool` | `True` | `ORI_ADMIN__FEATURES__ENABLED` | Master toggle for all admin features |
| `auth.session_secret` | `str` | `change-me-in-production` | `ORI_ADMIN__AUTH__SESSION_SECRET` | Secret for signing session cookies (required in production) |
| `auth.session_lifetime` | `int` | `86400` | `ORI_ADMIN__AUTH__SESSION_LIFETIME` | Session validity in seconds |
| `auth.idle_timeout` | `int` | `3600` | `ORI_ADMIN__AUTH__IDLE_TIMEOUT` | Idle session expiry in seconds |
| `resource_defaults.per_page` | `int` | `20` | `ORI_ADMIN__RESOURCE_DEFAULTS__PER_PAGE` | Default rows per page |
| `resource_defaults.default_sort` | `str \| None` | `None` | — | Default sort field for all resources |
| `ui.theme` | `str` | `system` | `ORI_ADMIN__UI__THEME` | UI colour scheme (`light`, `dark`, or `system`) |
| `tenancy.enabled` | `bool` | `False` | `ORI_ADMIN__TENANCY__ENABLED` | Enable multi-tenant resource scoping |
| `audit.read_audit_enabled` | `bool` | `False` | `ORI_ADMIN__AUDIT__READ_AUDIT_ENABLED` | Log GET requests for compliance (off by default) |

## Environment Variables

| Variable | Description |
|---------|-------------|
| `ORI_ADMIN__ENABLED` | Master toggle (`true`/`false`) |
| `ORI_ADMIN__PREFIX` | Admin URL prefix |
| `ORI_ADMIN__TITLE` | Panel title |
| `ORI_ADMIN__CONTRIBUTOR_COLLISION_MODE` | `warn` or `error` |
| `ORI_ADMIN__AUTH__SESSION_SECRET` | Session signing secret |
| `ORI_ADMIN__AUTH__SESSION_LIFETIME` | Session TTL in seconds |
| `ORI_ADMIN__AUTH__IDLE_TIMEOUT` | Idle timeout in seconds |
| `ORI_ADMIN__FEATURES__AUDIT_LOGGING` | Enable/disable audit logging |
| `ORI_ADMIN__RESOURCE_DEFAULTS__PER_PAGE` | Default rows per page |
| `ORI_ADMIN__UI__THEME` | `light`, `dark`, or `system` |
| `ORI_ADMIN__TENANCY__ENABLED` | Enable tenancy |
| `ORI_ADMIN__AUDIT__READ_AUDIT_ENABLED` | Enable read-operation audit logging |

## Best Practices

- Keep config minimal — use sensible defaults.
- Use environment variables for secrets (never hardcode `session_secret`).
- Set `contributor_collision_mode` to `"error"` in CI to catch naming conflicts.
- Use `AdminModule.stub()` for test configurations instead of `AdminModule.configure()`.
