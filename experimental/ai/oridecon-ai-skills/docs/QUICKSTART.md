---
title: oridecon-ai-skills Quickstart
description: Install, wire, and run your first skill in under 5 minutes.
sidebar:
  order: 1
---

**oridecon-ai-skills** provides a composable skill/tool registry, executor, built-in tools, and discovery for the Oridecon AI subsystem.

```bash
uv add oridecon-ai-skills
```

## Minimal example

```python
import asyncio
from oridecon import Application, OrideconConfig
from oridecon.ai.skills import SkillsModule


async def main() -> None:
    config = OrideconConfig.from_yaml()
    app = Application(name="skills-demo", config=config)
    app.add_module(SkillsModule.configure())
    async with app.boot():
        from oridecon.contracts.ai.skills import SkillExecutorProtocol
        executor = await app.container.resolve(SkillExecutorProtocol)
        result = await executor.execute("current_datetime", {})
        if result.is_ok():
            print(result.unwrap().output)
        else:
            print("Error:", result.unwrap_err())


asyncio.run(main())
```

## Wiring with a provider

```python
from oridecon import Application, OrideconConfig
from oridecon.ai.skills import SkillsProvider
from oridecon.ai.skills import SkillsConfig


async def main() -> None:
    config = OrideconConfig.from_yaml()
    app = Application(name="skills-demo", config=config)
    app.add_provider(SkillsProvider(config=SkillsConfig(enable_builtin=True)))
    async with app.boot():
        ...

```

## Next steps

- [Guide](/packages/oridecon-ai-skills/guide/) — mental model, core concepts, common patterns
- [Architecture](/packages/oridecon-ai-skills/architecture/) — internal design and extension points
- [Configuration](/packages/oridecon-ai-skills/configuration/) — every config option
- [API Reference](/packages/oridecon-ai-skills/api/) — generated API docs
