---
title: oridecon-vector Quickstart
description: Install, configure, and run your first vector store in under 5 minutes.
sidebar:
  order: 1
---

```bash
uv add oridecon-vector
```

Install the backend driver for your vector store:

```bash
uv add "oridecon-vector[pgvector]"    # PostgreSQL + pgvector
uv add "oridecon-vector[qdrant]"      # Qdrant
uv add "oridecon-vector[pinecone]"    # Pinecone
uv add "oridecon-vector[chroma]"      # ChromaDB
uv add "oridecon-vector[weaviate]"    # Weaviate
uv add "oridecon-vector[all]"         # Every backend
```

---

## Minimal Example

```python
import asyncio
from oridecon import Application
from oridecon.vector import VectorModule


async def main() -> None:
    async with Application.boot(
        name="vector-demo",
        modules=[VectorModule.configure()],
    ) as app:
        store = await app.container.resolve(VectorStoreProtocol)
        await store.create_collection(
            CollectionConfig(name="my_docs", dimension=1536)
        )
        print("Collection ready!")


asyncio.run(main())
```

---

## What Just Happened

1. `VectorModule.configure()` created a `VectorProvider` with default config (in-memory backend).
2. The provider registered `VectorStoreProtocol` and `VectorCollectionProtocol` in the container.
3. An in-memory `MemoryVectorStore` was created and connected during `boot()`.
4. `store.create_collection()` created a vector collection capable of storing 1536-dimensional embeddings.

---

## Next Steps

- [Guide](./GUIDE.md) — mental model, core concepts, common patterns
- [Configuration](./CONFIGURATION.md) — all config keys and env vars
- [How-Tos](./HOWTOS.md) — copy-pasteable recipes
