# AUDIT_RULES.md — Oridecon Framework Rules Audit

> **Source**: Static rule analysis for architectural boundaries, import policy, and package coverage.

---

## Severity Summary

| Severity | Count |
|----------|-------|
| critical | 0 |
| important | 40 |
| minor | 0 |

## Findings

| File | Line | Rule ID | Severity | Message |
|------|------|---------|----------|---------|
| `core/oridecon-contracts/src/oridecon/contracts/ai/governance/__init__.py` | 44 | `init-no-logic` | `important` | core/oridecon-contracts/src/oridecon/contracts/ai/governance/__init__.py declares ClassDef 'GovernanceDecision' in __init__.py. |
| `core/oridecon-contracts/src/oridecon/contracts/ai/governance/__init__.py` | 53 | `init-no-logic` | `important` | core/oridecon-contracts/src/oridecon/contracts/ai/governance/__init__.py declares ClassDef 'CostTrackingProtocol' in __init__.py. |
| `core/oridecon-contracts/src/oridecon/contracts/ai/governance/__init__.py` | 71 | `init-no-logic` | `important` | core/oridecon-contracts/src/oridecon/contracts/ai/governance/__init__.py declares ClassDef 'AIGovernanceProtocol' in __init__.py. |
| `core/oridecon-contracts/src/oridecon/contracts/ai/governance/__init__.py` | 97 | `init-no-logic` | `important` | core/oridecon-contracts/src/oridecon/contracts/ai/governance/__init__.py declares ClassDef 'AuditEventType' in __init__.py. |
| `core/oridecon-contracts/src/oridecon/contracts/ai/governance/__init__.py` | 116 | `init-no-logic` | `important` | core/oridecon-contracts/src/oridecon/contracts/ai/governance/__init__.py declares ClassDef 'AIAuditEvent' in __init__.py. |
| `core/oridecon-contracts/src/oridecon/contracts/ai/governance/__init__.py` | 148 | `init-no-logic` | `important` | core/oridecon-contracts/src/oridecon/contracts/ai/governance/__init__.py declares ClassDef 'AIAuditStoreProtocol' in __init__.py. |
| `experimental/ai/oridecon-ai-relay/src/oridecon/ai/relay/mappers/claude/__init__.py` | 19 | `init-no-logic` | `important` | experimental/ai/oridecon-ai-relay/src/oridecon/ai/relay/mappers/claude/__init__.py declares ClassDef 'ClaudeMapper' in __init__.py. |
| `experimental/ai/oridecon-ai-relay/src/oridecon/ai/relay/mappers/openai_responses/__init__.py` | 20 | `init-no-logic` | `important` | experimental/ai/oridecon-ai-relay/src/oridecon/ai/relay/mappers/openai_responses/__init__.py declares ClassDef 'OpenAIResponsesMapper' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/controllers/auth/__init__.py` | 24 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/controllers/auth/__init__.py declares ClassDef 'AuthController' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/controllers/resource/__init__.py` | 28 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/controllers/resource/__init__.py declares ClassDef 'ResourceController' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 65 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'UserCreated' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 73 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'UserUpdated' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 81 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'UserDeactivated' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 88 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'UserDeleted' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 95 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'ResourceCreated' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 105 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'ResourceUpdated' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 115 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'ResourceDeleted' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 125 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'BulkOperationCompleted' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 141 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'AdminEvent' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 148 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'ResourceRestored' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 156 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'ResourceViewed' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 164 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'ExportStarted' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 174 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'ExportCompleted' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 186 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'ExportFailed' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 195 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'ImportStarted' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 205 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'ImportCompleted' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 217 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'AdminUserLoggedIn' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 226 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'AdminUserLoggedOut' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 233 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'AdminUserCreated' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 243 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'AdminUserUpdated' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 251 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'PasswordChanged' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 258 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'RolesAssigned' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 267 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'ActionExecuted' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 278 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'SettingsUpdated' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 286 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'AdminStarted' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 294 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'AdminStopped' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py` | 299 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/events/__init__.py declares ClassDef 'ConfigReloaded' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/integrations/__init__.py` | 19 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/integrations/__init__.py declares FunctionDef 'register' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/integrations/__init__.py` | 24 | `init-no-logic` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/integrations/__init__.py declares FunctionDef 'get' in __init__.py. |
| `experimental/apps/oridecon-admin/src/oridecon/admin/navigation/__init__.py` | 10 | `import-absolute-only` | `important` | experimental/apps/oridecon-admin/src/oridecon/admin/navigation/__init__.py uses a relative import; replace it with an absolute import. |

## Rule Diagnostics

| Rule ID | Severity | Findings | Detected Error About |
|---------|----------|----------|----------------------|
| `import-absolute-only` | `important` | 1 | Relative imports obscure package boundaries and are disallowed across the framework. |
| `init-no-logic` | `important` | 39 | __init__.py files should contain exports only so package entry points stay declarative. |

## Package Coverage

- Discovered packages: 54
- Covered packages: 54
- Missing packages: 0
- Coverage status: **PASS**

### Covered Packages

- `oridecon`
- `oridecon-admin`
- `oridecon-ai`
- `oridecon-ai-agents`
- `oridecon-ai-evaluation`
- `oridecon-ai-feedback`
- `oridecon-ai-governance`
- `oridecon-ai-guard`
- `oridecon-ai-llm`
- `oridecon-ai-mcp`
- `oridecon-ai-memory`
- `oridecon-ai-observability`
- `oridecon-ai-prompt`
- `oridecon-ai-rag`
- `oridecon-ai-relay`
- `oridecon-ai-relay-gateway`
- `oridecon-ai-session`
- `oridecon-ai-skills`
- `oridecon-ai-workers`
- `oridecon-audit`
- `oridecon-auth`
- `oridecon-cache`
- `oridecon-cli`
- `oridecon-contracts`
- `oridecon-events`
- `oridecon-features`
- `oridecon-graph`
- `oridecon-graphql`
- `oridecon-http`
- `oridecon-monitor`
- `oridecon-multimedia`
- `oridecon-multimedia-beat`
- `oridecon-multimedia-image`
- `oridecon-multimedia-interpolate`
- `oridecon-multimedia-music`
- `oridecon-multimedia-tts`
- `oridecon-multimedia-upscale`
- `oridecon-multimedia-video`
- `oridecon-nosql`
- `oridecon-notification`
- `oridecon-queue`
- `oridecon-resilience`
- `oridecon-search`
- `oridecon-secrets`
- `oridecon-sql`
- `oridecon-storage`
- `oridecon-tasks`
- `oridecon-tenancy`
- `oridecon-testing`
- `oridecon-ui`
- `oridecon-vector`
- `oridecon-web`
- `oridecon-webhook`
- `oridecon-workflow`

### Missing Packages

- `(none)`

## Resolution Guide

- `import-absolute-only`: Replace relative imports (for example `from .module import ...`) with absolute imports rooted at `oridecon...` so module ownership stays explicit.
- `init-no-logic`: Keep `__init__.py` export-only. Move functions/classes to dedicated modules and re-export symbols through `__all__` from `__init__.py`.

