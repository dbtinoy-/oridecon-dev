---
title: oridecon-queue Quickstart
description: Install, configure, and publish your first message in 5 minutes.
sidebar:
  order: 1
---

## Install

```bash
uv add oridecon-queue
```

Optional extras for production backends:

```bash
# Redis
uv add "oridecon-queue[redis]"

# RabbitMQ
uv add "oridecon-queue[rabbitmq]"

# Kafka
uv add "oridecon-queue[kafka]"

# SQS
uv add "oridecon-queue[sqs]"
```

## Minimal Example

```python
import asyncio

from oridecon import Application
from oridecon.contracts.queue import BusMessage, QueueProtocol
from oridecon.di.module import module, Module
from oridecon.queue import QueueModule
from oridecon.queue.config import QueueConfig, NamedQueueConfig


# 1. Configure an in-memory queue
config = QueueConfig(backends=[
    NamedQueueConfig(name="default", driver="memory", primary=True),
])


# 2. Wire the module
@module(imports=[QueueModule.configure(config)])
class AppModule(Module):
    pass


async def main() -> None:
    async with Application.boot(name="app", modules=[AppModule]) as app:
        queue = await app.container.resolve(QueueProtocol)

        # Subscribe before publishing
        async def on_message(msg: BusMessage) -> None:
            print(f"Received: {msg.payload}")

        await queue.subscribe("greetings", on_message)

        # Publish
        msg = BusMessage(topic="greetings", payload="Hello, world!")
        await queue.publish("greetings", msg)

        await asyncio.sleep(0.1)  # let the handler run


asyncio.run(main())
```

:::note[What just happened?]
1. `QueueConfig` declared an in-memory backend named `"default"` marked as `primary`.
2. `QueueModule.configure()` created an IoC module that registered `QueueProtocol` in the container.
3. A `QueueProtocol` instance was resolved and wired with subscribe/publish.
:::

## What You Configured

- **Driver:** `"memory"` — no external broker needed.
- **Primary flag:** `primary=True` — this backend gets the unnamed `QueueProtocol` binding.
- **Named injection:** Use `Annotated[QueueProtocol, Named("default")]` to inject a specific backend.

## Next Steps

- [Guide](./GUIDE.md) — core concepts
- [How-Tos](./HOWTOS.md) — common recipes
- [Configuration](./CONFIGURATION.md) — all options
