# 08 — Truthful CLI Capabilities, Health, Doctor, and Fixes

Finding IDs: CLI-DIAG-01, CLI-CAP-01, CLI-TREE-01  
Priority: P1/P2  
Primary owners: `core/oridecon-contracts`, `oridecon-cli`, extension packages  
Depends on: doc 07 invocation output, command tree, ProjectContext, and AppSession

## 1. Non-negotiable rule

> A visible command performs the documented operation or reports that the
> capability is unavailable with a nonzero status. A diagnostic reports PASS
> only after it executed and verified its condition.

“Not implemented”, “coming soon”, placeholder `None`, and a constant
`{"status": "ok"}` are never successful capabilities.

## 2. Current contract mismatch

`core/oridecon-contracts` correctly tries to keep contributions independent of
the CLI package, but the executable contract is incomplete and inconsistent:

- `HealthCheckContribution` documents
  `async def check(container) -> HealthCheckResult` but no contracts-owned
  `HealthCheckResult` exists;
- the CLI's health registry invokes synchronous zero-argument classes returning
  CLI-local `CheckResult`;
- contributed checks return arbitrary dicts with values such as `ok` and often
  “not implemented” messages;
- Doctor documents a sync zero-argument result type that likewise does not
  exist in contracts; `can_fix` has no fix callable or outcome contract;
- shell contributions are documented async container factories but current
  shell does not boot an app or invoke them;
- doctor rendering has at least one stale `result.message` reference that can
  display the wrong result;
- command contribution metadata says only where a Typer group lives; it cannot
  state or test capability availability.

The solution belongs in `oridecon-contracts`, not in extension imports from
`oridecon-cli`.

## 3. Contracts-owned diagnostic model

Add `core/oridecon-contracts/src/oridecon/contracts/cli/diagnostics.py`.
Keep values frozen, serializable, and free of Typer/Rich/CLI runtime imports.

### 3.1 Status and severity

```python
class DiagnosticStatus(StrEnum):
    PASS = "pass"            # check executed and condition is true
    WARN = "warn"            # check executed; non-fatal issue found
    FAIL = "fail"            # check executed/errored; required condition false
    SKIP = "skip"            # intentionally not selected/applicable
    UNAVAILABLE = "unavailable"  # implementation exists, prerequisite absent

class DiagnosticSeverity(StrEnum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"
```

Definitions are enforced:

- PASS requires a non-empty assertion summary and cannot contain placeholder
  markers.
- WARN is for genuinely non-blocking findings; an author must not downgrade a
  failed requirement just to preserve exit 0.
- FAIL includes assertion failure, timeout, invalid result, and unexpected
  exception. Details are safe, user-actionable, and redacted.
- SKIP requires a machine `reason` such as `filtered`, `not_applicable`, or
  `dependency_check_failed`. It is never a missing implementation.
- UNAVAILABLE means real implementation was reached but a declared optional
  prerequisite is not installed/configured/bootable. It includes an install or
  configuration remediation.

### 3.2 Context and outcome

```python
@dataclass(frozen=True, slots=True)
class DiagnosticContext:
    project_root: Path
    config_path: Path | None
    environment: str
    profile: str | None
    config: Mapping[str, JsonValue]
    container: ContainerResolverProtocol | None = None
    app: object | None = None

@dataclass(frozen=True, slots=True)
class DiagnosticOutcome:
    check_id: str
    status: DiagnosticStatus
    summary: str
    details: Mapping[str, JsonValue] = field(default_factory=dict)
    remediation: tuple[str, ...] = ()
```

Runtime-assigned fields (`contributor`, category, severity, duration, start/end,
exception code) belong to an envelope created by the runner so a contribution
cannot spoof timing/ownership.

Validate JSON serialization and size limits before rendering. Redact values by
key/type and contributor-provided sensitive-path metadata; never serialize a
whole config, container, exception `__dict__`, connection URL, API key, JWT, or
credential object.

### 3.3 Contribution descriptors

Evolve descriptors to explicit phases and call signatures:

```python
@dataclass(frozen=True)
class DiagnosticContribution:
    id: str
    label: str
    description: str
    check_path: str
    contributor: str
    phase: DiagnosticPhase       # STATIC or RUNTIME
    category: str = "general"
    severity: DiagnosticSeverity = WARNING
    timeout_seconds: float = 10.0
    requires: tuple[CapabilityRequirement, ...] = ()
    fix_path: str | None = None
    fix_risk: FixRisk | None = None
```

All new checks use one signature, sync or async accepted at the adapter boundary:

```python
async def check(context: DiagnosticContext) -> DiagnosticOutcome: ...
```

Prefer async implementations; the runner awaits awaitables and can run a truly
blocking sync check in a bounded worker thread. A check cannot access a concrete
CLI output object.

Keep `HealthCheckContribution` and `DoctorCheckContribution` as deprecated
constructors mapping to `DiagnosticContribution` for one release:

- Health → `RUNTIME`, container required;
- Doctor → `STATIC` unless explicitly migrated;
- old dict results go through a strict compatibility adapter;
- unknown status/missing fields/placeholder text maps to FAIL with
  `invalid_legacy_result`, never PASS;
- emit contributor/path deprecation diagnostics and publish a removal release.

## 4. Runner and aggregate semantics

Add one `DiagnosticRunner` in the CLI. It receives final assembled descriptors
and doc 07's invocation/AppSession.

### 4.1 Static doctor

`oridecon doctor`:

- locates/parses the project/config without booting the application;
- runs STATIC checks only by default;
- supports `--runtime` to open one AppSession and include runtime checks;
- supports repeatable `--check ID`, `--category`, `--contributor`, and
  `--timeout` cap;
- lists every selected outcome, including skip/unavailable;
- uses deterministic descriptor order `(phase, category, contributor, id)` even
  if checks execute concurrently.

### 4.2 Runtime health

`oridecon health [TARGET]`:

- opens one shared AppSession through doc 07;
- passes its app/container/config to all selected runtime checks;
- bounds concurrency (configurable small default) so checks do not overload a
  backend;
- wraps each check with the smaller of contribution timeout and invocation
  timeout;
- cancels outstanding checks on process cancellation, then closes AppSession;
- supports `--watch INTERVAL` only as explicit JSONL/human streaming mode with
  clean signal handling; ordinary `--json` remains one document.

Do not create one application/container per check. Do not run runtime checks in
completion/help/list commands.

### 4.3 Dependency and timeout behavior

Build a check dependency graph only where an explicit prerequisite check ID is
declared. Cycles/unknown IDs fail assembly. If a prerequisite FAILs, dependent
checks receive SKIP `dependency_check_failed`; if an optional capability is
missing, the check returns UNAVAILABLE.

Timeout and exception are FAIL outcomes with stable machine codes. The human
summary names the check; debug traceback goes to doc 07's protected stderr path.
One check exception cannot abort rendering of other completed outcomes.

### 4.4 Exit aggregation

| Selected outcomes | Exit |
| --- | --- |
| all PASS/SKIP, or PASS/WARN without `--strict` | 0 |
| any WARN with `--strict` | 1 |
| any FAIL | 1 |
| critical UNAVAILABLE | 1 |
| explicitly requested single check/capability unavailable | 3 |
| aggregate noncritical UNAVAILABLE plus otherwise healthy | 0, but aggregate status `degraded` and item remains visible |
| no checks discovered/selected due to missing requested contributor | 3 |
| invalid usage/config | 2 |

A check marked critical defines a runtime requirement; if not configured, it is
unhealthy rather than optional. Contributors must choose severity accordingly.
JSON aggregate includes counts by exact status and `healthy`/`degraded`/`failed`.

## 5. Real fix contract

### 5.1 Types

Add contracts-owned types:

```python
class FixRisk(StrEnum):
    SAFE = "safe"
    MUTATING = "mutating"
    DESTRUCTIVE = "destructive"

@dataclass(frozen=True)
class FixPlan:
    check_id: str
    summary: str
    changes: tuple[PlannedChange, ...]

class FixStatus(StrEnum):
    APPLIED = "applied"
    NO_CHANGE = "no_change"
    REFUSED = "refused"
    FAILED = "failed"

@dataclass(frozen=True)
class FixOutcome:
    check_id: str
    status: FixStatus
    summary: str
    changed_paths: tuple[Path, ...] = ()
```

A fix callable accepts `DiagnosticContext` and a typed `FixRequest(dry_run,
confirmed)`. It must not print.

### 5.2 UX and safety

- `doctor --fix` first runs checks, computes plans, and shows them.
- SAFE fixes may run after one confirmation; non-interactive mode requires
  `--yes`.
- MUTATING fixes require explicit selected check(s) plus `--yes` when stdin is
  not a TTY.
- DESTRUCTIVE fixes require an explicit check ID and `--yes`; never run through
  blanket `--fix`.
- `--dry-run --fix` is pure and returns plans without filesystem/config/backend
  mutations.
- Back up or atomically replace files; constrain paths to project root unless a
  specific system-level fix declares otherwise.
- After an APPLIED/NO_CHANGE result, rerun the check. Success requires PASS (or
  documented WARN); otherwise overall exit is 1.
- Run the same fix twice: second result must be NO_CHANGE and leave bytes/state
  unchanged.
- A declared `fix_path` must import and return the contract type. `can_fix=True`
  without a callable is invalid and removed.

Do not implement “fix” as advice text; advice belongs in remediation.

## 6. Capability availability for commands

Add contracts-owned `CapabilityAvailability`:

```python
class AvailabilityStatus(StrEnum):
    AVAILABLE = "available"
    UNCONFIGURED = "unconfigured"
    UNAVAILABLE = "unavailable"

@dataclass(frozen=True)
class CapabilityAvailability:
    status: AvailabilityStatus
    reason: str | None = None
    remediation: tuple[str, ...] = ()
```

Extend `CommandContribution` with an optional `availability_path` and explicit
requirements. Availability functions inspect ProjectContext/DiagnosticContext
but never print or boot unless `requires_app_context` declares runtime
resolution. Runtime commands re-check after boot; help-time metadata is not an
authorization/security decision.

Rules:

- a command group with no implemented subcommands is not contributed to the
  visible tree;
- a compatibility hidden stub may remain for one release and must raise typed
  `CapabilityUnavailable` (exit 3), never return normally;
- an implemented but unconfigured optional command may remain visible because
  its help teaches configuration; invocation exits 3 with remediation;
- an implementation error is exit 1, not “unavailable”;
- `oridecon contrib capabilities --json` lists available/unconfigured/hidden
  capabilities from descriptors so omission from normal help is still
  diagnosable.

## 7. Placeholder inventory and retirement

Static scan on 2026-09-04 found 62 explicit placeholder messages in 13 command
groups:

| Group/package | Placeholder messages | Phase-0 action | Required implementation boundary |
| --- | ---: | --- | --- |
| audit | 5 | hide/fail placeholder subcommands | audit query/export/stats/retention protocols |
| auth | 5 | hide/fail | user/session/role/token protocols; secret-safe output |
| cache | 5 | hide/fail | cache health/stats/get; key iteration/flush only if backend supports it |
| events | 4 | remove core shadow; hide placeholders | event bus/registry/store capabilities; replay only with store protocol |
| features | 5 | hide/fail | feature registry/evaluation/mutation protocol |
| monitor | 4 | hide/fail | monitor health/metrics/SLO/alert read protocols |
| notification | 4 | hide/fail | configured channel/inbox/send protocol; test sends clearly labeled |
| sql | 5 | retire duplicate group into `db` | database/migration service used by existing root surface |
| tasks | 7 | hide/fail | task registry/store/worker control protocols |
| tenancy | 4 | hide/fail | tenant query/lifecycle protocols and authorization |
| vector | 4 | hide/fail | collection/query/stats/delete capabilities |
| workflow | 5 | hide/fail | workflow registry/runner/history protocols |
| AI | 5 | hide/fail | provider/model registry and safe connectivity checks |

There are also 29 placeholder messages across 26 diagnostic files in audit,
auth, cache, events, features, monitor, NoSQL, notification, queue, resilience,
search, SQL, storage, tasks, tenancy, vector, web, workflow, and AI surfaces.
Phase 0 maps every one to FAIL/UNAVAILABLE or removes its contribution; none may
remain successful.

### 7.1 Per-group implementation order

Implement protocol-first, in this order:

1. **Read-only status/list/inspect** commands where a stable service protocol
   already exists. These establish output, availability, and fake-service
   tests.
2. **Bounded operational actions** (retry, invalidate one key, run one workflow)
   with typed IDs, timeout, and per-item outcomes.
3. **Bulk/destructive actions** (flush, purge, delete collection, revoke all)
   only after dry-run, confirmation, authorization/audit, and idempotency
   contracts exist.
4. **Backend-specific features** appear only when a capability protocol says the
   active backend supports them; do not branch on concrete implementation class
   names in the command.

An owner must inventory actual existing protocols before coding each group. If
no stable protocol exists, keep the command unavailable rather than importing a
private backend just to make the CLI look complete.

### 7.2 Operation requirements

Every implemented subcommand must have:

- a fake/in-memory protocol test proving a real method was called with parsed
  typed inputs;
- a failure/timeout/unavailable test and exact exit status;
- human + JSON output snapshots without secrets;
- idempotency/concurrency behavior where relevant;
- destructive `--dry-run` and `--yes` tests;
- one AppSession integration test when runtime state is required;
- help/completion metadata from the final command tree.

Status commands must not mutate. Mutation commands must not report success from
an empty/no-op adapter unless “already in desired state” is a typed successful
outcome.

## 8. Diagnostics implementation requirements

### Static checks

Doctor checks should validate facts available without app boot, such as:

- config parses and known keys/types are valid;
- required secret source is present/strong enough without revealing value;
- selected backend extra/package/tool is installed;
- project target/source layout is coherent;
- migration paths/directories are reachable;
- incompatible options or duplicated providers are declared.

They must not claim network/database/service health.

### Runtime checks

Health checks resolve public protocols from the booted container and perform a
bounded, side-effect-free probe:

- database `SELECT 1`/protocol ping and migration readiness if supported;
- cache set/get/delete only in an isolated health namespace or a native ping;
- queue/event/notification checks that avoid sending production messages unless
  explicitly requested;
- store/index/vector checks through native health/stat protocols;
- provider/model checks distinguish configured credentials from actual bounded
  connectivity; do not make external calls in default offline CI.

Use fake/local drivers for offline contract tests. Network integration checks
carry markers and are not mislabeled PASS when deselected.

## 9. Source and behavior enforcement

Add `dev/checks/cli_capabilities.py` and make it part of quality CI. It should:

- inspect every `CommandContribution`, check/fix/shell path, and import it in a
  subprocess;
- reject visible command/check source containing known placeholder markers
  (`not implemented`, `coming soon`, `placeholder`, `TODO`) unless in a test
  asserting rejection;
- flag command callbacks whose only observable work is echo/return constant and
  no service/generator call or typed unavailable exception (heuristic, reviewed
  allowlist required);
- reject diagnostic constant PASS/`status: ok` without an assertion/probe call;
- validate descriptor IDs, timeouts, requirements, conflicts, JSON
  serializability, and callable signatures;
- fail deprecated legacy adapters after their removal version;
- generate a capability matrix doc from descriptors and `--check` it.

Static heuristics are defense in depth. The definitive gate is parameterized
behavior tests that invoke every visible command/check with success and failure
fakes. Maintain a checked-in expected set derived from descriptors, not another
manual list.

## 10. Security and privacy

- Diagnostics and commands never print secret values, DSNs with credentials,
  authorization headers, token claims not explicitly safe, user password data,
  or arbitrary config reprs.
- Contributor detail payloads are data-only, size-limited, and redacted before
  output/logging.
- Fixes cannot write outside approved scope, follow symlinks unexpectedly, or
  execute shell strings.
- Runtime checks are side-effect-free by default. A `--deep` check that sends a
  test event/notification is explicit, uniquely tagged, cleaned up, rate-limited,
  and unavailable in production unless enabled.
- Operational commands rely on application service authorization/tenant context;
  the CLI's local visibility is not permission enforcement.
- Exceptions expose correlation/stable codes in normal output, tracebacks only
  in debug, always redacted.

## 11. Migration phases

### Phase A — stop false green immediately

- Add source inventory as a checked fixture.
- Change all placeholder PASS/ok outcomes to FAIL or UNAVAILABLE with
  remediation, or remove the contribution.
- Hide/failing-stub placeholder subcommands; resolve core `events` shadow and
  duplicate SQL ownership.
- Fix stale doctor rendering and preserve doc 07 output flags.

### Phase B — contracts and adapters

- Add diagnostic/fix/availability types to contracts.
- Implement strict legacy adapters and contract tests in contracts package.
- Add runner aggregation, timeout, ordering, JSON, exit semantics.

### Phase C — AppSession and real diagnostics

- Wire static doctor and runtime health to doc 07 ProjectContext/AppSession.
- Migrate extension checks in batches; delete arbitrary dict results.
- Implement safe idempotent fixes and recheck behavior.

### Phase D — real commands

- Implement read-only protocol-backed commands first, then operations.
- Remove hidden compatibility stubs only when scripts have had the declared
  deprecation window.

### Phase E — enforce removal

- Turn legacy result/descriptor warnings into errors at the removal release.
- Require capability matrix `--check` and every-visible-command parameterized
  test in CI.

## 12. Acceptance criteria

- [ ] Result, context, status, severity, fix, and availability types live in
      `oridecon-contracts`; extensions do not import CLI runtime types.
- [ ] Every selected check yields one validated typed outcome with owner,
      duration, timeout behavior, deterministic order, and redacted details.
- [ ] PASS means a real assertion ran; no placeholder status is green.
- [ ] Doctor is static by default; health/runtime doctor share one AppSession and
      always close it.
- [ ] Exit codes and JSON aggregates follow section 4 for pass/warn/fail/skip/
      unavailable/empty cases.
- [ ] Fix dry-run is pure; mutations require appropriate confirmation; fixes are
      idempotent and automatically rechecked.
- [ ] All 62 command and 29 diagnostic placeholder messages are removed from
      visible successful paths.
- [ ] Core no longer shadows optional `events`; SQL commands have one owner.
- [ ] Every visible extension command calls a real public protocol or exits
      nonzero unavailable, with success/failure/JSON tests.
- [ ] Source/capability matrix checks and behavior parameterization run on every
      push/PR.

## 13. Rollback

Rollback may hide a newly unstable optional command/check or report it
UNAVAILABLE with a nonzero/degraded aggregate. It may not restore constant PASS,
normal-returning “not implemented”, placeholder shell values, or swallowed
errors. Keep the strict legacy adapter for only the announced compatibility
release; extending it requires an explicit release decision and still cannot
map placeholder text to PASS.
