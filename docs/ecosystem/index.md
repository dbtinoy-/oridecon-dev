---
title: The Ecosystem
description: Every open-source Oridecon package, grouped by what it does.
sidebar:
  order: 1
---

Oridecon is a monorepo of small, focused packages. The two foundation packages — `oridecon` and `oridecon-contracts` — are all you need to start. Everything else is an **extension**: install only what your application uses.

Every extension depends **only** on `oridecon` and `oridecon-contracts`, never on another extension. That boundary is what keeps the ecosystem composable — see [Architecture](/fundamentals/architecture/).

:::note[Maturity]
All packages are **alpha (0.1.x)** and MIT-licensed. Public APIs may change before 1.0.
:::

```bash
# Install the foundation plus only the extensions you need
pip install oridecon oridecon-web oridecon-sql oridecon-auth
```

---

## Foundation

| Package | What it does |
|---------|--------------|
| [`oridecon`](/packages/oridecon/) | Async-first DI container, `Application` lifecycle, modules, providers, config, and the `Result` type. |
| [`oridecon-contracts`](/packages/oridecon-contracts/) | Zero-dependency protocols, value types, and exceptions shared across every package. |

---

## Web & API

| Package | What it does |
|---------|--------------|
| [`oridecon-web`](/packages/oridecon-web/) | ASGI web layer — controllers, routing, middleware, OpenAPI docs, CORS, CSRF, rate limiting. `WebProvider`. |
| [`oridecon-graphql`](/packages/oridecon-graphql/) | GraphQL server (Strawberry) — schema, subscriptions, depth/complexity limits, persisted queries. |
| [`oridecon-http`](/packages/oridecon-http/) | Outbound HTTP client with resilience and observability built in. |

---

## Data & Persistence

| Package | What it does |
|---------|--------------|
| [`oridecon-sql`](/packages/oridecon-sql/) | Async SQL for Postgres / MySQL / SQLite — repositories, migrations, query building. `DatabaseProvider`. |
| [`oridecon-nosql`](/packages/oridecon-nosql/) | Document-store abstraction (MongoDB, DynamoDB, Firestore). |
| [`oridecon-cache`](/packages/oridecon-cache/) | Multi-backend caching — Redis, Memcached, in-memory — behind `CacheBackendProtocol`. |
| [`oridecon-storage`](/packages/oridecon-storage/) | Unified blob storage — S3, GCS, Azure Blob, R2, local filesystem. |
| [`oridecon-search`](/packages/oridecon-search/) | Full-text search — Elasticsearch, Meilisearch, Typesense, and SQL backends. |
| [`oridecon-vector`](/packages/oridecon-vector/) | Vector store backends (pgvector, Qdrant, Pinecone, in-memory) for embeddings. |
| [`oridecon-graph`](/packages/oridecon-graph/) | Graph database support (Neo4j, in-memory). |

---

## AI

| Package | What it does |
|---------|--------------|
| [`oridecon-ai`](/packages/oridecon-ai/) | Orchestration layer that discovers and wires the AI subsystems below. |
| [`oridecon-ai-llm`](/packages/oridecon-ai-llm/) | Multi-provider LLM client (OpenAI, Anthropic, Gemini, Ollama, Groq, Mistral, …) with routing and thinking suppression. |
| [`oridecon-ai-rag`](/packages/oridecon-ai-rag/) | Retrieval-augmented generation — chunking, retrieval, synthesis, citations. |
| [`oridecon-ai-agents`](/packages/oridecon-ai-agents/) | Agents with tools and strategies (ReAct, plan-and-execute). |
| [`oridecon-ai-memory`](/packages/oridecon-ai-memory/) | Episodic, semantic, and working memory for AI systems. |
| [`oridecon-ai-skills`](/packages/oridecon-ai-skills/) | Skill/tool registry, executor, and built-in tools. |
| [`oridecon-ai-session`](/packages/oridecon-ai-session/) | AI conversation sessions — branching, checkpointing, multi-agent. |
| [`oridecon-ai-mcp`](/packages/oridecon-ai-mcp/) | Model Context Protocol server and client for AI agents. |
| [`oridecon-ai-workers`](/packages/oridecon-ai-workers/) | Background AI work — batch embedding, document ingestion, maintenance. |
| [`oridecon-ai-feedback`](/packages/oridecon-ai-feedback/) | Collect, process, and store feedback on AI responses. |
| [`oridecon-ai-guard`](/packages/oridecon-ai-guard/) | Input/output guard pipeline — LLM safety and content filtering. |
| [`oridecon-ai-governance`](/packages/oridecon-ai-governance/) | AI governance — policy enforcement, audit trails, budget tracking. |
| [`oridecon-ai-evaluation`](/packages/oridecon-ai-evaluation/) | Evaluation framework — benchmarks and quality gates for AI outputs. |
| [`oridecon-ai-prompt`](/packages/oridecon-ai-prompt/) | Prompt management — templates, composition, optimization. |

---

## Messaging, Events & Workflow

| Package | What it does |
|---------|--------------|
| [`oridecon-events`](/packages/oridecon-events/) | Event sourcing and CQRS — domain events, aggregates, command/query buses, projections. |
| [`oridecon-queue`](/packages/oridecon-queue/) | Message bus / queue with named multi-backend support (Redis, RabbitMQ, Kafka, SQS, …). |
| [`oridecon-notification`](/packages/oridecon-notification/) | Email, SMS, and push delivery with multi-backend support. |
| [`oridecon-webhook`](/packages/oridecon-webhook/) | Webhook management — subscriptions, delivery tracking, HMAC verification, dead-letter queue. |
| [`oridecon-workflow`](/packages/oridecon-workflow/) | Workflow orchestration — pipelines, bulk ops, sagas, graph engine. |

---

## Background Work

| Package | What it does |
|---------|--------------|
| [`oridecon-tasks`](/packages/oridecon-tasks/) | Background tasks — scheduling, workers, and job queues over memory / Redis / AMQP / Postgres. |

---

## Observability & Reliability

| Package | What it does |
|---------|--------------|
| [`oridecon-monitor`](/packages/oridecon-monitor/) | Health checks, metrics, tracing, and structured logging (Prometheus / OpenTelemetry). |
| [`oridecon-resilience`](/packages/oridecon-resilience/) | Circuit breaker, retry, bulkhead, rate limiting, throttle, fallback. |
| [`oridecon-audit`](/packages/oridecon-audit/) | Append-only, HMAC-verified, retention-managed audit trail. |
| [`oridecon-ai-observability`](/packages/oridecon-ai-observability/) | Tracing, metrics, and health checks specific to AI calls. |

---

## Security & Multi-Tenancy

| Package | What it does |
|---------|--------------|
| [`oridecon-auth`](/packages/oridecon-auth/) | Authentication & authorization — JWT, OAuth2, RBAC, password hashing, web guards. |
| [`oridecon-tenancy`](/packages/oridecon-tenancy/) | Multi-tenant resolution, lifecycle, and isolation strategies. |
| [`oridecon-features`](/packages/oridecon-features/) | Feature-flag management with caching and pluggable providers. |

---

## Developer Tooling

| Package | What it does |
|---------|--------------|
| [`oridecon-cli`](/packages/oridecon-cli/) | `oridecon` command — project scaffolding (`new`), dev server (`run`/`dev`), migrations (`db`), inspection. |
| [`oridecon-testing`](/packages/oridecon-testing/) | Fakes, test clients/beds, fixed clock, and protocol compliance suites for fast, decoupled tests. |

---

## Choosing Packages

A typical web application starts with:

```bash
pip install oridecon oridecon-web oridecon-sql oridecon-auth oridecon-cache
```

Add capabilities as you need them — `oridecon-ai-llm` for an LLM feature, `oridecon-tasks` for background jobs, `oridecon-events` for an event-driven domain. Because every package targets a contract, you can adopt one without rewriting the rest of your app.

---

## Next Steps

- [Installation](/getting-started/installation/) — set up your environment
- [Architecture](/fundamentals/architecture/) — the boundary rules that hold the ecosystem together
- [Your First App](/getting-started/first-app/) — wire `oridecon-web` end to end
