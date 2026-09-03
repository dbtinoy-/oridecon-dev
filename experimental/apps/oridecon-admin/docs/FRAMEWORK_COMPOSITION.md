# Framework Composition Map

## Three-Ring Architecture

```
  ┌────────────────────────────────────────────────────┐
  │ Ring 3 — App / Plugin code                         │
  │  - declares Resources, custom RowActions,          │
  │    PageDefinitions, widgets, settings panels       │
  │  - registers via BaseAdminContributor              │
  └────────────────────────────────────────────────────┘
              ↑ depends only on contracts
  ┌────────────────────────────────────────────────────┐
  │ Ring 2 — oridecon-admin                            │
  │  - Resource/Action/Page/Form/Table orchestration   │
  │  - DashboardAssembler, NavigationAssembler         │
  │  - AdminRenderer, AdminRouter, AdminBuilder        │
  │  - resource-scoped RBAC (field/action/record)      │
  │  - admin-specific UX (filter bar, command palette) │
  └────────────────────────────────────────────────────┘
              ↑ consumes
  ┌────────────────────────────────────────────────────┐
  │ Ring 1 — Framework packages (existing)             │
  │  oridecon-contracts ← all admin-facing protocols   │
  │  oridecon (core), oridecon-ui, oridecon-web        │
  │  oridecon-auth (identity, sessions, OAuth)         │
  │  oridecon-tenancy (tenant resolution, isolation)   │
  │  oridecon-monitor (metrics, health, observability) │
  │  oridecon-events (command/query/event buses)       │
  │  oridecon-cache, oridecon-tasks, oridecon-search,  │
  │  oridecon-resilience (OPTIONAL light-up)           │
  └────────────────────────────────────────────────────┘
```

Admin orchestrates; it does not implement identity, tenancy, or metrics.

## Required Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `oridecon` | ≥0.2 | DI container, `Provider`, `Module`, `Result` |
| `oridecon-contracts` | ≥0.2 | All admin-facing protocols, `BaseAdminContributor` |
| `oridecon-ui` | ≥0.2 | UI components: atoms, molecules, organisms |
| `oridecon-web` | ≥0.2 | ASGI / Starlette integration, `AdminRouter` |
| `oridecon-sql` | ≥0.2 | Database provider, data source protocol |
| `oridecon-events` | ≥0.2 | CQRS buses, domain events |

## Optional Integrations

| Integration | Package | Declarative knob | What it gives you |
|---|---|---|---|
| **Cache** | `oridecon-cache` | `Resource.cacheable = True` | `list()` results cached with TTL; invalidation on create/update/delete |
| **Tasks** | `oridecon-tasks` | `BulkAction.task_runner = "tasks"` | Bulk actions dispatched as background tasks; progress visible in admin UI |
| **Search** | `oridecon-search` | `Resource.searchable = True` | Resources indexed on create/update/delete; `?q=` uses framework search engine |
| **Resilience** | `oridecon-resilience` | `DataSource.resilient = True` | Data-source calls wrapped in retry + circuit-breaker |
| **Features** | `oridecon-features` | `AdminBuilder.feature(name)` | Feature-flag gating for admin sections |
| **Storage** | `oridecon-storage` | `FileField.storage = "s3"` | File uploads routed through framework storage backend |
| **Auth** | `oridecon-auth` | *(automatic when installed)* | Identity, sessions, JWT, OAuth delegated to framework |
| **Tenancy** | `oridecon-tenancy` | `AdminConfig.tenancy.enabled = True` | Multi-tenant resource scoping delegated to framework |
| **Monitor** | `oridecon-monitor` | *(automatic when installed)* | Metrics, health checks, structured logging delegated to framework |

## What Admin Does NOT Do For You

- **Identity, sessions, OAuth, JWT** — delegated to `oridecon-auth`. Admin keeps only resource-scoped RBAC (field/action/record-level permissions).
- **Tenant resolution and isolation** — delegated to `oridecon-tenancy`. Admin keeps only tenant-scoped resource query wrappers.
- **Metrics, health checks, tracing** — delegated to `oridecon-monitor`. Admin keeps only the dashboard health rollup widgets.
- **CQRS buses** — delegated to `oridecon-events`. Admin defines only the message marker classes.
