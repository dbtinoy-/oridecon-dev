# AUDIT_TESTS.md — Oridecon Framework Targeted Test Execution Audit

> **Source**: Live pytest execution evidence for targeted scopes, with `tests/` directory scanning as supporting context.

---

## Summary

- Total passed tests: 0
- Total failed tests: 1832
- Total skipped tests: 47
- Total warnings: 2
- Aggregate code coverage: 2.00%

- Representative commands run: 55
- Commands passing: 0
- Commands failing: 55
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
| Package tests: core/oridecon-contracts | 0.0% | 0/286 | 286 | 0 | 0 | 2 | 6025 ms |
| Package tests: core/oridecon | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 687 ms |
| Package tests: experimental/ai/oridecon-ai-agents | 0.0% | 0/72 | 72 | 0 | 0 | 2 | 2183 ms |
| Package tests: experimental/ai/oridecon-ai-evaluation | 0.0% | 0/44 | 44 | 0 | 0 | 2 | 1374 ms |
| Package tests: experimental/ai/oridecon-ai-feedback | 0.0% | 0/48 | 48 | 0 | 0 | 2 | 1565 ms |
| Package tests: experimental/ai/oridecon-ai-governance | 0.0% | 0/71 | 68 | 3 | 0 | 2 | 2936 ms |
| Package tests: experimental/ai/oridecon-ai-guard | 0.0% | 0/16 | 16 | 0 | 0 | 2 | 1107 ms |
| Package tests: experimental/ai/oridecon-ai-llm | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 692 ms |
| Package tests: experimental/ai/oridecon-ai-mcp | 0.0% | 0/40 | 40 | 0 | 0 | 2 | 2035 ms |
| Package tests: experimental/ai/oridecon-ai-memory | 0.0% | 0/4 | 4 | 0 | 0 | 2 | 891 ms |
| Package tests: experimental/ai/oridecon-ai-observability | 0.0% | 0/50 | 50 | 0 | 0 | 2 | 1527 ms |
| Package tests: experimental/ai/oridecon-ai-prompt | 0.0% | 0/44 | 44 | 0 | 0 | 2 | 1596 ms |
| Package tests: experimental/ai/oridecon-ai-rag | 0.0% | 0/4 | 4 | 0 | 0 | 2 | 902 ms |
| Package tests: experimental/ai/oridecon-ai-relay-gateway | 0.0% | 0/106 | 106 | 0 | 1 | 2 | 3853 ms |
| Package tests: experimental/ai/oridecon-ai-relay | 0.0% | 0/4 | 4 | 0 | 0 | 2 | 950 ms |
| Package tests: experimental/ai/oridecon-ai-session | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 688 ms |
| Package tests: experimental/ai/oridecon-ai-skills | 0.0% | 0/12 | 12 | 0 | 0 | 2 | 1047 ms |
| Package tests: experimental/ai/oridecon-ai-workers | 0.0% | 0/48 | 48 | 0 | 0 | 2 | 1841 ms |
| Package tests: experimental/ai/oridecon-ai | 0.0% | 0/82 | 38 | 44 | 0 | 2 | 2976 ms |
| Package tests: experimental/apps/oridecon-admin | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 687 ms |
| Package tests: experimental/apps/oridecon-builder | 0.0% | 0/0 | 0 | 0 | 0 | 5 | 732 ms |
| Package tests: experimental/apps/oridecon-cli | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 752 ms |
| Package tests: experimental/apps/oridecon-ui | 0.0% | 0/140 | 140 | 0 | 0 | 2 | 4012 ms |
| Package tests: experimental/multimedia/oridecon-multimedia-beat | 0.0% | 0/12 | 12 | 0 | 0 | 2 | 1735 ms |
| Package tests: experimental/multimedia/oridecon-multimedia-image | 0.0% | 0/16 | 16 | 0 | 0 | 2 | 1494 ms |
| Package tests: experimental/multimedia/oridecon-multimedia-interpolate | 0.0% | 0/10 | 10 | 0 | 0 | 2 | 925 ms |
| Package tests: experimental/multimedia/oridecon-multimedia-music | 0.0% | 0/14 | 14 | 0 | 0 | 2 | 1455 ms |
| Package tests: experimental/multimedia/oridecon-multimedia-tts | 0.0% | 0/22 | 22 | 0 | 0 | 2 | 1562 ms |
| Package tests: experimental/multimedia/oridecon-multimedia-upscale | 0.0% | 0/14 | 14 | 0 | 0 | 2 | 1496 ms |
| Package tests: experimental/multimedia/oridecon-multimedia-video | 0.0% | 0/36 | 36 | 0 | 0 | 2 | 1969 ms |
| Package tests: experimental/multimedia/oridecon-multimedia | 0.0% | 0/44 | 44 | 0 | 0 | 2 | 1304 ms |
| Package tests: packages/oridecon-audit | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 692 ms |
| Package tests: packages/oridecon-auth | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 690 ms |
| Package tests: packages/oridecon-cache | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 692 ms |
| Package tests: packages/oridecon-events | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 695 ms |
| Package tests: packages/oridecon-features | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 690 ms |
| Package tests: packages/oridecon-graph | 0.0% | 0/40 | 40 | 0 | 0 | 2 | 1551 ms |
| Package tests: packages/oridecon-graphql | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 1160 ms |
| Package tests: packages/oridecon-http | 0.0% | 0/54 | 54 | 0 | 0 | 2 | 1969 ms |
| Package tests: packages/oridecon-monitor | 0.0% | 0/102 | 102 | 0 | 0 | 2 | 2615 ms |
| Package tests: packages/oridecon-nosql | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 695 ms |
| Package tests: packages/oridecon-notification | 0.0% | 0/68 | 68 | 0 | 1 | 2 | 2415 ms |
| Package tests: packages/oridecon-queue | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 688 ms |
| Package tests: packages/oridecon-resilience | 0.0% | 0/66 | 66 | 0 | 0 | 2 | 1748 ms |
| Package tests: packages/oridecon-search | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 687 ms |
| Package tests: packages/oridecon-secrets | 0.0% | 0/24 | 24 | 0 | 0 | 2 | 1145 ms |
| Package tests: packages/oridecon-sql | 2.0% | 0/280 | 280 | 0 | 0 | 2 | 11196 ms |
| Package tests: packages/oridecon-storage | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 694 ms |
| Package tests: packages/oridecon-tasks | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 692 ms |
| Package tests: packages/oridecon-tenancy | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 689 ms |
| Package tests: packages/oridecon-testing | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 683 ms |
| Package tests: packages/oridecon-vector | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 685 ms |
| Package tests: packages/oridecon-web | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 1134 ms |
| Package tests: packages/oridecon-webhook | 0.0% | 0/0 | 0 | 0 | 0 | 4 | 683 ms |
| Package tests: packages/oridecon-workflow | 0.0% | 0/6 | 6 | 0 | 0 | 2 | 934 ms |

### Execution Scope Notes

- `framework-core`: real test execution for `oridecon/tests`.
- `package`: real test execution for `<package>/tests` across every discovered Oridecon package with tests.
### Package tests: core/oridecon-contracts

- Scope: `core/oridecon-contracts/tests`
- Command: `uv run pytest core/oridecon-contracts/tests -q -m not integration --cov=core/oridecon.contracts`
- Status: **FAIL**
- Exit code: `2`
- Duration: `6025 ms`
- Parsed summary: `143 errors in 5.12s`
- Counters: passed=0, total=286, failed=286, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
___________ ERROR collecting tests/admin/test_principal_protocol.py ____________
ImportError while importing test module 'core/oridecon-contracts/tests/admin/test_principal_protocol.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
core/oridecon-contracts/tests/admin/test_principal_protocol.py:5: in <module>
    from oridecon.contracts.admin import AdminPrincipal, AdminPrincipalProviderProtocol
...
```

### Package tests: core/oridecon

- Scope: `core/oridecon/tests`
- Command: `uv run pytest core/oridecon/tests -q -m not integration --cov=core/oridecon`
- Status: **FAIL**
- Exit code: `4`
- Duration: `687 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'core/oridecon/tests/conftest.py'.
core/oridecon/tests/conftest.py:12: in <module>
    from oridecon.app import Application
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: experimental/ai/oridecon-ai-agents

- Scope: `experimental/ai/oridecon-ai-agents/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-agents/tests -q -m not integration --cov=experimental/ai/oridecon.ai.agents`
- Status: **FAIL**
- Exit code: `2`
- Duration: `2183 ms`
- Parsed summary: `36 errors in 1.45s`
- Counters: passed=0, total=72, failed=72, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
_______________ ERROR collecting tests/crew/test_crew_runner.py ________________
ImportError while importing test module 'experimental/ai/oridecon-ai-agents/tests/crew/test_crew_runner.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/ai/oridecon-ai-agents/tests/crew/test_crew_runner.py:9: in <module>
    from oridecon.ai.agents.crew import Crew, CrewBuilder, CrewTask, Process
...
```

### Package tests: experimental/ai/oridecon-ai-evaluation

- Scope: `experimental/ai/oridecon-ai-evaluation/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-evaluation/tests -q -m not integration --cov=experimental/ai/oridecon.ai.evaluation`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1374 ms`
- Parsed summary: `22 errors in 0.66s`
- Counters: passed=0, total=44, failed=44, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
________ ERROR collecting tests/integration/test_config_integration.py _________
ImportError while importing test module 'experimental/ai/oridecon-ai-evaluation/tests/integration/test_config_integration.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/ai/oridecon-ai-evaluation/tests/integration/test_config_integration.py:4: in <module>
    from oridecon.ai.evaluation.config import EvaluationConfig
...
```

### Package tests: experimental/ai/oridecon-ai-feedback

- Scope: `experimental/ai/oridecon-ai-feedback/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-feedback/tests -q -m not integration --cov=experimental/ai/oridecon.ai.feedback`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1565 ms`
- Parsed summary: `24 errors in 0.85s`
- Counters: passed=0, total=48, failed=48, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
___________ ERROR collecting tests/unit/di/test_config_alignment.py ____________
ImportError while importing test module 'experimental/ai/oridecon-ai-feedback/tests/unit/di/test_config_alignment.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/ai/oridecon-ai-feedback/tests/unit/di/test_config_alignment.py:7: in <module>
    from oridecon.ai.feedback.config import FeedbackConfig
...
```

### Package tests: experimental/ai/oridecon-ai-governance

- Scope: `experimental/ai/oridecon-ai-governance/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-governance/tests -q -m not integration --cov=experimental/ai/oridecon.ai.governance`
- Status: **FAIL**
- Exit code: `2`
- Duration: `2936 ms`
- Parsed summary: `3 skipped, 34 errors in 2.19s`
- Counters: passed=0, total=71, failed=68, skipped=3, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
_________ ERROR collecting tests/integration/test_admin_contributor.py _________
ImportError while importing test module 'experimental/ai/oridecon-ai-governance/tests/integration/test_admin_contributor.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/ai/oridecon-ai-governance/tests/integration/test_admin_contributor.py:19: in <module>
    from oridecon.ai.governance.admin import (
...
```

### Package tests: experimental/ai/oridecon-ai-guard

- Scope: `experimental/ai/oridecon-ai-guard/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-guard/tests -q -m not integration --cov=experimental/ai/oridecon.ai.guard`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1107 ms`
- Parsed summary: `8 errors in 0.39s`
- Counters: passed=0, total=16, failed=16, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
__________ ERROR collecting tests/integration/test_guard_lifecycle.py __________
ImportError while importing test module 'experimental/ai/oridecon-ai-guard/tests/integration/test_guard_lifecycle.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/ai/oridecon-ai-guard/tests/integration/test_guard_lifecycle.py:7: in <module>
    from oridecon.ai.guard.config import GuardConfig
...
```

### Package tests: experimental/ai/oridecon-ai-llm

- Scope: `experimental/ai/oridecon-ai-llm/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-llm/tests -q -m not integration --cov=experimental/ai/oridecon.ai.llm`
- Status: **FAIL**
- Exit code: `4`
- Duration: `692 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'experimental/ai/oridecon-ai-llm/tests/conftest.py'.
experimental/ai/oridecon-ai-llm/tests/conftest.py:14: in <module>
    from oridecon.ai.llm.registry.core import ProviderRegistry
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: experimental/ai/oridecon-ai-mcp

- Scope: `experimental/ai/oridecon-ai-mcp/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-mcp/tests -q -m not integration --cov=experimental/ai/oridecon.ai.mcp`
- Status: **FAIL**
- Exit code: `2`
- Duration: `2035 ms`
- Parsed summary: `20 errors in 1.31s`
- Counters: passed=0, total=40, failed=40, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
___________ ERROR collecting tests/integration/test_mcp_lifecycle.py ___________
ImportError while importing test module 'experimental/ai/oridecon-ai-mcp/tests/integration/test_mcp_lifecycle.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/ai/oridecon-ai-mcp/tests/integration/test_mcp_lifecycle.py:7: in <module>
    from oridecon.ai.mcp.config import MCPConfig
...
```

### Package tests: experimental/ai/oridecon-ai-memory

- Scope: `experimental/ai/oridecon-ai-memory/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-memory/tests -q -m not integration --cov=experimental/ai/oridecon.ai.memory`
- Status: **FAIL**
- Exit code: `2`
- Duration: `891 ms`
- Parsed summary: `2 errors in 0.18s`
- Counters: passed=0, total=4, failed=4, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
_________ ERROR collecting tests/integration/test_memory_lifecycle.py __________
ImportError while importing test module 'experimental/ai/oridecon-ai-memory/tests/integration/test_memory_lifecycle.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/ai/oridecon-ai-memory/tests/integration/test_memory_lifecycle.py:7: in <module>
    from oridecon.ai.memory.config import MemoryConfig
...
```

### Package tests: experimental/ai/oridecon-ai-observability

- Scope: `experimental/ai/oridecon-ai-observability/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-observability/tests -q -m not integration --cov=experimental/ai/oridecon.ai.observability`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1527 ms`
- Parsed summary: `25 errors in 0.81s`
- Counters: passed=0, total=50, failed=50, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
______ ERROR collecting tests/integration/test_observability_lifecycle.py ______
ImportError while importing test module 'experimental/ai/oridecon-ai-observability/tests/integration/test_observability_lifecycle.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/ai/oridecon-ai-observability/tests/integration/test_observability_lifecycle.py:7: in <module>
    from oridecon.ai.observability.config import ObservabilityConfig
...
```

### Package tests: experimental/ai/oridecon-ai-prompt

- Scope: `experimental/ai/oridecon-ai-prompt/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-prompt/tests -q -m not integration --cov=experimental/ai/oridecon.ai.prompt`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1596 ms`
- Parsed summary: `22 errors in 0.88s`
- Counters: passed=0, total=44, failed=44, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
___________ ERROR collecting tests/unit/di/test_config_alignment.py ____________
ImportError while importing test module 'experimental/ai/oridecon-ai-prompt/tests/unit/di/test_config_alignment.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/ai/oridecon-ai-prompt/tests/unit/di/test_config_alignment.py:7: in <module>
    from oridecon.ai.prompt.config import PromptConfig
...
```

### Package tests: experimental/ai/oridecon-ai-rag

- Scope: `experimental/ai/oridecon-ai-rag/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-rag/tests -q -m not integration --cov=experimental/ai/oridecon.ai.rag`
- Status: **FAIL**
- Exit code: `2`
- Duration: `902 ms`
- Parsed summary: `2 errors in 0.18s`
- Counters: passed=0, total=4, failed=4, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
___________ ERROR collecting tests/integration/test_rag_lifecycle.py ___________
ImportError while importing test module 'experimental/ai/oridecon-ai-rag/tests/integration/test_rag_lifecycle.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/ai/oridecon-ai-rag/tests/integration/test_rag_lifecycle.py:7: in <module>
    from oridecon.ai.rag.config import RAGConfig
...
```

### Package tests: experimental/ai/oridecon-ai-relay-gateway

- Scope: `experimental/ai/oridecon-ai-relay-gateway/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-relay-gateway/tests -q -m not integration --cov=experimental/ai/oridecon.ai.relay.gateway`
- Status: **FAIL**
- Exit code: `2`
- Duration: `3853 ms`
- Parsed summary: `1 warning, 53 errors in 3.11s`
- Counters: passed=0, total=106, failed=106, skipped=0, warnings=1, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
_ ERROR collecting tests/integration/test_admin_contributor_actions_health.py __
ImportError while importing test module 'experimental/ai/oridecon-ai-relay-gateway/tests/integration/test_admin_contributor_actions_health.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/ai/oridecon-ai-relay-gateway/tests/integration/test_admin_contributor_actions_health.py:11: in <module>
    from oridecon.ai.relay.gateway.admin.contributor i
```

### Package tests: experimental/ai/oridecon-ai-relay

- Scope: `experimental/ai/oridecon-ai-relay/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-relay/tests -q -m not integration --cov=experimental/ai/oridecon.ai.relay`
- Status: **FAIL**
- Exit code: `2`
- Duration: `950 ms`
- Parsed summary: `2 errors in 0.24s`
- Counters: passed=0, total=4, failed=4, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
___________________ ERROR collecting tests/integration/relay ___________________
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
...
```

### Package tests: experimental/ai/oridecon-ai-session

- Scope: `experimental/ai/oridecon-ai-session/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-session/tests -q -m not integration --cov=experimental/ai/oridecon.ai.session`
- Status: **FAIL**
- Exit code: `4`
- Duration: `688 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'experimental/ai/oridecon-ai-session/tests/conftest.py'.
experimental/ai/oridecon-ai-session/tests/conftest.py:10: in <module>
    from oridecon.contracts.ai.session import SessionState, SessionStatus, SessionTurn
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: experimental/ai/oridecon-ai-skills

- Scope: `experimental/ai/oridecon-ai-skills/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-skills/tests -q -m not integration --cov=experimental/ai/oridecon.ai.skills`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1047 ms`
- Parsed summary: `6 errors in 0.33s`
- Counters: passed=0, total=12, failed=12, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
___________________ ERROR collecting tests/test_toolkits.py ____________________
ImportError while importing test module 'experimental/ai/oridecon-ai-skills/tests/test_toolkits.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/ai/oridecon-ai-skills/tests/test_toolkits.py:9: in <module>
    from oridecon.contracts.ai.skills import (
...
```

### Package tests: experimental/ai/oridecon-ai-workers

- Scope: `experimental/ai/oridecon-ai-workers/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai-workers/tests -q -m not integration --cov=experimental/ai/oridecon.ai.workers`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1841 ms`
- Parsed summary: `24 errors in 1.13s`
- Counters: passed=0, total=48, failed=48, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
_________ ERROR collecting tests/integration/test_worker_lifecycle.py __________
ImportError while importing test module 'experimental/ai/oridecon-ai-workers/tests/integration/test_worker_lifecycle.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/ai/oridecon-ai-workers/tests/integration/test_worker_lifecycle.py:7: in <module>
    from oridecon.ai.workers.config import WorkersConfig
...
```

### Package tests: experimental/ai/oridecon-ai

- Scope: `experimental/ai/oridecon-ai/tests`
- Command: `uv run pytest experimental/ai/oridecon-ai/tests -q -m not integration --cov=experimental/ai/oridecon.ai`
- Status: **FAIL**
- Exit code: `2`
- Duration: `2976 ms`
- Parsed summary: `44 skipped, 19 errors in 2.23s`
- Counters: passed=0, total=82, failed=38, skipped=44, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
___________ ERROR collecting tests/integration/test_ai_lifecycle.py ____________
ImportError while importing test module 'experimental/ai/oridecon-ai/tests/integration/test_ai_lifecycle.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/ai/oridecon-ai/tests/integration/test_ai_lifecycle.py:8: in <module>
    from oridecon.ai.config import AIConfig
...
```

### Package tests: experimental/apps/oridecon-admin

- Scope: `experimental/apps/oridecon-admin/tests`
- Command: `uv run pytest experimental/apps/oridecon-admin/tests -q -m not integration --cov=experimental/apps/oridecon.admin`
- Status: **FAIL**
- Exit code: `4`
- Duration: `687 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'experimental/apps/oridecon-admin/tests/conftest.py'.
experimental/apps/oridecon-admin/tests/conftest.py:27: in <module>
    from oridecon.testing import TestEnvironment
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: experimental/apps/oridecon-builder

- Scope: `experimental/apps/oridecon-builder/tests`
- Command: `uv run pytest experimental/apps/oridecon-builder/tests -q -m not integration --cov=experimental/apps/oridecon.builder`
- Status: **FAIL**
- Exit code: `5`
- Duration: `732 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.



---------- coverage: platform linux, python 3.12.3-final-0 -----------

no tests ran in 0.02s
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
/home/admin/.local/lib/python3.12/site-packages/pytest_asyncio/plugin.py:247: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid
```

### Package tests: experimental/apps/oridecon-cli

- Scope: `experimental/apps/oridecon-cli/tests`
- Command: `uv run pytest experimental/apps/oridecon-cli/tests -q -m not integration --cov=experimental/apps/oridecon.cli`
- Status: **FAIL**
- Exit code: `4`
- Duration: `752 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'experimental/apps/oridecon-cli/tests/conftest.py'.
experimental/apps/oridecon-cli/tests/conftest.py:15: in <module>
    from oridecon.cli.contributors.core import CoreCliContributor
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: experimental/apps/oridecon-ui

- Scope: `experimental/apps/oridecon-ui/tests`
- Command: `uv run pytest experimental/apps/oridecon-ui/tests -q -m not integration --cov=experimental/apps/oridecon.ui`
- Status: **FAIL**
- Exit code: `2`
- Duration: `4012 ms`
- Parsed summary: `70 errors in 3.28s`
- Counters: passed=0, total=140, failed=140, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
___________ ERROR collecting tests/integration/test_ui_lifecycle.py ____________
ImportError while importing test module 'experimental/apps/oridecon-ui/tests/integration/test_ui_lifecycle.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/apps/oridecon-ui/tests/integration/test_ui_lifecycle.py:7: in <module>
    from oridecon.ui.config import UIConfig
...
```

### Package tests: experimental/multimedia/oridecon-multimedia-beat

- Scope: `experimental/multimedia/oridecon-multimedia-beat/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia-beat/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia.beat`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1735 ms`
- Parsed summary: `6 errors in 0.97s`
- Counters: passed=0, total=12, failed=12, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
_______________ ERROR collecting tests/unit/di/test_provider.py ________________
ImportError while importing test module 'experimental/multimedia/oridecon-multimedia-beat/tests/unit/di/test_provider.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/multimedia/oridecon-multimedia-beat/tests/unit/di/test_provider.py:5: in <module>
    from oridecon.contracts.multimedia.exceptions import ProviderNotInstalledError
...
```

### Package tests: experimental/multimedia/oridecon-multimedia-image

- Scope: `experimental/multimedia/oridecon-multimedia-image/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia-image/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia.image`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1494 ms`
- Parsed summary: `8 errors in 0.76s`
- Counters: passed=0, total=16, failed=16, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
_______________ ERROR collecting tests/unit/di/test_provider.py ________________
ImportError while importing test module 'experimental/multimedia/oridecon-multimedia-image/tests/unit/di/test_provider.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/multimedia/oridecon-multimedia-image/tests/unit/di/test_provider.py:5: in <module>
    from oridecon.contracts.core.health import HealthStatus
...
```

### Package tests: experimental/multimedia/oridecon-multimedia-interpolate

- Scope: `experimental/multimedia/oridecon-multimedia-interpolate/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia-interpolate/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia.interpolate`
- Status: **FAIL**
- Exit code: `2`
- Duration: `925 ms`
- Parsed summary: `5 errors in 0.21s`
- Counters: passed=0, total=10, failed=10, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
_______________ ERROR collecting tests/unit/di/test_provider.py ________________
ImportError while importing test module 'experimental/multimedia/oridecon-multimedia-interpolate/tests/unit/di/test_provider.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/multimedia/oridecon-multimedia-interpolate/tests/unit/di/test_provider.py:3: in <module>
    from oridecon.contracts.multimedia.exceptions import ProviderNotInstalledError

```

### Package tests: experimental/multimedia/oridecon-multimedia-music

- Scope: `experimental/multimedia/oridecon-multimedia-music/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia-music/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia.music`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1455 ms`
- Parsed summary: `7 errors in 0.72s`
- Counters: passed=0, total=14, failed=14, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
_______________ ERROR collecting tests/unit/di/test_provider.py ________________
ImportError while importing test module 'experimental/multimedia/oridecon-multimedia-music/tests/unit/di/test_provider.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/multimedia/oridecon-multimedia-music/tests/unit/di/test_provider.py:6: in <module>
    from oridecon.contracts.core.health import HealthStatus
...
```

### Package tests: experimental/multimedia/oridecon-multimedia-tts

- Scope: `experimental/multimedia/oridecon-multimedia-tts/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia-tts/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia.tts`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1562 ms`
- Parsed summary: `11 errors in 0.83s`
- Counters: passed=0, total=22, failed=22, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
_______________ ERROR collecting tests/unit/di/test_provider.py ________________
ImportError while importing test module 'experimental/multimedia/oridecon-multimedia-tts/tests/unit/di/test_provider.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/multimedia/oridecon-multimedia-tts/tests/unit/di/test_provider.py:6: in <module>
    from oridecon.contracts.core.health import HealthStatus
...
```

### Package tests: experimental/multimedia/oridecon-multimedia-upscale

- Scope: `experimental/multimedia/oridecon-multimedia-upscale/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia-upscale/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia.upscale`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1496 ms`
- Parsed summary: `7 errors in 0.75s`
- Counters: passed=0, total=14, failed=14, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
_______________ ERROR collecting tests/unit/di/test_provider.py ________________
ImportError while importing test module 'experimental/multimedia/oridecon-multimedia-upscale/tests/unit/di/test_provider.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/multimedia/oridecon-multimedia-upscale/tests/unit/di/test_provider.py:3: in <module>
    from oridecon.contracts.multimedia.exceptions import ProviderNotInstalledError
...
```

### Package tests: experimental/multimedia/oridecon-multimedia-video

- Scope: `experimental/multimedia/oridecon-multimedia-video/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia-video/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia.video`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1969 ms`
- Parsed summary: `18 errors in 1.22s`
- Counters: passed=0, total=36, failed=36, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
________ ERROR collecting tests/integration/test_compose_real_ffmpeg.py ________
ImportError while importing test module 'experimental/multimedia/oridecon-multimedia-video/tests/integration/test_compose_real_ffmpeg.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/multimedia/oridecon-multimedia-video/tests/integration/test_compose_real_ffmpeg.py:6: in <module>
    from oridecon.contracts.multimedia.types import ComposeLayer,
```

### Package tests: experimental/multimedia/oridecon-multimedia

- Scope: `experimental/multimedia/oridecon-multimedia/tests`
- Command: `uv run pytest experimental/multimedia/oridecon-multimedia/tests -q -m not integration --cov=experimental/multimedia/oridecon.multimedia`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1304 ms`
- Parsed summary: `22 errors in 0.59s`
- Counters: passed=0, total=44, failed=44, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
_________ ERROR collecting tests/integration/test_full_registration.py _________
ImportError while importing test module 'experimental/multimedia/oridecon-multimedia/tests/integration/test_full_registration.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
experimental/multimedia/oridecon-multimedia/tests/integration/test_full_registration.py:7: in <module>
    from oridecon.contracts.multimedia.protocols import (
...
```

### Package tests: packages/oridecon-audit

- Scope: `packages/oridecon-audit/tests`
- Command: `uv run pytest packages/oridecon-audit/tests -q -m not integration --cov=packages/oridecon.audit`
- Status: **FAIL**
- Exit code: `4`
- Duration: `692 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-audit/tests/conftest.py'.
packages/oridecon-audit/tests/conftest.py:7: in <module>
    from oridecon.audit.logging.logger import AuditLogger
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: packages/oridecon-auth

- Scope: `packages/oridecon-auth/tests`
- Command: `uv run pytest packages/oridecon-auth/tests -q -m not integration --cov=packages/oridecon.auth`
- Status: **FAIL**
- Exit code: `4`
- Duration: `690 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-auth/tests/conftest.py'.
packages/oridecon-auth/tests/conftest.py:31: in <module>
    from oridecon.app import Application
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: packages/oridecon-cache

- Scope: `packages/oridecon-cache/tests`
- Command: `uv run pytest packages/oridecon-cache/tests -q -m not integration --cov=packages/oridecon.cache`
- Status: **FAIL**
- Exit code: `4`
- Duration: `692 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-cache/tests/conftest.py'.
packages/oridecon-cache/tests/conftest.py:12: in <module>
    from oridecon.testing import TestEnvironment
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: packages/oridecon-events

- Scope: `packages/oridecon-events/tests`
- Command: `uv run pytest packages/oridecon-events/tests -q -m not integration --cov=packages/oridecon.events`
- Status: **FAIL**
- Exit code: `4`
- Duration: `695 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-events/tests/conftest.py'.
packages/oridecon-events/tests/conftest.py:17: in <module>
    from oridecon.logging import get_logger
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: packages/oridecon-features

- Scope: `packages/oridecon-features/tests`
- Command: `uv run pytest packages/oridecon-features/tests -q -m not integration --cov=packages/oridecon.features`
- Status: **FAIL**
- Exit code: `4`
- Duration: `690 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-features/tests/conftest.py'.
packages/oridecon-features/tests/conftest.py:13: in <module>
    from oridecon.testing import TestEnvironment
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: packages/oridecon-graph

- Scope: `packages/oridecon-graph/tests`
- Command: `uv run pytest packages/oridecon-graph/tests -q -m not integration --cov=packages/oridecon.graph`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1551 ms`
- Parsed summary: `20 errors in 0.83s`
- Counters: passed=0, total=40, failed=40, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
_______ ERROR collecting tests/integration/graph/test_graph_lifecycle.py _______
ImportError while importing test module 'packages/oridecon-graph/tests/integration/graph/test_graph_lifecycle.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
packages/oridecon-graph/tests/integration/graph/test_graph_lifecycle.py:15: in <module>
    from oridecon.contracts.core.health import HealthStatus
...
```

### Package tests: packages/oridecon-graphql

- Scope: `packages/oridecon-graphql/tests`
- Command: `uv run pytest packages/oridecon-graphql/tests -q -m not integration --cov=packages/oridecon.graphql`
- Status: **FAIL**
- Exit code: `4`
- Duration: `1160 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-graphql/tests/conftest.py'.
packages/oridecon-graphql/tests/conftest.py:82: in <module>
    from oridecon.testing import TestEnvironment
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: packages/oridecon-http

- Scope: `packages/oridecon-http/tests`
- Command: `uv run pytest packages/oridecon-http/tests -q -m not integration --cov=packages/oridecon.http`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1969 ms`
- Parsed summary: `27 errors in 1.24s`
- Counters: passed=0, total=54, failed=54, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
__________ ERROR collecting tests/integration/test_http_lifecycle.py ___________
ImportError while importing test module 'packages/oridecon-http/tests/integration/test_http_lifecycle.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
packages/oridecon-http/tests/integration/test_http_lifecycle.py:7: in <module>
    from oridecon.http.config import HTTPClientConfig
...
```

### Package tests: packages/oridecon-monitor

- Scope: `packages/oridecon-monitor/tests`
- Command: `uv run pytest packages/oridecon-monitor/tests -q -m not integration --cov=packages/oridecon.monitor`
- Status: **FAIL**
- Exit code: `2`
- Duration: `2615 ms`
- Parsed summary: `51 errors in 1.86s`
- Counters: passed=0, total=102, failed=102, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
________ ERROR collecting tests/integration/test_monitor_integration.py ________
ImportError while importing test module 'packages/oridecon-monitor/tests/integration/test_monitor_integration.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
packages/oridecon-monitor/tests/integration/test_monitor_integration.py:7: in <module>
    from oridecon.serialization import loads
...
```

### Package tests: packages/oridecon-nosql

- Scope: `packages/oridecon-nosql/tests`
- Command: `uv run pytest packages/oridecon-nosql/tests -q -m not integration --cov=packages/oridecon.nosql`
- Status: **FAIL**
- Exit code: `4`
- Duration: `695 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-nosql/tests/conftest.py'.
packages/oridecon-nosql/tests/conftest.py:39: in <module>
    from oridecon.testing import TestEnvironment
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: packages/oridecon-notification

- Scope: `packages/oridecon-notification/tests`
- Command: `uv run pytest packages/oridecon-notification/tests -q -m not integration --cov=packages/oridecon.notification`
- Status: **FAIL**
- Exit code: `2`
- Duration: `2415 ms`
- Parsed summary: `1 warning, 34 errors in 1.68s`
- Counters: passed=0, total=68, failed=68, skipped=0, warnings=1, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
____________ ERROR collecting tests/backends/push/test_web_push.py _____________
ImportError while importing test module 'packages/oridecon-notification/tests/backends/push/test_web_push.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
packages/oridecon-notification/tests/backends/push/test_web_push.py:9: in <module>
    from pywebpush import WebPushException
...
```

### Package tests: packages/oridecon-queue

- Scope: `packages/oridecon-queue/tests`
- Command: `uv run pytest packages/oridecon-queue/tests -q -m not integration --cov=packages/oridecon.queue`
- Status: **FAIL**
- Exit code: `4`
- Duration: `688 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-queue/tests/conftest.py'.
packages/oridecon-queue/tests/conftest.py:13: in <module>
    from oridecon.testing import TestEnvironment
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: packages/oridecon-resilience

- Scope: `packages/oridecon-resilience/tests`
- Command: `uv run pytest packages/oridecon-resilience/tests -q -m not integration --cov=packages/oridecon.resilience`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1748 ms`
- Parsed summary: `33 errors in 1.03s`
- Counters: passed=0, total=66, failed=66, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
_ ERROR collecting tests/integration/idempotency/test_idempotency_lifecycle.py _
ImportError while importing test module 'packages/oridecon-resilience/tests/integration/idempotency/test_idempotency_lifecycle.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
packages/oridecon-resilience/tests/integration/idempotency/test_idempotency_lifecycle.py:16: in <module>
    from oridecon.contracts.core.idempotency import IdempotencyStoreProtocol
E   ModuleNotFoundError: No module named 'oridecon'
_______ ERROR collecting tests/integration/test_resilience_components.py ___
```

### Package tests: packages/oridecon-search

- Scope: `packages/oridecon-search/tests`
- Command: `uv run pytest packages/oridecon-search/tests -q -m not integration --cov=packages/oridecon.search`
- Status: **FAIL**
- Exit code: `4`
- Duration: `687 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-search/tests/conftest.py'.
packages/oridecon-search/tests/conftest.py:27: in <module>
    from oridecon.testing import TestEnvironment
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: packages/oridecon-secrets

- Scope: `packages/oridecon-secrets/tests`
- Command: `uv run pytest packages/oridecon-secrets/tests -q -m not integration --cov=packages/oridecon.secrets`
- Status: **FAIL**
- Exit code: `2`
- Duration: `1145 ms`
- Parsed summary: `12 errors in 0.43s`
- Counters: passed=0, total=24, failed=24, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
__________________ ERROR collecting tests/unit/test_audit.py ___________________
ImportError while importing test module 'packages/oridecon-secrets/tests/unit/test_audit.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
packages/oridecon-secrets/tests/unit/test_audit.py:7: in <module>
    from oridecon.secrets.audit import SecretAuditDecorator
...
```

### Package tests: packages/oridecon-sql

- Scope: `packages/oridecon-sql/tests`
- Command: `uv run pytest packages/oridecon-sql/tests -q -m not integration --cov=packages/oridecon.sql`
- Status: **FAIL**
- Exit code: `2`
- Duration: `11196 ms`
- Parsed summary: `2 deselected, 140 errors in 10.36s`
- Counters: passed=0, total=280, failed=280, skipped=0, warnings=0, coverage=2.0%
- Example failures: none
- Output snippet:

```text
==================================== ERRORS ====================================
____________ ERROR collecting tests/integration/test_migrations.py _____________
ImportError while importing test module 'packages/oridecon-sql/tests/integration/test_migrations.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
packages/oridecon-sql/tests/integration/test_migrations.py:10: in <module>
    from oridecon.sql.migrations import (
packages/oridecon-sql/src/oridecon/sql/migrations/__init__.py:5: in <module>
    from oridecon.sql.migrations.base import (
packages/oridecon-sql/src/ori
```

### Package tests: packages/oridecon-storage

- Scope: `packages/oridecon-storage/tests`
- Command: `uv run pytest packages/oridecon-storage/tests -q -m not integration --cov=packages/oridecon.storage`
- Status: **FAIL**
- Exit code: `4`
- Duration: `694 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-storage/tests/conftest.py'.
packages/oridecon-storage/tests/conftest.py:12: in <module>
    from oridecon.testing import TestEnvironment
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: packages/oridecon-tasks

- Scope: `packages/oridecon-tasks/tests`
- Command: `uv run pytest packages/oridecon-tasks/tests -q -m not integration --cov=packages/oridecon.tasks`
- Status: **FAIL**
- Exit code: `4`
- Duration: `692 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-tasks/tests/conftest.py'.
packages/oridecon-tasks/tests/conftest.py:17: in <module>
    from oridecon.testing import TestEnvironment
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: packages/oridecon-tenancy

- Scope: `packages/oridecon-tenancy/tests`
- Command: `uv run pytest packages/oridecon-tenancy/tests -q -m not integration --cov=packages/oridecon.tenancy`
- Status: **FAIL**
- Exit code: `4`
- Duration: `689 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-tenancy/tests/conftest.py'.
packages/oridecon-tenancy/tests/conftest.py:7: in <module>
    from oridecon.contracts.tenancy.commands import CreateTenantCommand
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: packages/oridecon-testing

- Scope: `packages/oridecon-testing/tests`
- Command: `uv run pytest packages/oridecon-testing/tests -q -m not integration --cov=packages/oridecon.testing`
- Status: **FAIL**
- Exit code: `4`
- Duration: `683 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-testing/tests/conftest.py'.
packages/oridecon-testing/tests/conftest.py:4: in <module>
    from oridecon.testing import TestEnvironment
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: packages/oridecon-vector

- Scope: `packages/oridecon-vector/tests`
- Command: `uv run pytest packages/oridecon-vector/tests -q -m not integration --cov=packages/oridecon.vector`
- Status: **FAIL**
- Exit code: `4`
- Duration: `685 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-vector/tests/conftest.py'.
packages/oridecon-vector/tests/conftest.py:15: in <module>
    from oridecon.contracts.data.vector.enums import DistanceMetric
E   ModuleNotFoundError: No module named 'oridecon.contracts'
```

### Package tests: packages/oridecon-web

- Scope: `packages/oridecon-web/tests`
- Command: `uv run pytest packages/oridecon-web/tests -q -m not integration --cov=packages/oridecon.web`
- Status: **FAIL**
- Exit code: `4`
- Duration: `1134 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-web/tests/conftest.py'.
packages/oridecon-web/tests/conftest.py:31: in <module>
    from oridecon.testing.fixtures.bed import TestEnvironment
E   ModuleNotFoundError: No module named 'oridecon.testing'
```

### Package tests: packages/oridecon-webhook

- Scope: `packages/oridecon-webhook/tests`
- Command: `uv run pytest packages/oridecon-webhook/tests -q -m not integration --cov=packages/oridecon.webhook`
- Status: **FAIL**
- Exit code: `4`
- Duration: `683 ms`
- Parsed summary: `summary unavailable`
- Counters: passed=0, total=0, failed=0, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning.
ImportError while loading conftest 'packages/oridecon-webhook/tests/conftest.py'.
packages/oridecon-webhook/tests/conftest.py:11: in <module>
    from oridecon.webhook.config import WebhookConfig
E   ModuleNotFoundError: No module named 'oridecon'
```

### Package tests: packages/oridecon-workflow

- Scope: `packages/oridecon-workflow/tests`
- Command: `uv run pytest packages/oridecon-workflow/tests -q -m not integration --cov=packages/oridecon.workflow`
- Status: **FAIL**
- Exit code: `2`
- Duration: `934 ms`
- Parsed summary: `3 errors in 0.21s`
- Counters: passed=0, total=6, failed=6, skipped=0, warnings=0, coverage=0.0%
- Example failures: none
- Output snippet:

```text
WARNING: Failed to generate report: No data to report.


==================================== ERRORS ====================================
________ ERROR collecting tests/integration/test_workflow_components.py ________
ImportError while importing test module 'packages/oridecon-workflow/tests/integration/test_workflow_components.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
packages/oridecon-workflow/tests/integration/test_workflow_components.py:7: in <module>
    from oridecon.workflow.config import BulkOperationConfig
...
```

