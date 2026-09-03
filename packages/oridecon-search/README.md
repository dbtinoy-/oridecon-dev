# oridecon-search

Full-text search and indexing for Oridecon Framework — Elasticsearch, Meilisearch, Typesense, and OpenSearch

---

## Overview

oridecon-search provides a unified `SearchEngineProtocol` interface over Meilisearch, Elasticsearch, OpenSearch, Typesense, PostgreSQL full-text, MySQL, MongoDB, and SQLite. It supports typo-tolerant search, faceting, fuzzy matching, result caching, and analytics. All services are wired via `SearchProvider`, which registers the search engine protocol with the DI container.

---


> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon-search
# Optional extras
uv add "oridecon-search[meilisearch]"     # Meilisearch
uv add "oridecon-search[elasticsearch]"   # Elasticsearch 8.x
uv add "oridecon-search[typesense]"       # Typesense
uv add "oridecon-search[postgres,mysql,sqlite,mongodb]"  # Database backends
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module

# Import the module from the package
from oridecon.search import SearchModule


@module(imports=[SearchModule.configure(...)])
class AppModule(Module):
    pass


async with Application.boot(modules=[AppModule]) as app:
    # use app.container to resolve services
    ...
```

## Configuration

> **Default config:** Pass `SearchConfig()` explicitly to use all defaults (in-memory backend). `SearchModule.configure()` with **no arguments raises `ValueError`** — a config or engine must be specified. The in-memory `NullBackend` is fine for development and tests.

### Option 1 — YAML file

```yaml
# application.yaml
search:
  backend_type: meilisearch
  meilisearch:
    url: http://localhost:7700
    api_key: "${MEILI_API_KEY}"
  query:
    strategy: fuzzy
    default_limit: 10
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_SEARCH__ENABLED=true
# Environment variables for each field
```

### Option 3 — Python

```python
from oridecon.search.config import SearchConfig, BackendType
from oridecon.search import SearchModule

config = SearchConfig(backend_type=BackendType.MEILISEARCH, ...)
SearchModule.configure(config)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `backend_type` | `memory` | `ORI_SEARCH__BACKEND_TYPE` | Active backend (`meilisearch`, `elasticsearch`, `opensearch`, `typesense`, `postgres`, `mysql`, `sqlite`, `mongodb`, `memory`) |
| `timeout` | `30.0` | `ORI_SEARCH__TIMEOUT` | Default request timeout in seconds |
| `query.strategy` | `fuzzy` | `ORI_SEARCH__QUERY__STRATEGY` | Query strategy (`fuzzy`, `exact`, `semantic`, `hybrid`) |
| `query.default_limit` | `20` | `ORI_SEARCH__QUERY__DEFAULT_LIMIT` | Default number of results returned |
| `query.max_limit` | `100` | `ORI_SEARCH__QUERY__MAX_LIMIT` | Maximum allowed result limit |
| `query.fuzzy_threshold` | `0.8` | `ORI_SEARCH__QUERY__FUZZY_THRESHOLD` | Fuzzy match threshold (0–1; 1 = exact) |
| `meilisearch.url` | `http://localhost:7700` | `ORI_SEARCH__MEILISEARCH__URL` | MeiliSearch server URL |
| `meilisearch.api_key` | `null` | `ORI_SEARCH__MEILISEARCH__API_KEY` | MeiliSearch authentication key |
| `elasticsearch.hosts` | `[http://localhost:9200]` | `ORI_SEARCH__ELASTICSEARCH__HOSTS` | Elasticsearch cluster hosts |
| `operations.bulk_chunk_size` | `500` | `ORI_SEARCH__OPERATIONS__BULK_CHUNK_SIZE` | Documents per bulk index request |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `SearchModule.configure(config, enable_facets)` | Configure with explicit SearchConfig |
| `SearchModule.stub()` | Minimal config for testing |

## Key Features

- **Protocol abstraction** — Swap backends without changing application code
- **Meilisearch** — Typo-tolerant, instant search with faceting
- **Elasticsearch** — Full Lucene query DSL; aggregations; multi-index
- **Typesense** — Fast, schema-enforced search with scoped API keys
- **PostgreSQL FTS** — `tsvector`/`tsquery` via `oridecon-sql`; no extra infra
- **MySQL FTS** — `FULLTEXT` index support for MySQL / MariaDB
- **MongoDB Text** — Native `$text` operator with language stemming
- **SQLite FTS5** — Local development with zero dependencies
- **Cached search** — Transparent result caching via `CacheBackend`
- **Analytics** — Query recording and hit-rate analytics for ranking improvement

## Testing

```python
async with Application.boot(modules=[SearchModule.stub()]) as app:
    # your test code
    ...
```

## Key Source Files

| File | What it contains |
|------|----------------|
| `src/oridecon/search/module.py` | `SearchModule` class with factory methods |
| `src/oridecon/search/di/provider.py` | `SearchProvider` — wires search protocols into DI container |
| `src/oridecon/search/config.py` | `SearchConfig` and sub-config classes |
| `src/oridecon/search/engine/` | Search engine abstraction and federation |
| `src/oridecon/search/backends/` | Search engine implementations for each backend |
| `src/oridecon/search/indexing/` | Index management and document indexing |