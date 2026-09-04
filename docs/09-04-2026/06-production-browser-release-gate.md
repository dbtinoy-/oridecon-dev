# 06 — Mandatory Offline Production-Browser Release Gate

Finding IDs: BROW-01, BROW-02, UI-A11Y-01, UI-TBL-01, ADM-NAV-01,
ADM-NAV-02, ADM-AUTH-01  
Priority: P1 release gate  
Primary tools: pytest, pytest-playwright, Playwright Chromium

## 1. Goal

Turn browser behavior into a required release signal against real Oridecon UI
and admin code. The gate must:

- boot the real admin lifecycle and component gallery;
- use shipped CSS/JS/assets only;
- own its server, database, auth, port, and teardown;
- fail on browser/page/console/network errors and on unexpected skips;
- verify behavior, keyboard/focus/ARIA, multi-instance isolation, and cleanup;
- produce useful failure artifacts.

It replaces neither unit tests nor server integration tests. It catches the
class of failures those tests cannot: malformed directives the browser ignores,
duplicate IDs, stale HTMX responses, incorrect focus/scroll/history, leaked
listeners/EventSources, missing assets, and unauthorized UI data.

## 2. Current gap

### UI suite

`experimental/apps/oridecon-ui/tests/a11y/` builds a useful gallery but loads
Tailwind, HTMX, Alpine, focus, and axe from CDNs. Every test is skipped unless
`--run-a11y` is passed. If requested browser dependencies are absent, parts of
the suite can still skip.

### Admin suite

`experimental/apps/oridecon-admin/tests/browser/` has an ephemeral-server
pattern and vendored HTMX, which should be retained. Most behavior tests,
however, construct small synthetic Starlette pages and copied lifecycle scripts
rather than booting `bootstrap.create_app`, the real shell renderers, routes,
auth/session stores, and shipped admin assets. It is also opt-in.

### CI

Playwright and `pytest-playwright` are already declared in root tooling/QA
groups, but no required job installs Chromium. Both primary workflows are
manual-only at present (doc 09 fixes triggers).

## 3. Test topology

Create a shared package at `tests/browser_support/` with no imports from test
modules back into product code:

```text
tests/browser_support/
  server.py              # pre-bound socket + uvicorn lifecycle
  network.py             # offline request policy
  console.py             # console/page error collector
  artifacts.py           # trace/screenshot/DOM/log retention
  accessibility.py       # local axe injection + keyboard assertions
experimental/apps/oridecon-ui/tests/browser/
experimental/apps/oridecon-admin/tests/browser/
```

Keep package-specific fixtures in each package. Shared helpers implement
infrastructure only; product-specific setup/assertions remain with their owner.

Mark tests `@pytest.mark.browser` and optionally `a11y`. Local default pytest
may continue excluding the expensive marker, but the CI browser command
explicitly selects it. Once selected or when `ORI_BROWSER_GATE=1`, missing
Playwright, Chromium, a local axe asset, or a server dependency is a hard setup
failure—not `pytest.skip`.

## 4. Real admin fixture

### 4.1 Parameterize the playground

Refactor `experimental/apps/oridecon-admin/playground/serve.py` without turning
it into test-only code:

```python
@dataclass(frozen=True)
class PlaygroundSettings:
    database_url: str
    setup_token: str
    session_secret: str
    prefix: str = "/admin"
    debug: bool = False
    seed: bool = True
    clock: Clock | None = None

async def build_app(settings: PlaygroundSettings) -> PlaygroundApp: ...
```

`PlaygroundApp` (or a fixture-owned resource bundle) exposes the ASGI app and a
single `aclose()` path for providers/container/temp resources. Production code
still goes through `Container` → `DatabaseProvider` → admin `create_app()`.
Use a temporary SQLite file per worker/test session for browser runs; keep SQL
auth/session/audit state real and demo resources deterministic.

Remove hard-coded `DB_PATH`, setup/session secrets, and port from the builder.
The executable `main()` may supply documented development defaults, but tests
never use or delete the repository's `playground.db`.

### 4.2 Own the HTTP server

The pytest fixture:

1. creates an IPv4 TCP socket bound to `127.0.0.1:0` and keeps it open;
2. builds the app with a temp DB and prefix parameter;
3. starts `uvicorn.Server.serve(sockets=[socket])` in a fixture task/thread;
4. waits on a bounded readiness endpoint and reports server logs on timeout;
5. yields the exact base URL and setup/auth helpers;
6. requests graceful exit, awaits it with a timeout, then force-cancels if
   needed;
7. closes app/container/provider resources and temp directory;
8. asserts no server task, child process, or open SQLite connection remains.

Keeping the pre-bound socket removes choose-port-then-bind races. Do not use a
fixed 8000 or require an operator-started process.

### 4.3 Setup and authentication

Exercise two modes:

- a dedicated test walks the real first-run setup UI once with a generated
  setup token and test mail sink;
- ordinary scenarios use a helper that creates users/roles through the
  framework's public setup/service APIs, then signs in through the real login
  form. Do not fabricate session cookies.

Add deterministic roles:

- full administrator;
- restricted viewer without user/settings capability;
- expired/invalid session.

Inject a clock/session expiry collaborator where needed rather than sleeping.
If session expiry cannot yet accept a clock, add a test helper at the repository
boundary to expire the real stored session; do not mock the browser response.

### 4.4 Real behavior-only fixture routes

The playground may add clearly named demonstration resources/pages to expose
composition states, but they must use shipped renderers/controllers/assets:

- a page with two DataTables and independent query namespaces;
- long content to verify `.admin-shell-scroll`;
- form validation and CRUD resources;
- page-scoped overlays/editors.

Do not copy shell scripts into test HTML. A test-only route that constructs a
synthetic mini implementation does not satisfy this gate.

## 5. Offline component gallery

Replace CDN strings in `tests/a11y/gallery.py` with the asset resolver from doc
04. Serve gallery pages through the same ephemeral server helper, with package
static routes and production layout/head generation.

Gallery requirements:

- light, dark, high-contrast/system-theme cases;
- narrow/mobile and desktop viewports;
- interactive, disabled, loading, validation, empty, error, and overflow states;
- at least two instances of every stateful component;
- hostile text fixtures to verify doc 02 escaping;
- no global fixed IDs;
- no test-only CSS that masks missing production styles.

Vendor a pinned `axe-core` distribution under a test tooling asset directory
with version, SHA-256, and license metadata. Inject it from disk with
`page.add_script_tag(path=...)`; never fetch it. Keep axe as a test dependency,
not a production admin asset.

## 6. Zero-outbound-network policy

Install a Playwright context route before page creation:

- allow only the fixture's exact scheme/host/port plus `data:`/`blob:` where
  explicitly expected;
- abort and record every other HTTP(S), WebSocket, beacon, font, source map, or
  redirect target;
- fail at teardown with method, resource type, and redacted URL;
- treat DNS/connection failures as attempted outbound requests, not proof that
  the page is offline-safe.

Also scan rendered HTML/CSS/JS/source maps for `http://`, `https://`, protocol-
relative URLs, CDN hostnames, and remote `@import`/font declarations. Use an
allowlist only for literal examples in inert code blocks and require path,
owner, reason, and expiry.

Run CI with an additional network-denial mechanism where practical, but keep
browser route enforcement because it produces better diagnostics.

## 7. Failure policy and artifacts

Each test context installs collectors before navigation:

- `pageerror`: always fail;
- console `error`: always fail;
- console `warning`: fail unless in a tiny checked-in allowlist with owner and
  expiry; framework deprecations are not indefinitely allowlisted;
- failed requests and non-expected 4xx/5xx: fail with request/response details;
- unhandled dialog/download/popup: fail unless the test declares it;
- duplicate IDs after initial load and every swap: fail;
- axe serious/critical (and defined WCAG 2.2 AA rule set): fail;
- leaked-resource counters after teardown: fail.

On failure retain:

- Playwright trace (`trace.zip`);
- full-page screenshot;
- final DOM and accessibility snapshot;
- console/network event JSON;
- server log and seed/config metadata with secrets redacted;
- test/video only when configured to control artifact size.

Upload artifacts for failed CI runs with a bounded retention period. Never
include passwords, setup tokens, cookies, CSRF values, database files, or form
secrets; artifact helper must redact them before writing.

## 8. Required scenario matrix

### 8.1 Rendering and components

- plain strings, component-returned strings, wrappers, and admin partials stay
  text; explicit trusted SVG/template paths render;
- invalid Alpine attributes are absent from final DOM;
- InputGroup/FormField labels, required/error/help relationships and focus;
- Tooltip hover/focus/Escape/edge placement/reduced motion;
- Tabs Arrow/Home/End/Enter/Space, mobile select, URL mode, two instances;
- Builder/QueryBuilder add/remove/reorder/root operation/max-depth/hidden JSON,
  keyboard behavior, two instances;
- TaskProgress one EventSource, completion/failure/retry/removal teardown;
- VirtualScroll fallback/load/end/error/focus/observer teardown;
- icon visibility and names with no Font Awesome request/classes.

### 8.2 Admin navigation

- plain no-JS link/form fallback (run a context with JavaScript disabled);
- sidebar, settings, search/palette, breadcrumbs, title, active state, and full
  frame stay synchronized;
- rapid A→B navigation with delayed A cannot show A;
- Back/Forward restores exact query, title, active navigation, content, and
  shell scroll;
- network/500 failure retains old page and URL, announces, retries;
- accidental full document fragment triggers hard fallback, not nested body;
- custom prefix `/ops/console` and simulated ASGI root path;
- mobile sidebar/palette/dialog focus trap and invoker restoration.

### 8.3 CRUD and forms

- create, validation failure, correction, edit, delete confirmation/cancel;
- focus first error/summary and preserve non-secret values;
- CSRF failure is clear and does not replay mutation;
- field widgets (date/file/relation/rich text where shipped) initialize once and
  teardown on swap;
- browser reload and no-JS flow reach equivalent server outcomes.

Do not reimplement September 1 import/export/relation work. Select a small
representative smoke of those existing flows only to catch navigation regressions.

### 8.4 Multiple tables

- two real table roots have no duplicate IDs;
- sorting/filtering/pagination on table B does not alter table A;
- query URL preserves both namespaces;
- selection/select-all/bulk controls and downloads originate in the intended
  table;
- keyboard shortcuts apply only to focused table;
- delayed response in one table cannot overwrite the other or a newer request;
- repeated swaps leave one controller/listener/Sortable/resizer instance.

### 8.5 Authorization and auth expiry

- restricted user sidebar, search results, and palette omit Users/Settings and
  inaccessible resources;
- authorized empty palette stays empty and Enter executes nothing;
- fabricated direct command/action/URL returns 403 and no privileged payload;
- expiry during frame navigation, table refresh, and form mutation reaches
  login safely; mutation is not replayed;
- logout invalidates history-restored protected fragments;
- impersonation uses effective permissions and banner stays synchronized.

### 8.6 Accessibility

For gallery and representative admin pages:

- automated axe WCAG 2.2 AA scan;
- keyboard-only happy path with visible focus;
- accessible names/roles/states/relationships;
- focus order, traps, restoration, and post-navigation/error focus;
- live announcement count/content (no duplicate chatter);
- zoom/reflow at 200%/400% and narrow viewport horizontal overflow checks;
- reduced motion and dark/system contrast checks;
- touch target size for primary mobile controls.

Automated axe is necessary but not sufficient; behavior assertions above remain
explicit.

## 9. CI and local commands

Add a required `browser-production` job in `.github/workflows/ci.yml`:

```yaml
- run: uv sync --group tooling --group qa --locked
- run: uv run playwright install --with-deps chromium
- run: >-
    ORI_BROWSER_GATE=1 uv run pytest
    experimental/apps/oridecon-ui/tests/browser
    experimental/apps/oridecon-admin/tests/browser
    -m browser --browser chromium --tracing retain-on-failure
```

Pin the GitHub runner/Python and Playwright through the lock. Cache browser
binaries keyed by OS + Playwright version only if integrity and cache misses are
handled correctly; never skip installation merely because a stale directory
exists.

Expose local targets:

- `make browser-install` — explicit Chromium install;
- `make test-browser` — production behavior gate;
- `make test-a11y` — a11y subset;
- `make test-ui` / `make test-admin` — package test surfaces.

Commands in docs and CI call the same Make/script authority. Browser job runs on
push and PR and is included in the aggregate required status from doc 09.

## 10. Wheel/static-asset verification

Add a packaging lane before declaring release readiness:

1. build UI and admin wheels;
2. inspect wheel manifests for CSS, JS, licenses, icons, and generated manifest;
3. install into an isolated environment without repository source on
   `PYTHONPATH`;
4. render/serve a minimal gallery/admin asset smoke;
5. request every manifest URL and compare SHA-256/content type;
6. verify zero fallback to source-tree paths or CDN.

This can be a smaller browser smoke on every PR and full scenario gate on source,
with both required for release.

## 11. Rollout

1. Land infrastructure and run in non-blocking reporting mode for a short,
   time-bounded stabilization window (for example, five consecutive green PR
   runs; record the exact decision in the implementation PR).
2. Classify every failure as product bug, harness bug, or explicitly owned
   temporary allowlist. Never add a blanket warning/network allowlist.
3. Make the job required and set gate mode so selected tests cannot skip.
4. Delete copied synthetic behavior pages after equivalent real-app scenarios
   pass; retain only small infrastructure unit tests that deliberately test the
   harness.
5. Add the wheel/static smoke to release workflow and branch protection.

Rollback a flaky test by marking it with an issue, owner, reason, and expiry of
at most 14 days while keeping the job required. Do not disable the entire job or
restore a silent skip. Security/authorization/offline tests are not eligible for
quarantine.

## 12. Acceptance criteria

- [ ] Browser gate starts/stops its own real admin app, temp SQLite state, and
      random port with no leaked process/resource.
- [ ] Gallery/admin use shipped local assets and local axe; any outbound attempt
      fails with useful diagnostics.
- [ ] Selected gate tests cannot skip because Playwright/Chromium/assets are
      absent.
- [ ] Page errors, console errors/unowned warnings, failed requests, duplicate
      IDs, serious/critical axe results, and leaks fail the test.
- [ ] The full scenario matrix covers navigation, CRUD, overlays, keyboard,
      multiple tables, teardown, custom prefix, restricted user, and auth expiry.
- [ ] Failure artifacts are useful and secret-free.
- [ ] Source behavior and installed-wheel assets are both tested.
- [ ] Push/PR branch protection requires `browser-production` and the aggregate
      status.
