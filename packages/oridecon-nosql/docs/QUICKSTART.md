---
title: oridecon-nosql Quickstart
description: Get up and running with NoSQL document stores in minutes.
---

:::tip[Package]
`oridecon-nosql` — Document-store abstraction (MongoDB, DynamoDB, Firestore) for the Oridecon Framework.
:::

## Install

```bash
uv add oridecon-nosql
```

Add an optional backend extra for your driver:

```bash
uv add "oridecon-nosql[mongodb]"       # motor
uv add "oridecon-nosql[dynamodb]"      # aioboto3
uv add "oridecon-nosql[firestore]"     # google-cloud-firestore
```

---

## Minimal Example

```python
import asyncio
from oridecon import Application
from oridecon.contracts.data.nosql import DocumentStoreProtocol
from oridecon.nosql import NoSQLModule, NoSQLConfig


async def main() -> None:
    async with Application.boot(
        name="nosql-demo",
        modules=[
            NoSQLModule.configure(
                NoSQLConfig(driver="mongodb")
            ),
        ],
    ) as app:
        store = await app.container.resolve(DocumentStoreProtocol)
        collection = store.collection("users")
        result = await collection.insert_one(
            {"name": "Alice", "email": "alice@example.com"}
        )
        print(f"Inserted: {result.document_id}")


asyncio.run(main())
```

:::note
Replace `"mongodb"` with `"firestore"` or configure a `backends` list for multi-store setups. DynamoDB requires explicit table configuration through `DynamoDBConfig`.
:::

---

## How It Works

1. **`NoSQLModule.configure()`** creates a `NoSQLProvider` with the given config.
2. The provider registers a `DocumentStoreProtocol` singleton in the container.
3. On boot, the provider connects to the document store.
4. Services receive the store via constructor injection.

## Next Steps

- [Guide](./GUIDE.md) — mental model, core concepts, common patterns
- [How-Tos](./HOWTOS.md) — task-oriented recipes
- [Configuration](./CONFIGURATION.md) — every config key with env-var names
