---
title: oridecon-cache Quickstart
description: Install and configure multi-backend caching for your Oridecon application
---

:::note[What you'll learn]
- Install `oridecon-cache` with `uv`
- Wire the cache with `CacheModule` or `CacheProvider`
- Get, set, and delete cache entries with TTL
:::

## Install

```bash
uv add oridecon-cache
```

:::tip
For Redis backend support, add the optional dependency:

```bash
uv add oridecon-cache[redis]
```

For Memcached: `uv add oridecon-cache[memcached]`. For semantic caching with FAISS: `uv add oridecon-cache[semantic]`.
:::

## Minimal Setup — CacheModule

```python
import asyncio
from oridecon import Application
from oridecon.cache import CacheModule

async def main():
    async with Application.boot(
        name="my-app",
        modules=[CacheModule.configure()],
    ) as app:
        from oridecon.cache import CacheService

        cache = await app.container.resolve(CacheService)
        await cache.set("greeting", "Hello, Oridecon!")
        value = await cache.get("greeting")
        print(value)  # "Hello, Oridecon!"

asyncio.run(main())
```

## Using CacheProvider Directly

```python
from oridecon import Application
from oridecon.cache import CacheProvider


def create_app() -> Application:
    app = Application(name="my-app")
    app.add_provider(CacheProvider())
    return app
```

## Testing with CacheModule.stub()

```python
from oridecon.cache import CacheModule

# In-memory backend with no external connections
test_module = CacheModule.stub()
```

## Next Steps

- [Guide](./GUIDE.md) — caching concepts and workflows
- [How-Tos](./HOWTOS.md) — Redis, Memcached, stampede protection recipes
- [Configuration](./CONFIGURATION.md) — all configuration keys
