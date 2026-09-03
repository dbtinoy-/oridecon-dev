# oridecon-contracts

Core types and protocols for the Oridecon Framework.

---

## Overview

`oridecon-contracts` defines all Protocols, base types, Result types, domain
models, and exception hierarchies used across the Oridecon ecosystem. It has
**zero runtime dependencies** so it can be imported into any package — including
thin integrations — without pulling in the full framework.

This package is the single source of truth for every interface in Oridecon.
All other packages depend on contracts; no implementation package defines its
own protocol that another package depends on.


> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon-contracts
```

## Quick Start

### Result type

```python
from oridecon.result import Result, Ok, Err


async def find_user(user_id: str) -> Result[User, UserNotFound]:
    user = await db.get(user_id)
    if not user:
        return Err(UserNotFound(user_id))
    return Ok(user)


# Safe consumption
result = await find_user("u-123")
name = result.match(ok=lambda u: u.name, err=lambda e: "unknown")
```

### Domain models

```python
from oridecon.domain.models import Entity, ValueObject
from oridecon.domain import AggregateRoot
from oridecon.contracts.domain.events import DomainEvent


class UserCreated(DomainEvent):
    user_id: str
    email: str


class User(AggregateRoot):
    email: str
```

### Protocols

```python
from oridecon.contracts.infra.cache import CacheBackendProtocol
from oridecon.contracts.data import DatabaseProviderProtocol
from oridecon.contracts.security.secrets import SecretStoreProtocol
```

## Key Modules

| Module | What it contains |
|--------|-----------------|
| `oridecon.result` | `Result[T, E]`, `Ok`, `Err`, `as_result()`, `as_result_sync()`, `try_catch()`, `ResultPipeline` |
| `oridecon.domain.models` | `DomainModel`, `Entity`, `ValueObject` (concrete domain models, in core `oridecon`) |
| `oridecon.domain` | `AggregateRoot` (re-exported from `oridecon.domain.models.aggregate`) |
| `oridecon.contracts.domain.base` | `DomainModelProtocol`, `ID` |
| `oridecon.contracts.domain.events` | `DomainEvent` |
| `oridecon.contracts.infra.cache` | `CacheBackendProtocol` |
| `oridecon.contracts.data` | `DatabaseProviderProtocol` |
| `oridecon.contracts.security.secrets` | `SecretStoreProtocol` |
| `oridecon.contracts.core.di` | `ContainerRegistrarProtocol`, `ContainerResolverProtocol` |
| `oridecon.contracts.core.provider` | `ProviderProtocol`, `ProviderPriority` |
| `oridecon.contracts.core.registry` | `RegistryProtocol`, `StrategyRegistryProtocol`, `BackendRegistryProtocol` |
| `oridecon.contracts.exceptions` | `OrideconError`, full error hierarchy |

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/contracts/__init__.py` | Lazy-loading re-exports of all public types |
| `src/oridecon/result/` | Result type and Ok/Err helpers |
| `src/oridecon/contracts/domain/` | `DomainModelProtocol`, `DomainEvent` |
| `src/oridecon/contracts/core/` | Container, Provider, Registry protocols |
| `src/oridecon/contracts/exceptions/` | OrideconError and domain error hierarchies |

## Design Principles

- **Zero dependencies** — no third-party runtime imports
- **Protocol-only** — defines interfaces, never implementations
- **Stable contract** — all other Oridecon packages depend on this one; breaking changes are versioned
