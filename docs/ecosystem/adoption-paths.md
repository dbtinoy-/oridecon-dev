---
title: "Adoption Paths"
description: "Staged adoption guide — start small, add capabilities as you grow."
---

Oridecon is designed for incremental adoption. You don't need to install everything at once — start with the core and add packages as your application grows.

## Tier 1 — Starter (1-3 packages)

The minimal foundation: dependency injection, application structure, and a Result type.

- **`oridecon`** + **`oridecon-contracts`** — Core: DI container, Application abstraction, Configuration, structured logging, Result type
- **Add `oridecon-web`** → Build an HTTP API with routing, middleware, request validation, and error handling
- Configuration via YAML files, structured logging built in

:::tip
This tier is enough to build a complete API server. At this stage you have no database, no caching, and no auth — perfect for prototypes and early-stage services.
:::

## Tier 2 — Standard (4-8 packages)

Add persistence, caching, authentication, and developer tooling.

- **Add `oridecon-sql`** → Database persistence with migrations, repositories, and query building
- **Add `oridecon-cache`** → Response caching, session store, rate limiter backing
- **Add `oridecon-auth`** → JWT authentication, RBAC, route guards, password hashing
- **Add `oridecon-cli`** → Development server, database migrations, code scaffolding
- **Add `oridecon-testing`** → Fakes, test beds, and compliance test suites

:::note
This tier is the sweet spot for most production applications. You have persistence, caching, auth, and testing — everything needed for a standard web application or API service.
:::

## Tier 3 — Advanced (8-15 packages)

Search, file storage, background jobs, event-driven architecture, notifications, and multi-tenancy.

- **Add `oridecon-search`** → Full-text search with Meilisearch, Elasticsearch, or Typesense
- **Add `oridecon-storage`** → File uploads, CDN integration, presigned URLs
- **Add `oridecon-tasks`** → Background job processing, cron scheduling, task queues
- **Add `oridecon-events`** → Event-driven architecture, CQRS, domain events
- **Add `oridecon-notification`** → Email, SMS, and push notification delivery
- **Add `oridecon-webhook`** → Outbound webhook dispatch with retry and signing
- **Add `oridecon-monitor`** + **`oridecon-resilience`** → Health checks, metrics, circuit breakers, retry policies
- **Add `oridecon-tenancy`** → Multi-tenant SaaS support with data isolation

:::tip
The event bus (`oridecon-events`) and task queue (`oridecon-tasks`) both integrate with `oridecon-resilience` for fault tolerance. See [Compatibility & Dependencies](/ecosystem/compatibility/) for these cross-package wiring notes.
:::

## Tier 4 — AI-Powered (15+ packages)

Add LLM integration, RAG, agents, memory, and production AI infrastructure.

- **Add `oridecon-ai-llm`** → LLM integration with provider routing (OpenAI, Anthropic, Google, local)
- **Add `oridecon-ai-rag`** + **`oridecon-vector`** → RAG pipeline with document ingestion, chunking, embedding, and hybrid search
- **Add `oridecon-ai-agents`** + **`oridecon-ai-skills`** → AI agents with tool use, multi-step reasoning, and sub-agent delegation
- **Add `oridecon-ai-memory`** + **`oridecon-ai-session`** → Persistent conversation history, episodic and semantic memory
- **Add `oridecon-ai-mcp`** → MCP server and client — expose agents as MCP tools, connect to external MCP servers
- **Add `oridecon-ai-workers`** + **`oridecon-ai-observability`** + **`oridecon-ai-feedback`** → Background processing, token usage tracking, cost attribution, feedback collection

:::tip
You don't have to commit to a tier all at once. Each package is independently installable and adopts incrementally. Mix and match — use `oridecon-ai-llm` without RAG, or `oridecon-vector` without the AI packages.
:::

## Decision Flow

```
Starting a new project?
├── Prototype or microservice → **Tier 1**
├── Standard web app or API → **Tier 2**
├── Scaling app with advanced needs → **Tier 3**
└── Building AI features → **Tier 2 first**, then **Tier 4**
```

Each tier is a superset of the one before it. You can move between tiers as your requirements evolve — no rewrite needed.

---

See [Choosing Backends](/ecosystem/choosing-backends/) to pick the right infrastructure for each package, and [Compatibility & Dependencies](/ecosystem/compatibility/) for version requirements and known constraints.
