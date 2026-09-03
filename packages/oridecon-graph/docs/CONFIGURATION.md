---
title: oridecon-graph Configuration
description: Every configuration key, its type, default, and environment variable.
---

Config section: `graph:`  
Env prefix: `ORI_GRAPH__`

## GraphConfig (Top Level)

| Key | Type | Default | Env Variable | Description |
|-----|------|---------|-------------|-------------|
| `enabled` | `bool` | `true` | `ORI_GRAPH__ENABLED` | Enable graph store subsystem |
| `backend` | `str` | `"memory"` | `ORI_GRAPH__BACKEND` | Graph backend (`memory` or `neo4j`) |
| `default_traversal_max_depth` | `int` | `10` | `ORI_GRAPH__DEFAULT_TRAVERSAL_MAX_DEPTH` | Default traversal max depth |
| `default_query_limit` | `int` | `100` | `ORI_GRAPH__DEFAULT_QUERY_LIMIT` | Default query result limit |
| `bulk_batch_size` | `int` | `1000` | `ORI_GRAPH__BULK_BATCH_SIZE` | Batch size for bulk operations |
| `max_retries` | `int` | `3` | `ORI_GRAPH__MAX_RETRIES` | Max retries for operations |
| `retry_delay` | `float` | `1.0` | `ORI_GRAPH__RETRY_DELAY` | Delay between retries (seconds) |
| `neo4j` | `Neo4jConfig` | defaults | `ORI_GRAPH__NEO4J__*` | Neo4j-specific settings |
| `memory` | `MemoryConfig` | defaults | `ORI_GRAPH__MEMORY__*` | In-memory specific settings |

## Neo4jConfig

| Key | Type | Default | Env Variable | Description |
|-----|------|---------|-------------|-------------|
| `uri` | `str` | `"bolt://localhost:7687"` | `ORI_GRAPH__NEO4J__URI` | Neo4j BOLT URI |
| `username` | `str` | `"neo4j"` | `ORI_GRAPH__NEO4J__USERNAME` | Neo4j username |
| `password` | `SecretStr` | `""` | `ORI_GRAPH__NEO4J__PASSWORD` | Neo4j password |
| `database` | `str` | `"neo4j"` | `ORI_GRAPH__NEO4J__DATABASE` | Target database name |
| `max_connection_pool_size` | `int` | `100` | `ORI_GRAPH__NEO4J__MAX_CONNECTION_POOL_SIZE` | Max connection pool size |
| `connection_timeout` | `float` | `30.0` | `ORI_GRAPH__NEO4J__CONNECTION_TIMEOUT` | Connection timeout (seconds) |
| `max_transaction_retry_time` | `float` | `30.0` | `ORI_GRAPH__NEO4J__MAX_TRANSACTION_RETRY_TIME` | Max transaction retry time |
| `fetch_size` | `int` | `100` | `ORI_GRAPH__NEO4J__FETCH_SIZE` | Default fetch size |
| `encrypted` | `bool` | `false` | `ORI_GRAPH__NEO4J__ENCRYPTED` | Use SSL/TLS encryption |
| `trust` | `str` | `"TRUST_SYSTEM_CA_SIGNED_CERTIFICATES"` | `ORI_GRAPH__NEO4J__TRUST` | Trust strategy for SSL |

## MemoryConfig

| Key | Type | Default | Env Variable | Description |
|-----|------|---------|-------------|-------------|
| `max_nodes` | `int` | `1000000` | `ORI_GRAPH__MEMORY__MAX_NODES` | Maximum nodes in memory |
| `max_edges` | `int` | `5000000` | `ORI_GRAPH__MEMORY__MAX_EDGES` | Maximum edges in memory |

---

## Minimal YAML Example (In-Memory)

```yaml
graph:
  backend: memory
```

## Production YAML Example (Neo4j)

```yaml
graph:
  backend: neo4j
  neo4j:
    uri: bolt://neo4j.example.com:7687
    username: neo4j
    password: ${NEO4J_PASSWORD}
    database: myapp
    max_connection_pool_size: 50
    encrypted: true
```

## Environment Variable Override

```bash
export ORI_GRAPH__BACKEND="neo4j"
export ORI_GRAPH__NEO4J__URI="bolt://neo4j-cluster:7687"
export ORI_GRAPH__NEO4J__PASSWORD="s3cret!"
export ORI_GRAPH__DEFAULT_TRAVERSAL_MAX_DEPTH=5
```
