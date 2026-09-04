# 05 — Admin Navigation, State, and Authorization

Finding IDs: ADM-NAV-01, ADM-NAV-02, ADM-AUTH-01, UI-TBL-01, UI-ID-01  
Priority: P0/P1  
Primary package: `experimental/apps/oridecon-admin`  
Depends on: doc 02 render scopes, doc 03 controller lifecycle

## 1. Problem statement

Admin navigation currently has multiple incompatible protocols:

- a document-level click listener intercepts eligible plain same-origin anchors
  and asks HTMX to swap the whole `body`;
- settings and other explicit links target `#main-content`;
- request context classifies a fragment from client-controlled `HX-Target`;
- renderers independently decide full versus partial output;
- `AdminNavPushMiddleware` adds history only for body/no-target requests;
- topbar, impersonation banner, and breadcrumbs are siblings of
  `#main-content`, so swapping that node alone leaves route-dependent shell
  state stale.

There is no single owner for title, breadcrumbs, active navigation, history,
scroll, focus, announcements, cancellation, failures, or authentication expiry.
The table script has the same ownership problem at a smaller scale, and the
command palette can expose privileged defaults to a restricted user.

## 2. One typed navigation contract

### 2.1 Server-side types

Add an admin navigation module, for example
`src/oridecon/admin/navigation/contracts.py`:

```python
class FragmentKind(StrEnum):
    DOCUMENT = "document"
    PAGE_FRAME = "page-frame"
    COMPONENT = "component"

class HistoryMode(StrEnum):
    PUSH = "push"
    REPLACE = "replace"
    NONE = "none"

@dataclass(frozen=True, slots=True)
class NavigationResponse:
    kind: FragmentKind
    content: RenderValue
    canonical_url: str
    title: str
    history: HistoryMode
    focus_id: str | None = None
    announcement: str | None = None
```

`AdminRenderer` is the only conversion from this contract to an HTTP response.
Controllers return page/view models or a `NavigationResponse`; they do not
hand-roll `HX-*` headers or choose shell templates independently.

The response builder must:

- render a complete document only for a non-HTMX document request;
- render one exact outer page-frame root for page navigation;
- render the addressed component root for component requests;
- set `Vary: HX-Request, HX-Target, X-Oridecon-Fragment` where response shape
  differs and use private/no-store cache policy for authenticated pages;
- produce at most one case-insensitive `HX-Push-Url` or `HX-Replace-Url` header;
- preserve request `root_path`, path, and query in the canonical URL;
- never infer authorization from fragment kind or target name.

### 2.2 Trusted fragment classification

Do not let arbitrary `HX-Target` select any server template. Add named request
helpers emitted by framework components:

- `X-Oridecon-Fragment: page-frame` for primary GET navigation;
- `X-Oridecon-Fragment: component:<scope-key>` for an endpoint explicitly
  declared to support that component fragment.

The route/renderer owns an allowlist of supported fragment kinds and target
keys. `HX-Target` remains useful for diagnostics and compatibility, but it is
validated against the server-owned response target. Unknown/mismatched values
return a structured 400 or a full hard-navigation redirect; they never expose a
different internal view.

During one compatibility release, map the known body/`main-content` targets to
`PAGE_FRAME` with a deprecation response header in debug/test. Remove generic
classification after all framework links migrate.

## 3. Canonical page frame

Restructure `ui/templates/shell.py` and `shell_sections.py` so one outer root,
`#admin-page-frame`, contains every route-sensitive shell region:

- sidebar and active navigation state;
- topbar/search trigger;
- impersonation banner;
- breadcrumbs;
- flash region associated with navigation;
- the main heading and content;
- page-scoped dialogs/controllers.

The persistent outer shell owns only document assets, the global live-region /
toast host, and the page-frame insertion point. If preserving the sidebar DOM
is later shown to be materially necessary, move it out only with an explicit
OOB active-state contract and tests; do not silently return to swapping
`#main-content` alone.

Page navigation targets `#admin-page-frame` with `outerHTML`. Full documents and
frame fragments render that root from the same function. The frame stores safe
metadata as data attributes/JSON (`data-page-title`, canonical URL, focus
candidate) so initial load, after-swap, and history restore use the same source.

Benefits of the intentionally broad frame boundary:

- active sidebar, banner, topbar, breadcrumbs, and content cannot disagree;
- IDs and controller ownership reset as one render scope;
- no out-of-band patch list has to stay synchronized;
- no nested `html`/`body` can be inserted into page content.

## 4. Link and form behavior

### 4.1 Progressive enhancement

Introduce `AdminLink` / `admin_nav_attrs()` and use it for framework-owned
primary navigation. It renders:

- a canonical, prefix-aware `href` that works without JavaScript;
- HTMX GET metadata targeting the page frame;
- a busy indicator relationship;
- optional current-page semantics.

Delete the broad document click interceptor. A plain anchor remains a plain
anchor. Modified clicks, non-left clicks, downloads, external URLs, target
windows, hashes, opt-out links, and content-editor links retain native browser
behavior without a growing blacklist.

Forms keep canonical method/action and server redirects. Enhanced forms target
either their own component root or the page frame as declared by the route.
Mutation endpoints continue to enforce CSRF and permission checks regardless of
request headers.

### 4.2 Prefix-safe URL generation

All links, form actions, redirects, login return URLs, static URLs, palette
results, and push/replace URLs use the existing mounted request URL builder.
Test `/admin`, `/ops/console`, and an ASGI `root_path` deployment. No JavaScript
concatenates `"/admin"`.

Fix `AdminNavPushMiddleware._build_push_url()` immediately:

1. decode/use `raw_path` for the path when present;
2. always append `?` plus `query_string` when non-empty;
3. include normalized `root_path` exactly once;
4. reject CR/LF and non-relative output;
5. replace an existing case-insensitive history header rather than append a
   second value.

Add direct ASGI tests for raw path + query, encoded path, root path, empty query,
existing mixed-case header, and duplicate prevention.

Prefer moving history choice out of this middleware into
`NavigationResponse`. Keep the middleware only as a one-release compatibility
adapter, then delete it.

## 5. Client navigation lifecycle

Move lifecycle code from inline `shell_scripts.py` into a versioned shipped
asset `static/js/admin-navigation.js`, registered through doc 03's controller
runtime.

### 5.1 Request and cancellation

- Only page-frame requests participate in the page-navigation coordinator.
- Assign a monotonically increasing request token per shell.
- Before a new primary navigation starts, abort the prior frame request. An old
  response must never replace a newer frame.
- Mark the frame/shell `aria-busy=true`, disable only controls whose duplicate
  action is unsafe, and expose a visible delayed progress state without
  flashing for fast requests.
- Clear busy state on settle, cancellation, error, hard redirect, and teardown.
- Component requests have their own root-scoped cancellation policy and do not
  cancel unrelated tables/forms.

### 5.2 History and title

The server is authoritative:

- ordinary successful primary GET: `PUSH` exact path + query;
- redirect/canonicalization: `REPLACE` canonical exact URL;
- validation/component refresh: usually `NONE`;
- table state declares its own mode per action (section 7).

On initial load, swap, and history restore, read `data-page-title` and update
`document.title`. HTMX snapshots must restore the matching frame/title pair.
Never derive a title by scraping arbitrary text after the fact.

### 5.3 Scroll, focus, and announcements

- For a new primary push, reset `.admin-shell-scroll` (the actual scroll owner)
  after the frame is inserted but before focus; do not call only
  `window.scrollTo`.
- Store/restore per-history-entry shell scroll for Back/Forward. A pop/history
  restore does not apply the new-navigation reset.
- Focus the declared target or first page `<h1 tabindex="-1">` after a
  user-initiated primary navigation. Do not steal focus after background table
  refresh or validation.
- A persistent `role=status aria-live=polite aria-atomic=true` announces the
  page title once. Errors use an assertive alert/toast only when immediate
  attention is required.
- Preserve focus by stable ID inside component replacement where possible;
  otherwise focus the component heading/error summary.
- Honor reduced motion for progress/scroll behavior.

### 5.4 Failures and response validation

Before swapping a frame fragment, validate that it contains exactly one
`#admin-page-frame` root and no `html`/`body` ancestor. If contract validation
fails, log a correlation ID and perform a canonical full navigation rather than
nesting a document.

On network/5xx failure, keep the old frame visible, clear busy state, announce
failure, and offer Retry plus a normal link. Never push a failed URL or replace
the page with an empty error body.

Response policy:

| Response | Enhanced behavior | No-JS behavior |
| --- | --- | --- |
| 2xx page frame | validated swap + declared history/title/focus | full page 2xx |
| 3xx canonical success | full/navigation renderer resolves to exact canonical response; no duplicate history | native redirect |
| 401/419 session expiry | auth-expiry handler performs hard navigation to prefix-safe login URL | 303 login redirect |
| 403 | permission-safe forbidden page/frame; no hidden data | full forbidden page |
| 404 | not-found page/frame with canonical URL | full not-found page |
| 422 form validation | replace form/component, focus summary/first error, no page history | full form with errors |
| network/5xx | retain old frame, retry/fallback link, no history | browser/server error page |

## 6. Authentication expiry

Add one auth-response helper used by middleware/controllers:

- full request: `303` to the login route;
- HTMX request: `401` (or the chosen documented expiry status) with
  `HX-Redirect` and `X-Oridecon-Login-Url`; client `htmx:responseError` handling
  hard-navigates if the installed HTMX version does not process that status;
- return target is a validated same-origin relative URL under the configured
  mount. Sign it if existing auth flow signs state;
- no form body, query secrets, or palette text is copied into the return URL;
- authenticated fragments are `Cache-Control: private, no-store` and not
  restored across logout/login as stale privileged history.

Browser tests expire a real session during page navigation, table refresh, and
form submit. The user must reach login without nested markup, infinite retry,
or unauthorized content. After login, only a safe GET destination may resume;
mutations are never replayed automatically.

## 7. Multi-table state contract

### 7.1 Server identity and query namespaces

Each table receives a stable `table_key` from the page renderer. RenderScope
derives root, data, filter, selection-status, pagination, dialog, and form IDs.
Remove literal `table`, `table-data`, `select-all`, and global Zone IDs.

For pages with multiple URL-stateful tables, each config declares parameter
names or a namespace, for example `orders_page`, `orders_sort`,
`customers_page`. Parsing and URL generation preserve unknown/other-table
parameters. A table response can never reset another table's filters merely by
building its own URL.

### 7.2 State ownership

| State | Owner | History behavior |
| --- | --- | --- |
| filter/sort/page/per-page | server URL query + table view model | explicit push for committed page/sort; debounced search uses replace; policy tested |
| visible rows/total/all IDs | server fragment for that table | no globals |
| selected/expanded/focused rows | client table root | no URL unless a product requirement explicitly adds it |
| column widths/order | user preference store keyed by user + resource + schema version | no page history |
| in-flight request/controller resources | client root | aborted/destroyed on replacement |

A response includes immutable root-scoped JSON state. The controller never
writes instance data to `window`; code registration may be global, instance
state may not.

### 7.3 HTMX interactions

- filter/sort/page links target only that table's outer/data root as declared;
- bulk operations originate from and return to the same table key;
- second-table download/import helpers receive the initiating root explicitly;
- `allIds` comes from that table's current server result and is not overwritten
  by another response;
- out-of-order table responses are token-checked per table;
- replacement destroys Sortable/resizers/listeners and mounts one new instance;
- page-frame navigation destroys all table roots through the same lifecycle.

## 8. Authorization-aware command palette

### 8.1 Registry and filtering

Replace hard-coded defaults with an immutable registry:

```python
AdminCommand(
    id="users.list",
    label="Users",
    kind=CommandKind.NAVIGATE,
    permission="admin.users.read",
    url_factory=...,
    keywords=("accounts",),
)
```

At request time, build `AuthorizedCommandSet` using the same canonical
permission service used by endpoints/sidebar. Search only that set, plus
resource records whose resource/action permission has passed.

Semantics are important:

- `commands is None` means “resolve the registry”;
- `commands == []` means an authorized empty result and stays empty;
- no `commands or DEFAULT_COMMANDS` fallback;
- impersonation/restricted sessions use their effective capability set;
- result labels/metadata do not reveal inaccessible resource existence.

### 8.2 Typed execution

Navigation results are canonical `AdminLink`s. Action results contain an opaque
allowlisted command ID, not a JavaScript callback or arbitrary URL. Execution
POSTs to one CSRF-protected endpoint, re-resolves authorization server-side,
validates typed input, logs the action, and returns a typed component/page
response. Destructive commands require the existing confirmation policy.

Directly invoking a hidden command returns 403 even if the client fabricates a
palette result. Hiding is UX, never enforcement.

### 8.3 Palette behavior

- Dialog has an accessible name and focus trap; opening focuses input, Escape
  closes, close restores invoker focus.
- Arrow keys move active descendant; Enter runs exactly the active authorized
  result; empty state is announced and cannot activate a stale default.
- Debounce/abort search requests; discard stale responses.
- Results and IDs are scoped to the dialog instance.
- Closing/removing the frame aborts search and removes listeners.

## 9. Implementation phases

### Phase A — immediate correctness tests/fixes

- Fix query-preserving, header-replacing middleware behavior.
- Add restricted-user tests that prove authorized empty palette results stay
  empty and privileged defaults do not appear.
- Add duplicate-ID/two-table characterization tests.

### Phase B — response/frame contract

- Add contracts, renderer, request classification, and page-frame shell.
- Migrate sidebar/settings/search links and core forms.
- Keep old body/main-content compatibility adapter with diagnostics.

### Phase C — lifecycle and auth expiry

- Ship external coordinator; remove generic click interception and inline
  duplicate navigation handlers.
- Add cancellation/history/title/scroll/focus/error/expiry behavior.

### Phase D — tables and palette

- Migrate table renderers/client controller to stable keys.
- Land authorized command registry/executor and migrate all static commands.

### Phase E — remove compatibility

- Remove body-target middleware inference, old target aliases, and old script
  branches after browser telemetry/tests show no internal users.

## 10. Acceptance criteria

- [ ] One typed response contract governs document, page-frame, and component
      rendering; arbitrary `HX-Target` cannot select a view.
- [ ] The page-frame swap includes sidebar/topbar/banner/breadcrumb/content, or
      any later narrower boundary has explicit tested OOB synchronization.
- [ ] Plain links/forms work with JavaScript disabled; only explicit admin links
      enhance to frame swaps.
- [ ] Raw path + query + custom root path survives history generation exactly,
      with one history header.
- [ ] Rapid navigation cannot show a stale response; failed requests retain the
      previous page and never change history.
- [ ] New navigation resets the real shell scroller; Back/Forward restores
      matching frame, URL, title, active nav, and scroll.
- [ ] Page focus/announcement and form error focus pass keyboard tests.
- [ ] Session expiry works for page, table, and form requests without replaying
      mutations.
- [ ] Two tables preserve independent URL/client/preference state and leak no
      listeners/controllers after repeated swaps.
- [ ] Restricted users never receive or execute Users/Settings/other disallowed
      commands; an authorized empty list remains empty.
- [ ] `/admin`, a custom prefix, and ASGI `root_path` pass the production browser
      matrix.

## 11. Rollout and rollback

Ship behind `navigation_contract_v2` for one release, enabled in playground and
CI first. The flag selects the complete server+client protocol; never run old
and new click coordinators together. Record old-target compatibility warnings
in debug logs without user data.

Rollback is full-document navigation: disable enhancement and preserve canonical
links/forms. Do not roll back the query-string fix, authorization filtering,
escaping, or permission checks. Remove the flag only after all internal admin
link factories and browser scenarios use the new contract.
