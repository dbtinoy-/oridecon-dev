# Validation — 09-04-2026 Program Status (2026-09-04)

Validates the status statement: *"Everything P0 is untouched. The trust
boundary, escaping, concurrent state, auth leak, and CI gate are all still
broken. The P1 items partially addressed by arena are incremental — the
underlying architecture (process globals, ID collisions, navigation
ownership) remains."*

## 1. Method

- **Baseline:** `66aea39` (`origin/main`) vs **HEAD** `07cf057`
  (`arena/01a06c10-oridecon-dev`). The 09-04 docs are byte-identical in both.
  The arena work changed 150 files / ~10.4k insertions, including
  `core/base.py`, new `core/render_context.py`, `core/trusted_html.py`,
  `core/slot.py`, `core/zones.py`, admin `command_palette.py`,
  `data_table/*`, `shell*.py`, and 80+ new/changed tests.
- **Static tracing** of the exact HEAD sources (file:line below).
- **Runtime characterization** of the *actual HEAD sources*: `core/base.py`,
  `render_context.py`, `trusted_html.py`, `zones.py` were loaded into a stub
  package (`oridecon.logging` / `oridecon.ui.config` stubbed; `markupsafe`
  installed into a throwaway venv). No app dependencies (`uv` absent) so the
  full suite, admin boot, and browser tests were **not** executed — same
  limitation the audit records for its own pass.
- Repro: `python3 -m venv /tmp/v && /tmp/v/bin/pip install markupsafe`, copy
  the four `core/*` files into a stub `oridecon/ui/core` package plus a stub
  `oridecon/logging.py` and `oridecon/ui/config.py`, then run the assertions
  shown in §4. The printed outputs below are from that run.

## 2. Verdict summary

| Claim | Verdict | One-line evidence |
| --- | --- | --- |
| P0 "untouched" | **Partly wrong** | 4 of 5 P0 areas were materially modified; 2 remain open |
| Trust boundary still broken | **True (as audit defines it)** | top-level `render_to_string` / `Component.__html__()` still emit plain strings verbatim |
| Escaping still broken | **True, but narrowed** | child boundary now escapes; `Markup`/`raw()`/top-level still bypass |
| Concurrent state still broken | **False** | composition stack and render context are ContextVar-based; verified task-isolated |
| Auth leak still broken | **False at the palette surface** | static defaults no longer privileged; `commands=[]` preserved; endpoint filters via `can_view_resource` |
| CI gate still broken | **True** | both workflows are still `workflow_dispatch`-only |
| P1 changes are "incremental" | **Partly wrong** | new typed trust grant, render scopes, strict Slot, Alpine validator = real architecture |
| Process globals remain | **Partly true** | Python-side globals largely removed; window/browser globals remain |
| ID collisions remain | **True (provable)** | no response-wide render context is ever installed; identical IDs repeat across components |
| Navigation ownership remains | **True** | body-swap delegation, main-content fragments, palette pushState = 3 owners |

## 3. P0 findings — current state

### UI-SEC-01 — top-level strings / component strings still verbatim — **OPEN**

`core/base.py`:

- `render_to_string()` (line 509): `if isinstance(value, str): return value`
  — files lines 493–510 document this as intended ("strings are returned
  verbatim").
- `Component.__html__()` (line 453–484) → `render_to_string(rendered)` where
  `rendered = self.render()`. A component whose `render()` returns a plain
  string gets that string emitted **verbatim**.
- `_render_child()` (line 276+) escapes string children — the **new** child
  boundary. This is the substantive improvement: a `Component` child inside
  an `Element` no longer bypasses escaping.

Production path still exposed: `engine/renderer.py::render_partial` (line 267)
returns `HTMLResponse(render_to_string(content))`; `render_page` similarly
feeds component content into the shell. Any custom `Column.render()` /
`render()` returning `"<b>" + data + "</b>"` reaches the browser raw.

Runtime result against HEAD sources:

```text
1. render_to_string("<script>alert(1)</script>")          -> '<script>alert(1)</script>'
4. render_to_string(Comp(user="<script>…"))               -> '<b><script>alert(1)</script></b>'
5. el("div", Comp(...))                                   -> <div>&lt;b&gt;&lt;script&gt;…&lt;/b&gt;</div>   (escaped)
7. render_child_to_string(Comp(...))                      -> '&lt;b&gt;&lt;i&gt;x&lt;/i&gt;&lt;/b&gt;'        (escaped)
```

The audit's own acceptance test (`render_to_string("<b>" + user + "</b>")`
must be escaped, doc 02 §3.2/§4) still fails. `tests/unit/test_escaping_policy.py::TestTopLevelRenderVerbatim` was **retained** — it pins
verbatim top-level behavior, which doc 02 explicitly says must be replaced
("characterization tests that must be replaced, not retained as desired
behavior").

### UI-SEC-02 — `Markup`, `raw()`/`RawHTML` still bypass; arbitrary `__html__` fixed — **PARTIALLY CLOSED**

- New `TrustedHTML` (dataclass, `value` + required `source`) and
  `trusted_html()` are the new grant type — `core/trusted_html.py`.
- **Fixed:** arbitrary `__html__` objects are no longer trusted (trust list is
  now typed: `Element`, `RawHTML`, `TrustedHTML`, concrete htpy node types —
  `_is_html_structure`, line 90–96). Runtime result E shows the forged object
  is escaped to its `str()` repr, and `test_trusted_html.py::_ForgedHtmlObject`
  pins this.
- **Still open:** `markupsafe.Markup` passes verbatim as a child *and* at top
  level (`_render_child` line 250–252: `if isinstance(child, Markup): return
  child`), and `raw()`/`RawHTML` remain a verbatim escape hatch (now
  attributed, `source="legacy raw() compatibility adapter"`, but still
  unvalidated). Runtime: C (`Markup` child) and D (`raw()` child) both render
  event-bearing markup.
- **Laundering pattern persists:** admin still does
  `trusted_html(render_to_string(...))` — 19 `trusted_html(` call sites and
  120 `render_to_string(` uses in `experimental/apps/oridecon-admin/src`
  (`dashboard/page_fallbacks.py:76,95`, `page_handlers.py:266`,
  `widget_cards.py`, `admin_slide_over.py`, `content_renderer.py`, …). These
  now carry a source label but still erase per-node provenance — exactly the
  pattern doc 02 asked to stop.

### UI-CONC-01 — cross-task state — **CLOSED at the base layer**

- `_context_stack` / `_no_context` are now `ContextVar`s with immutables
  (tuples) and explicit token bookkeeping (`_enter/_exit_composition_context`,
  `NoContext` — `base.py` lines 291–366). No list-append/global mutation
  remains on the composition path.
- New `RenderContext`/`RenderScope` use one `ContextVar`
  (`render_context.py`).
- Runtime interleaving test (two tasks each creating an `el(...)` with an
  `await` inside) produced correctly isolated children:

```text
A: <div-a><span></span></div-a>
B: <div-b><span></span></div-b>
```

- `tests/unit/test_composition_isolation.py` / `test_render_context.py`
  cover this.
- **Residual process state** (not the audited bug, but not zero): the module
  sets `_warned_html_strings` and `_debug_components_cache` in `base.py`
  (lines 555–607) remain process-wide; bot-side globals
  `window.LexigramTableInitialized`, `window.LexigramTableLogic`,
  `window.LexigramBulkProgressTasks` remain (`data_table_client_logic.py`
  lines 439–441).

### ADM-AUTH-01 — command palette privilege leak — **CLOSED at the palette surface**

- `CommandPalette.__init__` default is now only **Dashboard + Dark Mode**
  (non-privileged); `commands=[]` is preserved (`[]` no longer collapses via
  `or`). `AdminShell` carries the same distinction (shell.py lines 71–73).
- `controllers/command_palette.py` filters the static set through
  `search_service.can_view_resource(user, "users"/"settings")` and merges
  only `allowed_resources_for(user)` results; authorization exceptions are
  logged and **fail closed** (`continue`).
- JS no longer falls back to a privileged set: `normalizeCommands(data)`
  assigns even an empty array (`command_palette.py` lines 149–154); short
  queries show only the (safe) static commands.
- Not runtime-verified end-to-end (no running app); the same authorizer is
  shared with dynamic search, which is the direction doc 05 required.

### CI-GATE-01 — workflows still manual-only — **OPEN**

`.github/workflows/ci.yml` and `dep-refresh.yml` are unchanged versus main:

```yaml
# on:
#   push:
#     branches: [main]
#   pull_request:
#   workflow_dispatch:

on:
  workflow_dispatch:
```

Seven jobs are still defined (`changes`, `quality`, `tests`, `integration`,
`coverage`, `example`, `audit`), but nothing runs on push/PR. README
"## ci — what runs on every push/pr" (README.md:146) remains false. Browser
deps / Playwright / Chromium appear **nowhere** in `ci.yml`; the Makefile has
no `test-e2e` target (only `test-unit` excludes `e2e`), so BROW-01/02 also
remain.

## 4. P1 "architecture remains" — current state

### Process globals — **materially reduced; bot-side globals remain**

Python side: composition globals → ContextVars; zone resolution → ContextVar;
table IDs → response-local `RenderScope` (`core/zones.py`); the old
`LexigramTableInitialized`/global `allIds` Python script state is gone
(`allIds` is now per-`x-data` inside each table root, `rendering.py` lines
204–211, and `self._all_ids` is instance-local).

Still global: `window.LexigramTableInitialized`, `window.LexigramTableLogic`,
`window.LexigramBulkProgressTasks` plus a **document-level**
`bulk-progress-start` listener registered before the init guard
(`data_table_client_logic.py` ~line 439) — i.e. one extra listener per table
instance on the page. `LexigramDownloadBulk`/`LexigramImportUpload` are
idempotent (`|| function…`).

### ID collisions — **REMAIN; provable**

The new `RenderScope` is only correct when **one scope spans the whole
response**. Nothing in the app does that:

- `render_context(` appears **only in tests**; `get_render_scope()` ×16 in
  admin src all hit the per-call fallback in
  `ensure_render_context()`/`render_to_string`/`__html__` (base.py lines 159,
  278, 453, 498).
- Each standalone `render_to_string(component)` therefore gets a *fresh*
  scope, so counters restart at 1.

Empirical (HEAD sources):

```text
9.  two standalone scopes, same role  -> oridecon-tab-1 / oridecon-tab-1  COLLIDE
10. within one render_context          -> oridecon-tab-1 / oridecon-tab-2  distinct
12. two nested tables, same table_key  -> no error (fresh scopes) => duplicate DOM IDs
```

Concretely: `TabGroup(tab_group_key=None)` uses a counter
(`tab_group.py:55–56`) → every instance on a page gets
`oridecon-tab-group-root-1`; two same-`name` `QueryBuilder`s /
`Repeater`s emit identical scope IDs; two tables of the same resource render
`oridecon-table-data-<key>` twice (namespace determinism hides the clash);
`Zones.claim_table_id` raises unless inside an active `table_scope`, but
`table_zone_id` mints a fresh scope (`zones.py:312–317`) so sibling-table
detection doesn't share state. `claim_once` ("at most once per response",
`rendering.py:451–457`) also can't dedupe across per-component scopes, so the
client controller script is emitted once per table.

The mechanism is sound; **the missing piece is the response-wide context
owner** (one `render_context(RenderContext(scope=RenderScope()))` around each
full/partial render, which doc 04/05-style wiring was supposed to add).

### Navigation ownership — **REMAINS fragmented**

- Generic same-origin link interceptor still body-swaps: inline script in
  `shell_scripts.py` (`search_overlay_markup`) → `window.htmx.ajax('GET',
  url.href, { target: 'body', swap: 'innerHTML' })` (line ~152), after only
  aborting stale `.widget-body[hx-get]` loads.
- Settings/nav links still target `#main-content` fragments; server still
  classifies solely by `HX-Target == "main-content"` (`controllers/base.py`
  387–391).
- Command palette executes its **own** navigation:
  `htmx.ajax(...,{target:'#main-content'})` + `history.pushState`
  (`command_palette.py:204–214`).
- No single owner for: stale-nav cancellation, `document.title`, focus
  restoration/announcements, auth-expiry handling, or failure recovery.
- Scroll reset is still `window.scrollTo(0, 0)` (shell_scripts.py ~line 152
  and palette) while the scroll container is `.admin-shell-scroll`
  (`shell_sections.py:315–320`). `syncSettingsPanelNavigation` patches only
  settings-panel active styling on `pushedIntoHistory`/`historyRestore`/
  `popstate`.
- `data_admin_navigation`/`data_settings_back` markers exist but there is no
  shared controller consuming them.

## 5. Other P1/P2 that changed vs the audit text

- **UI-COMP-01** — largely addressed: `Slot` is now exactly-one-Element,
  non-mutating (shallow clone), typed events, explicit conflict/override
  rules (`core/slot.py`); `as_child` clones instead of mutating (`base.py`
  409–421).
- **UI-ID-01** — partially addressed (zone scoping exists; see §4).
- **UI-ALP-01** — addressed: `_validate_alpine_attribute_name` rejects
  `x-bind-value`/`x-transition-*`/`--` forms; **zero** `x_bind_*`/
  `x_transition_*` call sites remain in UI/admin src; canonical `alpine`
  helpers (`attributes/alpine.py`) used by palette, tabs, builder, etc.
- **UI-INT-01** — addressed: Builder/QueryBuilder controllers are real
  `<script>` + `Alpine.data` now, and query builder's `findNode` seeds the
  queue with `this.tree`, so root-targeted ops work
  (`query_builder.py:247–250`).
- **UI-INT-02** — addressed: TaskProgress uses a single `init()`; the
  rendered `x-init` removed (line 25 doc; script owns EventSource/cleanup).
- **UI-A11Y-01** — substantially addressed (scoped ids, roving focus with
  `target.focus()`, dynamic `aria-selected`/`aria-controls`, escape handling);
  Tooltip rewritten with focusable-check + focus/blur/escape `x-on`s and a
  dedup/conflict contract.
- **UI-FORM-01** — partially addressed (FormField clones the input, puts
  `aria-describedby`/`aria-invalid` on the input; `x-bind:required` etc.);
  InputGroup still stores its own `input_type` (unchanged from main).
- **UI-ASSET-01** — addressed: **zero** `fas fa-`/`fa fa-`/`far fa-` remain
  in UI/admin src (icons via `get_icon`/`ICONS`).
- **BROW-01/02** — open (no browser in CI; admin browser tests remain
  opt-in/synthetic per docs 06).
- **P2** (UI-CFG-*, UI-API-*, UI-COPY-*, CLI-*, REPO-ONB-*, EX-*/CI-*): not
  touched by this change set.

## 6. Corrected one-liner

> P0 is not "untouched": the trust boundary and escaping were reworked at
> the *child* boundary (real fix), concurrent-state globals were replaced
> with ContextVars (verified), and the command-palette auth leak was closed.
> But UI-SEC-01/02 and CI-GATE-01 remain open by the audit's own acceptance
> criteria, so "still broken" stands for trust, escaping and CI, while
> "still broken" is wrong for concurrent state and the palette auth leak.
> On P1: the changes are substantive architecture (typed trust, scopes,
> strict Slot, Alpine validation), not surface patch — but two real
> architecture gaps remain, and both are about **ownership**: no
> response-wide render context is installed (ID uniqueness is per-component,
> provably colliding), and navigation still has three owners (body-swap
> interceptor, main-content fragments, palette pushState) with no shared
> controller for focus/title/cancel/scroll.

## 7. Recommended next slices (smallest that closes the gaps)

1. **Wire one render context per response** in `AdminRenderer.render_page` /
   `render_partial` (and the admin mount/decorators), plus a regression test
   rendering two TabGroups/two same-key tables in one response.
2. **Unify the string policy**: one normalizer for `render_to_string`,
   `Element.__html__`, component children, partials; delete
   `TestTopLevelRenderVerbatim`; add the audit's failing-first test
   (`render_to_string("<b>"+user+"</b>")` escaped).
3. **Retire `Markup` and `raw()`** from the trust set behind a documented
   deprecation window; keep only source-attributed `TrustedHTML` and
   framework nodes.
4. **One navigation controller** (server `HX-Target` contract + client
   lifecycle: abort, title, focus/announcement, `.admin-shell-scroll`
   reset, auth-expiry, history) and migrate palette + body-swap onto it.
5. **Enable push/PR CI** (uncomment triggers), add the browser deps and a
   required aggregate status; make browser steps fail rather than skip.

## 8. Implementation status (post "full implement")

| Slice | Status | Evidence |
| --- | --- | --- |
| 1. One render context per response | Done | `AdminRenderScopeMiddleware` installed in `routing.py`; `render_page`/`render_partial` self-wrap in `RenderContext(RenderScope())`; `Zones.table_zone_id` resolves through the active scope; same-response ID regression tests in `test_render_boundary.py`/`test_render_context.py`. |
| 2. Unified string policy | Done | Single normalizer in `ui/core/base.py` for `render_to_string`, `Element.__html__`, component children, partials; `TestTopLevelRenderVerbatim` removed; `render_to_string("<b>"+user+"</b>")` escaped at every depth (`test_render_escaping.py`, `test_render_boundary.py`). |
| 3. Retire `Markup`/`raw()` | Done | `TrustedHTML` is a str subclass with `__html__`, immutable `source`, named producers (`trusted_template_output`/`trusted_svg_icon`/`trusted_static_script`); all framework producers migrated; `Markup`/`raw()` warn via compatibility adapters, removed v0.2.0; import-aware `dev/checks/ui_trusted_html.py` + allowlist (12 paths) clean; `lint-ui-trust` wired into `Makefile ci` and CI quality job. |
| 4. One navigation controller | Done | `window.OrideconNavigator` (abort, `HX-Target` contract, title via `X-Admin-Title`, `.admin-shell-scroll` reset, focus/`oridecon:nav:complete`, auth-expiry redirect, history/popstate) emitted by `admin_navigator_script`; body-swap interceptor removed from `search_overlay_markup`; palette routes through navigator; `AdminNavPushMiddleware` now covers `#main-content` and declares `HX-Target`; server- and client-side tests in `test_navigation_controller.py`, `test_navigation_partial_contract.py`, `test_nav_push_middleware.py`. |
| 5. Push/PR CI + browser gate | Done (needs a live GitHub run) | `ci.yml` triggers enabled; `browser` job installs Chromium and runs `--browser-gate` (fail, never skip); required `aggregate` status; `dep-refresh.yml` weekly schedule restored. Local sandbox could not download Chromium so the browser job itself is unverified here; admin unit suite (6005 passed) and Playwright collection (27 tests) are green. |

