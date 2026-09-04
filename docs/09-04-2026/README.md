# Repository UI, UX & DX Improvement Program (2026-09-04)

This directory records a repository-wide audit and a set of implementation-ready
plans for improving Oridecon's product and contributor experience. The primary
product surfaces are `experimental/apps/oridecon-admin` and
`experimental/apps/oridecon-ui`; the CLI, public APIs, docs, examples, tests,
and contribution workflows are treated as first-class developer experience.

These are **plans, not claims that the fixes have shipped**. The audit was based
on static source tracing and comparison with the completed work under
[`docs/09-01-2026/`](../09-01-2026/). No source implementation was changed as
part of this planning pass.

## Documents

| Doc | Plan | Primary outcome |
| --- | --- | --- |
| [01-audit-and-priorities.md](01-audit-and-priorities.md) | Evidence-backed audit, priority queue, ownership, and September 1 exclusions | One non-duplicative backlog with explicit severity and dependencies |
| [02-ui-rendering-and-composition.md](02-ui-rendering-and-composition.md) | Rendering trust boundary, escaping, child composition, slots, and render scopes | Plain strings are always text; trusted HTML and DOM identity are explicit |
| [03-ui-interactions-and-accessibility.md](03-ui-interactions-and-accessibility.md) | Alpine attributes, external interaction controllers, forms, tabs, tooltips, tables, builders, progress, and icon ownership | Interactive components work in real browsers, per instance, with teardown and keyboard parity |
| [04-ui-config-api-and-copy-dx.md](04-ui-config-api-and-copy-dx.md) | Config propagation, asset policy, public export registry, docs generation, and component-copy lifecycle | One resolved UI policy, one public API authority, and safely owned copied components |
| [05-admin-navigation-state-and-authorization.md](05-admin-navigation-state-and-authorization.md) | Admin navigation response contract, lifecycle, table identity, and authorization-aware command palette | Predictable SPA-like navigation without weakening no-JS or authorization behavior |
| [06-production-browser-release-gate.md](06-production-browser-release-gate.md) | Offline Playwright/a11y gate against shipped layouts and assets | Browser behavior becomes a mandatory production release signal rather than an opt-in synthetic check |
| [07-cli-runtime-and-project-lifecycle.md](07-cli-runtime-and-project-lifecycle.md) | Invocation context, output, command assembly, completion, launch resolution, subprocesses, scaffolds, and shell | Global flags work everywhere and generated projects run through one truthful lifecycle |
| [08-cli-capabilities-and-diagnostics.md](08-cli-capabilities-and-diagnostics.md) | Contracts-owned health/doctor outcomes and retirement of placeholder-success commands | Every visible command and diagnostic reports a real capability and a meaningful exit status |
| [09-repository-onboarding-examples-and-ci.md](09-repository-onboarding-examples-and-ci.md) | Onboarding, Make targets, example catalog/fleet, managed tests, CI triggers, and dependency automation | A fresh contributor can follow one tested path, and push/PR CI enforces it |

## Priority model

- **P0 — security/correctness blocker:** unsafe trust boundary, authorization
  leak, cross-request state leak, or a green gate that does not run.
- **P1 — release blocker:** primary behavior is broken, instance-unsafe,
  inaccessible, or not covered against shipped code.
- **P2 — product/DX reliability:** configuration, lifecycle, API, docs, or
  onboarding drift that makes supported behavior unpredictable.
- **P3 — cleanup/follow-up:** consolidation or polish after the governing
  contract and release gate exist.

The priority is about execution order, not file order. Detailed findings and
owners are in doc 01.

## Integrated critical path

Implement in the following order. Each numbered item is intended to be a
reviewable PR or a short sequence of stacked PRs; later work must not bypass the
contracts established earlier.

1. **Turn the gates on and capture red characterization tests.** Enable push and
   pull-request CI, add a required aggregate status, make browser dependencies
   fail rather than skip in gate mode, and add regression tests that demonstrate
   the current rendering, directive, duplicate-ID, command-palette, CLI-output,
   and fixed-port example failures. Do not make an unsafe behavior the accepted
   snapshot merely to get green.
2. **Fix the UI trust boundary and composition model.** Introduce typed render
   nodes and explicit trusted HTML, escape top-level and component-returned
   strings, stop pre-render/re-raw laundering, make Slot exactly-one-child and
   non-mutating, and isolate or retire implicit context composition.
3. **Fix attribute syntax and small broken primitives.** Add canonical Alpine
   attribute helpers plus source/rendered-output guards, migrate all malformed
   bindings/transitions, and repair `InputGroup`, `FormField`, `Tooltip`, and
   `Tabs` before using those primitives in larger surfaces.
4. **Introduce render scopes and owned browser controllers.** Make IDs and
   selectors per root, move complex JavaScript out of serialized Python dicts
   and inline scripts, and give every controller deterministic `mount`/`destroy`
   behavior across HTMX swaps.
5. **Adopt the admin page-frame navigation contract.** Move navigation into one
   server/client protocol, then migrate sidebar, settings, search, forms, table
   state, title/focus/scroll/history handling, and authorization-aware commands.
6. **Make the production browser suite mandatory.** Exercise the real playground
   lifecycle and shipped bundles offline, including custom prefixes,
   restricted users, multi-instance roots, cancellation, teardown, keyboard,
   ARIA, and HTMX history.
7. **Consolidate UI platform DX.** Bind config at render scope, establish one
   asset/version policy, generate lazy/type/docs exports from one registry, and
   close the copied-component add/diff/update lifecycle.
8. **Consolidate CLI lifecycle.** Introduce one invocation context and command
   tree, one launch resolver for `dev`/`run`/`shell`, exit-code propagation, and
   executable scaffold scenarios.
9. **Make extension capabilities truthful.** Land contracts-owned diagnostic
   outcomes and availability metadata, hide or fail unavailable commands, then
   implement extension groups protocol-first in prioritized batches.
10. **Close repository onboarding drift.** Add the missing authoritative
    engineering guide, derive all 24 examples from one catalog, replace fixed
    ports and hard-coded lists, and make docs/examples/browser checks required
    push/PR signals.

## Cross-plan release invariants

A change in this program is complete only when all relevant invariants hold:

1. **Security:** untrusted strings cannot become executable markup through
   nesting, wrappers, components, `__html__`, or partial responses.
2. **Authorization:** hidden navigation is not treated as enforcement; visible
   navigation, command search, and direct endpoints all use the same
   fail-closed capability decision.
3. **Isolation:** two roots on one page and two concurrent render tasks do not
   share IDs, selection, event listeners, observers, streams, or mutable data.
4. **Lifecycle:** every browser resource and every booted application has a
   named owner and a deterministic cleanup path, including replacement,
   cancellation, errors, and test teardown.
5. **Progressive enhancement:** canonical links and forms work without
   JavaScript; HTMX/Alpine improve behavior rather than define whether an
   operation is reachable.
6. **Accessibility:** keyboard, focus, names, relationships, state, reduced
   motion, and live announcements are verified in a browser, not inferred from
   markup alone.
7. **Offline reproducibility:** production and test pages make no third-party
   network requests. Vendored files have versions, checksums, licenses, and one
   owner.
8. **Truthful interfaces:** docs, help, JSON, exit codes, health checks, and
   visible commands never report a capability that is missing or skipped.
9. **Generated-authority checks:** duplicated artifacts are generated and
   checked for drift; hand-maintained parallel inventories are prohibited.
10. **Evidence:** every repaired bug has a test that fails on the old behavior;
    required suites cannot silently skip in CI.

## Explicit September 1 exclusions

The work in [`docs/09-01-2026/`](../09-01-2026/) is the baseline and must not be
reimplemented. In particular, this program does **not** reopen first-admin
setup, canonical permissions, mailer onboarding, saved views, bulk outcome UX,
imports/exports, relation mutations, Security Center, security-header TTL, or
the CSP report-only feature.

The following items are valid follow-ups rather than duplicates:

- R17/B13 fixed malformed `x_on_*` handlers and made an initial accessibility
  pass. This program covers still-malformed `x_bind_*` / `x_transition_*`
  families, browser semantics, multi-instance isolation, and mandatory gates.
- R18 and the frontend asset policy made the admin self-hosted. This program
  removes test CDNs, assigns shared UI asset ownership, removes unowned Font
  Awesome assumptions, and checks the actual shipped bundles offline.
- R34–R37 established CSP telemetry/settings. This program may assert those
  existing headers and reports in browser tests, but does not redesign them.
- Existing admin browser tests established an ephemeral server and vendored
  HTMX. This program retains that useful harness concept while replacing
  synthetic behavior pages with the real admin lifecycle.

Doc 01 contains a fuller overlap table and a change-time checklist.

## Validation status for this planning pass

No tests, lint, type checks, builds, docs snippets, browser runs, or package
isolation tests were executed. The checkout does not provide `uv`, and the
system Python does not contain the workspace's runtime/test dependencies.
Implementation PRs must therefore establish their own baseline before changing
behavior and record exact commands and results in their PR descriptions.
