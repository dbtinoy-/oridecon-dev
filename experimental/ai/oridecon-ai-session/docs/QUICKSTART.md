---
title: oridecon-ai-session Quickstart
description: Install, wire, and create your first AI session in under 5 minutes.
sidebar:
  order: 1
---

**oridecon-ai-session** provides stateful conversation session management — branching, checkpointing, multi-agent group sessions, and context pruning.

```bash
uv add oridecon-ai-session
```

## Minimal example

```python
import asyncio
from oridecon import Application, OrideconConfig
from oridecon.ai.session import SessionModule


async def main() -> None:
    config = OrideconConfig.from_yaml()
    app = Application(name="session-demo", config=config)
    app.add_module(SessionModule.configure())
    async with app.boot():
        from oridecon.contracts.ai.session import SessionManagerProtocol
        manager = await app.container.resolve(SessionManagerProtocol)
        state = await manager.create(user_id="user-42")
        print(f"Session {state.session_id} created ({state.status})")


asyncio.run(main())
```

## Wiring with a provider

```python
from oridecon import Application, OrideconConfig
from oridecon.ai.session import SessionProvider
from oridecon.ai.session import SessionConfig


async def main() -> None:
    config = OrideconConfig.from_yaml()
    app = Application(name="session-demo", config=config)
    app.add_provider(SessionProvider(config=SessionConfig(backend="in_memory")))
    async with app.boot():
        ...
```

## Next steps

- [Guide](/packages/oridecon-ai-session/guide/) — mental model, core concepts, common patterns
- [Architecture](/packages/oridecon-ai-session/architecture/) — internal design and extension points
- [Configuration](/packages/oridecon-ai-session/configuration/) — every config option
- [API Reference](/packages/oridecon-ai-session/api/) — generated API docs
