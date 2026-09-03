# oridecon-graph

Graph database support for the Oridecon Framework (Neo4j, in-memory).

---

## Overview

`oridecon-graph` provides graph storage backends with DI wiring for in-memory and Neo4j implementations behind the graph contracts. It supports node and edge creation, graph traversal queries, Cypher compilation for Neo4j, and lazy graph creation.

---


> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon-graph
# With Neo4j support
uv add "oridecon-graph[neo4j]"
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module
from oridecon.graph import GraphConfig, GraphModule
from oridecon.contracts.data.graph import (
    GraphStoreProtocol,
    TraversalQuery,
    StartSpec,
    TraversalStep,
)


@module(imports=[GraphModule.configure(GraphConfig(backend="memory"))])
class AppModule(Module):
    pass


async def main() -> None:
    async with Application.boot(modules=[AppModule]) as app:
        store = await app.container.resolve(GraphStoreProtocol)
        graph = await store.get_graph()

        await graph.create_node(["Person"], {"name": "Alice"}, node_id="alice")
        await graph.create_node(["Person"], {"name": "Bob"}, node_id="bob")
        await graph.create_edge("alice", "bob", "KNOWS")

        paths = await graph.traverse(
            TraversalQuery(
                start=StartSpec(node_ids=("alice",)),
                steps=(TraversalStep(edge_types=("KNOWS",)),),
            )
        )
        assert paths


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## Configuration

> **Zero-config usage:** Call `GraphModule.configure()` with no arguments to use all defaults (in-memory backend).

### Option 1 — YAML file

```yaml
# application.yaml
graph:
  enabled: true
  backend: neo4j
  default_traversal_max_depth: 10
  neo4j:
    uri: bolt://localhost:7687
    password: "${NEO4J_PASSWORD}"
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_GRAPH__BACKEND=neo4j
export ORI_GRAPH__NEO4J__URI=bolt://localhost:7687
```

### Option 3 — Python

```python
from oridecon.graph import GraphConfig, GraphModule
from oridecon.graph.config import Neo4jConfig

GraphModule.configure(
    GraphConfig(
        backend="neo4j",
        neo4j=Neo4jConfig(
            uri="bolt://localhost:7687",
            password="${NEO4J_PASSWORD}",
        ),
    )
)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `enabled` | `true` | `ORI_GRAPH__ENABLED` | Enable or disable the graph subsystem |
| `backend` | `memory` | `ORI_GRAPH__BACKEND` | Graph backend to use (`memory` or `neo4j`) |
| `default_traversal_max_depth` | `10` | `ORI_GRAPH__DEFAULT_TRAVERSAL_MAX_DEPTH` | Maximum depth for graph traversals |
| `default_query_limit` | `100` | `ORI_GRAPH__DEFAULT_QUERY_LIMIT` | Default result limit for graph queries |
| `bulk_batch_size` | `1000` | `ORI_GRAPH__BULK_BATCH_SIZE` | Batch size for bulk insert and update operations |
| `max_retries` | `3` | `ORI_GRAPH__MAX_RETRIES` | Retry attempts on transient graph errors |
| `retry_delay` | `1.0` | `ORI_GRAPH__RETRY_DELAY` | Seconds between retry attempts |
| `neo4j.uri` | `bolt://localhost:7687` | `ORI_GRAPH__NEO4J__URI` | Neo4j Bolt connection URI |
| `neo4j.username` | `neo4j` | `ORI_GRAPH__NEO4J__USERNAME` | Neo4j authentication username |
| `neo4j.password` | — | `ORI_GRAPH__NEO4J__PASSWORD` | Neo4j authentication password (**required for production**) |
| `neo4j.database` | `neo4j` | `ORI_GRAPH__NEO4J__DATABASE` | Target Neo4j database name |
| `neo4j.max_connection_pool_size` | `100` | `ORI_GRAPH__NEO4J__MAX_CONNECTION_POOL_SIZE` | Maximum driver connection pool size |
| `memory.max_nodes` | `1000000` | `ORI_GRAPH__MEMORY__MAX_NODES` | Node capacity for the in-memory backend |
| `tenancy.enabled` | `False` | — | Enable per-tenant graph isolation |
| `tenancy.strategy` | `"node_property"` | — | `"node_property"` or `"graph_per_tenant"` |
| `tenancy.template` | `"{logical}_t_{tenant}"` | — | Template for resolving tenant-specific graph names |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `GraphModule.configure(config=None)` | Register `GraphProvider` with a config |
| `GraphModule.stub(config=None)` | Lightweight test module with in-memory backend |

## Key Features

- **In-memory backend** — no external service needed; for development and tests
- **Neo4j backend** — async Neo4j driver with Cypher query compilation
- **Graph traversal** — `TraversalQuery`, `StartSpec`, `TraversalStep` for graph walks
- **Named graphs** — lazy graph creation per name
- **Connection pooling** — configurable pool size for Neo4j driver

## Testing

```python
async with Application.boot(modules=[GraphModule.stub()]) as app:
    store = await app.container.resolve(GraphStoreProtocol)
    graph = await store.get_graph()
    # Test with in-memory backend
```

## Key Source Files

| File | What it contains |
|------|----------------|
| `src/oridecon/graph/module.py` | `GraphModule.configure()`, `.stub()` |
| `src/oridecon/graph/config.py` | `GraphConfig`, `GraphTenancyConfig`, `Neo4jConfig` |
| `src/oridecon/graph/di/provider.py` | `GraphProvider` boot and registration |
| `src/oridecon/graph/backends/memory/backend.py` | `InMemoryGraphStore` implementation |
| `src/oridecon/graph/backends/neo4j/backend.py` | `Neo4jGraphStore` implementation |
| `src/oridecon/graph/backends/neo4j/cypher.py` | `CypherCompiler` |
| `src/oridecon/graph/tenancy/` | Tenancy decorator and resolver (`decorator.py`, `resolver.py`); strategy enum lives in `oridecon.contracts.data.graph.tenancy` |

## Multi-Tenancy

`oridecon-graph` supports two isolation strategies:

### Strategies

| Strategy | `GraphTenancyStrategy` | How It Works |
|----------|----------------------|--------------|
| **Graph per tenant** | `GRAPH_PER_TENANT` | Graph names are resolved through a `TemplatedTenantCollectionResolver`, giving each tenant an isolated named graph |
| **Node property** | `NODE_PROPERTY` | Graph names pass through unchanged; every node/edge gets a `tenant_id` property, and `find_nodes` auto-injects a `tenant_id` filter |

### Configuration

```python
from oridecon.graph import GraphModule
from oridecon.graph.config import GraphConfig, GraphTenancyConfig

config = GraphConfig(
    backend="neo4j",
    tenancy=GraphTenancyConfig(
        enabled=True,
        strategy="node_property",
        template="{logical}_t_{tenant}",
    ),
)
GraphModule.configure(config)
```

### Components

| Component | Role |
|-----------|------|
| `GraphTenancyConfig` | Dataclass with `enabled`, `strategy`, and `template` |
| `TemplatedTenantCollectionResolver` | Resolves logical → physical graph names |
| `TenantGraphStoreDecorator` | Strategy-aware decorator: resolves names (GRAPH_PER_TENANT) or wraps returned graphs (NODE_PROPERTY) |
| `TenantPropertyFilterGraph` | Auto-injects `tenant_id` into create_node/create_edge properties and find_nodes filters |