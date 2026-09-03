# AUDIT_TESTS.md — Oridecon Framework Targeted Test Execution Audit

> **Source**: Live pytest execution evidence for targeted scopes, with `tests/` directory scanning as supporting context.

---

## Summary

- Total passed tests: 33270
- Total failed tests: 12
- Total skipped tests: 364
- Total warnings: 352
- Aggregate code coverage: 76.59%

- Representative commands run: 55
- Commands passing: 51
- Commands failing: 4
- Packages with tests: 55
- Test files: 3523
- Test functions: 33389

### Exit Codes Reference

- **`0`**: Success — All tests passed and code coverage met the configured threshold.
- **`1`**: Failure — Functional tests failed OR code coverage fell below the package's `--cov-fail-under` threshold.
- **`timeout`**: The test command exceeded the execution time limit (120s) and was automatically terminated.

## Execution Evidence

| Label | Code Coverage | Pass/Total | Failed | Skipped | Warnings | Exit Code | Duration |
|-------|---------------|------------|---------|----------|------|-----------|----------|
| Package tests: core/oridecon-contracts | 34.0% | 1814/1814 | 0 | 0 | 4 | 0 | 10376 ms |
| Package tests: core/oridecon | 38.0% | 3089/3094 | 0 | 5 | 2 | 0 | 54031 ms |
| Package tests: experimental/ai/oridecon-ai-agents | 85.0% | 402/402 | 0 | 0 | 4 | 0 | 5887 ms |
| Package tests: experimental/ai/oridecon-ai-evaluation | 97.0% | 167/167 | 0 | 0 | 4 | 0 | 1863 ms |
| Package tests: experimental/ai/oridecon-ai-feedback | 96.0% | 260/260 | 0 | 0 | 4 | 0 | 2097 ms |
| Package tests: experimental/ai/oridecon-ai-governance | 88.0% | 544/544 | 0 | 0 | 47 | 0 | 4612 ms |
| Package tests: experimental/ai/oridecon-ai-guard | 87.0% | 242/242 | 0 | 0 | 7 | 0 | 2130 ms |
| Package tests: experimental/ai/oridecon-ai-llm | 71.0% | 953/974 | 0 | 21 | 4 | 0 | 31074 ms |
| Package tests: experimental/ai/oridecon-ai-mcp | 54.0% | 400/400 | 0 | 0 | 4 | 0 | 3526 ms |
| Package tests: experimental/ai/oridecon-ai-memory | 83.0% | 240/240 | 0 | 0 | 4 | 0 | 2394 ms |
| Package tests: experimental/ai/oridecon-ai-observability | 87.0% | 260/260 | 0 | 0 | 4 | 0 | 2622 ms |
| Package tests: experimental/ai/oridecon-ai-prompt | 87.0% | 307/307 | 0 | 0 | 4 | 0 | 2362 ms |
| Package tests: experimental/ai/oridecon-ai-rag | 62.0% | 528/535 | 0 | 7 | 4 | 0 | 6830 ms |
| Package tests: experimental/ai/oridecon-ai-relay-gateway | 94.0% | 581/581 | 0 | 0 | 4 | 0 | 4146 ms |
| Package tests: experimental/ai/oridecon-ai-relay | 91.0% | 534/534 | 0 | 0 | 4 | 0 | 5593 ms |
| Package tests: experimental/ai/oridecon-ai-session | 89.0% | 219/219 | 0 | 0 | 4 | 0 | 2373 ms |
| Package tests: experimental/ai/oridecon-ai-skills | 80.0% | 286/286 | 0 | 0 | 6 | 0 | 5338 ms |
| Package tests: experimental/ai/oridecon-ai-workers | 87.0% | 328/328 | 0 | 0 | 4 | 0 | 3777 ms |
| Package tests: experimental/ai/oridecon-ai | 42.0% | 470/489 | 0 | 19 | 4 | 1 | 15022 ms |
| Package tests: experimental/apps/oridecon-admin | 79.0% | 5845/5897 | 12 | 40 | 33 | 1 | 73098 ms |
| Package tests: experimental/apps/oridecon-builder | 0.0% | 0/0 | 0 | 0 | 0 | 1 | 409 ms |
| Package tests: experimental/apps/oridecon-cli | 81.0% | 894/895 | 0 | 1 | 6 | 0 | 22957 ms |
| Package tests: experimental/apps/oridecon-ui | 77.0% | 1444/1522 | 0 | 78 | 4 | 0 | 7228 ms |
| Package tests: experimental/multimedia/oridecon-multimedia-beat | 74.0% | 21/21 | 0 | 0 | 4 | 0 | 2659 ms |
| Package tests: experimental/multimedia/oridecon-multimedia-image | 92.0% | 54/54 | 0 | 0 | 4 | 0 | 2175 ms |
| Package tests: experimental/multimedia/oridecon-multimedia-interpolate | 88.0% | 23/23 | 0 | 0 | 4 | 0 | 1865 ms |
| Package tests: experimental/multimedia/oridecon-multimedia-music | 87.0% | 47/47 | 0 | 0 | 4 | 0 | 2010 ms |
| Package tests: experimental/multimedia/oridecon-multimedia-tts | 79.0% | 63/63 | 0 | 0 | 4 | 0 | 2263 ms |
| Package tests: experimental/multimedia/oridecon-multimedia-upscale | 92.0% | 42/42 | 0 | 0 | 4 | 0 | 2066 ms |
| Package tests: experimental/multimedia/oridecon-multimedia-video | 87.0% | 182/182 | 0 | 0 | 4 | 0 | 5661 ms |
| Package tests: experimental/multimedia/oridecon-multimedia | 58.0% | 89/89 | 0 | 0 | 5 | 0 | 4598 ms |
| Package tests: packages/oridecon-audit | 87.0% | 293/293 | 0 | 0 | 4 | 0 | 2363 ms |
| Package tests: packages/oridecon-auth | 69.0% | 632/636 | 0 | 4 | 15 | 0 | 29888 ms |
| Package tests: packages/oridecon-cache | 81.0% | 874/887 | 0 | 13 | 6 | 0 | 10779 ms |
| Package tests: packages/oridecon-events | 64.0% | 1002/1017 | 0 | 15 | 4 | 0 | 11985 ms |
| Package tests: packages/oridecon-features | 84.0% | 253/253 | 0 | 0 | 17 | 0 | 3493 ms |
| Package tests: packages/oridecon-graph | 80.0% | 263/264 | 0 | 1 | 4 | 0 | 2202 ms |
| Package tests: packages/oridecon-graphql | 76.0% | 520/522 | 0 | 2 | 23 | 0 | 5837 ms |
| Package tests: packages/oridecon-http | 85.0% | 457/457 | 0 | 0 | 8 | 0 | 2772 ms |
| Package tests: packages/oridecon-monitor | 78.0% | 317/338 | 0 | 21 | 4 | 1 | 8173 ms |
| Package tests: packages/oridecon-nosql | 91.0% | 537/537 | 0 | 0 | 4 | 0 | 3345 ms |
| Package tests: packages/oridecon-notification | 85.0% | 296/296 | 0 | 0 | 7 | 0 | 5854 ms |
| Package tests: packages/oridecon-queue | 85.0% | 235/235 | 0 | 0 | 4 | 0 | 4442 ms |
| Package tests: packages/oridecon-resilience | 75.0% | 311/311 | 0 | 0 | 4 | 0 | 20753 ms |
| Package tests: packages/oridecon-search | 66.0% | 813/818 | 0 | 5 | 4 | 0 | 4154 ms |
| Package tests: packages/oridecon-secrets | 59.0% | 134/134 | 0 | 0 | 4 | 0 | 1640 ms |
| Package tests: packages/oridecon-sql | 61.0% | 1351/1442 | 0 | 91 | 10 | 0 | 12372 ms |
| Package tests: packages/oridecon-storage | 64.0% | 463/466 | 0 | 3 | 4 | 0 | 6647 ms |
| Package tests: packages/oridecon-tasks | 76.0% | 537/553 | 0 | 16 | 4 | 0 | 11821 ms |
| Package tests: packages/oridecon-tenancy | 85.0% | 362/362 | 0 | 0 | 4 | 0 | 2927 ms |
| Package tests: packages/oridecon-testing | 17.0% | 443/458 | 0 | 15 | 2 | 0 | 8133 ms |
| Package tests: packages/oridecon-vector | 78.0% | 533/533 | 0 | 0 | 4 | 0 | 4134 ms |
| Package tests: packages/oridecon-web | 81.0% | 1421/1428 | 0 | 7 | 6 | 0 | 14794 ms |
| Package tests: packages/oridecon-webhook | 90.0% | 336/336 | 0 | 0 | 4 | 0 | 2760 ms |
| Package tests: packages/oridecon-workflow | 73.0% | 559/559 | 0 | 0 | 4 | 0 | 13694 ms |

### Execution Scope Notes

- `framework-core`: real test execution for `oridecon/tests`.
- `package`: real test execution for `<package>/tests` across every discovered Oridecon package with tests.
### Package tests: core/oridecon-contracts

- Scope: `core/oridecon-contracts/tests`
- Command: `uv run pytest core/oridecon-contracts/tests -q -m not integration --cov=core/oridecon.contracts`
- Status: **PASS**
- Exit code: `0`
- Duration: `10376 ms`
- Parsed summary: `1814 passed, 4 warnings in 9.03s`
- Counters: passed=1814, total=1814, failed=0, skipped=0, warnings=4, coverage=34.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:19:25 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [  3%]
........................................................................ [  7%]
........................................................................ [ 11%]
........................................................................ [ 15%]
........................................................................ [ 19%]
........................................................................ [ 23%]
........................................................................ [ 27%]
....................................................
```

### Package tests: core/oridecon

- Scope: `core/oridecon/tests`
- Command: `uv run pytest core/oridecon/tests -q -m not integration --cov=core/oridecon`
- Status: **PASS**
- Exit code: `0`
- Duration: `54031 ms`
- Parsed summary: `3089 passed, 5 skipped, 19 deselected, 2 warnings in 51.45s`
- Counters: passed=3089, total=3094, failed=0, skipped=5, warnings=2, coverage=38.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:19:35 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
2026-09-03 20:19:35 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=1 imports=0 is_global=False module=CoreModule providers=1
2026-09-03 20:19:35 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=1 imports=1 is_global=False module=CacheModule providers=1
2026-09-03 20:19:35 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=1 imports=2 is_global=False module=WebModule providers=1
.........................................................
```

### Package tests: experimental/ai/oridecon-ai-agents

- Scope: `experimental/ai/oridecon-ai-agents/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-agents/tests -q -m not integration --cov=experimental/ai/oridecon.ai.agents`
- Status: **PASS**
- Exit code: `0`
- Duration: `5887 ms`
- Parsed summary: `402 passed, 10 deselected, 4 warnings in 4.61s`
- Counters: passed=402, total=402, failed=0, skipped=0, warnings=4, coverage=85.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:20:29 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 17%]
........................................................................ [ 35%]
........................................................................ [ 53%]
........................................................................ [ 71%]
........................................................................ [ 89%]
..........................................                               [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/_
```

### Package tests: experimental/ai/oridecon-ai-evaluation

- Scope: `experimental/ai/oridecon-ai-evaluation/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-evaluation/tests -q -m not integration --cov=experimental/ai/oridecon.ai.evaluation`
- Status: **PASS**
- Exit code: `0`
- Duration: `1863 ms`
- Parsed summary: `167 passed, 4 warnings in 0.71s`
- Counters: passed=167, total=167, failed=0, skipped=0, warnings=4, coverage=97.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:20:35 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 43%]
........................................................................ [ 86%]
.......................                                                  [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewriteWarning: Module already imported so cannot be rewritten; oridecon.testing.fix
```

### Package tests: experimental/ai/oridecon-ai-feedback

- Scope: `experimental/ai/oridecon-ai-feedback/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-feedback/tests -q -m not integration --cov=experimental/ai/oridecon.ai.feedback`
- Status: **PASS**
- Exit code: `0`
- Duration: `2097 ms`
- Parsed summary: `260 passed, 4 warnings in 0.94s`
- Counters: passed=260, total=260, failed=0, skipped=0, warnings=4, coverage=96.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:20:37 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 27%]
........................................................................ [ 55%]
........................................................................ [ 83%]
............................................                             [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewr
```

### Package tests: experimental/ai/oridecon-ai-governance

- Scope: `experimental/ai/oridecon-ai-governance/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-governance/tests -q -m not integration --cov=experimental/ai/oridecon.ai.governance`
- Status: **PASS**
- Exit code: `0`
- Duration: `4612 ms`
- Parsed summary: `544 passed, 7 deselected, 47 warnings in 3.39s`
- Counters: passed=544, total=544, failed=0, skipped=0, warnings=47, coverage=88.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:20:39 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 13%]
........................................................................ [ 26%]
........................................................................ [ 39%]
........................................................................ [ 52%]
........................................................................ [ 66%]
........................................................................ [ 79%]
........................................................................ [ 92%]
........................................            
```

### Package tests: experimental/ai/oridecon-ai-guard

- Scope: `experimental/ai/oridecon-ai-guard/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-guard/tests -q -m not integration --cov=experimental/ai/oridecon.ai.guard`
- Status: **PASS**
- Exit code: `0`
- Duration: `2130 ms`
- Parsed summary: `242 passed, 17 deselected, 7 warnings in 0.97s`
- Counters: passed=242, total=242, failed=0, skipped=0, warnings=7, coverage=87.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:20:44 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 29%]
........................................................................ [ 59%]
........................................................................ [ 89%]
..........................                                               [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewr
```

### Package tests: experimental/ai/oridecon-ai-llm

- Scope: `experimental/ai/oridecon-ai-llm/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-llm/tests -q -m not integration --cov=experimental/ai/oridecon.ai.llm`
- Status: **PASS**
- Exit code: `0`
- Duration: `31074 ms`
- Parsed summary: `953 passed, 21 skipped, 19 deselected, 4 warnings in 29.58s`
- Counters: passed=953, total=974, failed=0, skipped=21, warnings=4, coverage=71.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:20:46 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
ssssssssssssssss........................................................ [  7%]
........................................................................ [ 14%]
........................................................................ [ 22%]
.....................................................................sss [ 29%]
s....................................................................... [ 36%]
........................................................................ [ 44%]
........................................................................ [ 51%]
....................................................
```

### Package tests: experimental/ai/oridecon-ai-mcp

- Scope: `experimental/ai/oridecon-ai-mcp/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-mcp/tests -q -m not integration --cov=experimental/ai/oridecon.ai.mcp`
- Status: **PASS**
- Exit code: `0`
- Duration: `3526 ms`
- Parsed summary: `400 passed, 13 deselected, 4 warnings in 2.30s`
- Counters: passed=400, total=400, failed=0, skipped=0, warnings=4, coverage=54.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:21:17 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 18%]
........................................................................ [ 36%]
........................................................................ [ 54%]
........................................................................ [ 72%]
........................................................................ [ 90%]
........................................                                 [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/_
```

### Package tests: experimental/ai/oridecon-ai-memory

- Scope: `experimental/ai/oridecon-ai-memory/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-memory/tests -q -m not integration --cov=experimental/ai/oridecon.ai.memory`
- Status: **PASS**
- Exit code: `0`
- Duration: `2394 ms`
- Parsed summary: `240 passed, 16 deselected, 4 warnings in 1.20s`
- Counters: passed=240, total=240, failed=0, skipped=0, warnings=4, coverage=83.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:21:21 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 30%]
........................................................................ [ 60%]
........................................................................ [ 90%]
........................                                                 [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewr
```

### Package tests: experimental/ai/oridecon-ai-observability

- Scope: `experimental/ai/oridecon-ai-observability/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-observability/tests -q -m not integration --cov=experimental/ai/oridecon.ai.observability`
- Status: **PASS**
- Exit code: `0`
- Duration: `2622 ms`
- Parsed summary: `260 passed, 10 deselected, 4 warnings in 1.41s`
- Counters: passed=260, total=260, failed=0, skipped=0, warnings=4, coverage=87.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:21:23 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 27%]
........................................................................ [ 55%]
........................................................................ [ 83%]
............................................                             [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewr
```

### Package tests: experimental/ai/oridecon-ai-prompt

- Scope: `experimental/ai/oridecon-ai-prompt/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-prompt/tests -q -m not integration --cov=experimental/ai/oridecon.ai.prompt`
- Status: **PASS**
- Exit code: `0`
- Duration: `2362 ms`
- Parsed summary: `307 passed, 4 warnings in 1.19s`
- Counters: passed=307, total=307, failed=0, skipped=0, warnings=4, coverage=87.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:21:26 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 23%]
........................................................................ [ 46%]
........................................................................ [ 70%]
........................................................................ [ 93%]
...................                                                      [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .ve
```

### Package tests: experimental/ai/oridecon-ai-rag

- Scope: `experimental/ai/oridecon-ai-rag/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-rag/tests -q -m not integration --cov=experimental/ai/oridecon.ai.rag`
- Status: **PASS**
- Exit code: `0`
- Duration: `6830 ms`
- Parsed summary: `528 passed, 7 skipped, 8 deselected, 4 warnings in 5.52s`
- Counters: passed=528, total=535, failed=0, skipped=7, warnings=4, coverage=62.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:21:28 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
..........................................................s............. [ 13%]
...sss..........ss...................................................... [ 26%]
.........................................................s.............. [ 40%]
........................................................................ [ 53%]
........................................................................ [ 67%]
........................................................................ [ 80%]
........................................................................ [ 94%]
...............................                     
```

### Package tests: experimental/ai/oridecon-ai-relay-gateway

- Scope: `experimental/ai/oridecon-ai-relay-gateway/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-relay-gateway/tests -q -m not integration --cov=experimental/ai/oridecon.ai.relay.gateway`
- Status: **PASS**
- Exit code: `0`
- Duration: `4146 ms`
- Parsed summary: `581 passed, 4 warnings in 2.88s`
- Counters: passed=581, total=581, failed=0, skipped=0, warnings=4, coverage=94.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:21:35 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
2026-09-03 20:21:35 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=RelayModule providers=0
........................................................................ [ 12%]
........................................................................ [ 24%]
........................................................................ [ 37%]
........................................................................ [ 49%]
........................................................................ [ 61%]
..........................
```

### Package tests: experimental/ai/oridecon-ai-relay

- Scope: `experimental/ai/oridecon-ai-relay/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-relay/tests -q -m not integration --cov=experimental/ai/oridecon.ai.relay`
- Status: **PASS**
- Exit code: `0`
- Duration: `5593 ms`
- Parsed summary: `534 passed, 4 warnings in 4.38s`
- Counters: passed=534, total=534, failed=0, skipped=0, warnings=4, coverage=91.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:21:39 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
2026-09-03 20:21:39 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=RelayModule providers=0
........................................................................ [ 13%]
........................................................................ [ 26%]
........................................................................ [ 40%]
........................................................................ [ 53%]
........................................................................ [ 67%]
..........................
```

### Package tests: experimental/ai/oridecon-ai-session

- Scope: `experimental/ai/oridecon-ai-session/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-session/tests -q -m not integration --cov=experimental/ai/oridecon.ai.session`
- Status: **PASS**
- Exit code: `0`
- Duration: `2373 ms`
- Parsed summary: `219 passed, 4 warnings in 1.20s`
- Counters: passed=219, total=219, failed=0, skipped=0, warnings=4, coverage=89.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:21:45 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 32%]
........................................................................ [ 65%]
........................................................................ [ 98%]
...                                                                      [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewr
```

### Package tests: experimental/ai/oridecon-ai-skills

- Scope: `experimental/ai/oridecon-ai-skills/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-skills/tests -q -m not integration --cov=experimental/ai/oridecon.ai.skills`
- Status: **PASS**
- Exit code: `0`
- Duration: `5338 ms`
- Parsed summary: `286 passed, 6 warnings in 4.15s`
- Counters: passed=286, total=286, failed=0, skipped=0, warnings=6, coverage=80.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:21:47 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 25%]
........................................................................ [ 50%]
........................................................................ [ 75%]
......................................................................   [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewr
```

### Package tests: experimental/ai/oridecon-ai-workers

- Scope: `experimental/ai/oridecon-ai-workers/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-workers/tests -q -m not integration --cov=experimental/ai/oridecon.ai.workers`
- Status: **PASS**
- Exit code: `0`
- Duration: `3777 ms`
- Parsed summary: `328 passed, 7 deselected, 4 warnings in 2.60s`
- Counters: passed=328, total=328, failed=0, skipped=0, warnings=4, coverage=87.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:21:52 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 21%]
........................................................................ [ 43%]
........................................................................ [ 65%]
........................................................................ [ 87%]
........................................                                 [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .ve
```

### Package tests: experimental/ai/oridecon-ai

- Scope: `experimental/ai/oridecon-ai/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai/tests -q -m not integration --cov=experimental/ai/oridecon.ai`
- Status: **FAIL**
- Exit code: `1`
- Duration: `15022 ms`
- Parsed summary: `470 passed, 19 skipped, 15 deselected, 4 warnings in 13.67s`
- Counters: passed=470, total=489, failed=0, skipped=19, warnings=4, coverage=42.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:21:56 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 15%]
........................................................................ [ 30%]
..................................................................ss.... [ 45%]
................................s....................................... [ 60%]
..........................................................s.s........... [ 75%]
........................................................................ [ 90%]
...........................................
ERROR: Coverage failure: total of 42 is less than fail-under=43
                        
```

### Package tests: experimental/apps/oridecon-admin

- Scope: `experimental/apps/oridecon-admin/tests`
- Command: `uv run pytest experimental/apps/oridecon-admin/tests -q -m not integration --cov=experimental/apps/oridecon.admin`
- Status: **FAIL**
- Exit code: `1`
- Duration: `73098 ms`
- Parsed summary: `12 failed, 5845 passed, 40 skipped, 29 deselected, 33 warnings in 70.61s (0:01:10)`
- Counters: passed=5845, total=5897, failed=12, skipped=40, warnings=33, coverage=79.0%
- Example failures: `experimental/apps/oridecon-admin/tests/unit/resources/test_filtered_export_handler.py::TestClientScriptsCarryFilteredExport::test_admin_js_forwards_scope_and_list_query`, `experimental/apps/oridecon-admin/tests/unit/services/test_export_center.py::TestCreateExport::test_creates_owned_job_and_redirects`, `experimental/apps/oridecon-admin/tests/unit/services/test_xlsx_export.py::TestEncodeRowsAsXlsx::test_roundtrip_headers_and_values`, `experimental/apps/oridecon-admin/tests/unit/services/test_xlsx_export.py::TestEncodeRowsAsXlsx::test_column_union_across_ragged_rows`, `experimental/apps/oridecon-admin/tests/unit/services/test_xlsx_export.py::TestEncodeRowsAsXlsx::test_explicit_fieldnames_control_order_and_subset`
- Output snippet:

```text
2026-09-03 20:22:11 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
ssssssssssssssssssssss.................................................. [  1%]
........................................................................ [  2%]
......................................................s................. [  3%]
.ss..................................................................... [  4%]
........................................................................ [  6%]
........................................................................ [  7%]
........................................................................ [  8%]
....................................................
```

### Package tests: experimental/apps/oridecon-builder

- Scope: `experimental/apps/oridecon-builder/tests`
- Command: `uv run pytest experimental/apps/oridecon-builder/tests -q -m not integration --cov=experimental/apps/oridecon.builder`
- Status: **FAIL**
- Exit code: `1`
- Duration: `409 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
Traceback (most recent call last):
  File ".venv/bin/pytest", line 10, in <module>
    sys.exit(_console_main())
             ~~~~~~~~~~~~~^^
  File ".venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 253, in _console_main
    code = _main(prog=_get_prog_name(sys.argv))
  File ".venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 223, in _main
    config = _prepareconfig(new_args, plugins, prog=prog)
  File "/ho
```

### Package tests: experimental/apps/oridecon-cli

- Scope: `experimental/apps/oridecon-cli/tests`
- Command: `uv run pytest experimental/apps/oridecon-cli/tests -q -m not integration --cov=experimental/apps/oridecon.cli`
- Status: **PASS**
- Exit code: `0`
- Duration: `22957 ms`
- Parsed summary: `894 passed, 1 skipped, 7 deselected, 6 warnings in 21.18s`
- Counters: passed=894, total=895, failed=0, skipped=1, warnings=6, coverage=81.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:23:25 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [  8%]
........................................................................ [ 16%]
........................................................................ [ 24%]
........................................................................ [ 32%]
........................................................................ [ 40%]
........................................................................ [ 48%]
........................................................................ [ 56%]
....................................................
```

### Package tests: experimental/apps/oridecon-ui

- Scope: `experimental/apps/oridecon-ui/tests`
- Command: `uv run pytest experimental/apps/oridecon-ui/tests -q -m not integration --cov=experimental/apps/oridecon.ui`
- Status: **PASS**
- Exit code: `0`
- Duration: `7228 ms`
- Parsed summary: `1444 passed, 78 skipped, 8 deselected, 4 warnings in 5.89s`
- Counters: passed=1444, total=1522, failed=0, skipped=78, warnings=4, coverage=77.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:23:48 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss [  4%]
........................................................................ [  9%]
........................................................................ [ 14%]
........................................................................ [ 18%]
........................................................................ [ 23%]
........................................................................ [ 28%]
........................................................................ [ 33%]
....................................................
```

### Package tests: experimental/multimedia/oridecon-multimedia-beat

- Scope: `experimental/multimedia/oridecon-multimedia-beat/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia-beat/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia.beat`
- Status: **PASS**
- Exit code: `0`
- Duration: `2659 ms`
- Parsed summary: `21 passed, 12 deselected, 4 warnings in 1.29s`
- Counters: passed=21, total=21, failed=0, skipped=0, warnings=4, coverage=74.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:23:55 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
.....................                                                    [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewriteWarning: Module already imported so cannot be rewritten; oridecon.testing.fixtures.core
    self.import_plugin(import_spec)

.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  /home/admin/Documents/AI/applications/lexigr
```

### Package tests: experimental/multimedia/oridecon-multimedia-image

- Scope: `experimental/multimedia/oridecon-multimedia-image/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia-image/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia.image`
- Status: **PASS**
- Exit code: `0`
- Duration: `2175 ms`
- Parsed summary: `54 passed, 4 warnings in 0.80s`
- Counters: passed=54, total=54, failed=0, skipped=0, warnings=4, coverage=92.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:23:57 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
......................................................                   [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewriteWarning: Module already imported so cannot be rewritten; oridecon.testing.fixtures.core
    self.import_plugin(import_spec)

.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  /home/admin/Documents/AI/applications/lexigr
```

### Package tests: experimental/multimedia/oridecon-multimedia-interpolate

- Scope: `experimental/multimedia/oridecon-multimedia-interpolate/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia-interpolate/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia.interpolate`
- Status: **PASS**
- Exit code: `0`
- Duration: `1865 ms`
- Parsed summary: `23 passed, 4 warnings in 0.50s`
- Counters: passed=23, total=23, failed=0, skipped=0, warnings=4, coverage=88.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:24:00 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
.......................                                                  [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewriteWarning: Module already imported so cannot be rewritten; oridecon.testing.fixtures.core
    self.import_plugin(import_spec)

.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  /home/admin/Documents/AI/applications/lexigr
```

### Package tests: experimental/multimedia/oridecon-multimedia-music

- Scope: `experimental/multimedia/oridecon-multimedia-music/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia-music/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia.music`
- Status: **PASS**
- Exit code: `0`
- Duration: `2010 ms`
- Parsed summary: `47 passed, 4 warnings in 0.68s`
- Counters: passed=47, total=47, failed=0, skipped=0, warnings=4, coverage=87.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:24:01 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
...............................................                          [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewriteWarning: Module already imported so cannot be rewritten; oridecon.testing.fixtures.core
    self.import_plugin(import_spec)

.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  /home/admin/Documents/AI/applications/lexigr
```

### Package tests: experimental/multimedia/oridecon-multimedia-tts

- Scope: `experimental/multimedia/oridecon-multimedia-tts/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia-tts/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia.tts`
- Status: **PASS**
- Exit code: `0`
- Duration: `2263 ms`
- Parsed summary: `63 passed, 4 warnings in 0.89s`
- Counters: passed=63, total=63, failed=0, skipped=0, warnings=4, coverage=79.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:24:03 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
...............................................................          [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewriteWarning: Module already imported so cannot be rewritten; oridecon.testing.fixtures.core
    self.import_plugin(import_spec)

.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  /home/admin/Documents/AI/applications/lexigr
```

### Package tests: experimental/multimedia/oridecon-multimedia-upscale

- Scope: `experimental/multimedia/oridecon-multimedia-upscale/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia-upscale/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia.upscale`
- Status: **PASS**
- Exit code: `0`
- Duration: `2066 ms`
- Parsed summary: `42 passed, 4 warnings in 0.70s`
- Counters: passed=42, total=42, failed=0, skipped=0, warnings=4, coverage=92.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:24:06 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
..........................................                               [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewriteWarning: Module already imported so cannot be rewritten; oridecon.testing.fixtures.core
    self.import_plugin(import_spec)

.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  /home/admin/Documents/AI/applications/lexigr
```

### Package tests: experimental/multimedia/oridecon-multimedia-video

- Scope: `experimental/multimedia/oridecon-multimedia-video/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia-video/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia.video`
- Status: **PASS**
- Exit code: `0`
- Duration: `5661 ms`
- Parsed summary: `182 passed, 4 warnings in 4.26s`
- Counters: passed=182, total=182, failed=0, skipped=0, warnings=4, coverage=87.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:24:08 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 39%]
........................................................................ [ 79%]
......................................                                   [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewriteWarning: Module already imported so cannot be rewritten; oridecon.testing.fix
```

### Package tests: experimental/multimedia/oridecon-multimedia

- Scope: `experimental/multimedia/oridecon-multimedia/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia`
- Status: **PASS**
- Exit code: `0`
- Duration: `4598 ms`
- Parsed summary: `89 passed, 5 warnings in 3.39s`
- Counters: passed=89, total=89, failed=0, skipped=0, warnings=5, coverage=58.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:24:13 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 80%]
.................                                                        [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewriteWarning: Module already imported so cannot be rewritten; oridecon.testing.fixtures.core
    self.import_plugin(import_spec)

.venv/lib/python3.13/site-packag
```

### Package tests: packages/oridecon-audit

- Scope: `packages/oridecon-audit/tests`
- Command: `uv run pytest packages/oridecon-audit/tests -q -m not integration --cov=packages/oridecon.audit`
- Status: **PASS**
- Exit code: `0`
- Duration: `2363 ms`
- Parsed summary: `293 passed, 17 deselected, 4 warnings in 1.18s`
- Counters: passed=293, total=293, failed=0, skipped=0, warnings=4, coverage=87.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:24:18 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 24%]
........................................................................ [ 49%]
........................................................................ [ 73%]
........................................................................ [ 98%]
.....                                                                    [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .ve
```

### Package tests: packages/oridecon-auth

- Scope: `packages/oridecon-auth/tests`
- Command: `uv run pytest packages/oridecon-auth/tests -q -m not integration --cov=packages/oridecon.auth`
- Status: **PASS**
- Exit code: `0`
- Duration: `29888 ms`
- Parsed summary: `632 passed, 4 skipped, 2 deselected, 15 warnings in 28.49s`
- Counters: passed=632, total=636, failed=0, skipped=4, warnings=15, coverage=69.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:24:20 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 11%]
........................................................................ [ 22%]
........................................................................ [ 33%]
........................................................................ [ 45%]
.....ssss............................................................... [ 56%]
........................................................................ [ 67%]
........................................................................ [ 79%]
....................................................
```

### Package tests: packages/oridecon-cache

- Scope: `packages/oridecon-cache/tests`
- Command: `uv run pytest packages/oridecon-cache/tests -q -m not integration --cov=packages/oridecon.cache`
- Status: **PASS**
- Exit code: `0`
- Duration: `10779 ms`
- Parsed summary: `874 passed, 13 skipped, 13 deselected, 6 warnings in 9.41s`
- Counters: passed=874, total=887, failed=0, skipped=13, warnings=6, coverage=81.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:24:50 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [  8%]
.................................................ss..................... [ 16%]
........................................................................ [ 24%]
..........................................................ssssssssss.... [ 32%]
........................................................................ [ 40%]
........................................................................ [ 48%]
........................................................................ [ 56%]
....................................................
```

### Package tests: packages/oridecon-events

- Scope: `packages/oridecon-events/tests`
- Command: `uv run pytest packages/oridecon-events/tests -q -m not integration --cov=packages/oridecon.events`
- Status: **PASS**
- Exit code: `0`
- Duration: `11985 ms`
- Parsed summary: `1002 passed, 15 skipped, 11 deselected, 4 warnings in 10.61s`
- Counters: passed=1002, total=1017, failed=0, skipped=15, warnings=4, coverage=64.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:25:01 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
...s.................................................................... [  7%]
........................................................................ [ 14%]
........................................................................ [ 21%]
........................................................................ [ 28%]
........................................................................ [ 35%]
........................................................................ [ 42%]
........................................................................ [ 49%]
....................................................
```

### Package tests: packages/oridecon-features

- Scope: `packages/oridecon-features/tests`
- Command: `uv run pytest packages/oridecon-features/tests -q -m not integration --cov=packages/oridecon.features`
- Status: **PASS**
- Exit code: `0`
- Duration: `3493 ms`
- Parsed summary: `253 passed, 14 deselected, 17 warnings in 2.27s`
- Counters: passed=253, total=253, failed=0, skipped=0, warnings=17, coverage=84.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:25:13 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 28%]
........................................................................ [ 56%]
........................................................................ [ 85%]
.....................................                                    [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewr
```

### Package tests: packages/oridecon-graph

- Scope: `packages/oridecon-graph/tests`
- Command: `uv run pytest packages/oridecon-graph/tests -q -m not integration --cov=packages/oridecon.graph`
- Status: **PASS**
- Exit code: `0`
- Duration: `2202 ms`
- Parsed summary: `263 passed, 1 skipped, 7 deselected, 4 warnings in 1.04s`
- Counters: passed=263, total=264, failed=0, skipped=1, warnings=4, coverage=80.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:25:17 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 27%]
..................s..................................................... [ 54%]
........................................................................ [ 81%]
................................................                         [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewr
```

### Package tests: packages/oridecon-graphql

- Scope: `packages/oridecon-graphql/tests`
- Command: `uv run pytest packages/oridecon-graphql/tests -q -m not integration --cov=packages/oridecon.graphql`
- Status: **PASS**
- Exit code: `0`
- Duration: `5837 ms`
- Parsed summary: `520 passed, 2 skipped, 11 deselected, 23 warnings in 4.32s`
- Counters: passed=520, total=522, failed=0, skipped=2, warnings=23, coverage=76.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:25:19 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
s....................................................................... [ 13%]
........................................................................ [ 27%]
.................s...................................................... [ 41%]
........................................................................ [ 55%]
........................................................................ [ 68%]
........................................................................ [ 82%]
........................................................................ [ 96%]
..................                                  
```

### Package tests: packages/oridecon-http

- Scope: `packages/oridecon-http/tests`
- Command: `uv run pytest packages/oridecon-http/tests -q -m not integration --cov=packages/oridecon.http`
- Status: **PASS**
- Exit code: `0`
- Duration: `2772 ms`
- Parsed summary: `457 passed, 9 deselected, 8 warnings in 1.53s`
- Counters: passed=457, total=457, failed=0, skipped=0, warnings=8, coverage=85.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:25:25 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 15%]
........................................................................ [ 31%]
........................................................................ [ 47%]
........................................................................ [ 63%]
........................................................................ [ 78%]
........................................................................ [ 94%]
.........................                                                [100%]
=============================== warnings summary ===
```

### Package tests: packages/oridecon-monitor

- Scope: `packages/oridecon-monitor/tests`
- Command: `uv run pytest packages/oridecon-monitor/tests -q -m not integration --cov=packages/oridecon.monitor`
- Status: **FAIL**
- Exit code: `1`
- Duration: `8173 ms`
- Parsed summary: `317 passed, 21 skipped, 4 deselected, 4 warnings in 6.97s`
- Counters: passed=317, total=338, failed=0, skipped=21, warnings=4, coverage=78.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:25:27 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
.s..........................ssssss...................................... [ 21%]
...s................................................sss.s............... [ 43%]
........................................................................ [ 64%]
...........................................................ssss......... [ 86%]
.............................................
ERROR: Coverage failure: total of 78 is less than fail-under=80
                                                                         [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/
```

### Package tests: packages/oridecon-nosql

- Scope: `packages/oridecon-nosql/tests`
- Command: `uv run pytest packages/oridecon-nosql/tests -q -m not integration --cov=packages/oridecon.nosql`
- Status: **PASS**
- Exit code: `0`
- Duration: `3345 ms`
- Parsed summary: `537 passed, 10 deselected, 4 warnings in 2.12s`
- Counters: passed=537, total=537, failed=0, skipped=0, warnings=4, coverage=91.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:25:36 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 13%]
........................................................................ [ 26%]
........................................................................ [ 40%]
........................................................................ [ 53%]
........................................................................ [ 67%]
........................................................................ [ 80%]
........................................................................ [ 93%]
.................................                   
```

### Package tests: packages/oridecon-notification

- Scope: `packages/oridecon-notification/tests`
- Command: `uv run pytest packages/oridecon-notification/tests -q -m not integration --cov=packages/oridecon.notification`
- Status: **PASS**
- Exit code: `0`
- Duration: `5854 ms`
- Parsed summary: `296 passed, 8 deselected, 7 warnings in 4.38s`
- Counters: passed=296, total=296, failed=0, skipped=0, warnings=7, coverage=85.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:25:39 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 24%]
........................................................................ [ 48%]
........................................................................ [ 72%]
........................................................................ [ 97%]
........                                                                 [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .ve
```

### Package tests: packages/oridecon-queue

- Scope: `packages/oridecon-queue/tests`
- Command: `uv run pytest packages/oridecon-queue/tests -q -m not integration --cov=packages/oridecon.queue`
- Status: **PASS**
- Exit code: `0`
- Duration: `4442 ms`
- Parsed summary: `235 passed, 20 deselected, 4 warnings in 3.22s`
- Counters: passed=235, total=235, failed=0, skipped=0, warnings=4, coverage=85.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:25:45 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 30%]
........................................................................ [ 61%]
........................................................................ [ 91%]
...................                                                      [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewr
```

### Package tests: packages/oridecon-resilience

- Scope: `packages/oridecon-resilience/tests`
- Command: `uv run pytest packages/oridecon-resilience/tests -q -m not integration --cov=packages/oridecon.resilience`
- Status: **PASS**
- Exit code: `0`
- Duration: `20753 ms`
- Parsed summary: `311 passed, 23 deselected, 4 warnings in 19.57s`
- Counters: passed=311, total=311, failed=0, skipped=0, warnings=4, coverage=75.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:25:49 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 23%]
........................................................................ [ 46%]
........................................................................ [ 69%]
........................................................................ [ 92%]
.......................                                                  [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .ve
```

### Package tests: packages/oridecon-search

- Scope: `packages/oridecon-search/tests`
- Command: `uv run pytest packages/oridecon-search/tests -q -m not integration --cov=packages/oridecon.search`
- Status: **PASS**
- Exit code: `0`
- Duration: `4154 ms`
- Parsed summary: `813 passed, 5 skipped, 15 deselected, 4 warnings in 2.89s`
- Counters: passed=813, total=818, failed=0, skipped=5, warnings=4, coverage=66.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:26:10 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [  8%]
........................................................................ [ 17%]
........................................................................ [ 26%]
........................................................................ [ 35%]
........................................................................ [ 44%]
........................................................................ [ 53%]
........................................................................ [ 61%]
....................................................
```

### Package tests: packages/oridecon-secrets

- Scope: `packages/oridecon-secrets/tests`
- Command: `uv run pytest packages/oridecon-secrets/tests -q -m not integration --cov=packages/oridecon.secrets`
- Status: **PASS**
- Exit code: `0`
- Duration: `1640 ms`
- Parsed summary: `134 passed, 4 warnings in 0.48s`
- Counters: passed=134, total=134, failed=0, skipped=0, warnings=4, coverage=59.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:26:14 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 53%]
..............................................................           [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885: PytestAssertRewriteWarning: Module already imported so cannot be rewritten; oridecon.testing.fixtures.core
    self.import_plugin(import_spec)

.venv/lib/python3.13/site-packag
```

### Package tests: packages/oridecon-sql

- Scope: `packages/oridecon-sql/tests`
- Command: `uv run pytest packages/oridecon-sql/tests -q -m not integration --cov=packages/oridecon.sql`
- Status: **PASS**
- Exit code: `0`
- Duration: `12372 ms`
- Parsed summary: `1351 passed, 91 skipped, 9 deselected, 10 warnings in 10.79s`
- Counters: passed=1351, total=1442, failed=0, skipped=91, warnings=10, coverage=61.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:26:16 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................s............................... [  4%]
........................................................................ [  9%]
........................................................................ [ 14%]
..........................................ss............................ [ 19%]
........................................................................ [ 24%]
........................................................................ [ 29%]
........................................................................ [ 34%]
...........................................s........
```

### Package tests: packages/oridecon-storage

- Scope: `packages/oridecon-storage/tests`
- Command: `uv run pytest packages/oridecon-storage/tests -q -m not integration --cov=packages/oridecon.storage`
- Status: **PASS**
- Exit code: `0`
- Duration: `6647 ms`
- Parsed summary: `463 passed, 3 skipped, 22 deselected, 4 warnings in 5.45s`
- Counters: passed=463, total=466, failed=0, skipped=3, warnings=4, coverage=64.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:26:28 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 15%]
........................................................................ [ 30%]
............................................s........................... [ 46%]
........................................................................ [ 61%]
........................................................................ [ 77%]
........................................................................ [ 92%]
................................s                                        [100%]
=============================== warnings summary ===
```

### Package tests: packages/oridecon-tasks

- Scope: `packages/oridecon-tasks/tests`
- Command: `uv run pytest packages/oridecon-tasks/tests -q -m not integration --cov=packages/oridecon.tasks`
- Status: **PASS**
- Exit code: `0`
- Duration: `11821 ms`
- Parsed summary: `537 passed, 16 skipped, 9 deselected, 4 warnings in 10.51s`
- Counters: passed=537, total=553, failed=0, skipped=16, warnings=4, coverage=76.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:26:35 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 13%]
........................................................................ [ 26%]
........................................................................ [ 39%]
.........sssss.......................................................... [ 52%]
......................................................sssssssss......... [ 65%]
........................................................................ [ 78%]
...........................................ss........................... [ 91%]
.................................................   
```

### Package tests: packages/oridecon-tenancy

- Scope: `packages/oridecon-tenancy/tests`
- Command: `uv run pytest packages/oridecon-tenancy/tests -q -m not integration --cov=packages/oridecon.tenancy`
- Status: **PASS**
- Exit code: `0`
- Duration: `2927 ms`
- Parsed summary: `362 passed, 4 deselected, 4 warnings in 1.72s`
- Counters: passed=362, total=362, failed=0, skipped=0, warnings=4, coverage=85.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:26:47 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 19%]
........................................................................ [ 39%]
........................................................................ [ 59%]
........................................................................ [ 79%]
........................................................................ [ 99%]
..                                                                       [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/_
```

### Package tests: packages/oridecon-testing

- Scope: `packages/oridecon-testing/tests`
- Command: `uv run pytest packages/oridecon-testing/tests -q -m not integration --cov=packages/oridecon.testing`
- Status: **PASS**
- Exit code: `0`
- Duration: `8133 ms`
- Parsed summary: `443 passed, 15 skipped, 13 deselected, 2 warnings in 6.90s`
- Counters: passed=443, total=458, failed=0, skipped=15, warnings=2, coverage=17.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:26:49 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
.................s...................................................... [ 15%]
........................................................................ [ 31%]
........................................................................ [ 47%]
........................................................................ [ 62%]
................ssssssssssssss.......................................... [ 78%]
........................................................................ [ 94%]
..........................                                               [100%]
=============================== warnings summary ===
```

### Package tests: packages/oridecon-vector

- Scope: `packages/oridecon-vector/tests`
- Command: `uv run pytest packages/oridecon-vector/tests -q -m not integration --cov=packages/oridecon.vector`
- Status: **PASS**
- Exit code: `0`
- Duration: `4134 ms`
- Parsed summary: `533 passed, 20 deselected, 4 warnings in 2.85s`
- Counters: passed=533, total=533, failed=0, skipped=0, warnings=4, coverage=78.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:26:58 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 13%]
........................................................................ [ 27%]
........................................................................ [ 40%]
........................................................................ [ 54%]
........................................................................ [ 67%]
........................................................................ [ 81%]
........................................................................ [ 94%]
.............................                       
```

### Package tests: packages/oridecon-web

- Scope: `packages/oridecon-web/tests`
- Command: `uv run pytest packages/oridecon-web/tests -q -m not integration --cov=packages/oridecon.web`
- Status: **PASS**
- Exit code: `0`
- Duration: `14794 ms`
- Parsed summary: `1421 passed, 7 skipped, 7 deselected, 6 warnings in 13.28s`
- Counters: passed=1421, total=1428, failed=0, skipped=7, warnings=6, coverage=81.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:27:02 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
sss..................................................................... [  5%]
........................................................................ [ 10%]
........................................................................ [ 15%]
........................................................................ [ 20%]
.......s................................................................ [ 25%]
........................................................................ [ 30%]
............................................s........................... [ 35%]
....................................................
```

### Package tests: packages/oridecon-webhook

- Scope: `packages/oridecon-webhook/tests`
- Command: `uv run pytest packages/oridecon-webhook/tests -q -m not integration --cov=packages/oridecon.webhook`
- Status: **PASS**
- Exit code: `0`
- Duration: `2760 ms`
- Parsed summary: `336 passed, 4 warnings in 1.51s`
- Counters: passed=336, total=336, failed=0, skipped=0, warnings=4, coverage=90.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:27:17 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 21%]
........................................................................ [ 42%]
........................................................................ [ 64%]
........................................................................ [ 85%]
................................................                         [100%]
=============================== warnings summary ===============================
.venv/lib/python3.13/site-packages/_pytest/config/__init__.py:885
  .ve
```

### Package tests: packages/oridecon-workflow

- Scope: `packages/oridecon-workflow/tests`
- Command: `uv run pytest packages/oridecon-workflow/tests -q -m not integration --cov=packages/oridecon.workflow`
- Status: **PASS**
- Exit code: `0`
- Duration: `13694 ms`
- Parsed summary: `559 passed, 23 deselected, 4 warnings in 12.47s`
- Counters: passed=559, total=559, failed=0, skipped=0, warnings=4, coverage=73.0%
- Example failures: none
- Output snippet:

```text
2026-09-03 20:27:19 [debug    ] module_decorated               _logger_name=oridecon.di.module.decorator controllers=0 exports=0 imports=0 is_global=False module=TestingModule providers=0
........................................................................ [ 12%]
........................................................................ [ 25%]
........................................................................ [ 38%]
........................................................................ [ 51%]
........................................................................ [ 64%]
........................................................................ [ 77%]
........................................................................ [ 90%]
....................................................
```

