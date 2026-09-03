# oridecon-ai-skills

AI skills and tools for the Oridecon Framework — registry, executor, builtin tools, discovery

---

## Overview

Composable, registry-based skill execution for the Oridecon AI framework. Define skills as classes or decorated functions, execute them with retry, caching, permission enforcement, and timeout — and compose them into chains, pipelines, parallel fans, and content-routers. Zero-config usage starts with sensible defaults.


> Full documentation: [docs.oridecon.dev](https://docs.oridecon.dev)
## Install

```bash
uv add oridecon-ai-skills
```

## Quick Start

```python
from oridecon import Application
from oridecon.di.module import Module, module

from oridecon.ai.skills import SkillsModule
from oridecon.ai.skills.config import SkillsConfig


@module(
    imports=[
        SkillsModule.configure(
            SkillsConfig(
                enable_builtin=True,
                builtin_skills=["current_datetime", "math_calculate"],
                cache_enabled=True,
                enforce_permissions=False,
            )
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

> **Zero-config usage:** Call `SkillsModule.configure()` with no arguments to use defaults.

### Option 1 — YAML file

```yaml
# application.yaml
ai_skills:
  default_timeout_seconds: 30.0
  cache_enabled: true
  enforce_permissions: true
  enable_builtin: true
  builtin_skills:
    - "current_datetime"
    - "math_calculate"
```

### Option 2 — Profiles + Environment Variables *(recommended)*

```bash
export ORI_AI_SKILLS__ENFORCE_PERMISSIONS=true
# Environment variables for each field
```

### Option 3 — Python

```python
from oridecon.ai.skills.config import SkillsConfig
from oridecon.ai.skills import SkillsModule

config = SkillsConfig(
    default_timeout_seconds=30.0,
    cache_enabled=True,
    enforce_permissions=True,
    enable_builtin=True,
    builtin_skills=["current_datetime", "math_calculate", "text_summarize"],
)
SkillsModule.configure(config)
```

### Config reference

| Field | Default | Env var | Description |
|-------|---------|---------|-------------|
| `default_timeout_seconds` | `30.0` | `ORI_AI_SKILLS__DEFAULT_TIMEOUT_SECONDS` | Execution timeout per skill |
| `max_retries` | `2` | `ORI_AI_SKILLS__MAX_RETRIES` | Retry attempts on failure |
| `max_concurrent_executions` | `10` | `ORI_AI_SKILLS__MAX_CONCURRENT_EXECUTIONS` | Semaphore cap on concurrent executions |
| `cache_enabled` | `True` | `ORI_AI_SKILLS__CACHE_ENABLED` | Global result caching switch |
| `cache_ttl_seconds` | `3600` | `ORI_AI_SKILLS__CACHE_TTL_SECONDS` | Default TTL for cached results |
| `enforce_permissions` | `True` | `ORI_AI_SKILLS__ENFORCE_PERMISSIONS` | Enable permission checks |
| `auto_discover` | `False` | `ORI_AI_SKILLS__AUTO_DISCOVER` | Scan `scan_packages` on boot |
| `enable_builtin` | `True` | `ORI_AI_SKILLS__ENABLE_BUILTIN` | Register built-in skills on boot |
| `builtin_skills` | (list) | `ORI_AI_SKILLS__BUILTIN_SKILLS` | Which built-in skills to register |
| `enable_skill_sources` | `True` | `ORI_AI_SKILLS__ENABLE_SKILL_SOURCES` | Scan external SKILL.md sources on boot |

## Module Factory Methods

| Method | Description |
|--------|-------------|
| `SkillsModule.configure(config)` | Configure with explicit config |
| `SkillsModule.stub(config)` | Minimal config for testing |

## Key Features

- **Class-based skills**: `AbstractSkill` base class with `SkillDefinition`
- **Function-based skills**: `@skill` decorator for registering functions
- **Skill executor**: Retry, caching, permissions, and timeout enforcement
- **Built-in skills**: DateTime, Math, HTTPRequest, WebSearch, FileRead, FileWrite, DatabaseQuery, CodeExecute
- **Composition**: `SkillChain`, `ParallelSkills`, `SkillPipeline`, `SkillRouter`
- **MCP bridge**: `MCPSkillBridge` imports MCP tools as skills and exports skills as MCP tools
- **Registry**: Named lookup and registration via `SkillRegistry`

## Testing

```python
async with Application.boot(modules=[SkillsModule.stub()]) as app:
    # your test code
    ...
```

## Key Source Files

| File | What it contains |
|------|-----------------|
| `src/oridecon/ai/skills/module.py` | `SkillsModule.configure()`, `.stub()` |
| `src/oridecon/ai/skills/config.py` | `SkillsConfig` |
| `src/oridecon/ai/skills/base/core.py` | `AbstractSkill`, `FunctionSkill` |
| `src/oridecon/ai/skills/decorators/core.py` | `@skill`, `@skill_param` |
| `src/oridecon/ai/skills/executor/core.py` | `SkillExecutor` |
| `src/oridecon/ai/skills/registry/core.py` | `SkillRegistry` |
| `src/oridecon/ai/skills/composition/` | chain, parallel, pipeline, router |
| `src/oridecon/ai/skills/discovery/mcp_bridge.py` | `MCPSkillBridge` |
| `src/oridecon/ai/skills/di/provider.py` | `SkillsProvider` |
