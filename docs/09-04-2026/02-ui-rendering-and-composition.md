# 02 — UI Rendering, Trust Boundaries, and Composition

Finding IDs: UI-SEC-01, UI-SEC-02, UI-CONC-01, UI-COMP-01, UI-ID-01  
Priority: P0 foundation  
Primary package: `experimental/apps/oridecon-ui`

## 1. Problem statement

The renderer has two contradictory policies. `Element` escapes direct string
children, but `render_to_string()` returns strings verbatim and recursively
uses that behavior for top-level values and component results. Wrappers then
pre-render values and wrap them in `raw()`. The apparent “strings are data”
rule can therefore be bypassed merely by crossing a component or wrapper
boundary.

Composition has the same provenance problem: structured children are often
flattened to strings; `as_child` mutates another component; `children=` means
different things in `Element` and `Component`; and implicit composition stores
its active parent in process globals.

This plan changes the governing rule to:

> **A plain Python string is text at every render depth. HTML structure is a
> typed value. Verbatim markup requires an explicit, auditable trust grant.**

Escaping is a security invariant and is not controlled by `UIConfig`.

## 2. Current evidence

Primary paths:

- `src/oridecon/ui/core/base.py`
  - `Element.__html__` and `_render_child` escape direct strings.
  - `render_to_string` returns strings unchanged.
  - any `__html__` object is treated as trusted structure.
  - `RawHTML` accepts an arbitrary string.
  - `_context_stack` and `_no_context` are process globals.
  - `Component._render_as_child` modifies `child.props` and only considers the
    first child.
  - `Component.__html__` reconstructs `UIConfig()` and can flatten the tree for
    a debug comment.
- `src/oridecon/ui/core/slot.py` calls a component's `render()` directly or
  `str()`s the child.
- `tests/unit/test_escaping_policy.py` intentionally asserts top-level strings
  pass verbatim and accepts every `__html__` object; these are characterization
  tests that must be replaced, not retained as desired behavior.
- `molecules/card.py`, admin card/layout classes,
  `oridecon-admin/ui/templates/shell.py`, and
  `oridecon-admin/engine/renderer.py` pre-render and re-mark content as raw.
- `core/zones.py` exposes fixed IDs consumed by tables, modals, flash,
  slide-over, and search controls.

## 3. Target types and contract

### 3.1 Typed render values

Add `src/oridecon/ui/core/nodes.py` as the one type authority:

```python
from collections.abc import Iterable
from typing import Protocol, TypeAlias

class Renderable(Protocol):
    def render(self) -> "RenderValue": ...

RenderValue: TypeAlias = (
    None | str | "Element" | "Fragment" | "TrustedHTML" | Renderable
)
```

`Fragment` is an immutable tuple of render values. Do not expose an arbitrary
iterable as a long-lived node: consume generators once during normalization so
rendering and ID allocation are deterministic.

Introduce one internal normalizer:

```python
def normalize(value: object, context: RenderContext) -> Node: ...
def render_node(node: Node, context: RenderContext) -> str: ...
```

All public boundaries (`render_to_string`, `Element.__html__`, component child
rendering, fragments, response helpers) call the same normalizer. There must be
no separate top-level string policy.

### 3.2 Escaping matrix

| Value | Meaning | Output rule |
| --- | --- | --- |
| `None` | no node | empty |
| `str` (including `Markup` during final state) | text | `html.escape(..., quote=False)` |
| attribute value | data | `html.escape(..., quote=True)` plus name validation |
| `Element` | framework structure | render tag/validated attrs and recursively normalize children |
| `Component` / `Renderable` | deferred structure or text | call once; recursively normalize result under the same context |
| `Fragment` / iterable compatibility | ordered children | recursively normalize each child |
| `TrustedHTML` | audited verbatim markup | emit unchanged |
| unknown object | text representation | `html.escape(str(value))` |

A component returning `"<strong>name</strong>"` therefore renders
`&lt;strong&gt;name&lt;/strong&gt;` whether top-level, nested, in a Card, in an
admin partial, or in a list.

### 3.3 Explicit trusted HTML capability

Add `src/oridecon/ui/core/trusted_html.py`:

```python
@dataclass(frozen=True, slots=True)
class TrustedHTML:
    value: str
    source: str

    def __html__(self) -> str: ...

def trusted_html(value: str, *, source: str) -> TrustedHTML: ...
```

Requirements:

- `source` is mandatory, non-empty, and names the sanitizer/template/owned
  asset responsible for the markup. It is diagnostic metadata, not a sanitizer.
- Public docs state that user input must be sanitized before this call.
- Add named constructors for known safe producers rather than sprinkling the
  generic function: e.g. `trusted_template_output`, `trusted_svg_icon`, and
  `trusted_static_script` in their owning modules.
- `TrustedHTML` is the **only final-state arbitrary verbatim string type**.
- Framework `Element` is structural and does not need a trust grant.
- Do not infer trust from `looks_like_html`, object module names, a config flag,
  or presence of `__html__`.

### 3.4 Compatibility policy

This changes a public 0.1 API, so use a short, visible migration rather than a
silent flag:

1. In the first migration release, `RawHTML`, `raw()`, `Markup`, and generic
   `__html__` enter a compatibility adapter. Each call emits one deduplicated
   `DeprecationWarning` with origin and the replacement. The adapter returns a
   `TrustedHTML` internally.
2. Framework-owned call sites are migrated in the same release. CI prohibits
   new `raw(`, `RawHTML(`, direct `Markup(`, or unregistered generic `__html__`
   use outside an allowlist file with owner/reason/removal version.
3. In the next declared minor release, `raw()` raises unless the application
   explicitly imports it from a `legacy` module. Generic `__html__` is rejected;
   known htpy values go through a registered adapter by concrete supported
   type/version.
4. In the removal release, delete the legacy module and make `Markup` ordinary
   text unless wrapped by a named trusted adapter.

Do **not** retain `auto_escape=False` as an escape hatch. Doc 04 deprecates that
field without changing this invariant.

## 4. Composition model

### 4.1 Positional children are canonical

- `el(tag, *children, **attrs)` and `Component(*children, **props)` use
  positional children only.
- Add a `children()`/`fragment()` helper for a pre-existing sequence.
- Reserve the name `children` in attributes/props. In migration release one,
  `el(..., children=...)` raises a targeted `TypeError` immediately because it
  currently becomes an HTML attribute or disappears unpredictably.
- `Component(children=...)` emits a deprecation warning and normalizes to
  positional children for one release, then raises.
- Components with semantic content use explicit parameters (`trigger=`,
  `header=`, `body=`, `footer=`) rather than overloading generic children.

### 4.2 Slot is exactly one element and never mutates it

Replace current `as_child` behavior with an explicit `Slot` contract:

```python
Slot(child, attrs=..., class_name=..., events=..., ref=...)
```

Rules:

- exactly one child is required;
- it must normalize to one `Element` (not text, fragment, trusted HTML, or a
  component producing multiple roots);
- merge creates a new Element; never modify `child.attrs`, `child.props`, or
  child lists;
- class tokens concatenate and de-duplicate while preserving child order;
- style dictionaries merge; raw style strings conflict unless identical;
- ordinary attributes are child-wins by default;
- `id`, `name`, `value`, `href`, and `type` conflicts raise unless the Slot API
  explicitly declares an override;
- event handlers compose in child-then-parent order only through typed event
  values; string concatenation is forbidden;
- multiple refs are not guessed: raise with a useful message;
- accessibility attributes merge only when their semantics allow token lists
  (`aria-describedby`, `aria-labelledby`); scalar conflicts raise.

Deprecate boolean `as_child` on the base Component. Components that support
polymorphism accept `as_child: Element | Component | None` or a documented
`child=` slot and delegate to `Slot`.

### 4.3 Remove hidden auto-parenting

Preferred final state: remove Streamlit-like constructor side effects and make
composition explicit. A constructor must not attach itself merely because
another object happens to be active.

Migration:

1. Add a source inventory and tests for all `with Component` / `with el(...)`
   uses.
2. Convert framework call sites to positional construction or `.add()`.
3. While compatibility remains, replace `_context_stack` and `_no_context`
   with `ContextVar[tuple[Parent, ...]]` and token-based reset. Never mutate a
   shared list stored in a ContextVar; set a new tuple on enter.
4. Validate strict LIFO exit. If an exception or mismatched exit occurs, reset
   from the token rather than leaving a poisoned parent.
5. Warn on implicit attachment, remove `NoContext`, then remove context-manager
   composition in the declared release.

Concurrency tests must use `asyncio.gather()` with barriers that interleave
construction in two tasks; each result must contain only its own sentinel.
Also test nested exceptions and repeated renders.

## 5. Render context and deterministic identity

Add `RenderContext` / `RenderScope` under `core/render_context.py`. Doc 04 adds
resolved policy; this plan defines identity:

```python
@dataclass(frozen=True)
class RenderContext:
    scope: RenderScope
    settings: ResolvedUISettings

class RenderScope:
    def id(self, role: str, *, key: str | None = None) -> str: ...
    def child(self, namespace: str) -> "RenderScope": ...
```

Properties:

- IDs are valid HTML IDs, deterministic for the same scope/key/tree, and unique
  within one response.
- A caller can provide a stable instance key for HTMX replacement. Random UUIDs
  are not generated during render because they break snapshots, labels, and
  server/client targeting.
- Duplicate explicit keys in one scope raise in debug/test mode and log+suffix
  only in production compatibility mode; the gate runs strict.
- Each complete response receives a root scope. A partial receives the stable
  scope key of the component it replaces.
- `Zones` becomes semantic roles (`data`, `filters`, `flash`) resolved through a
  scope; it no longer owns fixed process-wide IDs.
- Labels, descriptions, tabs, tables, modals, slide-overs, virtual scroll, and
  dashboard regions obtain IDs from the same scope.

Standalone `render_to_string(value)` creates a secure default context so simple
usage stays possible. Nested rendering must reuse the active context rather
than create a fresh scope for every component.

## 6. Call-site migration

### Phase A — characterization and inventory

Add:

- `tests/unit/core/test_render_boundary.py`
- `tests/unit/core/test_trusted_html.py`
- `tests/unit/core/test_composition_isolation.py`
- `tests/unit/core/test_slot_contract.py`
- `dev/checks/ui_trusted_html.py` with a checked-in allowlist containing path,
  owner, reason, and removal version.

Inventory all `raw`, `RawHTML`, `Markup`, `__html__`, `render_to_string` inside
constructors/wrappers, `children=`, and context-manager composition in both UI
and admin.

### Phase B — one renderer

Implement nodes, context, and normalization. Route `Element`, `Component`, and
`render_to_string` through it. Remove fallback paths that catch renderer errors
and return `repr()` as HTML; errors should preserve context and fail rendering.

### Phase C — stop trust laundering

Migrate, at minimum:

- UI Card and layout wrappers;
- admin Card, `AdminShell`, shell section builders, and layouts;
- `AdminRenderer.render_page` and `render_partial`;
- table/list/dashboard content renderers;
- toast/icon/template/static-script producers.

Pass structured values through wrappers. Where an external template engine is
the trusted producer, wrap once at its output boundary with a named adapter and
record the template autoescape policy.

`HTMLResponse` calls accept only the final renderer output. A controller must
not call `str(content)` as a fallback.

### Phase D — composition and scopes

Migrate children, Slot/as-child call sites, implicit contexts, and fixed Zones.
Do this before table/controller changes in docs 03/05 so those changes build on
stable identities.

### Phase E — deprecation enforcement

Enable warnings as errors in UI/admin tests for framework-owned deprecated
calls. Generate migration notes with before/after examples and removal release.

## 7. Security test matrix

Test every payload at all boundaries:

- `<script>alert(1)</script>`;
- `<img src=x onerror=alert(1)>`;
- `</script><script>...` in script-adjacent values;
- quotes/ampersands in text and attributes;
- malicious `Component.render()` string;
- malicious object with `__html__`;
- list/generator/nested component variants;
- Card/AdminCard/AdminShell/full page/partial/table cell/toast paths;
- debug-components on and off;
- htpy supported element and unsupported lookalike.

Assertions:

- plain payload tags never appear as nodes;
- they are escaped exactly once;
- trusted fixtures appear verbatim only through `TrustedHTML`;
- a trusted wrapper around unsanitized input is clearly visible in the trust
  allowlist (code review control);
- Content Security Policy remains defense in depth, not the escaping mechanism.

Property-based tests should generate mixed trees and assert rendering a string
at any depth produces the same escaped text. Fuzz invalid tag/attribute names
and reject them rather than emitting browser-reparsed syntax.

## 8. Acceptance criteria

- [ ] `render_to_string("<b>x</b>")` returns escaped text.
- [ ] A Component returning that string is escaped top-level and nested.
- [ ] Card, AdminCard, layouts, full pages, and partials preserve structured
      children without pre-render/re-raw cycles.
- [ ] Arbitrary `__html__` no longer grants final-state trust.
- [ ] Every verbatim framework string is a `TrustedHTML` with an attributable
      source or a temporary allowlisted legacy adapter.
- [ ] `auto_escape` cannot disable escaping.
- [ ] Slot rejects zero/multiple/non-element roots, merges deterministically,
      and does not mutate its child.
- [ ] `children=` misuse has a targeted diagnostic and a declared removal path.
- [ ] Concurrent/interleaved composition and render scopes are isolated.
- [ ] Two same-type components in one scope have unique, stable IDs; an HTMX
      replacement can reproduce its target ID from a stable key.
- [ ] UI/admin unit, type, lint, and production browser security tests pass.

## 9. Rollback and compatibility

Do not offer a global rollback to unsafe string behavior. If migration exposes
an owned renderer that intentionally returns HTML, convert that renderer to
Elements or an audited trusted producer. A temporary per-call legacy adapter is
the only rollback mechanism, is warning-producing, and must include a removal
version. Release notes must call out the security correction as a breaking
behavioral change even within 0.1.
