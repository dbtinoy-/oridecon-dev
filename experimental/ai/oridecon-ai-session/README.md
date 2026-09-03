# oridecon-ai-session

AI session management for the Oridecon Framework — branching, checkpointing, multi-agent sessions

---

## Overview

Stateful conversation session management for the Oridecon AI framework. Provides full session lifecycle (create → turn → checkpoint → restore → close), pluggable persistence backends, timeline branching, and multi-agent group sessions. Zero-config usage starts with sensible defaults.


> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon-ai-session
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module

from oridecon.ai.session import SessionModule
from oridecon.ai.session.config import SessionConfig


@module(
    imports=[
        SessionModule.configure(
            SessionConfig(backend="in_memory"),
            enable_cleanup_scheduler=True,
        )
    ]
)
class AppModule(Module):
    pass


async with Application.boot(modules=[AppModule]) as app:
    # use app.container to resolve services
    ...
```

## Configuration

> **Zero-config usage:** Call `SessionModule.configure()` with no arguments to use defaults.

### Option 1 — YAML file

```yaml
# application.yaml
ai_session:
  backend: "cache"
  session_ttl: 86400
  max_turns_per_session: 1000
  auto_checkpoint_interval: 10
  consolidate_on_close: true
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_AI_SESSION__BACKEND=cache
# Environment variables for each field
```

### Option 3 — Python

```python
from oridecon.ai.session.config import SessionConfig
from oridecon.ai.session import SessionModule

config = SessionConfig(
    backend="cache",
    session_ttl=86400,
    max_turns_per_session=1000,
    auto_checkpoint_interval=10,
)
SessionModule.configure(config)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `enabled` | `True` | `ORI_AI_SESSION__ENABLED` | Enable the AI session subsystem |
| `backend` | `"in_memory"` | `ORI_AI_SESSION__BACKEND` | Persistence backend: `in_memory`, `cache`, `database` |
| `session_ttl` | `86400` | `ORI_AI_SESSION__SESSION_TTL` | Session max age in seconds (`0` = no expiry) |
| `cleanup_interval_s` | `600` | `ORI_AI_SESSION__CLEANUP_INTERVAL_S` | How often expired sessions are swept |
| `max_turns_per_session` | `1000` | `ORI_AI_SESSION__MAX_TURNS_PER_SESSION` | Hard turn cap before session is closed |
| `max_sessions_per_user` | `100` | `ORI_AI_SESSION__MAX_SESSIONS_PER_USER` | Concurrent session limit per user |
| `auto_checkpoint_interval` | `10` | `ORI_AI_SESSION__AUTO_CHECKPOINT_INTERVAL` | Checkpoint every N turns |
| `max_checkpoints_per_session` | `50` | `ORI_AI_SESSION__MAX_CHECKPOINTS_PER_SESSION` | Retained checkpoints per session |
| `max_branches_per_session` | `10` | `ORI_AI_SESSION__MAX_BRANCHES_PER_SESSION` | Max forked branches per session |
| `max_agents_per_group` | `10` | `ORI_AI_SESSION__MAX_AGENTS_PER_GROUP` | Max agents in a group session |
| `default_turn_strategy` | `"round_robin"` | `ORI_AI_SESSION__DEFAULT_TURN_STRATEGY` | Multi-agent turn strategy |
| `consolidate_on_close` | `True` | `ORI_AI_SESSION__CONSOLIDATE_ON_CLOSE` | Trigger memory consolidation on close |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `SessionModule.configure(config, enable_cleanup_scheduler)` | Configure with explicit config |
| `SessionModule.stub(config)` | Minimal config for testing |

## Key Features

- **Session lifecycle**: Create, turn, checkpoint, restore, suspend, close with FSM-enforced status transitions
- **Timeline branching**: `BranchManager` forks sessions into independent timelines that can be merged
- **Multi-agent groups**: `GroupSession` coordinates multiple agents with configurable turn-taking strategies
- **Persistence backends**: In-memory, Redis (cache), and database stores
- **Web middleware**: `SessionMiddleware` resolves session ID from cookie or HTTP header
- **Analytics**: Session analytics with turn counts, token totals, and cost tracking

## Testing

```python
async with Application.boot(modules=[SessionModule.stub()]) as app:
    # your test code
    ...
```

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/ai/session/module.py` | `SessionModule.configure()`, `.stub()` |
| `src/oridecon/ai/session/config.py` | `SessionConfig` |
| `src/oridecon/ai/session/manager/core.py` | `SessionManagerImpl` |
| `src/oridecon/ai/session/branching/branch_manager.py` | `BranchManager` |
| `src/oridecon/ai/session/multi_agent/group_session.py` | `GroupSession` |
| `src/oridecon/ai/session/middleware/session_middleware.py` | `SessionMiddleware` |
| `src/oridecon/ai/session/stores/` | Persistence backends |
| `src/oridecon/ai/session/di/provider.py` | `SessionProvider` |
