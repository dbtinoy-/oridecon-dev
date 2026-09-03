# AUDIT_DEPENDENCIES.md — Oridecon Framework Dependency Freshness Snapshot

> **Source**: Live command evidence from `uv pip list --outdated` and workspace
> manifest scans against `dev/checks/dep_pins.py`.

---

## Summary

- Outdated packages detected: 12
- Workspace members with own pyproject.toml: 54
- Unbounded third-party pins (baseline debt): 807

## Tool Results

| Tool | Status | Exit Code | Duration | Command |
|------|--------|-----------|----------|---------|
| `uv pip list --outdated` | **PASS** | 0 | 1927 ms | `uv pip list --outdated` |
| `check_dep_pins.py` | **PASS** | 0 | 411 ms | `uv run python dev/check_dep_pins.py` |

## Outdated Packages

| Package | Installed | Latest | Type |
|---------|-----------|--------|------|
| `argon2-cffi-bindings` | 25.1.0 | 26.1.0 | wheel |
| `botocore` | 1.40.61 | 1.43.81 | wheel |
| `click` | 8.4.2 | 8.5.0 | wheel |
| `cryptography` | 50.0.0 | 50.0.1 | wheel |
| `filelock` | 3.32.3 | 3.32.4 | wheel |
| `platformdirs` | 4.11.3 | 4.11.4 | wheel |
| `pydantic-core` | 2.46.4 | 2.48.0 | wheel |
| `python-discovery` | 1.5.2 | 1.5.3 | wheel |
| `rich` | 13.9.4 | 15.0.0 | wheel |
| `ruff` | 0.16.3 | 0.16.4 | wheel |
| `types-webencodings` | 0.5.0.20260408 | 0.6.0.20260826 | wheel |
| `virtualenv` | 21.7.4 | 21.7.5 | wheel |

## Direct Dependency Manifest

| Member | Own pyproject | Unbounded third-party pins |
|--------|---------------|----------------------------|
| `oridecon` | yes | 15 |
| `oridecon-admin` | yes | 35 |
| `oridecon-ai` | yes | 80 |
| `oridecon-ai-agents` | yes | 8 |
| `oridecon-ai-evaluation` | yes | 0 |
| `oridecon-ai-feedback` | yes | 7 |
| `oridecon-ai-governance` | yes | 8 |
| `oridecon-ai-guard` | yes | 8 |
| `oridecon-ai-llm` | yes | 33 |
| `oridecon-ai-mcp` | yes | 8 |
| `oridecon-ai-memory` | yes | 8 |
| `oridecon-ai-observability` | yes | 7 |
| `oridecon-ai-prompt` | yes | 8 |
| `oridecon-ai-rag` | yes | 21 |
| `oridecon-ai-relay` | yes | 7 |
| `oridecon-ai-relay-gateway` | yes | 9 |
| `oridecon-ai-session` | yes | 7 |
| `oridecon-ai-skills` | yes | 8 |
| `oridecon-ai-workers` | yes | 7 |
| `oridecon-audit` | yes | 8 |
| `oridecon-auth` | yes | 29 |
| `oridecon-cache` | yes | 25 |
| `oridecon-cli` | yes | 19 |
| `oridecon-contracts` | yes | 7 |
| `oridecon-events` | yes | 30 |
| `oridecon-features` | yes | 8 |
| `oridecon-graph` | yes | 7 |
| `oridecon-graphql` | yes | 20 |
| `oridecon-http` | yes | 9 |
| `oridecon-monitor` | yes | 24 |
| `oridecon-multimedia` | yes | 6 |
| `oridecon-multimedia-beat` | yes | 13 |
| `oridecon-multimedia-image` | yes | 8 |
| `oridecon-multimedia-interpolate` | yes | 8 |
| `oridecon-multimedia-music` | yes | 8 |
| `oridecon-multimedia-tts` | yes | 8 |
| `oridecon-multimedia-upscale` | yes | 8 |
| `oridecon-multimedia-video` | yes | 8 |
| `oridecon-nosql` | yes | 11 |
| `oridecon-notification` | yes | 20 |
| `oridecon-queue` | yes | 4 |
| `oridecon-resilience` | yes | 6 |
| `oridecon-search` | yes | 33 |
| `oridecon-secrets` | yes | 13 |
| `oridecon-sql` | yes | 25 |
| `oridecon-storage` | yes | 22 |
| `oridecon-tasks` | yes | 26 |
| `oridecon-tenancy` | yes | 8 |
| `oridecon-testing` | yes | 25 |
| `oridecon-ui` | yes | 15 |
| `oridecon-vector` | yes | 15 |
| `oridecon-web` | yes | 37 |
| `oridecon-webhook` | yes | 2 |
| `oridecon-workflow` | yes | 8 |

Baseline guard: `dev/checks/dep_pins.py` fails CI on unbounded third-party pins not covered by `dev/dep_pins_baseline.json`; regenerate deliberately with `--write-baseline`.
