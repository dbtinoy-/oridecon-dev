---
title: oridecon-tasks Quickstart
description: Install, define, and run background tasks in under 5 minutes.
---

:::note[Maturity]
`oridecon-tasks` is **alpha (0.1.x)** and MIT-licensed. Public APIs may change before 1.0.
:::

## Install

```bash
uv add oridecon-tasks
```

For Redis-backed queues:

```bash
uv add oridecon-tasks[redis]
```

For RabbitMQ-backed queues:

```bash
uv add oridecon-tasks[rabbitmq]
```

---

## Minimal Working Example

Define a task with the `@task` decorator and wire it through `TasksModule`:

```python
import asyncio
from oridecon import Application
from oridecon.contracts.infra.tasks import TaskQueueProtocol
from oridecon.tasks.module import TasksModule
from oridecon.tasks.decorators import task


@task(name="greet", max_retries=3)
async def greet(name: str) -> str:
    return f"Hello, {name}!"


async def main():
    async with Application.boot(
        name="my-app",
        modules=[TasksModule.configure(task_modules=[__name__])],
    ) as app:
        queue = await app.container.resolve(TaskQueueProtocol)
        job = await greet.apply_async(queue, "World")
        print(f"Enqueued: {job.id}")

        await asyncio.sleep(0.2)  # let the worker pick it up


asyncio.run(main())
```

> Use `task_modules=[...]` for exact modules or `task_packages=["app.tasks"]`
> to recursively import a package of task modules during provider boot.

---

## What Just Happened

| Step | What |
|------|------|
| `TasksModule.configure(task_modules=[__name__])` | Created a `DynamicModule`, imported the current module for task discovery, and started the worker pool |
| `Application.boot()` | Registered `TaskQueueProtocol` + `TaskExecutorProtocol` in the container, started the worker pool |
| `@task(name="greet")` | Wrapped `greet` with `.signature()`, `.s()`, `.apply_async()` methods |
| `greet.apply_async(queue, ...)` | Built a `JobProtocol` and enqueued it via `TaskQueueProtocol.enqueue()` |
| Worker | Polled the queue, dispatched the job to the registered handler via the `HandlerRegistry` |

---

## Next Steps

- [Guide](./GUIDE.md) — concepts, workflows, best practices
- [How-Tos](./HOWTOS.md) — task chaining, scheduling, Redis backends
- [Configuration](./CONFIGURATION.md) — all config keys and env vars
