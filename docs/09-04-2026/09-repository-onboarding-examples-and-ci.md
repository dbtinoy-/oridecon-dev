# 09 — Repository Onboarding, Examples, Make, CI, and Dependencies

Finding IDs: REPO-ONB-01, REPO-ONB-02, EX-CAT-01, EX-TEST-01,
EX-PORT-01, CI-EX-01, CI-GATE-01, CI-DEPS-01  
Priority: P1/P2  
Primary owners: repository maintainers, examples owner, CI/release owner  
Depends on: docs 06–08 for final browser/CLI commands

## 1. Goal

A contributor with a fresh clone should have one documented, executable path
from install to a working first app. Make, docs, CI, the example hub, and
dependency automation must call the same underlying authorities. A new example,
package, CLI capability, or UI asset must enter required tests without someone
remembering a second hard-coded list.

## 2. Current drift

### Onboarding and Make

- README, AGENTS, and CONTRIBUTING link repeatedly to root `DEVELOPMENT.md`, but
  that file does not exist.
- CONTRIBUTING documents `make docs`; no such target/docs-site configuration
  exists. The text says it regenerates API files, which is a different operation
  from building docs.
- README's “60 seconds” application and first-app walkthrough are not executed
  as snippets/scenarios in CI.
- `make dev`, README clone setup, devcontainer post-create, and CI use different
  `uv sync` arguments/locked guarantees.
- Make assigns `TYPED_PKGS` twice, so the first list is silently discarded.
- `lint-depth` help says max 4 while it executes max 6.
- `make test-pkg PKG=oridecon-web` resolves a nonexistent root path even though
  contributor docs recommend that spelling; `type-pkg` has the same package-
  location ambiguity.
- root README uses `docker compose up -d`, Make uses legacy `docker-compose` +
  `docker-compose.test.yml`, and CI uses `tests/docker-compose.yml --profile
  core`.
- `clean` recursively deletes every `API.md` and `INDEX.md`, which is too broad
  for a contributor-facing cleanup command.

### Examples

- There are 24 `examples/*/application.yaml` manifests: the hub plus 23 child
  examples.
- `ServiceRegistry` manually repeats 23 child paths, module targets, ports,
  names, blurbs, groups, and capabilities.
- Make's `DEMO_IMPORTS`, examples README, and CI repeat subsets/lists again.
- Make and docs still refer to nonexistent `examples/demo-hub` and module
  `demo_hub`; the actual names are `examples/example-hub` and `example_hub`.
- Hub registry port values disagree with manifests (for example auth-rbac and
  several 8000/8100 entries). Embedded mode ignores child ports, but neither the
  duplication nor standalone semantics are clear.
- `example-hub/tests/test_demo_ui_validation.py` calls
  `http://127.0.0.1:7000` through an unmanaged `httpx.Client`; it starts no
  server and owns no lifecycle.
- CI explicitly runs only eight example test directories and compile-checks
  three, while every example currently has a tests directory.

### CI and dependency updates

- `.github/workflows/ci.yml` is manual-only even though README says it runs on
  every push/PR.
- The `shared` paths-filter value uses one pipe-delimited string rather than a
  list of globs; docs/examples are not modeled as affected groups.
- Five package tests are silently deselected in the matrix rather than fixed or
  tracked as expiring expected failures.
- Integration services have no `always()` teardown step.
- No required production browser job installs Chromium.
- There is no stable final aggregate check suitable for branch protection when
  a dynamic matrix is empty/skipped.
- Dependabot is active for `uv` and GitHub Actions, while a second custom full
  lock-upgrade PR workflow exists in dormant manual form with overlapping
  intended ownership and a test step marked `continue-on-error`.

## 3. One authoritative engineering guide

Create root `DEVELOPMENT.md` and make it the source linked by README, AGENTS,
and CONTRIBUTING. Keep CONTRIBUTING focused on the human PR/DCO workflow and
AGENTS focused on architecture/code conventions; do not copy command matrices
between all three.

Required DEVELOPMENT sections:

1. supported OS/Python/uv/Docker/browser prerequisites and version checks;
2. fresh-clone setup with `uv sync --group tooling --group qa --group security
   --locked` and optional `.env` copy;
3. package/tier map and how to resolve a package slug to a path;
4. quick checks, full offline tests, coverage, package-specific tests;
5. integration profile lifecycle and cleanup;
6. browser installation/gate and artifacts;
7. docs generation/checking (not a nonexistent site build);
8. example catalog, individual/hub run/test commands;
9. adding packages/dependencies and updating `uv.lock`;
10. CI job-to-local-command parity;
11. version/release workflow, including per-package versions;
12. troubleshooting (missing extras, import path, browser, Docker, stale lock).

Place generated command tables between markers sourced from `make help` or a
small Make metadata script. Prose is human-owned; CI `--check` verifies generated
blocks rather than rewriting them.

## 4. Tested onboarding journeys

### 4.1 Repository contributor journey

The canonical sequence becomes:

```bash
uv sync --group tooling --group qa --group security --locked
cp .env.example .env                    # optional; documented
make check-fast                         # formatting/lint/boundaries/small checks
make test                               # offline, no Docker/network services
make check-examples                     # all catalog examples
# Optional:
make integration-up
make test-integration
make integration-down
make browser-install
make test-browser
```

Choose final target names during Make migration and use them verbatim in every
doc. Compatibility aliases may exist but docs show only canonical names.

A CI shell test in a clean checkout extracts/runs the non-destructive setup/check
commands with a temporary HOME/cache. It asserts the default offline path does
not contact PostgreSQL/Redis or require Docker.

### 4.2 First application journey

Make README and `docs/getting-started/first-app.md` derive from one executable
sample under `docs/examples/first_app/` (or use the canonical CLI-generated
`api` scaffold from doc 07):

1. install the documented package/extras;
2. import only public APIs;
3. create the app with the actual sync/async factory contract;
4. launch through `oridecon dev` using `[tool.oridecon].module`;
5. request `/hello?name=oridecon`, `/health`, and API-doc routes only if those
   routes actually ship by default;
6. stop cleanly and propagate process status.

Use snippet include markers or generation so README cannot drift from the tested
file. A pytest scenario runs the ASGI app in process and the CLI launcher on an
ephemeral socket. A built-artifact release scenario installs the published-shape
packages in a temporary environment and repeats it without monorepo
`PYTHONPATH` leakage.

Do not preserve claims merely because they are attractive. If `/docs`, `/redoc`,
or lazy boot is not default, correct the prose and test the real behavior.

### 4.3 Devcontainer

Align `.devcontainer` with the default offline story:

- post-create runs the same locked sync groups as DEVELOPMENT/CI;
- do not automatically require/start PostgreSQL and Redis for a unit-test-only
  contributor; expose an opt-in integration compose profile or a second
  container configuration;
- document `make integration-up` and browser installation inside the container;
- validate the workspace path and user-owned uv/browser caches;
- add a CI JSON/schema check for devcontainer and Compose files.

## 5. One logical 24-example catalog

### 5.1 Authority and schema

Create `examples/catalog.toml` for metadata that is not application runtime
config. Use table keys as slugs so path/slug is not repeated:

```toml
[schema]
version = 1

[examples.approval-flow]
display_name = "Approval Flow"
app_target = "approval_flow.app:create_app"
kind = "web"
group = "standard"
blurb = "State-machine approvals with retry and compensation"
check_path = "/"
capabilities = ["state machine", "approval gates", "history"]
featured = true
mount_in_hub = true

[examples.example-hub]
display_name = "Example Hub"
app_target = "example_hub.app:create_app"
kind = "hub"
mount_in_hub = false
```

The runtime `application.yaml` remains the sole source for application name,
server configuration, and standalone port. The catalog loader joins each TOML
entry to `examples/<slug>/application.yaml`; it does **not** repeat ports or app
config. The resulting `ExampleDefinition` is the one logical catalog consumed
by hub, tools, docs, and CI.

Validation requires exactly one entry for every manifest and vice versa (24 at
this baseline), unique slug/name, existing source/tests/README, valid
`module:factory`, valid group/kind/check path, and `example-hub` excluded from
its own child mount list. It explains duplicate standalone ports as allowed only
when examples are run individually; hub mode uses one hub port. If concurrent
standalone mode is supported later, allocate ports in the supervisor rather
than copying static alternatives into catalog metadata.

### 5.2 Loader ownership

Replace `example_hub.services.registry.ServiceRegistry`'s static list with an
immutable loader/model under `example_hub.catalog` (or a small dependency-free
shared examples tool that both hub and repository scripts import). Requirements:

- accepts an explicit `examples_root`; no fixed parent count in production API;
- validates TOML/YAML and returns all 24 definitions deterministically;
- provides `children()` for the 23 mountable entries;
- does not mutate `sys.path` while merely listing/validating;
- produces JSON for tooling and page view models;
- errors name the slug, field, source file, and remedy.

Fleet loading may use a scoped import-path context, but records and restores
`sys.path` on close and detects module-name collisions. Prefer an import service
based on each declared source root. Every child app starts/stops through its
actual Application lifecycle; a failed child is exposed in hub status, and the
required test fails if any expected child is down.

### 5.3 Repository command

Add `dev/examples.py` (Typer/argparse, no shell parsing) using the same loader:

- `catalog check [--json]`;
- `list [--kind/--group]`;
- `test [SLUG...]`;
- `compile [SLUG...]`;
- `smoke [SLUG...]` (import/boot/health without fixed port);
- `serve SLUG --port 0`;
- `hub` (foreground, graceful signals);
- `docs --check/--write` for generated inventory blocks.

Make targets are thin wrappers. Delete `DEMO_IMPORTS` and hard-coded CI paths.
A new manifest without catalog metadata or tests fails `catalog check` and the
example gate automatically includes it after metadata is added.

### 5.4 Naming migration

Use “example” consistently in new APIs/commands (`ExampleDefinition`,
`ExampleCatalog`, `check-examples`). Keep `demo` Make aliases for one release
only if external scripts plausibly use them. Immediately fix all
`examples/demo-hub`/`demo_hub` paths to `examples/example-hub`/`example_hub`.
The URL `/examples/<slug>` remains unchanged.

## 6. Managed example and hub tests

### 6.1 No external fixed server

Rewrite `test_demo_ui_validation.py` to use a fixture that builds the real hub,
runs lifespan, and either:

- uses `httpx.AsyncClient(ASGITransport(...))` for HTTP semantics that do not
  need a browser; or
- uses the doc 06 pre-bound ephemeral uvicorn fixture for browser/stream/socket
  behavior.

The fixture yields/async-closes clients, fleet, child Applications, and server.
It never assumes port 7000 or asks the operator to run `make demos-up`.

### 6.2 Test layers

1. **Catalog unit:** schema, one-to-one 24 inventory, malformed entry, missing
   source/readme/tests, target import, duplicate app/module.
2. **Per-example unit/ASGI:** run every catalog test directory and import target;
   request declared check/page/static paths using its own app lifecycle.
3. **Fleet integration (offline):** boot all 23 children in process, assert no
   failure, exact status/catalog equality, mounted prefix behavior, and reverse
   shutdown.
4. **Hub browser:** card/filter/search/link/static UX at an ephemeral URL,
   zero console/network errors, a11y, and one representative child interaction.
5. **Standalone smoke:** tool launches each web example on an ephemeral port in
   bounded batches, checks readiness, terminates, and catches assumptions hidden
   by hub mounting.

Avoid fragile assertions that every example must have a file literally named
`app.js`, identical copied navigation CSS, or one fixed DOM class unless those
are declared catalog/UI contracts. Prefer semantic page, manifest asset, and
accessibility checks. If shared nav CSS is a product asset, centralize it rather
than MD5-comparing 23 copies.

### 6.3 Fleet performance and isolation

- Record per-child boot time and total; set evidence-based timeouts.
- Use deterministic in-memory/SQLite/local fake providers; default example gate
  makes no paid/external API calls.
- Mark true external-provider demonstrations as opt-in integration and ensure
  local deterministic mode covers their UI/service contract.
- Reset env/config/import state between child apps; assert containers are
  distinct and all providers stop.
- Run a catalog subset per test for focused failures, plus one required all-
  children lifecycle scenario.

## 7. Makefile as a thin UX layer

### 7.1 Canonical targets

Refactor target bodies to invoke versioned Python scripts/shared commands rather
than reimplementing lists and policy in shell. Recommended public surface:

| Target | Contract |
| --- | --- |
| `setup` | locked contributor dependency sync |
| `check-fast` | format/lint + deterministic static/generated checks; no tests |
| `check` | check-fast + supported type checks |
| `test` | full offline non-integration suite |
| `test-pkg PKG=...` | catalog-resolved package tests; accepts distribution slug or repo path |
| `type-pkg PKG=...` | same package resolver |
| `coverage` | aggregate configured floor |
| `integration-up/down` | `docker compose -f tests/docker-compose.yml --profile core` |
| `test-integration` | integration scenarios, with preflight and guaranteed cleanup option |
| `browser-install` / `test-browser` / `test-a11y` | doc 06 authority |
| `check-examples` / `examples` | section 5 tool; all catalog entries / foreground hub |
| `docs-generate` / `docs-check` | generated references versus drift + links/imports/snippets |
| `ci` | same scripts as required CI, or a clear local superset |

Keep `dev`, `fmt`, `check-demos`, `demos-up`, and old integration names as
warning-producing aliases only for a declared transition where needed. Do not
create `make docs` unless it has one unambiguous contract; docs currently need
“generate” and “check”, not a pretend site server.

### 7.2 Package catalog

Create/extend one workspace package inventory from root workspace metadata. It
maps distribution name, repo path, source path, tests, typing status, and tier.
Use it for `test-pkg`, `type-pkg`, CI matrices, version tooling, and docs. Delete
duplicate `TYPED_PKGS`; typing status belongs in this machine-validated catalog
or package metadata.

Reject unknown/ambiguous `PKG` with suggestions. Tests prove
`PKG=oridecon-web`, `PKG=packages/oridecon-web`, and an experimental package
resolve correctly.

### 7.3 Safety and parity fixes

- Change help to max import depth 6 or policy to 4; command/help/docs must match.
- Use Docker Compose v2 consistently and one compose file/profile.
- Replace broad clean globs with explicit cache/build paths; generated docs are
  cleaned only by their owning generator.
- `make ci` must propagate every subcommand failure under `set -e` semantics and
  not depend on `.venv/bin/python` directly; use `uv run`.
- Make help is plain and usable without uv; command targets fail early with a
  clear uv prerequisite.
- Avoid background `nohup`/PID/sleep hub management. Canonical `make examples`
  runs foreground with signal-safe lifecycle. Tests use fixtures. If a local
  background command is retained, implement it in the supervisor with stale
  PID validation and bounded readiness, not Make shell snippets.

## 8. CI on push and pull requests

### 8.1 Triggers and permissions

Enable:

```yaml
on:
  push:
    branches: [main, dev]
  pull_request:
  workflow_dispatch:

permissions:
  contents: read
```

This avoids duplicate feature-branch push + PR runs while truthfully gating
protected branch pushes and every PR. If project policy truly requires all
branch pushes, remove the branch filter and document the cost; do not claim it
without configuration.

Use concurrency keyed by workflow + PR number/ref with cancellation for new
commits. Pin third-party actions to reviewed commit SHAs (annotated with release
version), and let the chosen dependency bot update those SHAs.

### 8.2 Change groups

Fix paths-filter syntax with arrays/multiline globs and model at least:

- core;
- backend packages;
- AI;
- multimedia;
- apps;
- examples;
- docs/dev tooling/shared config.

Changes to root config/lock/Make/workflows/contracts run all dependent groups.
UI/admin changes trigger apps + browser; CLI/contracts trigger CLI capability
and scaffold scenarios; catalog/example changes trigger all examples; docs
changes trigger docs checks. Validate group computation with fixture event
payloads or a pure script rather than testing YAML manually.

Path filtering may reduce unit shards, but required quality, generated-drift,
security-sensitive browser, and final aggregate signals cannot disappear
silently. Each skipped job reports an explicit successful “not affected” result
consumed by the aggregate.

### 8.3 Required job graph

Recommended graph:

1. `changes` — validated affected matrix;
2. `quality` — ruff, boundaries, typing, config/generated authorities (UI API /
   assets/directives, CLI capabilities, example catalog, docs snippets);
3. `unit-*` — affected package groups, no hidden deselects;
4. `coverage` — aggregate configured testpaths/floor;
5. `integration` — core profile scenarios with `always()` logs/teardown;
6. `examples` — catalog-driven all tests/compile/smoke + managed fleet;
7. `browser-production` — doc 06 Chromium/offline gate;
8. `audit` — dependency/security checks with an explicit vulnerability policy;
9. `ci-success` — `if: always()`, examines every required dependency and fails
   on failure/cancellation or unexplained skip.

Branch protection requires only stable job names such as `quality`,
`browser-production`, and `ci-success`, not dynamic matrix labels.

### 8.4 Remove invisible debt

The five current `--deselect` entries must be handled before/while enabling CI:

- fix them; or
- mark at the test with `xfail(strict=True, reason="issue URL; owner; expires
  YYYY-MM-DD")` only when the failure is understood and not security-related.

Add a checker that fails expired/no-issue xfails and forbidden CI `--deselect`,
`continue-on-error`, or blanket `|| true` for required tests. A strict xpass
forces cleanup. Do not make enabling CI contingent on silently dropping more
coverage.

Integration job always uploads redacted logs on failure and executes
`docker compose ... down -v --remove-orphans` under `if: always()`.

## 9. Documentation checks without inventing a site

There is no current docs-site config, so define honest commands:

- `docs-generate`: run existing error/CLI/env/dependency/public-API/example
  generators in write mode;
- `docs-check`: run those generators with `--check`, existing docs import/link/
  claim/default audits, Markdown formatting if adopted, and executable snippets;
- `docs-serve`: add only if/when a specific site generator and lock-pinned config
  are committed.

Fix CONTRIBUTING accordingly. Verify the external docs URL in a scheduled link
check with sensible retry; PR checks validate internal links deterministically
without turning transient internet failure into unrelated PR noise.

Every command shown in README/CONTRIBUTING/DEVELOPMENT/examples docs should be
represented in a machine-readable command fixture or extracted fenced-block
test. Commands that are destructive, publish, or require credentials are
parse/help-checked rather than executed.

## 10. One dependency-update owner

Choose Dependabot as the single automated update owner because `.github/
dependabot.yml` already declares both ecosystems.

Implementation:

1. Configure uv and GitHub Actions updates explicitly for target branch `dev`
   (the integration branch), weekly cadence, labels/reviewers as repository
   policy allows, and sensible grouping of compatible minor/patch updates.
2. Keep security updates separable/expedited; do not group unrelated breaking
   majors.
3. Require the same `ci-success` and browser gate on bot PRs; no automatic merge
   until repository policy deliberately enables it.
4. Ensure uv update PRs modify both declarations and `uv.lock`; quality runs
   `uv lock --check`/locked sync and fails drift.
5. Delete `.github/workflows/dep-refresh.yml` after a test Dependabot uv PR proves
   lock updates. Do not leave a dormant second owner that may later be scheduled.
6. Pin action SHAs and let Dependabot's Actions ecosystem update them.
7. Document emergency pin/ignore policy with reason, owner, and review date.

The existing custom refresh workflow's `continue-on-error` allows a knowingly
red lock PR and must not become the update policy. If maintainers instead choose
full-lock refreshes, they must disable Dependabot uv and make the custom workflow
scheduled, non-green on test failure, conflict-safe, and clearly owned. Do not
run both.

## 11. Implementation phases

### Phase A — correctness and triggers

- Add DEVELOPMENT, fix broken hub paths/managed client fixture, align docs with
  existing real commands.
- Enable PR/protected-branch CI, read-only permissions, integration cleanup, and
  aggregate status.
- Add browser job infrastructure from doc 06 in reporting then required mode.

### Phase B — catalog and example gate

- Add schema/24 entries/loader/validation.
- Migrate ServiceRegistry/Fleet, Make, CI, and docs to it.
- Delete static lists and fixed-port tests; land managed all-child scenarios.

### Phase C — Make/package/docs authorities

- Add workspace package resolver; remove duplicate typed-package list.
- Consolidate sync/Compose/test/docs targets and compatibility aliases.
- Add executable first-app/docs command checks.

### Phase D — CI debt and dependency ownership

- Fix or expiring-xfail current deselections and prohibit hidden exclusions.
- Pin actions, configure Dependabot target/grouping, prove lock PR, then remove
  custom refresh workflow.
- Require stable aggregate/browser statuses in branch protection.

## 12. Acceptance criteria

- [ ] Fresh-clone instructions and devcontainer use one locked dependency command
      and default offline tests require neither Docker nor external services.
- [ ] Root DEVELOPMENT exists; README/AGENTS/CONTRIBUTING link it; every shown
      non-destructive command is parse- or execution-tested.
- [ ] The first-app sample imports, boots, serves only documented routes, and
      stops through both ASGI and CLI launch scenarios.
- [ ] One validated logical catalog covers exactly all 24 manifests and drives
      the 23 hub children, Make, CI, and generated docs.
- [ ] No `demo-hub`/`demo_hub`, static `DEMO_IMPORTS`, hard-coded eight-suite CI,
      or duplicated registry port remains.
- [ ] Hub/example tests own app/server/client/port/cleanup and pass without an
      operator-started `127.0.0.1:7000` process.
- [ ] Package slug resolution makes documented `test-pkg`/`type-pkg` examples
      work and one typing-status authority exists.
- [ ] Make help/behavior, Compose path/profile, docs commands, and cleanup policy
      are accurate and safe.
- [ ] CI runs on every PR and protected-branch push with read-only default
      permissions, stable aggregate status, browser gate, integration teardown,
      and no silent deselect/continue-on-error debt.
- [ ] Dependabot alone owns automated uv/Actions updates, lock drift fails, and
      bot PRs pass the same required checks.

## 13. Rollout and rollback

Land push/PR triggers with concurrency cancellation and observe cost/runtime;
optimize through validated affected matrices, not by disabling required signals.
Keep old Make aliases for one release, but they invoke the new authority and
print migration guidance. The catalog migration should land atomically with hub,
Make, CI, and docs consumers so there is never a split inventory.

If the full fleet is temporarily too slow, shard it from the same catalog while
retaining one all-child lifecycle job; never return to a hand-picked list. If a
bot policy causes noisy PRs, adjust grouping/cadence or pause the one owner—do
not reactivate an overlapping updater. A flaky non-security test can use the
bounded quarantine policy in doc 06/section 8; CI triggers and aggregate status
remain enabled.
