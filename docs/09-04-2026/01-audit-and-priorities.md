# 01 — Audit, Evidence, and Priorities

Date: 2026-09-04  
Scope: repository-wide; admin and `oridecon-ui` are primary product surfaces.

## 1. Method and evidence limits

The audit traced render values, DOM attributes, client lifecycle, request
classification, authorization data, DI/config propagation, CLI assembly,
subprocess handling, public export manifests, copy commands, examples, Make
targets, and GitHub workflows. Findings below are source-proven unless marked
as a risk requiring a browser or executable test.

No dependency environment was available, so this is not runtime verification.
The first implementation slice must add characterization tests and confirm the
observed behavior before changing it. If execution contradicts a finding,
update this record rather than forcing code to match the plan.

## 2. Quantitative snapshot

| Surface | Observed fact | Consequence |
| --- | --- | --- |
| UI public API | Runtime/lazy manifests currently align at 236 names, while runtime maps, `TYPE_CHECKING` imports, docs, and a 152-name test list remain independently maintained | Alignment today does not prevent future drift |
| Alpine syntax | 10 UI binding call sites use `x_bind_*` forms that render `x-bind-*` or `x-bind--*`; 6 admin transition call sites use `x_transition_*` and render `x-transition-*` | Browser ignores directives that look plausible in snapshots |
| CLI commands | 62 explicit “not implemented” messages across 13 contributed command groups | Help advertises successful-looking no-ops |
| CLI diagnostics | 29 “not implemented” messages across 26 `checks.py` / `doctor.py` files, often returned with `status: ok` | Health output can be green without checking anything |
| Examples | 24 `examples/*/application.yaml` manifests; hub statically lists 23 children | Make, CI, hub, docs, and manifests can disagree |
| CI | Seven jobs are defined, but both workflows are `workflow_dispatch` only | README/badge language about every push/PR is false and regressions are not gated |
| Browser coverage | UI a11y pages use CDN Tailwind/HTMX/Alpine/focus/axe and are opt-in; admin browser tests are opt-in and mostly synthetic | A green default suite says little about shipped browser behavior |
| Admin assets | Tailwind, admin CSS, HTMX, Alpine/focus, Lucide, Sortable, and Trix are vendored; Font Awesome is not | Existing `fas fa-*` markup has no owned renderer |

## 3. Prioritized findings

### P0 — security/correctness blockers

| ID | Finding and evidence | Plan / owner | Blocks |
| --- | --- | --- | --- |
| UI-SEC-01 | `core/base.py::render_to_string()` returns every plain string verbatim, including top-level values and `Component.render()` results. Existing tests explicitly preserve top-level verbatim HTML. | Doc 02; UI core owner | All trustworthy component and admin rendering |
| UI-SEC-02 | `RawHTML`, `raw()`, `Markup`, and any arbitrary `__html__` object bypass escaping. Card/admin/layout wrappers pre-render strings and mark them raw, erasing provenance. | Doc 02; UI core + admin rendering owners | UI-SEC-01 migration |
| UI-CONC-01 | `core/base.py` uses process-global `_context_stack` and `_no_context`; concurrent tasks can attach children to another request's component tree. | Doc 02; UI core owner | Safe async rendering |
| ADM-AUTH-01 | Command-palette defaults unconditionally include Users and Settings. The endpoint filters dynamic resource search, but not static commands; `commands=[]` falls back to privileged defaults because `or` collapses an authorized empty list. | Doc 05; admin navigation/auth owner | Restricted-user browser release |
| CI-GATE-01 | `.github/workflows/ci.yml` and `dep-refresh.yml` only accept manual dispatch, while docs claim push/PR execution. | Docs 06 and 09; repository maintainers | Every release claim |

### P1 — release blockers

| ID | Finding and evidence | Plan / owner | Blocks |
| --- | --- | --- | --- |
| UI-COMP-01 | `Component` and `Element` interpret `children=` differently; `as_child` mutates the first child's props and ignores additional children; `Slot.render()` stringifies or directly calls render. | Doc 02; UI core | Reliable wrappers and copied components |
| UI-ID-01 | Global `Zones` IDs, fixed tab IDs, fixed virtual-scroll IDs, admin `#table`/`#table-data`, and page-content IDs collide under composition. | Docs 02, 03, 05; UI/admin | Multi-instance pages |
| UI-ALP-01 | Python underscore normalization emits invalid Alpine families (`x-bind-value`, `x-transition-enter`, `x-bind--class`) while prior guards cover only `x-on-*`. | Doc 03; UI core | Working bindings/transitions |
| UI-INT-01 | Builder and QueryBuilder serialize method bodies as JSON strings, so Alpine receives data properties rather than callable methods. QueryBuilder searches `this.tree.rules`, so operations targeting the root ID cannot find the root. | Doc 03; UI components | Builder/query UX |
| UI-INT-02 | `TaskProgress` defines Alpine `init()` and also renders `x-init="init()"`; Alpine's automatic init calls create two EventSources. | Doc 03; UI components | Stream correctness |
| UI-TBL-01 | `DataTableScriptRenderer` installs first-table process globals (`LexigramTableInitialized`, global `allIds`), document-wide selectors/listeners, and fixed-zone HTMX hooks. | Docs 03 and 05; UI/admin table owners | Multi-table and teardown |
| UI-A11Y-01 | `Tabs` uses fixed IDs, unsafe Python-repr JS interpolation, static ARIA state, and changes selection without moving focus; Tooltip lacks trigger/focus/position parity. | Doc 03; UI components | WCAG/browser gate |
| UI-FORM-01 | `InputGroup` stores built-in `type`; required `FormField` adds `str + Element`, puts ARIA state on a container, mutates child props, and suppresses render errors into a generic box. | Doc 03; UI components | Basic form reliability |
| UI-ASSET-01 | Builder, QueryBuilder, VirtualScroll, settings, and table views emit Font Awesome classes, but neither UI nor admin owns Font Awesome CSS. | Docs 03 and 04; UI/admin asset owners | Visible controls |
| ADM-NAV-01 | Generic same-origin interception body-swaps full documents, while settings and other links target `#main-content`. Server fragment classification follows `HX-Target`; history middleware separately handles body requests. | Doc 05; admin navigation | Coherent page lifecycle |
| ADM-NAV-02 | Navigation does not have one owner for stale-request cancellation, title/breadcrumb updates, main-scroll reset, focus, announcements, auth expiry, or failure recovery. Current click code resets `window`, while the scrolling element is `.admin-shell-scroll`. | Doc 05; admin navigation | Accessible resilient navigation |
| BROW-01 | Browser/a11y suites are optional and can skip after dependencies are requested; default production CI does not install a browser. | Doc 06; test infrastructure | Browser release confidence |
| BROW-02 | Admin behavior tests predominantly construct synthetic Starlette HTML rather than booting the shipped admin shell and real assets. | Doc 06; admin test owner | ADM-NAV validation |

### P2 — product and developer reliability

| ID | Finding and evidence | Plan / owner |
| --- | --- | --- |
| UI-CFG-01 | Components build/cache default `UIConfig()` instead of consuming provider config; `UIContext` carries theme/locale/user but no resolved render policy. | Doc 04; UI DI/core |
| UI-CFG-02 | `UIProvider` creates unrelated default layout config singletons. `UIConfig.htmx_version=2.0.4`, `BaseLayoutConfig.htmx_version=1.9.10`, and `HeadConfig` hardcodes CDN URLs. | Doc 04; UI DI/layout |
| UI-CFG-03 | `auto_escape`, `enable_sse`, `enable_realtime`, theme/version flags are inert or unsafe as global toggles. | Doc 04; UI config |
| UI-API-01 | Four public API authorities must stay manually synchronized despite current alignment. | Doc 04; UI API |
| UI-COPY-01 | `oridecon-ui add` recreates upstream package paths under the destination, leaves imports pointing upstream, silently ignores missing sources and `requires`, and has no provenance/hash/update ownership. | Doc 04; UI CLI |
| CLI-CTX-01 | The root stores `CLIContext`, but commands and `handle_errors` instantiate fresh `OutputManager`s, bypassing `--json`, `--quiet`, `--debug`, `--no-color`, and `--config`. | Doc 07; CLI runtime |
| CLI-OUT-01 | JSON may be multiple independent documents or mixed with Rich output; errors use stdout; subprocess exit codes are discarded. | Doc 07; CLI runtime |
| CLI-TREE-01 | Typer's tree, `_BUILTIN_COMMANDS`, `meta._build_command_registry`, and completion registry are competing command inventories. Built-in `events` shadows the extension contribution. | Docs 07 and 08; CLI runtime/contracts |
| CLI-RUN-01 | `dev`, `dev start`, and `run` use divergent target/factory/env/reload semantics and ignore generated `[tool.oridecon].module`; default backend can be returned even when unavailable. | Doc 07; CLI runtime |
| CLI-SHELL-01 | Shell advertises app/container/config/db/cache/events but deliberately injects `None`; contributed shell factories are never used. | Doc 07; CLI runtime |
| CLI-DIAG-01 | Contracts document async `(container)` health functions, the runner invokes sync zero-arg callables and expects CLI-local `CheckResult`, while extensions return incompatible dictionaries. Doctor also renders a stale `result.message`. | Doc 08; contracts + CLI |
| CLI-CAP-01 | Placeholder command and diagnostic bodies return normally, frequently with success wording/status. | Doc 08; all 13 contributor packages |
| REPO-ONB-01 | README and contributor docs link to a nonexistent root `DEVELOPMENT.md`; `make docs` is documented but absent. | Doc 09; repository maintainers |
| REPO-ONB-02 | The “60 seconds” code and first-app path are not protected by an executable snippet/scaffold scenario. | Docs 07 and 09; core/web/docs |
| EX-CAT-01 | `ServiceRegistry`, `DEMO_IMPORTS`, CI's eight test paths, docs, and 24 manifests duplicate inventory; Make/docs still use nonexistent `examples/demo-hub` while the real folder/module is `example-hub`/`example_hub`. | Doc 09; examples owner |
| EX-TEST-01 | `example-hub/tests/test_demo_ui_validation.py` calls `127.0.0.1:7000` without starting a server in the test. | Doc 09; examples owner |
| EX-PORT-01 | Hub registry ports and several application manifests disagree; several unrelated manifests reuse 8000/8100 without explaining standalone-only semantics. | Doc 09; examples owner |
| CI-EX-01 | Example CI hard-codes eight suites despite 24 manifests; root pytest intentionally excludes examples. | Doc 09; CI owner |
| CI-DEPS-01 | Dependabot and a dormant custom lock-refresh workflow have overlapping intended ownership and no documented policy. | Doc 09; dependency owner |

### P3 — consolidation after contracts land

- Remove compatibility shims for generic `__html__`, `RawHTML`, context-manager
  composition, old Alpine kwargs, and old CLI diagnostics after one documented
  deprecation window.
- Remove duplicate generated API lists, copied asset mirrors, static command
  registries, and hard-coded example imports only after their generated/check
  replacements are active.
- Split oversized inline browser scripts only through the controller ownership
  work; do not mechanically move them without lifecycle tests.

## 4. September 1 overlap ledger

| Completed September 1 area | Excluded from this program | Allowed follow-up here |
| --- | --- | --- |
| R1–R9 first-run/bootstrap/error/log hardening | No redesign of setup, login bootstrap, or startup logging | Reuse the real playground lifecycle for browser tests |
| R6 canonical permission scheme | No new permission naming migration | Make palette/navigation derive from the existing authorization result |
| R10–R16 admin product features and caching | No repeat implementations | Exercise them as real navigation/state scenarios where useful |
| R17/B13 `x_on_*` and initial a11y fixes | Do not repeat the exact handler replacements | Generalize validation to binding/transition/modifier families; test real keyboard/focus behavior |
| R18/admin frontend asset policy | Do not return admin to CDNs | Assign UI/shared asset ownership, eliminate test CDNs and unowned Font Awesome |
| R19–R33 import/export/relation work | No feature reimplementation | Ensure navigation/failure/browser contracts do not regress these pages |
| R34–R37 CSP telemetry/settings/TTL | No second CSP reporting design | Assert existing headers, offline assets, and report behavior in release tests |
| Existing ephemeral browser harness | Do not return to fixed operator-started ports | Boot actual admin app, make gate mode mandatory, and add failure artifacts |

Before opening an implementation PR, search all files in
`docs/09-01-2026/` for the affected symbol and include an “overlap check” in
the PR description.

## 5. Ownership and dependency map

| Workstream | Accountable code owner | Required collaborators | Depends on |
| --- | --- | --- | --- |
| Render nodes/trust/composition | `oridecon-ui` core | admin renderer/layout maintainers | Characterization tests |
| Alpine/controller/ID model | `oridecon-ui` components | admin table and asset maintainers | Render scopes |
| Admin navigation/palette | admin shell/navigation | auth, settings, table owners | Render contract + controllers |
| Browser release gate | admin/UI test infrastructure | CI maintainers | Real app fixtures and owned assets |
| UI config/API/copy | UI DI/API/CLI | docs and packaging maintainers | Render contract |
| CLI runtime | `oridecon-cli` | core Application lifecycle | Invocation and launch contracts |
| CLI capabilities | contracts + CLI | 13 extension package owners | Shared AppSession and outcomes |
| Onboarding/examples/CI | repository maintainers | all package owners | CLI/scaffold and browser commands |

## 6. Required implementation evidence

Every PR must include:

1. the finding IDs it closes;
2. a regression test that demonstrably fails on the parent revision;
3. unit/rendered-output tests plus browser/scenario tests for observable
   behavior;
4. exact lint/type/test/browser commands and results;
5. custom-prefix and restricted-user evidence for admin changes;
6. two-instance and teardown evidence for stateful UI changes;
7. JSON/human/quiet/debug and exit-code evidence for CLI changes;
8. no-third-party-request evidence for shipped browser pages;
9. generated-file `--check` evidence when an authority is introduced; and
10. a September 1 overlap check.

## 7. Program completion criteria

The program is complete when all P0/P1 items are closed, every P2 item is
implemented or explicitly deprecated with a removal version, push/PR CI is
required, the production Chromium gate runs offline with zero silent skips,
all visible CLI capabilities are real, and a fresh clone can follow the tested
onboarding path to a running generated app and example hub.
