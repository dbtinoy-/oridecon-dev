---
title: oridecon-resilience Quickstart
description: Get started with oridecon-resilience — circuit breakers, retries, bulkheads, and more
sidebar:
  order: 1
---

Install, wire, and use resilience patterns in under 5 minutes.

## Install

```bash
uv add oridecon-resilience
```

## Minimal Wiring

```python
import asyncio
from oridecon import Application
from oridecon.resilience import ResilienceProvider
from oridecon.resilience.config import ResilienceConfig

config = ResilienceConfig()
provider = ResilienceProvider()

async def main() -> None:
    async with Application.boot(
        name="demo",
        providers=[provider],
        config=config,
    ) as app:
        print("Resilience provider ready")

asyncio.run(main())
```

## Use a Decorator

```python
from oridecon.resilience import retry, RetryConfig
from oridecon.resilience import circuit_breaker, CircuitBreakerRegistry

cfg = RetryConfig(max_attempts=3, base_delay=1.0)
registry = CircuitBreakerRegistry()

@retry(cfg)
async def fetch_data(url: str) -> dict:
    ...

@circuit_breaker("api", registry)
async def call_external() -> dict:
    ...
```

## Use the Pipeline

```python
from oridecon.resilience import ResiliencePipeline
from oridecon.contracts.infra.resilience import RetryConfig, CircuitBreakerConfig

pipeline = ResiliencePipeline(
    retry_config=RetryConfig(max_attempts=3),
    circuit_config=CircuitBreakerConfig(failure_threshold=5),
)
result = await pipeline.execute(my_function, arg1, arg2)
```

## Next Steps

- [Guide](./GUIDE.md) — concepts and mental model
- [Configuration](./CONFIGURATION.md) — all config fields
- [How-Tos](./HOWTOS.md) — common recipes
