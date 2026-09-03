---
title: "oridecon-contracts Guide"
description: "Comprehensive guide to oridecon-contracts — the zero-dependency protocol layer at the base of the Oridecon ecosystem."
---

## Requirements

| Package | Required | Purpose |
|---------|----------|---------|
| _None_ | — | Zero-dependency protocol package |

# Guide

---

## Overview
`oridecon-contracts` is the **zero-dependency protocol layer** at the base of the Oridecon ecosystem. It defines the interfaces — protocols, shared value types, base exceptions, and cross-package enums — that every Oridecon package depends on.

### The Problem

Without a shared contract layer, extension packages would import from each other directly, creating a tangled dependency graph:

```
oridecon-web ──► oridecon-sql  ← cross-import = coupling
```

### The Solution

Every protocol that two or more packages need lives **here**, not in any extension. Packages depend on contracts, never on each other:

```
oridecon-web ──► oridecon-contracts ◄── oridecon-sql
```

### Mental Model

Think of this package as the **vocabulary** of the framework. It defines the words (`CacheBackendProtocol`, `Result`, `LLMClientProtocol`) that every package uses to communicate. The implementations live elsewhere — here we only define *what* something does, not *how*.

```
┌───────────────────────────────────────────────────────────┐
│                 oridecon-contracts                        │
│                                                           │
│  Core: ContainerRegistrarProtocol, Result, Provider       │
│  Data: DatabaseProviderProtocol, RepositoryProtocol       │
│  AI:   LLMClientProtocol, EmbeddingClientProtocol         │
│  Cache: CacheBackendProtocol                              │
│  Events: EventBusProtocol, CommandBusProtocol             │
│  Auth: TokenManagerProtocol, PasswordHasherProtocol       │
│  ...                                                      │
│                                                           │
│  Exceptions: OrideconError, DomainError,                  │
│              ContainerError, AIError, ...                 │
│                                                           │
│  Value Types: ChatMessage, HealthCheckResult,             │
│               DomainEvent, TokenUsage, ...                │
└───────────────────────────────────────────────────────────┘
```

---

## Core Concepts

### Protocols

Protocols are defined as `typing.Protocol` classes with `@runtime_checkable`. They define service boundaries but contain **no implementation code**.

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class CacheBackendProtocol(Protocol):
    """Interface for cache backends."""

    async def get(self, key: str) -> bytes | None:
        """Retrieve a value. Returns None if not found."""
        ...

    async def set(self, key: str, value: bytes, ttl: int) -> None:
        """Store a value with a TTL in seconds."""
        ...
```

All protocols live in `oridecon.contracts.*`, organized by **domain** (not by package name):

| Domain | File | Key Protocols |
|--------|------|---------------|
| Core | `core/di.py` | `ContainerRegistrarProtocol`, `ContainerResolverProtocol`, `BootContainerProtocol` |
| Data | `data/__init__.py` | `DatabaseProviderProtocol`, `RepositoryProtocol`, `UnitOfWorkProtocol` |
| Cache | `infra/cache.py` | `CacheBackendProtocol`, `CacheProviderProtocol` |
| AI/LLM | `ai/llm.py` | `LLMClientProtocol`, `EmbeddingClientProtocol`, `TokenCounterProtocol` |
| AI/Agents | `ai/__init__.py` | `AgentProtocol`, `ToolProtocol`, `ToolRegistryProtocol` |
| Auth | `auth/__init__.py` | `TokenManagerProtocol`, `PasswordHasherProtocol`, `AuthorizerProtocol` |
| Events | `events/__init__.py` | `EventBusProtocol`, `CommandBusProtocol`, `EventHandlerProtocol` |
| Workflow | `workflow/__init__.py` | `SagaProtocol`, `SagaManagerProtocol` |

### Shared Value Types

Value types are dataclasses, frozen dataclasses, and enums that appear in protocol method signatures. They always live in contracts if used across packages.

```python
from dataclasses import dataclass
from enum import Enum


class Role(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


@dataclass(frozen=True)
class ChatMessage:
    role: Role
    content: str
    name: str | None = None


@dataclass(frozen=True)
class HealthCheckResult:
    component: str
    status: HealthStatus
    message: str | None = None
```

### Exception Hierarchy

Base exceptions in contracts, leaf exceptions in extension packages:

```
OrideconError (contracts)
├── DomainError
├── ContainerError
├── ProviderError
├── AIError (contracts)
│   ├── LLMError      ← leaf exceptions in oridecon-ai-llm
│   ├── RAGError      ← leaf exceptions in oridecon-ai-rag
│   └── ...
├── AgentError
└── ...
```

### Enums

Cross-package enums use `class X(str, Enum)`:

| Enum | Location | Used By |
|------|----------|---------|
| `ProviderPriority` | `core/provider.py` | Every package's provider |
| `ServiceScope` | `core/scopes.py` | Container registration |
| `HealthStatus` | `core/health.py` | Health checks everywhere |
| `Environment` | `core/config.py` | Config system |
| `CircuitState` | `resilience/enums.py` | Circuit breaker |

---

## Typical Usage

```python
from __future__ import annotations

from typing import Protocol

from oridecon.contracts.core.di import ContainerRegistrarProtocol
from oridecon.contracts.infra.cache import CacheBackendProtocol
from oridecon.contracts.data import DatabaseProviderProtocol


class UserRepositoryProtocol(Protocol):
    async def find(self, user_id: str) -> dict | None: ...
```

---

## Common Patterns

### Pattern 1: Protocol-Based Service Injection

```python
from __future__ import annotations

from oridecon.contracts.infra.cache import CacheBackendProtocol
from oridecon.contracts.data import DatabaseProviderProtocol


class UserService:
    def __init__(
        self,
        db: DatabaseProviderProtocol,
        cache: CacheBackendProtocol | None = None,
    ) -> None:
        self.db = db
        self.cache = cache
```

### Pattern 2: Using Result<T, E>

```python
from __future__ import annotations

from oridecon.contracts.core.result import Result, Ok, Err
from oridecon.contracts.exceptions.domain import NotFoundError


async def find(self, user_id: str) -> Result[dict, NotFoundError]:
    user = await self.repo.get(user_id)
    if not user:
        return Err(NotFoundError(f"User {user_id} not found"))
    return Ok(user)
```

### Pattern 3: Creating a Cross-Package Exception

Extension packages extend contracts base exceptions:

```python
# oridecon-ai-llm/exceptions.py
from oridecon.contracts.ai.exceptions import LLMError

class LLMRateLimitError(LLMError):
    """Raised when the LLM provider rate-limits the request."""


class LLMModelNotFoundError(LLMError):
    """Raised when the requested model is unavailable."""
```

---

## Best Practices

- **Protocols define what, not how** — no implementation code in contracts
- **One definition per name** — never redefine a protocol, type, or exception from contracts
- **Domain organization** — protocols organized by domain (`ai/`, `data/`, `cache/`), not by package name
- **Separate types from protocols** — `protocols.py` for interfaces, `types.py` for dataclasses, `errors.py` for exceptions
- **Use `@runtime_checkable`** for all protocols to enable `isinstance()` checks
- **Frozen dataclasses** for value types that cross package boundaries
- **`str, Enum`** for all enums — never bare string constants

---

## Next Steps

- [Architecture](./ARCHITECTURE.md) — domain organization, protocol placement rules
- [How-Tos](./HOWTOS.md) — define a protocol, create shared types, add exceptions
- [Troubleshooting](./TROUBLESHOOTING.md) — common mistakes
