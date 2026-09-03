# AUDIT_OVERVIEW.md — Oridecon Framework Package Overview

> **Source**: Package directories and `pyproject.toml` metadata.

---

## Summary

- Packages discovered: 54
- Packages with tests: 54

## Packages

| Package | Version | Tests | Description |
|---------|---------|-------|-------------|
| `oridecon` | 0.1.3009 | yes | Async-first DI/IoC framework for Python — core package |
| `oridecon-admin` | 0.1.3010 | yes | Modern Python-first admin framework for Oridecon - HTMX, CRUD, dashboards, and extensions |
| `oridecon-ai` | 0.1.3007 | yes | AI Layer for Oridecon Framework - Native LLM, Vector, RAG integration |
| `oridecon-ai-agents` | 0.1.3007 | yes | Agent system for Oridecon Framework - AI agents with tools, strategies, and execution |
| `oridecon-ai-evaluation` | 0.1.3007 | yes | AI Evaluation framework for the Oridecon Framework |
| `oridecon-ai-feedback` | 0.1.3007 | yes | AI feedback collection for the Oridecon Framework — collection, processing, and storage |
| `oridecon-ai-governance` | 0.1.3007 | yes | AI governance for the Oridecon Framework — policy enforcement, audit trails, budget tracking |
| `oridecon-ai-guard` | 0.1.3007 | yes | AI input/output guard pipeline for the Oridecon Framework — LLM safety and content filtering |
| `oridecon-ai-llm` | 0.1.3007 | yes | LLM client layer for the Oridecon Framework — OpenAI, Anthropic, Ollama, Cohere, Groq, Mistral |
| `oridecon-ai-mcp` | 0.1.3008 | yes | MCP Server for Oridecon Framework - Model Context Protocol server for AI agents |
| `oridecon-ai-memory` | 0.1.3007 | yes | AI memory system for the Oridecon Framework — episodic, semantic, and working memory |
| `oridecon-ai-observability` | 0.1.3007 | yes | AI observability for the Oridecon Framework — tracing, metrics, and monitoring |
| `oridecon-ai-prompt` | 0.1.3007 | yes | AI prompt management for the Oridecon Framework — templates, composition, optimization |
| `oridecon-ai-rag` | 0.1.3007 | yes | Retrieval-Augmented Generation (RAG) pipeline for the Oridecon Framework |
| `oridecon-ai-relay` | 0.1.3007 | yes | Protocol-neutral conversion engine for the Oridecon AI relay — OpenAI Chat, Responses, Claude, and Gemini |
| `oridecon-ai-relay-gateway` | 0.1.3007 | yes | Protocol-facing relay gateway for the Oridecon AI relay — channel selection, orchestration, upstream I/O, and SSE handling |
| `oridecon-ai-session` | 0.1.3007 | yes | AI session management for the Oridecon Framework — branching, checkpointing, multi-agent sessions |
| `oridecon-ai-skills` | 0.1.3007 | yes | AI skills and tools for the Oridecon Framework — registry, executor, builtin tools, discovery |
| `oridecon-ai-workers` | 0.1.3007 | yes | AI background workers for the Oridecon Framework — batch embedding, document ingestion, DLQ, maintenance |
| `oridecon-audit` | 0.1.3007 | yes | Unified audit trail for the Oridecon Framework — append-only, HMAC-verified, retention-managed |
| `oridecon-auth` | 0.1.3007 | yes | Authentication and authorization for Oridecon Framework - JWT, OAuth2, SAML, LDAP, RBAC, and multi-tenancy |
| `oridecon-cache` | 0.1.3007 | yes | Multi-backend caching system for Oridecon Framework - Redis, Memcached, and in-memory caching |
| `oridecon-cli` | 0.1.3007 | yes | Command-line interface for Oridecon Framework - Project scaffolding, code generation, and development tools |
| `oridecon-contracts` | 0.1.3007 | yes | Core types and protocols for the Oridecon Framework |
| `oridecon-events` | 0.1.3007 | yes | Event Sourcing and CQRS engine for Oridecon Framework - Domain events, aggregates, and projections |
| `oridecon-features` | 0.1.3007 | yes | Feature flag management for the Oridecon Framework |
| `oridecon-graph` | 0.1.3007 | yes | Graph database support for the Oridecon Framework (Neo4j, in-memory) |
| `oridecon-graphql` | 0.1.3007 | yes | GraphQL support for Oridecon Framework - Strawberry, Apollo Federation, and subscriptions |
| `oridecon-http` | 0.1.3007 | yes | Outbound HTTP client for the Oridecon Framework |
| `oridecon-monitor` | 0.1.3007 | yes | Monitoring and observability for Oridecon Framework - Health checks, metrics, and system monitoring |
| `oridecon-multimedia` | 0.1.3007 | yes | Audio/video/image generation orchestrator for the Oridecon Framework |
| `oridecon-multimedia-beat` | 0.1.3007 | yes | Audio tempo/beat analysis for the Oridecon Framework — librosa and madmom backends |
| `oridecon-multimedia-image` | 0.1.3007 | yes | Image generation for the Oridecon Framework — local and API-based backends |
| `oridecon-multimedia-interpolate` | 0.1.3007 | yes | Video frame-rate interpolation for the Oridecon Framework — RIFE backend |
| `oridecon-multimedia-music` | 0.1.3007 | yes | Music generation for the Oridecon Framework — local and API-based backends |
| `oridecon-multimedia-tts` | 0.1.3007 | yes | Text-to-speech generation for the Oridecon Framework — local and API-based backends |
| `oridecon-multimedia-upscale` | 0.1.3007 | yes | Image and video super-resolution for the Oridecon Framework — Real-ESRGAN and HAT backends |
| `oridecon-multimedia-video` | 0.1.3007 | yes | Video generation for the Oridecon Framework — local and API-based backends |
| `oridecon-nosql` | 0.1.3007 | yes | NoSQL document store support for the Oridecon Framework (MongoDB, DynamoDB, Firestore) |
| `oridecon-notification` | 0.1.3007 | yes | SMS, push, and email notification delivery with Named DI multi-backend support for the Oridecon Framework |
| `oridecon-queue` | 0.1.3007 | yes | Message bus and queue with Named DI multi-backend support for the Oridecon Framework |
| `oridecon-resilience` | 0.1.3007 | yes | Resilience patterns for the Oridecon Framework (circuit breaker, retry, bulkhead, rate limiting, throttle, fallback) |
| `oridecon-search` | 0.1.3007 | yes | Full-text search and indexing for Oridecon Framework - Elasticsearch, Meilisearch, and Algolia |
| `oridecon-secrets` | 0.1.3007 | yes | Secret vaults with rotation, tenant scoping, and audit for Oridecon Framework |
| `oridecon-sql` | 0.1.3007 | yes | SQL database abstractions for Oridecon Framework — Postgres, MySQL, SQLite with migrations, repositories, and query building |
| `oridecon-storage` | 0.1.3007 | yes | Unified blob storage abstraction for Oridecon Framework - S3, GCS, Azure Blob, and local filesystem |
| `oridecon-tasks` | 0.1.3007 | yes | Background task processing for Oridecon Framework - Scheduling, workers, and job queues |
| `oridecon-tenancy` | 0.1.3007 | yes | Multi-tenant resolution, lifecycle, and isolation for the Oridecon Framework |
| `oridecon-testing` | 0.1.3007 | yes | Centralized testing infrastructure for Oridecon Framework - Fixtures, factories, and utilities |
| `oridecon-ui` | 0.1.3009 | yes | HTMX/htpy component library for Oridecon web applications |
| `oridecon-vector` | 0.1.3007 | yes | Vector store backends for the Oridecon Framework |
| `oridecon-web` | 0.1.3007 | yes | Web layer for Oridecon Framework - ASGI, routing, middleware, and API tooling |
| `oridecon-webhook` | 0.1.3007 | yes | Webhook management for the Oridecon Framework — subscription CRUD, delivery tracking, HMAC verification, and dead-letter queue |
| `oridecon-workflow` | 0.1.3007 | yes | Workflow orchestration for the Oridecon Framework (pipelines, bulk ops, sagas, graph engine) |

