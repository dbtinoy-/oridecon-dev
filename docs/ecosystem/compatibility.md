---
title: "Compatibility & Dependencies"
description: "Inter-package dependency rules, version notes, and known constraints."
---

## The Golden Rule

Every extension package depends only on `oridecon` and `oridecon-contracts`. No extension ever depends on another extension.

This rule keeps the dependency graph acyclic and ensures packages can be adopted independently. The core (`oridecon`) provides the DI container, Application abstraction, configuration, and logging. `oridecon-contracts` defines interface protocols that extensions implement.

## Documented Exceptions

A small number of cross-extension dependencies exist where the functionality is inherently coupled:

| Extension | Depends On | Reason |
|-----------|------------|--------|
| `oridecon-web` | `oridecon-ui` | Shared UI primitives for web responses |
| `oridecon-admin` | `oridecon-ui`, `oridecon-auth`, `oridecon-cache`, `oridecon-features`, `oridecon-resilience` | Admin dashboard functionality |
| `oridecon-events` | `oridecon-resilience` | Event buses use retry and circuit breaker |
| `oridecon-tasks` | `oridecon-resilience` | Background jobs need retry and timeout policies |
| `oridecon-ai` | `oridecon-ai-llm`, `oridecon-ai-rag`, `oridecon-ai-feedback`, `oridecon-ai-observability`, `oridecon-vector` | The orchestrator discovers and wires AI sub-packages via entry points |
| `oridecon-testing` | any extension (optional) | Cross-package test utilities |

:::note
These exceptions are explicitly managed and documented. Adding a new cross-extension dependency requires a design review to ensure it doesn't create circular or tangled imports.

**AI sub-packages** (`oridecon-ai-llm`, `oridecon-ai-rag`, `oridecon-ai-agents`, …) each depend **only** on `oridecon` and `oridecon-contracts` — they never import each other. Cross-AI-package communication goes through protocols resolved via the container.
:::

## Python & Runtime

- **Python version**: 3.11+ required
- **ASGI servers**: Fully compatible with **uvicorn**, **granian**, and **hypercorn**
- **Package manager**: Works with pip, uv, and poetry

## Known Constraints

### Oridecon SQL

Requires an async database driver. Connection strings must use the async variant:

| Database | Driver | Connection String |
|----------|--------|-------------------|
| PostgreSQL | `asyncpg` | `postgresql+asyncpg://user:pass@host/db` |
| MySQL | `aiomysql` | `mysql+aiomysql://user:pass@host/db` |
| SQLite | `aiosqlite` | `sqlite+aiosqlite:///path/to/db` |

### Oridecon NoSQL — Wire Status

| Backend | Status |
|---------|--------|
| MongoDB | **Wired** — provider is active and configurable |
| DynamoDB | Code exists but **not wired** — provider class written, not registered |
| Firestore | Code exists but **not wired** — provider class written, not registered |

### Oridecon Queue — Wire Status

| Backend | Status |
|---------|--------|
| Memory / Redis / RabbitMQ / Kafka / SQS | **Wired** — fully configurable |
| Azure Service Bus / GCP Pub/Sub | Code exists but **not wired** — provider classes written, not registered |

### Oridecon Graph

| Backend | Status |
|---------|--------|
| Neo4j | **Wired** — production-ready |
| In-memory | **Wired** — suitable for dev and testing |

## Optional Extras

Install backend-specific dependencies via extras:

| Package | Extras |
|---------|--------|
| `oridecon-sql` | `[postgres]`, `[mysql]`, `[sqlite]` |
| `oridecon-cache` | `[redis]`, `[memcached]`, `[semantic]` |
| `oridecon-queue` | `[redis]`, `[rabbitmq]`, `[kafka]`, `[sqs]`, `[azure]`, `[gcp]` |
| `oridecon-search` | `[elasticsearch]`, `[meilisearch]`, `[algolia]` |
| `oridecon-storage` | `[aws]`, `[gcp]`, `[azure]` |
| `oridecon-vector` | `[pgvector]`, `[qdrant]`, `[pinecone]`, `[chroma]`, `[weaviate]` |
| `oridecon-ai-llm` | `[openai]`, `[anthropic]`, `[ollama]`, `[groq]`, `[mistral]`, `[cohere]`, `[huggingface]` |

## Maturity

All packages are **alpha** (0.1.x). Breaking changes may occur before the 1.0 release. We follow [SemVer](https://semver.org/) — breaking changes increment the minor version while below 1.0.

---

See [Adoption Paths](/ecosystem/adoption-paths/) for a staged guide to integrating Oridecon packages.
