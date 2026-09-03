# oridecon-nosql

NoSQL document store support for the Oridecon Framework (MongoDB, DynamoDB, Firestore).

---

## Overview

`oridecon-nosql` provides async document-store backends behind a clean protocol interface. It ships with a MongoDB driver (Motor-based), a fluent query builder, aggregation pipelines, the repository pattern with specifications, a migration manager, and Named DI multi-backend support. The MongoDB driver is registered through the container; DynamoDB and Firestore backends are available as direct-use classes (`oridecon.nosql.backends.dynamodb`, `oridecon.nosql.backends.firestore`).

---


> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon oridecon-nosql

# With MongoDB support
uv add "oridecon-nosql[mongodb]"
# With DynamoDB support
uv add "oridecon-nosql[dynamodb]"
# With Firestore support
uv add "oridecon-nosql[firestore]"
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module
from oridecon.nosql import NoSQLModule
from oridecon.nosql.config import MongoDBConfig, NoSQLConfig
from oridecon.contracts.data.nosql.nosql import DocumentStoreProtocol


@module(
    imports=[
        NoSQLModule.configure(
            NoSQLConfig(
                driver="mongodb",
                mongodb=MongoDBConfig(
                    uri="mongodb://localhost:27017",
                    database="myapp",
                ),
            )
        )
    ]
)
class AppModule(Module):
    pass


async def main() -> None:
    async with Application.boot(modules=[AppModule]) as app:
        store = await app.container.resolve(DocumentStoreProtocol)
        collection = store.collection("users")

        await collection.insert_one({"name": "Alice", "age": 30})
        async for user in collection.find({"age": {"$gte": 25}}):
            print(user)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## Configuration

> **Zero-config usage:** Call `NoSQLModule.configure()` with no arguments to use all defaults.

### Option 1 — YAML file

```yaml
# application.yaml
nosql:
  driver: "mongodb"
  mongodb:
    uri: "mongodb://localhost:27017"
    database: "myapp"
    max_pool_size: 100
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_NOSQL__DRIVER=mongodb
export ORI_NOSQL__MONGODB__URI=mongodb://localhost:27017
export ORI_NOSQL__MONGODB__DATABASE=myapp
```

### Option 3 — Python

```python
from oridecon.nosql import NoSQLModule
from oridecon.nosql.config import NoSQLConfig, MongoDBConfig

NoSQLModule.configure(
    NoSQLConfig(
        driver="mongodb",
        mongodb=MongoDBConfig(uri="mongodb://localhost:27017", database="myapp"),
    )
)
```

### Config reference

**NoSQLConfig**

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `enabled` | `true` | `ORI_NOSQL__ENABLED` | Enable NoSQL support |
| `driver` | `"mongodb"` | `ORI_NOSQL__DRIVER` | NoSQL driver (`"mongodb"`; only MongoDB is module-wired today — DynamoDB/Firestore backends are direct-use classes) |
| `mongodb` | `MongoDBConfig()` | — | MongoDB-specific connection configuration |
| `backends` | `[]` | — | Named backend entries for multi-backend DI registration |

**MongoDBConfig**

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `uri` | `"mongodb://localhost:27017"` | `ORI_NOSQL__MONGODB__URI` | MongoDB connection URI |
| `database` | `"oridecon"` | `ORI_NOSQL__MONGODB__DATABASE` | Database name |
| `max_pool_size` | `100` | `ORI_NOSQL__MONGODB__MAX_POOL_SIZE` | Maximum connection pool size |
| `min_pool_size` | `10` | `ORI_NOSQL__MONGODB__MIN_POOL_SIZE` | Minimum connection pool size |
| `retry_writes` | `true` | `ORI_NOSQL__MONGODB__RETRY_WRITES` | Enable write retries |
| `retry_reads` | `true` | `ORI_NOSQL__MONGODB__RETRY_READS` | Enable read retries |
| `read_preference` | `"primaryPreferred"` | `ORI_NOSQL__MONGODB__READ_PREFERENCE` | Read preference mode |
| `write_concern_w` | `"majority"` | `ORI_NOSQL__MONGODB__WRITE_CONCERN_W` | Write concern level |
| `auth_source` | `"admin"` | `ORI_NOSQL__MONGODB__AUTH_SOURCE` | Authentication database |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `NoSQLModule.configure(config)` | Configure with explicit config |
| `NoSQLModule.scope(*repositories)` | Scope repository classes into a feature module |
| `NoSQLModule.stub()` | Minimal config for testing |

## Key Features

- **MongoDB backend** — async Motor-based with connection pooling and retry logic
- **Query builder** — type-safe fluent API for MongoDB queries and projections
- **Aggregation pipelines** — composable pipeline stages for complex aggregations
- **Repositories** — base `DocumentRepository` pattern with specification support
- **Migration manager** — index creation, field operations, and collection management
- **Named DI multi-backend** — multiple backends registered via `Annotated[DocumentStoreProtocol, Named("analytics")]`
- **Session and transaction context managers** — `mongodb_session()` and `mongodb_transaction()` (`oridecon.nosql.backends.mongodb.session`) for ACID operations

## Testing

`oridecon-nosql` ships no in-memory backend — `stub()` uses the MongoDB driver, so boot requires a reachable MongoDB. Point it at a test instance:

```python
from oridecon.nosql.config import MongoDBConfig, NoSQLConfig

config = NoSQLConfig(
    driver="mongodb",
    mongodb=MongoDBConfig(uri="mongodb://localhost:27017", database="testdb"),
)

async with Application.boot(modules=[NoSQLModule.stub(config)]) as app:
    store = await app.container.resolve(DocumentStoreProtocol)
    collection = store.collection("users")
    await collection.insert_one({"name": "Alice"})  # requires a live test MongoDB
```

## Key Source Files

| File | What it contains |
|------|----------------|
| `src/oridecon/nosql/module.py` | `NoSQLModule.configure()`, `.scope()`, `.stub()` |
| `src/oridecon/nosql/config.py` | `NoSQLConfig`, `MongoDBConfig`, `NamedNoSQLConfig` |
| `src/oridecon/nosql/di/provider.py` | `NoSQLProvider` boot and registration |
| `src/oridecon/nosql/backends/mongodb/backend.py` | `MongoDBDocumentStore` implementation |
| `src/oridecon/nosql/query/builder.py` | `DocumentQueryBuilder` |
| `src/oridecon/nosql/query/pipeline.py` | `AggregationPipeline` |
| `src/oridecon/nosql/repository/base.py` | `DocumentRepository` base class |
| `src/oridecon/nosql/migration/manager.py` | `MigrationManager` |