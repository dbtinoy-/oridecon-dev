---
title: "oridecon-cli CLI Matrix"
description: "Source-of-truth matrix documenting CLI entry points, commands, and lifecycle hooks across all Oridecon public packages."
---

# Public Package CLI Surface Matrix

Every public package in the Oridecon monorepo must have an explicit CLI
decision documented here.  The matrix is the source of truth for entry-point
expectations and is verified by boundary tests.

## Legend

| Column | Meaning |
|--------|---------|
| `entry_point` | exact `pyproject.toml` value or `none` |
| `root_commands` | root-level command names this package owns |
| `generators` | generator names this package owns |
| `health` | contributed health checks |
| `doctor` | contributed doctor checks |
| `shell` | contributed shell context |
| `hooks` | contributed CLI lifecycle hooks |
| `status` | `active` / `none` / `non-scope` |

## Matrix

### Packages WITH CLI Surface

| Package | Entry Point | Root Commands | Generators | Health | Doctor | Shell | Hooks | Status |
|---------|-------------|---------------|------------|--------|--------|-------|-------|--------|
| `oridecon-cli` (core) | `core = oridecon.cli.contributors.core:CoreCliContributor` | — | model, service, provider, event, test, command, query, guard | — | — | — | — | active |
| `oridecon-ai` | `ai = oridecon.ai.cli.contributor:AICliContributor` | ai | — | 2 (llm_provider, subsystem_discovery) | 1 (api_keys) | 1 (ai_client) | — | active |
| `oridecon-ai-mcp` | `mcp = oridecon.ai.mcp.cli.contributor:McpCliContributor` | mcp | mcp-controller, mcp-server | — | — | — | — | active |
| `oridecon-auth` | `auth = oridecon.auth.cli.contributor:AuthCliContributor` | auth | auth_guard, auth_policy | — | — | — | — | active |
| `oridecon-cache` | `cache = oridecon.cache.cli.contributor:CacheCliContributor` | cache | cache_repo | 1 | 1 | 1 | — | active |
| `oridecon-events` | `events = oridecon.events.cli.contributor:EventsCliContributor` | events | event_handler, saga | — | — | — | — | active |
| `oridecon-features` | `features = oridecon.features.cli.contributor:FeaturesCliContributor` | features | feature_flag | 1 | 1 | 1 | — | active |
| `oridecon-monitor` | `monitor = oridecon.monitor.cli.contributor:MonitorCliContributor` | monitor | metric | 2 | 2 | 1 | 1 | active |
| `oridecon-notification` | `notification = oridecon.notification.cli.contributor:NotificationCliContributor` | notify | notification_template | — | — | — | — | active |
| `oridecon-queue` | `queue = oridecon.queue.cli.contributor:QueueCliContributor` | — | message_consumer | — | — | — | — | active |
| `oridecon-search` | `search = oridecon.search.cli.contributor:SearchCliContributor` | — | search_index | — | — | — | — | active |
| `oridecon-sql` | `sql = oridecon.sql.cli.contributor:SqlCliContributor` | db | repository, filter, seeder, health | 1 | 2 | 2 | — | active |
| `oridecon-storage` | `storage = oridecon.storage.cli.contributor:StorageCliContributor` | — | storage_driver | 1 | 1 | — | — | active |
| `oridecon-tasks` | `tasks = oridecon.tasks.cli.contributor:TasksCliContributor` | tasks | task | — | — | — | — | active |
| `oridecon-tenancy` | `tenancy = oridecon.tenancy.cli.contributor:TenancyCliContributor` | tenancy | tenant_resolver | — | — | — | — | active |
| `oridecon-vector` | `vector = oridecon.vector.cli.contributor:VectorCliContributor` | vector | vector_collection | 1 | 1 | — | — | active |
| `oridecon-web` | `web = oridecon.web.cli.contributor:WebCliContributor` | — | controller, resource, middleware, graphql, webhook, websocket | — | 1 | — | — | active |
| `oridecon-workflow` | `workflow = oridecon.workflow.cli.contributor:WorkflowCliContributor` | workflow | workflow_def, pipeline, saga_step | 1 | — | 1 | — | active |
| `oridecon-audit` | `audit = oridecon.audit.cli.contributor:AuditCliContributor` | audit | — | 1 | 1 | — | — | active |
| `oridecon-graphql` | `graphql = oridecon.graphql.cli.contributor:GraphQLCliContributor` | — | dataloader | — | — | — | — | active |
| `oridecon-http` | `http = oridecon.http.cli.contributor:HttpCliContributor` | — | api_client | — | — | — | — | active |
| `oridecon-nosql` | `nosql = oridecon.nosql.cli.contributor:NoSqlCliContributor` | — | document_repo | — | — | — | — | active |
| `oridecon-resilience` | `resilience = oridecon.resilience.cli.contributor:ResilienceCliContributor` | — | — | 1 | 1 | 1 | — | active |

### Packages WITHOUT CLI Surface

| Package | Allowed Absence Reason | Status |
|---------|----------------------|--------|
| `oridecon` | Core framework runtime; CLI lives in `oridecon-cli`. No package-local CLI surface. | none |
| `oridecon-contracts` | Protocols, types, and exceptions only — no runtime CLI surface. | none |
| `oridecon-ai-llm` | CLI surface managed through `oridecon-ai` orchestrator. No standalone CLI. | none |
| `oridecon-ai-rag` | CLI surface managed through `oridecon-ai` orchestrator. No standalone CLI. | none |
| `oridecon-ai-agents` | CLI surface managed through `oridecon-ai` orchestrator. No standalone CLI. | none |
| `oridecon-ai-memory` | CLI surface managed through `oridecon-ai` orchestrator. No standalone CLI. | none |
| `oridecon-ai-skills` | CLI surface managed through `oridecon-ai` orchestrator. No standalone CLI. | none |
| `oridecon-ai-session` | CLI surface managed through `oridecon-ai` orchestrator. No standalone CLI. | none |
| `oridecon-ai-workers` | CLI surface managed through `oridecon-ai` orchestrator. No standalone CLI. | none |
| `oridecon-ai-observability` | CLI surface managed through `oridecon-ai` orchestrator. No standalone CLI. | none |
| `oridecon-ai-feedback` | CLI surface managed through `oridecon-ai` orchestrator. No standalone CLI. | none |
| `oridecon-secrets` | Secret management is runtime/API-only (backends, rotation, tenancy). No CLI surface. | none |
| `oridecon-graph` | No CLI surface yet. Graph DB operations are managed programmatically. | none |
| `oridecon-webhook` | No CLI surface yet. Webhook configuration is runtime-managed. | none |
| `oridecon-ui` | HTMX/htpy UI component library. No standalone CLI surface. | none |
| `oridecon-testing` | Pytest plugin and test utilities only. No CLI surface. | none |

## Conflict Policy

1. **Built-in commands** (registered in `experimental/apps/oridecon-cli/src/.../runtime/main.py`) always win.
2. **Scope-dist contributors** (public packages listed above with status `active`) win over non-scope contributors for same command name.
3. **First-registered wins** for scope-vs-scope conflicts (stable by entry-point discovery order).
4. All conflicts are recorded in `OrideconRuntime.command_conflicts` and inspectable via `oridecon contrib list`.

## Verification

This matrix is verified by:

- `tests/dev/test_cli_public_surface.py` — checks every public package has a documented CLI decision
- `experimental/apps/oridecon-cli/tests/unit/test_cli_contribution_system.py` — verifies contributor registration
- `tools/publish_public.sh` — package list must agree with this matrix
