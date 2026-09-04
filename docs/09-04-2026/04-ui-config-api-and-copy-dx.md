# 04 — UI Configuration, Assets, Public API, and Component-Copy DX

Finding IDs: UI-CFG-01, UI-CFG-02, UI-CFG-03, UI-API-01, UI-COPY-01,
UI-ASSET-01  
Priority: P2, with asset/config prerequisites for the P1 browser gate  
Depends on: docs 02 and 03

## 1. Resolved configuration must reach rendering

### Current split

- `UIProvider.register()` binds the supplied `UIConfig`, then creates unrelated
  default `HTMLDocumentConfig`, `BaseLayoutConfig`, `HeadConfig`, `FooterConfig`,
  and `ToastConfig` objects.
- `Component.__html__` constructs `UIConfig()` rather than resolving the
  provider instance; `_debug_components_enabled` caches another default.
- `UIContext` is correctly task-local but contains only theme/locale/user/extra.
- `UIConfig` says HTMX 2.0.4; `BaseLayoutConfig` says 1.9.10; `HeadConfig`
  hardcodes 1.9.10 and other third-party CDN URLs.
- `default_theme` and `theme` overlap. `auto_escape`, SSE, realtime, and several
  asset/version flags do not govern the actual render path.

### Target model

Add immutable `ResolvedUISettings` in `src/oridecon/ui/settings.py`:

```python
@dataclass(frozen=True, slots=True)
class ResolvedUISettings:
    theme: ThemePolicy
    debug_components: bool
    assets: AssetPolicy
    strict_ids: bool
```

Keep document content metadata (`lang`, title, description, favicon, extra
head) separate from application rendering policy. `UIConfig.resolve(env)` is
the only conversion from config sources to resolved settings.

Extend doc 02's `RenderContext` with these settings. Bind it at the request or
explicit render boundary:

- `UIProvider` registers the one resolved singleton and a context middleware /
  context factory;
- a request derives locale/user/request theme without mutating the singleton;
- nested components reuse the active context;
- standalone rendering constructs secure defaults (escaping on, bundled assets,
  debug off, strict IDs in tests);
- tests can pass `render_to_string(node, context=test_context)` explicitly.

Never use a process cache for request-sensitive settings. Expensive immutable
asset metadata can be cached by config fingerprint.

### Layout derivation

Refactor layout constructors/factories so `BaseLayoutConfig`, `HeadConfig`, and
related values are either:

1. caller-owned document content; or
2. deterministically derived from `ResolvedUISettings`.

Do not register disconnected default singletons. A container test must resolve
the root config, settings, and layout factory and prove a non-default theme,
debug policy, asset prefix, and locale reach rendered output.

## 2. Configuration decisions

| Current field | Decision | Migration |
| --- | --- | --- |
| `auto_escape` | Deprecate; ignored as of security migration, then remove | Config validation warns that escaping cannot be disabled; setting false never changes output |
| `default_theme`, `theme` | Replace with one typed `ThemePolicy(default, allow_user_override, storage_key)` | Accept old fields for one release; conflicting values are a validation error |
| `htmx_version`, `alpine_version`, URL fields | Remove from ordinary runtime config; versions belong to the asset manifest | Permit explicit application-supplied asset bundle object, not arbitrary version strings |
| `debug_components` | Keep, resolved by environment/request context | Production validation is an error unless explicitly acknowledged; no global default cache |
| `enable_sse` | Deprecate until an owned extension/controller and route contract exist | `true` emits “unsupported/inert” validation issue; TaskProgress uses native EventSource independently |
| `enable_realtime` | Deprecate as undefined | Replace future use with explicit feature capabilities, not a catch-all boolean |
| `HeadConfig` CDN defaults | Remove | Bundled/offline policy is default; external assets require an explicit application policy and CSP ownership |
| `extra_head`, inline CSS/JS strings | Change to structured nodes or `TrustedHTML` | Follow doc 02 allowlist/migration |

Unknown UI config keys should be errors in strict/test/production validation,
not silently ignored. If global `BaseConfig` policy requires compatibility,
report a `ConfigIssue` with the full path and a removal release.

## 3. One asset/version authority

### 3.1 Asset manifest

Create `src/oridecon/ui/assets/manifest.toml` and typed loader
`assets/manifest.py`. Each entry records:

- logical name and public filename;
- upstream project/version (or `owned`);
- SHA-256;
- license/SPDX and license-file path;
- load order/defer/module requirements;
- features/controllers that require it.

Make `oridecon-ui` the authority for shared UI runtime assets (HTMX,
Alpine/focus when still required, and `oridecon-ui.js`) and a compiled
`oridecon-ui.css` that makes the documented zero-config component surface
actually styled. Admin retains ownership of admin-specific CSS, Lucide,
Sortable, and Trix but consumes shared version metadata rather than declaring
conflicting copies.

If packaging constraints require an admin mirror of a shared file, generate it
from the UI manifest and check byte/hash equality in CI. A mirror is not a
second owner.

### 3.2 Asset policy

```python
AssetPolicy(
    mode=AssetMode.BUNDLED,
    prefix="/static/oridecon-ui",
    include=frozenset({"base", "interactions"}),
)
```

Modes:

- `BUNDLED` (secure default): package files, relative URLs, offline.
- `APPLICATION`: caller supplies a typed manifest/resolver and accepts version
  compatibility checks.
- `NONE`: render semantic/no-JS markup only; interactive components expose a
  debug diagnostic rather than silently pretending to work.

There is no default CDN mode. An application can deliberately provide external
assets through `APPLICATION`, with its own CSP and integrity policy, but tests
and admin never do.

Add `dev/checks/ui_assets.py --check` to verify files, hashes, licenses,
package-wheel inclusion, no unexpected remote URLs, no duplicate logical
versions, and generated CSS/JS freshness.

### 3.3 Remove Font Awesome assumptions

Follow doc 03's Icon migration. The asset manifest must not add Font Awesome as
an accidental compatibility fix.

## 4. One declarative public API registry

### 4.1 Authority

Replace hand-maintained parallel lists with
`src/oridecon/ui/exports/registry.py`:

```python
Export(
    name="Button",
    module="oridecon.ui.atoms.button",
    category="atoms",
    stability="stable",
    since="0.1.000",
    deprecated=None,
    copy_safe=True,
)
```

The registry must contain every top-level public symbol and enough metadata to
generate docs and compatibility checks. Duplicate names and missing attributes
fail generation.

### 4.2 Generated artifacts

Add `dev/generators/ui_public_api.py` with normal and `--check` modes. Generate:

- `exports/lazy.py` runtime map;
- `exports/public.py::__all__`;
- `src/oridecon/ui/__init__.pyi` static typing re-exports (prefer a stub over a
  150-line `TYPE_CHECKING` block in runtime `__init__.py`);
- category export modules only if downstream imports require them;
- `docs/PUBLIC_API.md` tables, stability, and deprecations;
- `tests/fixtures/public_api.json` compatibility snapshot.

The runtime `__init__.py` stays small: version, generated map/all, `__getattr__`,
`__dir__`. Generated files carry “do not edit” headers and source command.

### 4.3 Compatibility gate

Add `dev/checks/ui_public_api.py`:

- import every registry symbol lazily from an installed wheel and source tree;
- compare runtime `dir`, `__all__`, and typing names;
- fail removal of a stable symbol unless registry metadata includes a prior
  deprecation and allowed removal version;
- fail a documented symbol absent at runtime or a runtime public symbol absent
  from docs;
- detect eager import regressions with a subprocess module-load budget;
- compare generated files using `--check`, never rewrite in CI.

Replace the redundant 152-name canonical list with registry-derived tests. Keep
specific tests only for compatibility behavior that cannot be generated.

## 5. Closed component-copy lifecycle

### 5.1 Product decision

Copying framework implementation files verbatim is not ownership transfer. A
usable ShadCN-like workflow needs copy-safe sources, a target namespace,
provenance, dependency handling, diffs, and updates.

Create dedicated copy sources under
`src/oridecon/ui/registry/components/<name>/`. They may be generated from
canonical components only if the result is self-contained; otherwise maintain
copy variants as explicit product assets with behavior-parity tests. Copied
files must not import `oridecon.ui` unless the registry declares
`runtime_dependency = "oridecon-ui..."` and the UX says the copy is an
extension rather than standalone ownership.

### 5.2 Registry schema

Replace mutable `ComponentEntry` lists with validated immutable records:

```python
RegistryComponent(
    name="button",
    version=1,
    files=(RegistryFile(source="button.py", target="button.py"),),
    dependencies=("icon",),
    python_requires=("markupsafe>=2.1",),
    asset_requires=("base-css",),
    exports=("Button",),
)
```

Validate acyclic dependencies, existing files, safe relative targets, hashes,
and a complete transitive closure at package build and CLI startup.

### 5.3 Target resolution

Default target is derived from the current project's `[tool.oridecon].module`:
`src/<app_package>/components/ui`. Support explicit `--output` and
`--package`, but normalize/resolved paths and reject traversal outside the
project unless `--allow-outside-project` is deliberately supplied.

Do not reproduce `oridecon/ui/...` beneath `src/components/ui`. Rewrite imports
from a declared template namespace to the target package and generate/update
`__init__.py` exports deterministically.

### 5.4 Ownership file

Write `.oridecon/ui-components.json` atomically:

```json
{
  "schema": 1,
  "source_distribution": "oridecon-ui",
  "source_version": "...",
  "target_package": "my_app.components.ui",
  "components": {
    "button": {
      "registry_version": 1,
      "files": {"src/.../button.py": {"upstream_sha256": "...", "installed_sha256": "..."}}
    }
  }
}
```

No user content is stored. Paths are project-relative. Use temp files + replace
so interruption cannot leave a half-written ownership file.

### 5.5 Commands

Keep `oridecon-ui` as the package-specific executable and optionally contribute
an `oridecon ui` group through the root CLI after doc 07 assembly is complete:

- `list [--json]`: available components and requirements;
- `add NAME... [--dry-run] [--force]`: dependency closure, planned diff,
  transactional write;
- `status`: clean/modified/upstream-changed/missing/orphaned per owned file;
- `diff NAME`: user file versus installed upstream version;
- `update NAME... [--dry-run]`: update only clean owned files; for modified
  files emit a three-way conflict and leave them untouched;
- `doctor`: validate ownership file, imports, required Python packages/assets,
  and registry version.

`--force` is explicit destructive replacement and prints/returns every replaced
path. No command silently skips a missing registry source. Unknown/missing
requirements make add fail before writing.

Do not run a package manager implicitly by default. Print exact `uv add` steps;
`--install` may be added only through doc 07's subprocess/output policy and must
be separately confirmed.

### 5.6 Isolation and parity tests

For every registry component:

1. copy into a temporary generated project;
2. remove `oridecon-ui` from import visibility (except declared runtime mode);
3. import/compile/type-check copied exports;
4. render golden behavioral cases and compare semantic DOM with canonical
   behavior where parity is promised;
5. run two-instance browser cases for interactive copies;
6. modify a file, change upstream fixture, and verify update refuses to
   overwrite and produces a useful diff;
7. simulate write failure and verify transaction rollback/ownership integrity.

Replace current path-only CLI assertions with content, import, hash,
requirements, conflict, traversal, and atomicity assertions.

## 6. Documentation migration

Update UI README, configuration, quickstart, architecture, troubleshooting, and
public API from the new authorities:

- remove claims that inert flags work;
- state the bundled/application/no-assets model;
- document escaping/trusted HTML and Slot migration;
- show request-scoped settings;
- describe copy ownership and updates;
- provide executable examples that use only stable registry symbols.

Generated API/field tables should be embedded between markers and checked in
CI. Prose remains human-owned.

## 7. Phases and acceptance

### Phase A — config and asset authority

- Land resolved settings/context integration.
- Land manifest, package data, hash/license checks, offline bundle.
- Prove application config reaches a rendered request and standalone defaults
  remain secure.

### Phase B — public API generation

- Populate registry from the current 236-name surface without unreviewed
  additions/removals.
- Generate runtime, typing, docs, snapshot.
- Add `--check` to quality CI.

### Phase C — copy lifecycle

- Define copy-safe sources/schema and ownership file.
- Implement add/status/diff/update/doctor transactionally.
- Add isolated generated-project and browser tests.

Acceptance criteria:

- [ ] One `ResolvedUISettings` instance governs request rendering and derived
      layouts; no component reconstructs/caches defaults.
- [ ] Escaping cannot be disabled and inert flags have deprecation diagnostics.
- [ ] UI/admin production and test pages have no default remote assets.
- [ ] One manifest owns shared versions/checksums/licenses and wheel inclusion.
- [ ] No Font Awesome dependency remains.
- [ ] One registry generates the complete runtime/type/docs public surface and
      CI `--check` passes.
- [ ] Stable API removal requires an enforced deprecation record.
- [ ] Copied components land in the project namespace, import in isolation,
      record hashes, honor dependencies, update safely, and never silently lose
      user edits.
