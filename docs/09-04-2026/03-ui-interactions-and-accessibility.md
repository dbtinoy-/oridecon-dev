# 03 — UI Interactions, Alpine Correctness, and Accessibility

Finding IDs: UI-ALP-01, UI-INT-01, UI-INT-02, UI-TBL-01, UI-A11Y-01,
UI-FORM-01, UI-ASSET-01  
Priority: P1  
Depends on: doc 02 render values and render scopes

## 1. Goal

Make interactive components function in a real browser without global state,
stringified methods, malformed directives, fixed IDs, or implicit external icon
CSS. Every stateful root owns its data and resources, supports multiple
instances, provides deterministic teardown, and exposes truthful keyboard and
ARIA state.

## 2. Canonical attribute API and validation

### 2.1 Why kwargs are unsafe for Alpine

`Element` converts underscores to hyphens. That happens to work for `hx_get`,
but Alpine uses colons and modifiers:

- valid: `x-on:click`, `x-bind:value`, `x-transition:enter-start`;
- currently emitted: `x-bind-value`, `x-bind--class`,
  `x-transition-enter-start`.

These malformed attributes survive HTML snapshot tests and are ignored by the
browser. R17/B13 covered only `x_on_*`; the same class of defect remains.

### 2.2 Add typed helpers

Create `src/oridecon/ui/attributes/alpine.py`:

```python
state = alpine.expr("tabs")
select = alpine.expr("select(...)")
selected = alpine.expr("active")

alpine.data(state)                         # {"x-data": "tabs"}
alpine.on("click", select)                 # {"x-on:click": ...}
alpine.bind("aria-selected", selected)     # {"x-bind:aria-selected": ...}
alpine.model(alpine.expr("value"))         # {"x-model": ...}
alpine.show(selected)
alpine.transition("enter-start", alpine.expr("opacity-0"))
```

Validate event/property/modifier tokens against conservative patterns. Keep
expressions as explicitly typed `AlpineExpression` values so ordinary strings
cannot accidentally be treated as code in APIs that accept user data.

Create an equivalent namespace-aware HTML attribute validator in
`core/attributes.py`:

- reject `x-on-*`, `x-bind-*`, `x-transition-*` and any `x-*--*` output;
- reject malformed colon placement, empty directive arguments, duplicate
  modifiers, and uppercase browser-normalized names;
- permit valid `x-on:*`, `x-bind:*`, `x-transition:*`, bare `x-transition`, and
  documented dot modifiers;
- do **not** reject HTMX's distinct `hx-on-*` compatibility syntax or valid
  `hx-on:*`; test both explicitly;
- reject duplicate semantic attrs arriving through dict + kwargs.

Add `dev/checks/ui_directives.py` to parse Python AST for known-invalid keyword
families and render a component corpus to scan final HTML. Source and runtime
gates are both required.

### 2.3 Required migrations

Migrate all 10 UI binding sites, including:

- `molecules/tabs.py`;
- `molecules/builder.py`;
- `organisms/query_builder.py`;
- `organisms/task_progress.py`.

Migrate the six admin transition sites in
`admin/ui/templates/shell_sections.py`. Search the full repository for every
Alpine family rather than limiting the patch to these known lines.

## 3. Owned client-controller architecture

### 3.1 Asset and API shape

Add authored, external controller modules under
`src/oridecon/ui/static/js/controllers/` and an entry bundle
`oridecon-ui.js`. Use plain browser JavaScript with no runtime CDN or mandatory
Node build. If a build/minification step is introduced, commit the readable
source, generate the distributable, and add a `--check` reproducibility gate.

Expose one namespaced runtime:

```javascript
window.OrideconUI.register(name, factory)
window.OrideconUI.mount(root)
window.OrideconUI.destroy(root)
window.OrideconUI.scan(container)
```

A component renders:

- `data-ui-controller="tabs"` (one or space-separated names);
- stable root/child IDs from doc 02;
- a JSON `<script type="application/json" data-ui-props>` or safely encoded data
  attribute containing **data only**;
- semantic HTML that works in a basic no-JS state.

A factory returns `{ mount, destroy }` or a controller object. It stores state
on the root in a private WeakMap, never in process/window singleton data.

### 3.2 Lifecycle contract

- Initial `DOMContentLoaded`: scan document once.
- `htmx:beforeCleanupElement` / `htmx:beforeSwap`: destroy roots leaving the
  DOM before removal.
- `htmx:afterSwap` / `htmx:load`: scan only the inserted subtree.
- `destroy` is idempotent and removes listeners, timers, observers, Sortable
  instances, EventSources, AbortControllers, and references.
- Mounting an already-mounted root is a no-op or an explicit remount after
  destroy; never doubles listeners.
- Global keyboard listeners, where unavoidable, are registered by a root and
  filter to that root's active/focused state. They are removed on destroy.
- Do not use MutationObserver on the entire body as a substitute for the HTMX
  cleanup contract.
- Use event delegation inside the root where it reduces resource count.

Unit-test controller pure logic where possible; browser-test resource counts by
instrumenting constructors/addEventListener and asserting they return to the
baseline after repeated swaps.

## 4. Component-specific work

### 4.1 `InputGroup`

Path: `src/oridecon/ui/molecules/input_group.py`

- Set `self.input_type = input_type`; never assign built-in `type`.
- Validate against supported HTML input types or allow a documented custom
  string without converting it to a Python object repr.
- Associate label directly to input ID.
- Put `aria-invalid` and the complete space-separated `aria-describedby` list
  on the input. Error uses `role=alert`; help text remains available when an
  error is present unless product copy deliberately supersedes it.
- Allocate IDs from RenderScope; two groups with the same field name in
  different form scopes must not collide.

Regression: rendered `type="text"`, never `type="<class 'type'>"`.

### 4.2 `FormField`

Path: `src/oridecon/ui/molecules/form_field.py`

- Compose required marker as siblings, not `str + Element`.
- Render the input component structurally through the normal renderer; do not
  call `.render()` directly.
- Add an immutable attribute-forwarding protocol (`with_input_attrs`) or Slot;
  never mutate `input_component.props`.
- Apply `aria-invalid`, `aria-required`, and described-by IDs to the actual
  form control. Provide a protocol for components with multiple controls.
- Required marker is `aria-hidden=true`; the label/control conveys required
  semantics.
- Remove broad exception suppression. In production, component errors flow to
  the normal error boundary with a correlation ID; in debug/tests they raise.
  A generic inline box must not turn broken forms into apparently submittable
  pages.
- Conditional visibility must also define whether a hidden field is submitted;
  document and test disabled/value semantics.

### 4.3 `Tooltip`

Path: `src/oridecon/ui/atoms/tooltip.py`

Replace wrapper-only hover CSS with an owned tooltip relationship:

- require exactly one focusable trigger or explicitly wrap non-focusable
  content in a button only when the caller opts in;
- clone through Slot to place `aria-describedby` on the trigger, not an
  unrelated wrapper;
- generated tooltip ID is stable through RenderScope;
- show on hover **and focus**, hide on Escape and blur/pointer leave;
- retain while pointer moves between trigger and interactive tooltip only if
  interactive tooltips are supported; otherwise tooltip content must not be
  interactive;
- implement `top/right/bottom/left` with collision adjustment or restrict and
  validate the supported set;
- honor `prefers-reduced-motion`;
- supplied trigger IDs are resolved or rejected—never accepted and then
  ignored.

Browser tests assert accessible description, focus parity, Escape, two tooltip
instances, and edge positioning.

### 4.4 `Tabs` / `TabPanel`

Paths: `molecules/tabs.py`, controller `tabs.js`

- Render one scoped base ID; derive tab/select/panel IDs from it.
- Serialize initial tab and values as JSON data. Never use Python repr or
  single-quote interpolation for JavaScript.
- Validate unique tab values and exact panel correspondence. Unknown
  `active_tab` fails in debug and falls back with a warning only in production.
- Implement WAI-ARIA tabs:
  - one active tab has `aria-selected=true` and `tabindex=0`;
  - inactive tabs have `false` and `-1`;
  - ArrowLeft/Right (and Up/Down for vertical) wrap and move focus;
  - Home/End move focus;
  - manual activation uses Enter/Space; automatic activation is an explicit
    option;
  - selection updates panel hidden state, classes, and mobile select;
  - disabled tabs are skipped.
- URL mode stays ordinary anchors with no Alpine requirement. Custom prefix and
  query strings are treated as URLs, not script data.
- Server and client state remain synchronized after HTMX replacement.

### 4.5 Builder

Paths: `molecules/builder.py`, new `builder.js`

- JSON contains block definitions and initial items only; methods live in the
  controller factory.
- Never mutate shared field component props while rendering a block template.
  Define a field binding adapter that returns a cloned control with a scoped
  model path.
- Stable item keys are opaque strings; avoid reusing integer IDs after remove.
- Move/reorder/delete buttons have accessible names independent of icons,
  correct disabled state at boundaries, and live reorder announcements.
- Add keyboard reorder controls; drag-and-drop is enhancement only.
- Hidden JSON updates after every operation and before native form submit.
- Validate block type and payload server-side; client block definitions are not
  an authorization or schema boundary.
- Remove Font Awesome classes in favor of the owned Icon implementation.

### 4.6 QueryBuilder

Paths: `organisms/query_builder.py`, new `query-builder.js`

- Move methods from JSON to controller.
- `findNode` begins with the root, not `tree.rules`, so operations on root ID
  work. Root cannot be removed.
- Enforce max depth both when rendering and when adding groups; disabling the
  add control is not sufficient—controller refuses the operation.
- Normalize operators by field type; reset incompatible values on field change.
- Add fieldset/legend semantics or an equivalent named group structure.
- Buttons have specific accessible names (“Add rule to AND group”, “Remove
  Price rule”). Logic toggle exposes pressed/selected state.
- Hidden value updates deterministically and uses the documented schema.
- Two builders on one form do not cross-find nodes or hidden inputs.
- Replace Font Awesome with owned icons.

### 4.7 TaskProgress

Paths: `organisms/task_progress.py`, new `task-progress.js`

- Choose one initialization mechanism. The controller mounts exactly one
  EventSource; remove simultaneous Alpine automatic `init()` + `x-init`.
- Store the EventSource and Abort/timeout state per root.
- Validate progress payload shape and clamp numeric progress to 0–100.
- Use `role=progressbar` with dynamic `aria-valuenow`, min/max and an accessible
  label; status/message uses an appropriately throttled live region.
- Close on completed, failed, server error, root removal, navigation, and
  explicit cancel. Reconnect only under a documented bounded backoff policy.
- `on_complete` becomes a typed enum/action payload (navigate to safe URL or
  dispatch named event); do not execute caller-supplied callback paths.
- Retry reconnects the stream instead of reloading the whole page unless the
  caller explicitly requests reload.

Test one EventSource construction, malformed messages, disconnect/reconnect,
terminal cleanup, two roots, and HTMX removal.

### 4.8 VirtualScroll

Paths: `molecules/virtual_scroll.py`, new `virtual-scroll.js`

- Allocate root and sentinel IDs; remove `virtual-scroll-container` default.
- Scope `hx-target`/`hx-select` to the instance; default selectors must not
  reference a page-global `#table-content`.
- Prefer one sentinel per root and replace/remove it on each page; prevent
  duplicate in-flight loads.
- Keep native pagination or a “Load more” button as keyboard/no-JS fallback.
- Preserve focus and announce appended count; do not jump a keyboard user to a
  newly inserted item unexpectedly.
- Define end/error/retry states and teardown observers/requests.
- Replace spinner Font Awesome class with owned SVG/Icon plus text.

### 4.9 DataTable client behavior

Primary paths:

- UI `molecules/data_table_client_logic.py`;
- admin `ui/organisms/data_table/rendering.py` and table submodules.

Doc 05 owns admin integration; this plan owns controller rules:

- register controller code once from an external asset, never emit a global
  script per table;
- each table root owns IDs, `allIds`, selected/expanded/focused IDs, filters,
  sort/column state, Sortable/resizer instances, and requests;
- replace `document.querySelector`/`getElementById` with root queries or exact
  scoped targets;
- bulk-download/import helpers receive the initiating root rather than finding
  the first table;
- row keyboard navigation runs only while focus is in that table; Ctrl/Cmd+A
  must not steal selection elsewhere;
- update IDs from the fragment inserted into that same table only;
- no `LexigramTableInitialized`, `LexigramResizableRegistered`, or equivalent
  first-instance data globals;
- immutable server config is never overwritten by another instance's first
  render.

## 5. Icon and visual-asset ownership

Font Awesome is not shipped. Do not add a second icon library merely to make
`fas` classes work. Migrate known UI/admin sites to the existing icon API and
inline owned SVG nodes. Dynamic builder icon names pass through an allowlisted
icon registry with a fallback and accessible label; never interpolate a class
name as a dependency contract.

Add a source/render gate rejecting `fa`, `fas`, `far`, `fab`, and `fa-*` class
tokens outside an explicit migration fixture. Ensure decorative icons are
`aria-hidden`, while icon-only controls get names on the control.

Doc 04 defines shared bundle ownership and versions.

## 6. Tests and release slices

### Slice 1 — syntax and primitive bugs

- Add attribute helper/validator tests.
- Migrate malformed call sites.
- Fix InputGroup/FormField/Tooltip/Tabs.
- Run all existing snapshot/unit tests and new browser cases.

### Slice 2 — controller runtime

- Ship runtime + lifecycle integration.
- Migrate Tabs/Tooltip first as reference controllers.
- Add mount/destroy instrumentation tests.

### Slice 3 — complex editors/progress/scroll

- Migrate Builder, QueryBuilder, TaskProgress, VirtualScroll.
- Add schema, keyboard, multi-root, teardown tests.

### Slice 4 — table integration

- Pair with doc 05's scoped table markup and HTMX responses.
- Test two tables, fragment swaps, downloads/imports from the second root,
  selection isolation, and listener cleanup.

## 7. Acceptance criteria

- [ ] Source and rendered-output checks reject all invalid Alpine families and
      preserve valid Alpine and HTMX attribute forms.
- [ ] No method body is JSON-encoded as state.
- [ ] Every complex component can be mounted twice without state/selector/ID
      collision.
- [ ] Repeated HTMX replacement leaves one controller and no leaked resource.
- [ ] InputGroup and required FormField render valid, correctly related controls
      and errors.
- [ ] Tooltip and Tabs pass keyboard/focus/ARIA browser scenarios.
- [ ] QueryBuilder root operations work and max depth is enforced.
- [ ] TaskProgress creates one EventSource and closes it on every terminal or
      removal path.
- [ ] VirtualScroll has fallback controls and instance-scoped loading.
- [ ] No product UI relies on Font Awesome.
- [ ] Axe WCAG 2.2 AA scans and manual keyboard assertions pass against the
      offline component gallery in doc 06.
