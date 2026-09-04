# 07 — CLI Runtime, Launching, Scaffolds, and Shell

Finding IDs: CLI-CTX-01, CLI-OUT-01, CLI-TREE-01, CLI-RUN-01,
CLI-SHELL-01, REPO-ONB-02  
Priority: P1/P2  
Primary package: `experimental/apps/oridecon-cli`  
Related: doc 08 owns extension capability/diagnostic truthfulness

## 1. Goal

Every command should run inside one invocation context, emit through one output
policy, and derive from the final Typer/Click command tree. Generated projects,
`dev`, `run`, health, doctor, and shell should resolve and boot the same target.
Subprocess outcomes and signals must reach the caller. The CLI must never claim
an app, server, completion, or shell object exists when it does not.

## 2. Current evidence

- `runtime/main.py` creates a `CLIContext` in `ctx.obj`, but most commands create
  a fresh `OutputManager()` and never read it.
- `runtime/error_handler.py::handle_errors` creates another default output
  manager on every error, dropping JSON/quiet/debug/color policy.
- `OutputManager` prints one JSON value per method call, so a command can produce
  multiple documents or mix JSON with Rich/direct `typer.echo`/child output.
  Its one Console is configured with `stderr=False`, including errors.
- `runtime/main.py`, `_BUILTIN_COMMANDS`, `commands/meta.py`'s hard-coded
  registry, contributor records, and completion registry duplicate the command
  inventory. The custom `completion` command only completes top-level names and
  prints installation prose after the script.
- `run.py` determines factories from the literal name `create_app`; `dev.py`
  accepts only a file path. They differ on profile/environment/reload/workers
  and can choose a default backend even when none is installed.
- generated projects declare `[tool.oridecon] module = "<package>.app:app"`,
  while `run`/`dev` fallback discovery does not consult it.
- `subprocess.run(..., check=False)` and server manager calls discard child
  status; dual server/MCP teardown only terminates one direct process and can
  leave descendants or mask the first failure.
- `shell.py` advertises app/container/config/db/cache/events but injects `None`
  and never resolves contributed shell factories.
- scaffold help/README says generated projects boot through `oridecon dev`, so
  target resolution is a product contract, not an optional enhancement.

## 3. One invocation context

### 3.1 Model

Replace the loosely accessed dict with a typed context stored directly in
`typer.Context.obj` and in a scoped ContextVar only for decorators/callbacks
that Click cannot inject:

```python
@dataclass
class CLIInvocation:
    command_path: tuple[str, ...]
    project: ProjectContext
    output: OutputSession
    contributors: ContributorRuntime
    launch: LaunchService
    app_session_factory: AppSessionFactory
```

The root callback creates it once after validating global flags. Subcommand
callbacks receive `ctx: typer.Context` and call one `get_invocation(ctx)`. A
ContextVar adapter uses token set/reset around the complete Click invocation;
it is not process-global mutable state and cannot leak into a second
`CliRunner` call.

`ProjectContext` contains the resolved project root, pyproject path, explicit
application config path, cwd, environment/profile overrides, and config loader.
Keep lazy config/app boot, but cache success **and failure** per invocation so
multiple contributors do not boot or report the same invalid config repeatedly.

Add global `--project PATH` for a project root while preserving `--config PATH`
for application configuration. Resolve relative paths from the invocation cwd;
show both paths in debug diagnostics.

### 3.2 Error boundary

Move exception translation to the outer CLI runner or make `handle_errors`
always resolve the current invocation. No handler may instantiate a default
output policy.

Typed exceptions carry a stable machine code, safe message/details, suggestions,
and exit code. Unexpected exceptions:

- human mode: concise error on stderr; traceback only with `--debug`;
- JSON mode: structured redacted error in the one final envelope; optional safe
  debug metadata, never an uncontrolled `repr` of config/secrets;
- test mode: preserve `__cause__` for assertions;
- all modes: cleanup AppSession/processes before final emission.

Remove direct `print`, `typer.echo`, standalone Rich Consoles, and package-local
output manager construction from command paths. Add an AST/source check with a
small infrastructure allowlist (completion script raw writer and child process
plumbing).

## 4. Output and exit contract

### 4.1 Command result

Commands return or raise; they do not decide serialization:

```python
@dataclass(frozen=True)
class CommandResult:
    ok: bool
    data: JsonValue | None = None
    message: str | None = None
    warnings: tuple[Diagnostic, ...] = ()
    exit_code: int = 0
```

`OutputSession` can receive progress/events for human mode, but buffers the
machine representation and writes one final JSON document.

### 4.2 Streams

| Mode | stdout | stderr |
| --- | --- | --- |
| normal human | requested command data/result | progress, warnings, errors, debug/traceback |
| quiet | only explicitly requested raw data; otherwise empty | errors only |
| JSON | exactly one UTF-8 JSON document + newline | child logs and optional debug traceback; no Rich markup |
| completion script | script bytes only | diagnostics/errors |

Warnings do not disappear from JSON/quiet semantics: JSON includes them;
quiet shows warning only when it changes whether the requested operation
succeeded. `--no-color` and standard `NO_COLOR` disable ANSI in all CLI-owned
output. Color is auto-disabled for non-TTY streams.

JSON envelope v1:

```json
{
  "schema": "oridecon.cli/v1",
  "command": ["doctor"],
  "ok": false,
  "exit_code": 1,
  "data": {},
  "warnings": [],
  "error": {"code": "check_failed", "message": "...", "suggestions": []}
}
```

Keys have stable meanings; domain payloads live under `data`. Paths are strings,
datetimes are ISO 8601 UTC, enums use values, ordering is deterministic, and
serialization failure becomes a CLI error rather than falling back to Python
repr.

For long-running child processes in JSON mode, redirect/inherit child logs to
stderr and reserve stdout for the CLI's final result envelope. If event
streaming is needed later, add an explicit `--output jsonl` mode with a separate
schema; do not silently turn `--json` into NDJSON.

### 4.3 Exit codes

- `0`: requested operation completed successfully (warnings allowed unless
  `--strict` for commands that define it);
- `1`: operation/runtime/check failure;
- `2`: Click usage error or invalid configuration/input;
- `3`: requested optional capability/backend is unavailable;
- child server/tool exit: propagate its exact 1–125 code;
- signal: preserve conventional `128 + signal` (Ctrl-C 130) unless an exec-style
  launcher lets the shell receive it directly.

Never convert a child nonzero status to 0 because output was rendered
successfully. Do not invent a “partial success” zero status: report per-item
outcomes in data and return 1 when any requested item failed.

## 5. One assembled command tree

### 5.1 Factory, not import-time singleton mutation

Replace import-time global assembly with:

```python
def build_cli(discovery: ContributorDiscovery | None = None) -> typer.Typer:
    ...
```

Order:

1. create root and global callback;
2. register core-owned commands;
3. discover/validate contributors once;
4. register contributed groups/generators/diagnostics;
5. validate conflicts and final Click tree;
6. return the app.

Tests build fresh apps with explicit fake discovery; reloading modules and
mutating a singleton is no longer required. Contributor import failures are
recorded in `contrib doctor` and debug logs. A broken optional contributor must
not crash `--help`, but invoking a known unavailable contribution exits 3 with
an install/remediation hint.

### 5.2 Ownership and conflicts

The final Click `Command` tree is the authority for help, `list`, completion,
and docs generation. Delete `_BUILTIN_COMMANDS` and the separate built-in list
in `meta.py` after migration. Attach source/category/stability metadata to the
Click command context so `oridecon list --json` traverses the real tree.

Conflict rules:

- exact normalized path is unique;
- an explicitly core-owned command wins only if documented as core capability;
- contributor/contributor collision is an assembly error naming both entry
  points, not first-installed-wins;
- hidden/deprecated aliases cannot shadow visible paths;
- aliases point to the same command object/handler and carry a removal version;
- command ordering is deterministic by category/name, independent of entry
  point discovery order.

Transfer the `events` group to the `oridecon-events` contributor (or another
single declared owner); core must not reserve/shadow an optional extension's
name. Consolidate SQL operations under the existing `db` surface through a
contribution rather than exposing a second all-placeholder `sql` group.

### 5.3 Completion

Use Click/Typer's native shell completion generated from the **assembled** tree
(`--show-completion` / `--install-completion`) and retire custom top-level
scripts/registries. If the compatibility `oridecon completion --shell` remains
for one release, it delegates to the same Click completion engine and writes
only script bytes to stdout. Installation instructions go to stderr or docs,
never into `eval "$(...)"` output.

Test bash, zsh, fish, and PowerShell generation plus Click's completion protocol
for nested built-ins, contributed groups, dynamic generators, options, enum
values, file paths, and hidden commands. Shell completion must not boot the
application or make network calls.

## 6. Canonical project and target resolution

### 6.1 Project locator

Walk upward from cwd/`--project` to the nearest `pyproject.toml` with a real
`[project]` table, using the existing intent in contracts' `find_project_anchor`.
Skip virtual workspace-only roots. Resolve `src` package roots from build
metadata, not by mutating global `sys.path` indefinitely.

`ProjectDescriptor` contains:

- root and pyproject;
- exact `[tool.oridecon].module` target;
- application config path(s);
- app package and source roots;
- environment/profile;
- provenance for every resolved value.

Invalid TOML or an invalid declared target is an error. Do not silently fall
back when the user deliberately declared bad metadata.

### 6.2 Target precedence

One `TargetResolver` is used by `dev`, `run`, shell, health, runtime doctor, and
browser bootstrapping:

1. explicit CLI `TARGET` / `--entry` (user override);
2. exact `[tool.oridecon].module` value (canonical generated-project path);
3. an application-config module field only after it is formally added to the
   config schema;
4. deterministic conventional discovery under declared source roots.

Fallback discovery accepts `module:attr` or a Python file. It reports all
candidates and fails on ambiguity; it never chooses based on filesystem order.
A file is converted to a module relative to its source root and must stay inside
the project.

Return a typed `ApplicationTarget(module, attribute, source, project_root)`.
Do not infer factory status from attribute spelling. Probe/import in a bounded
child process and classify:

- ASGI/app object;
- sync zero-argument factory;
- async zero-argument factory;
- invalid/missing/argument-requiring object.

The probe emits a private JSON protocol, has a timeout, captures safe traceback
information, and does not leave a booted app in the CLI process. The launcher
adapts factory flags to each backend consistently.

## 7. Unified `dev` / `run` launch service

### 7.1 User-facing semantics

- `oridecon dev [TARGET]`: development mode, reload on by default, one worker,
  loopback host by default.
- `oridecon run [TARGET]`: production runner, reload off by default, explicit
  worker count, production validation.
- remove/deprecate confusing `oridecon dev start` production behavior; for one
  release it aliases `run` with a warning and same options.

Both expose the same target, host, port, server, profile, environment, config,
factory override (only if needed), and log options through shared option models.
Options differ only in documented defaults.

Validation before spawning:

- port 1–65535 and workers >= 1;
- reload + workers > 1 is rejected;
- MCP port differs from web port;
- requested server exists **and** `is_available()`; no unavailable default;
- backend supports requested reload/workers/factory combination;
- declared target is valid;
- `--host 0.0.0.0` gets an informational advertised URL, not a browser URL using
  the wildcard address.

Environment policy:

- explicit CLI profile/environment wins and is passed to every child;
- otherwise preserve existing process env and resolved config; do not overwrite
  a user-supplied `ORI_PROFILE` accidentally;
- log resolved provenance in debug with secret values redacted;
- never mutate `os.environ` globally for tests/parallel invocations.

### 7.2 Immutable launch plan

```python
@dataclass(frozen=True)
class LaunchPlan:
    target: ApplicationTarget
    backend: ServerBackend
    argv: tuple[str, ...]
    env: Mapping[str, str]
    cwd: Path
    mode: LaunchMode
```

Each server backend converts the common request to argv and validates unsupported
features. Use `sys.executable -m <server>` where supported so the selected
interpreter/environment is deterministic. Never construct a shell string.

`--dry-run`/`--check` returns the redacted target/backend/argv/env provenance
without spawning and is covered in JSON tests.

### 7.3 Process supervision

Create `ProcessRunner` / `ProcessSupervisor` with injected spawn/clock/signal
collaborators:

- children run in a process group/session on POSIX and the corresponding Windows
  group mechanism;
- forward SIGINT/SIGTERM once, wait a configurable grace period, then kill the
  process group;
- always await/reap children;
- web + MCP mode monitors both: first unexpected exit terminates the peer, and
  the initiating failure/signal determines the final status;
- partial spawn failure cleans up the already-started child;
- cleanup errors are diagnostics and do not mask the primary nonzero status;
- `KeyboardInterrupt` produces 130 after graceful cleanup;
- no broad exception path returns success.

Unit tests use fake executables/scripts that exit 0/7, sleep, spawn a descendant,
ignore TERM, or fail startup. Assert exact status and no live descendants.

## 8. AppSession for shell and runtime commands

Create a shared async context manager:

```python
async with AppSession.open(project, target, config) as session:
    session.app
    session.container
    session.config
```

It resolves target through section 6, creates the actual app/factory result,
awaits `Application.start()`, and guarantees `Application.stop()` on normal
exit, command error, failed contributed namespace, Ctrl-C, and timeout. Validate
object type explicitly; do not guess arbitrary attributes.

### Shell loop ownership

A synchronous REPL needs a live async loop. Use `asyncio.Runner` (or an
explicit loop thread if IPython constraints require it) and keep the same loop
for boot, contributed async factories, user helper calls, and shutdown. Expose a
`run(awaitable)` helper in the standard REPL; configure IPython auto-await only
when supported.

Base namespace contains exactly:

- `app`: the real started Application;
- `container`: its real container;
- `config`: its resolved configuration;
- `run`: loop-safe coroutine runner.

Resolve `ShellContextContribution.factory_path(container)` values asynchronously
through the final ContributorRuntime. Add only successful names. Conflict policy
is deterministic: core names are reserved, contributor/contributor collision
fails before entering the REPL, and optional unavailable values are omitted with
one diagnostic—not set to `None` while the banner claims availability.

`--no-app` prints a plain-shell banner and exposes none of those names.
`--ipython` exits 3 with an install hint if explicitly requested and unavailable;
do not silently switch interpreters. Never place secrets/tokens into the
namespace unless a contributor has an explicit unsafe/debug contract.

Test by injecting a fake REPL callable, a real tiny Application provider, async
shell factories, name collisions, boot failure, user exit, and shutdown failure.

## 9. Scaffold and generator lifecycle

### 9.1 Atomic generation

For `new`, render and validate in a temporary sibling directory, then atomically
rename to a new destination. Refuse non-empty destinations. If cross-device
rename is impossible, fail without partial output or use a journaled copy with
rollback.

For `init` and `gen` in an existing project:

- resolve the canonical ProjectDescriptor/layout;
- validate every target path remains under project root;
- calculate a plan before writes;
- default collision policy is fail (or existing documented skip), never silent
  destructive replacement;
- `--dry-run` performs no directories/files/metadata changes;
- `--force` lists overwritten paths and writes atomically per file with rollback
  journal;
- merge TOML/config through parsers while preserving unrelated fields/comments
  where the selected library supports it; do not overwrite whole files blindly.

CommandAssembler uses invocation output and returns one `GenerationResult`,
not one JSON success document per file.

### 9.2 Generated-project contract

All templates must agree on:

- `[tool.oridecon].module` and actual exported app/factory;
- src package/layout and generator destinations;
- `application.yaml` schema and env keys;
- one package-manager story (`uv` for repository docs/scaffolds; mention pip only
  as a package-install alternative where tested);
- development and production commands;
- health/docs endpoint claims only for templates that actually include web;
- secrets explicitly development-only and production validation guidance.

Update scaffold docstrings/README that currently say `pip install -e .` if the
canonical generated workflow uses `uv sync`.

### 9.3 Executable template matrix

For each canonical template (`minimal`, `api`, `web-api`, `graphql`, `worker`,
`full`, excluding aliases as separate products):

1. render into a temp directory;
2. parse pyproject/YAML and assert no undeclared/unknown config;
3. compile/import with repository packages available through controlled test
   dependencies, not ad-hoc permanent `PYTHONPATH` mutation;
4. run generated unit tests;
5. invoke CLI `--check` target resolution and prove it selects the declared
   target;
6. for web templates, launch on an ephemeral port, request documented endpoints,
   terminate, and assert status 0/no child leak;
7. run one generated component command and import its output;
8. build the generated wheel and inspect package inclusion;
9. run production config validation; expected dev-secret rejection must be
   documented rather than silently disabled.

Add a separate release scenario that installs built Oridecon artifacts into an
isolated temp environment, generates a project as an external user would, and
runs it without monorepo path leakage.

## 10. Migration phases

### Phase A — invocation/output characterization

Add `CliRunner` tests for every global flag before representative built-in,
contributed, generator, failing, and help command. Capture direct-print sites,
JSON multi-document behavior, and child exit loss. Land typed context/result and
central error/output boundary.

### Phase B — command authority/completion

Move construction to `build_cli`, attach metadata, derive list/completion from
Click, enforce conflicts, and transfer optional command ownership. Retain
completion compatibility alias for one release.

### Phase C — project/target/launch

Land ProjectDescriptor, TargetResolver, probe, shared options, immutable plans,
and ProcessSupervisor. Point `dev`/`run` at it; deprecate `dev start`.

### Phase D — AppSession/shell

Use the same resolver/lifecycle for shell and doc 08 runtime diagnostics. Remove
all placeholder namespace values and truthful-banner drift.

### Phase E — scaffold scenarios

Make generation transactional, align instructions, and enforce the full
executable matrix in CI.

## 11. Acceptance criteria

- [ ] `--json`, `--quiet`, `--debug`, `--no-color`, `--config`, and `--project`
      reach every built-in, contributed, generator, diagnostic, and failure path.
- [ ] JSON stdout is one parseable v1 document; completion stdout is only the
      script; human errors/warnings use stderr.
- [ ] Exit codes follow the contract and exact child status/signal propagates.
- [ ] The final Click tree is the only authority for help/list/completion/docs;
      command conflicts are deterministic.
- [ ] Nested contributed commands/options complete without booting an app.
- [ ] Generated `[tool.oridecon].module` is honored; explicit target overrides
      it; invalid declaration does not silently fall back.
- [ ] `dev` and `run` share resolution/backend/env/factory/process code and have
      only documented default differences.
- [ ] Unsupported backend/options fail before spawn; web+MCP cleanup leaves no
      descendants and preserves first failure.
- [ ] Shell exposes a real running app/container/config and resolved contributor
      objects, then always shuts down; `--no-app` claims none.
- [ ] Every canonical scaffold compiles, tests, resolves, launches where
      applicable, accepts generator output, and builds in an isolated scenario.

## 12. Rollout and rollback

Keep deprecated aliases (`dev start`, custom `completion`, old target option
spelling) for one declared minor release with stderr warnings suppressed only in
completion mode. Do not maintain two runtime implementations behind the alias.
JSON schema v1 is additive within its major version; breaking it requires a new
schema selector.

If the new enhanced launcher fails in the field, users can pass an explicit
`module:attr` and server backend through the same resolver, or run the backend
directly. Do not restore swallowed exit codes or an unavailable backend
fallback. AppSession can be disabled only by `shell --no-app` or static doctor;
never replace failed objects with `None` under a successful banner.
