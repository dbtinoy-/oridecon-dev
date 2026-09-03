# AUDIT_QUALITY.md — Oridecon Framework Quality Snapshot

> **Source**: Live command evidence from repository quality tools, with package counts as supporting context.

---

## Summary

- Tool checks run: 2
- Passing tools: 0
- Failing tools: 2
- Packages counted: 55
- Total mypy errors: 4533
- Packages with errors: 44

## Tool Results

| Tool | Status | Exit Code | Duration | Command |
|------|--------|-----------|----------|---------|
| `Ruff` | **FAIL** | 1 | 255 ms | `uv run ruff check .` |
| `Mypy` | **FAIL** | timeout | 632707 ms | `uv run mypy src/ (per-package across 55 packages)` |

### Ruff

- Status: **FAIL**
- Exit code: `1`
- Duration: `255 ms`
- Command: `uv run ruff check .`
- Output snippet:

```text
RUF022 [*] `__all__` is not sorted
   --> core/oridecon-contracts/src/oridecon/contracts/exceptions/__init__.py:99:11
    |
 97 |   )
 98 |
 99 |   __all__ = [
    |  ___________^
100 | |     "AuthenticationError",
...
```

### Mypy

- Status: **FAIL**
- Exit code: `timeout`
- Duration: `632707 ms`
- Command: `uv run mypy src/ (per-package across 55 packages)`
- Output snippet:

```text
[oridecon] 264 errors
[oridecon-admin] 958 errors
[oridecon-ai] 66 errors
[oridecon-ai-agents] 8 errors
[oridecon-ai-llm] 20 errors
[oridecon-ai-prompt] 1 errors
[oridecon-ai-rag] 12 errors
[oridecon-ai-relay] 1 errors
[oridecon-ai-skills] 1 errors
[oridecon-audit] 93 errors
[oridecon-auth] 71 errors
[oridecon-builder] 56 errors
[oridecon-cache] 198 errors
[oridecon-cli] 103 errors
[oridecon-contracts] 3 errors
[oridecon-events] 95 errors
[oridecon-features] 43 errors
[oridecon-graph] 78 errors
[oridecon-graphql] 129 errors
[oridecon-http] 48 errors
[oridecon-monitor] 138 errors
[oridecon-multimedia] 17 errors
[oridecon-multimedia-beat] 2 errors
[oridecon-multimedia-image] 6 errors
[oridecon-multimedia-interpolate] 4 errors
[oridecon-multimedia-music] 6 errors
[oridecon-multimedia-tts] 8 errors
[oridecon-multimedia-upscale] 4 errors
[oridecon-multimedia-video] Command timed out.
[oridecon-nosql] 30 errors
[oridecon-notification] 195 errors
[oridecon-queue] 31 errors
[oridecon-resilience] 117 errors
[oridecon-search] 131 errors
[oridecon-secrets] 2 errors
[oridecon-sql] 387 errors
[oridecon-storage] 28 errors
[oridecon-tasks] 180 errors
[oridecon-tenancy] 144 errors
[oridecon-testing] 216 errors
[oridecon-ui] 38 errors
[oridecon-vector] 177 errors
[oridecon-web] 302 errors
[oridecon-webhook] 20 errors
[oridecon-workflow] 102 errors
```

### Mypy Error Breakdown

#### By Error Code

| Code | Count | Description |
|------|-------|-------------|
| `import-not-found` | 3265 | Type checking error |
| `unused-ignore` | 487 | Unused type: ignore comment |
| `misc` | 244 | Miscellaneous type checking error |
| `no-any-return` | 226 | Function returns Any when specific type declared |
| `union-attr` | 57 | Type checking error |
| `attr-defined` | 48 | Attribute not defined on type |
| `valid-type` | 40 | Type checking error |
| `import-untyped` | 31 | Type checking error |
| `arg-type` | 25 | Argument type mismatch |
| `dict-item` | 25 | Type checking error |
| `assignment` | 14 | Type checking error |
| `var-annotated` | 12 | Variable missing type annotation |
| `str-format` | 12 | Type checking error |
| `redundant-cast` | 10 | Type checking error |
| `str` | 9 | Type checking error |

#### By Package (Top 10)

| Package | Errors |
|---------|--------|
| `oridecon-admin` | 958 |
| `oridecon-sql` | 387 |
| `oridecon-web` | 302 |
| `oridecon` | 264 |
| `oridecon-testing` | 216 |
| `oridecon-cache` | 198 |
| `oridecon-notification` | 195 |
| `oridecon-tasks` | 180 |
| `oridecon-vector` | 177 |
| `oridecon-tenancy` | 144 |

## Package Metrics

| Package | Source Files | Test Files |
|---------|--------------|------------|
| `oridecon` | 311 | 282 |
| `oridecon-admin` | 596 | 574 |
| `oridecon-ai` | 24 | 101 |
| `oridecon-ai-agents` | 59 | 44 |
| `oridecon-ai-evaluation` | 22 | 24 |
| `oridecon-ai-feedback` | 24 | 29 |
| `oridecon-ai-governance` | 77 | 46 |
| `oridecon-ai-guard` | 33 | 22 |
| `oridecon-ai-llm` | 160 | 131 |
| `oridecon-ai-mcp` | 63 | 37 |
| `oridecon-ai-memory` | 48 | 32 |
| `oridecon-ai-observability` | 26 | 30 |
| `oridecon-ai-prompt` | 45 | 34 |
| `oridecon-ai-rag` | 188 | 52 |
| `oridecon-ai-relay` | 42 | 44 |
| `oridecon-ai-relay-gateway` | 66 | 66 |
| `oridecon-ai-session` | 46 | 37 |
| `oridecon-ai-skills` | 52 | 40 |
| `oridecon-ai-workers` | 34 | 34 |
| `oridecon-audit` | 46 | 38 |
| `oridecon-auth` | 136 | 91 |
| `oridecon-builder` | 63 | 1 |
| `oridecon-cache` | 93 | 73 |
| `oridecon-cli` | 97 | 80 |
| `oridecon-contracts` | 346 | 168 |
| `oridecon-events` | 158 | 114 |
| `oridecon-features` | 34 | 26 |
| `oridecon-graph` | 25 | 33 |
| `oridecon-graphql` | 82 | 63 |
| `oridecon-http` | 32 | 32 |
| `oridecon-monitor` | 93 | 59 |
| `oridecon-multimedia` | 20 | 23 |
| `oridecon-multimedia-beat` | 12 | 7 |
| `oridecon-multimedia-image` | 14 | 9 |
| `oridecon-multimedia-interpolate` | 12 | 7 |
| `oridecon-multimedia-music` | 16 | 9 |
| `oridecon-multimedia-tts` | 21 | 13 |
| `oridecon-multimedia-upscale` | 16 | 9 |
| `oridecon-multimedia-video` | 29 | 20 |
| `oridecon-nosql` | 42 | 47 |
| `oridecon-notification` | 61 | 38 |
| `oridecon-queue` | 45 | 43 |
| `oridecon-resilience` | 55 | 38 |
| `oridecon-search` | 97 | 62 |
| `oridecon-secrets` | 25 | 15 |
| `oridecon-sql` | 197 | 159 |
| `oridecon-storage` | 38 | 38 |
| `oridecon-tasks` | 92 | 64 |
| `oridecon-tenancy` | 63 | 44 |
| `oridecon-testing` | 170 | 41 |
| `oridecon-ui` | 169 | 91 |
| `oridecon-vector` | 65 | 43 |
| `oridecon-web` | 202 | 176 |
| `oridecon-webhook` | 41 | 36 |
| `oridecon-workflow` | 68 | 54 |

