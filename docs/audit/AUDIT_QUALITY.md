# AUDIT_QUALITY.md — Oridecon Framework Quality Snapshot

> **Source**: Live command evidence from repository quality tools, with package counts as supporting context.

---

## Summary

- Tool checks run: 2
- Passing tools: 2
- Failing tools: 0
- Packages counted: 55
- Total mypy errors: 0
- Packages with errors: 0

## Tool Results

| Tool | Status | Exit Code | Duration | Command |
|------|--------|-----------|----------|---------|
| `Ruff` | **PASS** | 0 | 236 ms | `uv run ruff check .` |
| `Mypy` | **PASS** | 0 | 57116 ms | `uv run mypy src/ (per-package across 55 packages)` |

### Ruff

- Status: **PASS**
- Exit code: `0`
- Duration: `236 ms`
- Command: `uv run ruff check .`
- Output snippet:

```text
All checks passed!
```

### Mypy

- Status: **PASS**
- Exit code: `0`
- Duration: `57116 ms`
- Command: `uv run mypy src/ (per-package across 55 packages)`
- Output snippet:

```text
All per-package mypy checks passed.
```

## Package Metrics

| Package | Source Files | Test Files |
|---------|--------------|------------|
| `oridecon` | 311 | 282 |
| `oridecon-admin` | 575 | 531 |
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
| `oridecon-builder` | 51 | 1 |
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
| `oridecon-sql` | 197 | 157 |
| `oridecon-storage` | 38 | 38 |
| `oridecon-tasks` | 92 | 64 |
| `oridecon-tenancy` | 63 | 44 |
| `oridecon-testing` | 170 | 41 |
| `oridecon-ui` | 169 | 90 |
| `oridecon-vector` | 65 | 43 |
| `oridecon-web` | 202 | 176 |
| `oridecon-webhook` | 41 | 36 |
| `oridecon-workflow` | 68 | 54 |

