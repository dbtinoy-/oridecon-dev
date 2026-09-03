# Public API Reference

Every symbol exported from `oridecon.ui`, grouped by category.

**Stability tiers:**
- **✓ stable** — safe for production use
- **🔬 experimental** — may change, feedback welcome
- **⚠️ deprecated** — use replacement instead

---

## Core

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `Component` | Base class for all UI components | `oridecon.ui.core.base` | ✓ stable |
| `Element` | Lightweight HTML element compatible with htpy | `oridecon.ui.core.base` | ✓ stable |
| `RawHTML` | Wrapper for verbatim HTML strings | `oridecon.ui.core.base` | ✓ stable |
| `el` | Element factory function (pythonic kwargs) | `oridecon.ui.core.base` | ✓ stable |
| `raw` | Shorthand for `RawHTML(...)` | `oridecon.ui.core.base` | ✓ stable |
| `render_to_string` | Convert any renderable to HTML string | `oridecon.ui.core.base` | ✓ stable |

### Polymorphic Pattern

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `as_child` | Parameter on `Component.__init__()` enabling slot-based delegation | `oridecon.ui.core.base` | 🔬 experimental |

**Note:** `Slot` is used internally by the `asChild` pattern. All `Component` subclasses accept `as_child` as a constructor parameter. Components supporting asChild: `Button`, `Link`, `Card`, and any custom `Component` subclass.

---

## Context

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `UIContext` | Immutable request-scoped UI context dataclass | `oridecon.ui.core.context` | ✓ stable |
| `get_ui_context` | Retrieve the current ContextVar-bound context | `oridecon.ui.core.context` | ✓ stable |
| `reset_ui_context` | Replace context with a fresh default | `oridecon.ui.core.context` | ✓ stable |
| `set_ui_context` | Bind a context to the current execution scope | `oridecon.ui.core.context` | ✓ stable |

---

## Zones

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `Zone` | Named HTMX swap target (id + swap mode) | `oridecon.ui.core.zones` | ✓ stable |
| `Zones` | Canonical registry of all swap zones | `oridecon.ui.core.zones` | ✓ stable |
| `SwapMode` | Enum of HTMX swap modes | `oridecon.ui.core.zones` | ✓ stable |

---

## Icons

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `get_icon` | Resolve icon definition by name | `oridecon.ui.atoms.icons` | 🔬 experimental |
| `IconDefinition` | Icon metadata (name, svg, category) | `oridecon.ui.atoms.icons` | 🔬 experimental |
| `IconLibrary` | Registry of named icon collections | `oridecon.ui.atoms.icons` | 🔬 experimental |

---

## HTMX Namespaces

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `htmx` | HTMX attribute generators | `oridecon.ui.htmx` | ✓ stable |
| `helpers` | HTMX helper utilities | `oridecon.ui.htmx` | ✓ stable |
| `sse` | Server-Sent Events helpers | `oridecon.ui.htmx` | 🔬 experimental |

---

## Exceptions & Errors

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `UIError` | Base exception for all UI-domain errors | `oridecon.ui.exceptions` | ✓ stable |
| `ErrorCategory` | Enum of error categories (validation, not_found, etc.) | `oridecon.ui.exceptions` | ✓ stable |
| `FieldError` | Error for a specific form field | `oridecon.ui.exceptions` | ✓ stable |
| `ErrorResponse` | Standardized error response for HTMX | `oridecon.ui.exceptions` | ✓ stable |
| `validation_error` | Factory: 422 validation error | `oridecon.ui.exceptions` | ✓ stable |
| `not_found_error` | Factory: 404 not found error | `oridecon.ui.exceptions` | ✓ stable |
| `permission_error` | Factory: 403 permission error | `oridecon.ui.exceptions` | ✓ stable |
| `server_error` | Factory: 500 server error (optional retry) | `oridecon.ui.exceptions` | ✓ stable |
| `timeout_error` | Factory: 504 timeout error | `oridecon.ui.exceptions` | ✓ stable |
| `render_validation_errors` | Render field errors to HTML | `oridecon.ui.exceptions` | ✓ stable |
| `htmx_error_response` | Build complete HTMX error response tuple | `oridecon.ui.exceptions` | ✓ stable |

---

## DI

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `UIModule` | IoC module descriptor | `oridecon.ui.module` | ✓ stable |
| `UIProvider` | Provider that registers UI services | `oridecon.ui.di.provider` | ✓ stable |

---

## Protocols

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `RenderableProtocol` | Protocol for objects with `render()` method | `oridecon.ui.protocols` | ✓ stable |

---

## Styles — Design Tokens

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `SHADCN_DEFAULT_COLORS` | Light-mode CSS custom property definitions (oklch) | `oridecon.ui.styles.design_tokens` | ✓ stable |
| `SHADCN_DARK_COLORS` | Dark-mode CSS custom property definitions (oklch) | `oridecon.ui.styles.design_tokens` | ✓ stable |
| `render_css_variables` | Generate `:root` / `.dark` CSS blocks from color maps | `oridecon.ui.styles.design_tokens` | ✓ stable |
| `render_utility_classes` | Generate `.bg-*`, `.text-*`, `.border-*` utility classes | `oridecon.ui.styles.design_tokens` | ✓ stable |
| `SEMANTIC_UTILITY_CLASSES` | Map of CSS variable utility class definitions | `oridecon.ui.styles.design_tokens` | ✓ stable |
| `shadcn_css` | Generate complete ShadCN-compatible CSS with overrides | `oridecon.ui.styles.theme` | ✓ stable |
| `get_semantic_classes` | Resolve variant name to CSS variable classes | `oridecon.ui.styles.tokens` | ✓ stable |
| `get_button_classes` | Resolve button color to CSS variable classes | `oridecon.ui.styles.tokens` | ✓ stable |
| `get_alert_classes` | Resolve alert variant to CSS variable classes | `oridecon.ui.styles.tokens` | ✓ stable |
| `get_toast_classes` | Resolve toast type to CSS variable classes | `oridecon.ui.styles.tokens` | ✓ stable |
| `get_semantic_icon` | Resolve variant to icon name | `oridecon.ui.styles.tokens` | ✓ stable |
| `BUTTON_CLASSES` | Map of button color names to CSS classes | `oridecon.ui.styles.tokens` | ✓ stable |
| `ALERT_CLASSES` | Map of alert variant names to CSS classes | `oridecon.ui.styles.tokens` | ✓ stable |
| `TOAST_CLASSES` | Map of toast type names to CSS classes | `oridecon.ui.styles.tokens` | ✓ stable |
| `SEMANTIC_CLASSES` | Map of variant names to CSS variable classes | `oridecon.ui.styles.tokens` | ✓ stable |
| `SEMANTIC_ICONS` | Map of variant names to icon names | `oridecon.ui.styles.tokens` | ✓ stable |

---

## Constants

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `UITheme` | Enum: `DEFAULT`, `DARK`, `LIGHT`, `SYSTEM` | `oridecon.ui.constants` | ✓ stable |
| `Breakpoint` | Enum: responsive breakpoints (SM–XXL) | `oridecon.ui.constants` | ✓ stable |
| `UI_CSP_REQUIREMENTS` | CSP directives for external CDN assets | `oridecon.ui.constants` | ✓ stable |
| `__version__` | Package version | `oridecon.ui.constants` | ✓ stable |

---

## Decorators

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `component` | Metadata decorator (`__component_name__`) | `oridecon.ui.decorators` | ✓ stable |

---

## Hooks

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `UIComponentRenderedHook` | Payload fired after component render | `oridecon.ui.hooks` | 🔬 experimental |
| `UITemplateRenderedHook` | Payload fired after template render | `oridecon.ui.hooks` | 🔬 experimental |

---

## Accessibility

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `AriaAttrs` | Builder for ARIA attribute dicts | `oridecon.ui.accessibility` | ✓ stable |
| `AriaLive` | Enum for aria-live values (polite/assertive/off) | `oridecon.ui.accessibility` | ✓ stable |
| `AriaRole` | Enum for common ARIA roles | `oridecon.ui.accessibility` | ✓ stable |
| `SkipLink` | Visually-hidden skip-to-content link | `oridecon.ui.accessibility` | ✓ stable |
| `announce` | Send polite/assertive live region announcement | `oridecon.ui.accessibility` | ✓ stable |
| `announce_table_update` | Announce dynamic table changes | `oridecon.ui.accessibility` | ✓ stable |
| `button_aria` | Generate ARIA attrs for buttons | `oridecon.ui.accessibility` | ✓ stable |
| `dialog_aria` | Generate ARIA attrs for dialogs | `oridecon.ui.accessibility` | ✓ stable |
| `header_aria` | Generate ARIA attrs for headers | `oridecon.ui.accessibility` | ✓ stable |
| `keyboard_navigation_script` | Script for arrow-key navigation | `oridecon.ui.accessibility` | ✓ stable |
| `row_aria` | Generate ARIA attrs for table rows | `oridecon.ui.accessibility` | ✓ stable |
| `search_aria` | Generate ARIA attrs for search regions | `oridecon.ui.accessibility` | ✓ stable |
| `table_aria` | Generate ARIA attrs for tables | `oridecon.ui.accessibility` | ✓ stable |

---

## Config

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `UIConfig` | Root configuration for the UI provider | `oridecon.ui.config` | ✓ stable |
| `DebounceConfig` | HTMX debounce trigger configuration | `oridecon.ui.config` | ✓ stable |
| `HTMLDocumentConfig` | HTML document shell generation config | `oridecon.ui.config` | ✓ stable |
| `BaseLayoutConfig` | Layout configuration (extends HTMLDocumentConfig) | `oridecon.ui.config` | ✓ stable |
| `HeadConfig` | Head section renderer config | `oridecon.ui.config` | ✓ stable |
| `FooterConfig` | Footer renderer config | `oridecon.ui.config` | ✓ stable |
| `ToastConfig` | Toast container behavior config | `oridecon.ui.config` | ✓ stable |

---

## Atoms — Primitives

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `Button` | Styled button component | `oridecon.ui.atoms.button` | ✓ stable |
| `SubmitButton` | Submit button with Alpine loading state | `oridecon.ui.atoms.button` | ✓ stable |
| `Badge` | Status/count badge | `oridecon.ui.atoms.badge` | ✓ stable |
| `Spinner` | Loading spinner (SVG) | `oridecon.ui.atoms.spinner` | ✓ stable |
| `Icon` | SVG icon renderer | `oridecon.ui.atoms.icon` | ✓ stable |
| `Divider` | Horizontal/vertical divider | `oridecon.ui.atoms.divider` | ✓ stable |
| `Link` | Anchor link component | `oridecon.ui.atoms.link` | ✓ stable |
| `Label` | Form field label | `oridecon.ui.atoms.label` | ✓ stable |
| `Fieldset` | Form field group | `oridecon.ui.atoms.fieldset` | ✓ stable |
| `FileUpload` | Basic file upload input | `oridecon.ui.atoms.file_upload` | ✓ stable |
| `ProgressBar` | Progress indicator bar | `oridecon.ui.atoms.progress_bar` | ✓ stable |
| `Skeleton` | Loading skeleton placeholder | `oridecon.ui.atoms.skeleton` | ✓ stable |
| `Switch` | Toggle switch | `oridecon.ui.atoms.switch` | ✓ stable |
| `Tooltip` | Hover tooltip | `oridecon.ui.atoms.tooltip` | ✓ stable |
| `MarkdownEditor` | Markdown text editor | `oridecon.ui.atoms.editors` | 🔬 experimental |
| `RichEditor` | Rich text (WYSIWYG) editor | `oridecon.ui.atoms.editors` | 🔬 experimental |

---

## Atoms — Layout Primitives

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `Aside` | Sidebar element | `oridecon.ui.atoms.layout` | ✓ stable |
| `Col` | Flex column | `oridecon.ui.atoms.layout` | ✓ stable |
| `Container` | Centered page container | `oridecon.ui.atoms.layout` | ✓ stable |
| `Grid` | CSS Grid layout | `oridecon.ui.atoms.layout` | ✓ stable |
| `Row` | Grid row (flex row) | `oridecon.ui.atoms.layout` | ✓ stable |
| `Stack` | Vertical stack | `oridecon.ui.molecules.stack` | ✓ stable |

---

## Atoms — Inputs

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `AbstractInput` | Base class for all input types | `oridecon.ui.atoms.inputs` | ✓ stable |
| `Input` | Generic text input | `oridecon.ui.atoms.inputs` | ✓ stable |
| `TextInput` | Text input | `oridecon.ui.atoms.inputs` | ✓ stable |
| `PasswordInput` | Password input | `oridecon.ui.atoms.inputs` | ✓ stable |
| `EmailInput` | Email input | `oridecon.ui.atoms.inputs` | ✓ stable |
| `TextArea` | Multi-line text area | `oridecon.ui.atoms.inputs` | ✓ stable |
| `NumberInput` | Numeric input | `oridecon.ui.atoms.inputs` | ✓ stable |
| `Slider` | Range slider | `oridecon.ui.atoms.inputs` | ✓ stable |
| `DateInput` | Date picker | `oridecon.ui.atoms.inputs` | 🔬 experimental |
| `TimePicker` | Time picker | `oridecon.ui.atoms.inputs` | 🔬 experimental |
| `Select` | Single select dropdown | `oridecon.ui.atoms.inputs` | ✓ stable |
| `MultiSelect` | Multi-select dropdown | `oridecon.ui.atoms.inputs` | ✓ stable |
| `NativeMultiSelect` | Native HTML multi-select | `oridecon.ui.atoms.inputs` | ✓ stable |
| `LazySelect` | Lazily-loaded select (HTMX) | `oridecon.ui.atoms.inputs` | 🔬 experimental |
| `CheckboxList` | List of checkboxes | `oridecon.ui.atoms.inputs` | ✓ stable |
| `Radio` | Radio button group | `oridecon.ui.atoms.inputs` | ✓ stable |
| `BelongsTo` | BelongsTo relationship selector | `oridecon.ui.atoms.inputs` | 🔬 experimental |
| `MorphTo` | Polymorphic relationship selector | `oridecon.ui.atoms.inputs` | 🔬 experimental |
| `Checkbox` | Single checkbox | `oridecon.ui.atoms.inputs` | ✓ stable |
| `Toggle` | Toggle input | `oridecon.ui.atoms.inputs` | ✓ stable |
| `ColorPicker` | Color picker input | `oridecon.ui.atoms.inputs` | 🔬 experimental |
| `Hidden` | Hidden input | `oridecon.ui.atoms.inputs` | ✓ stable |
| `KeyValueField` | Key-value pair input | `oridecon.ui.atoms.inputs` | 🔬 experimental |
| `Rating` | Star rating input | `oridecon.ui.atoms.inputs` | 🔬 experimental |
| `TagsInput` | Tags/token input | `oridecon.ui.atoms.inputs` | 🔬 experimental |
| `AvatarUpload` | Avatar upload with preview | `oridecon.ui.atoms.inputs` | 🔬 experimental |
| `MultiFileUpload` | Multi-file upload | `oridecon.ui.atoms.inputs` | 🔬 experimental |

---

## Molecules

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `ActionButton` | Button with action/loading state | `oridecon.ui.molecules.action_button` | 🔬 experimental |
| `Alert` | Alert/notification banner | `oridecon.ui.molecules.alert` | ✓ stable |
| `SimpleAlert` | Minimal alert variant | `oridecon.ui.molecules.simple_alert` | ✓ stable |
| `Breadcrumbs` | Breadcrumb navigation | `oridecon.ui.molecules.breadcrumbs` | ✓ stable |
| `Card` | Content card container | `oridecon.ui.molecules.card` | ✓ stable |
| `Dropdown` | Dropdown menu | `oridecon.ui.molecules.dropdown` | ✓ stable |
| `EmptyState` | Empty state placeholder | `oridecon.ui.molecules.empty_state` | ✓ stable |
| `ErrorState` | Error state display | `oridecon.ui.molecules.error_state` | ✓ stable |
| `FormField` | Form field with label, input, and error | `oridecon.ui.molecules.form_field` | ✓ stable |
| `FieldSchema` | Schema-based form field definition | `oridecon.ui.molecules.form_field` | 🔬 experimental |
| `FormActions` | Form action buttons bar | `oridecon.ui.molecules.form_actions` | ✓ stable |
| `InputGroup` | Label + input + errors composite | `oridecon.ui.molecules.input_group` | ✓ stable |
| `LoadingOverlay` | Full-area loading overlay | `oridecon.ui.molecules.loading_overlay` | ✓ stable |
| `MetricCard` | Single metric display card | `oridecon.ui.molecules.metric_card` | ✓ stable |
| `Modal` | Modal dialog | `oridecon.ui.molecules.modal` | ✓ stable |
| `Popover` | Popover/tooltip container | `oridecon.ui.molecules.popover` | ✓ stable |
| `RichSelect` | Enhanced select with search | `oridecon.ui.molecules.rich_select` | 🔬 experimental |
| `Section` | Page section wrapper | `oridecon.ui.molecules.section` | ✓ stable |
| `StatCard` | Statistics card | `oridecon.ui.molecules.stat_card` | ✓ stable |
| `Tabs` | Tabbed container | `oridecon.ui.molecules.tabs` | ✓ stable |
| `TabPanel` | Individual tab panel | `oridecon.ui.molecules.tabs` | ✓ stable |

---

## Molecules — Toasts

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `InlineToast` | Component-rendered toast | `oridecon.ui.molecules.toast` | ✓ stable |
| `ServerToastChannel` | Server-pushed toast channel | `oridecon.ui.molecules.toast` | ✓ stable |
| `Toast` | Deprecated alias for `InlineToast` | `oridecon.ui.molecules.toast` | ⚠️ deprecated |
| `ToastData` | Toast data container | `oridecon.ui.molecules.toast` | ✓ stable |
| `ToastRenderer` | Deprecated alias for `ServerToastChannel` | `oridecon.ui.molecules.toast` | ⚠️ deprecated |
| `ToastType` | Enum of toast variants | `oridecon.ui.molecules.toast` | ✓ stable |
| `flash_to_toast` | Convert flash message to toast | `oridecon.ui.molecules.toast` | ✓ stable |

---

## Molecules — Realtime / Scroll

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `InfiniteScrollTrigger` | Infinite scroll trigger element | `oridecon.ui.molecules.virtual_scroll` | 🔬 experimental |
| `VirtualScroll` | Virtual scrolling container | `oridecon.ui.molecules.virtual_scroll` | 🔬 experimental |
| `RealTimeFeed` | Real-time update feed | `oridecon.ui.molecules.realtime` | 🔬 experimental |
| `LiveCounter` | Live-updating counter | `oridecon.ui.molecules.realtime` | 🔬 experimental |

---

## Molecules — Builder

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `Builder` | Dynamic form/component builder | `oridecon.ui.molecules.builder` | 🔬 experimental |

---

## Organisms

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `Form` | Full form organism with validation | `oridecon.ui.organisms.forms` | ✓ stable |
| `Repeater` | Repeatable form section | `oridecon.ui.organisms.repeater` | 🔬 experimental |
| `Chart` | Chart component | `oridecon.ui.organisms.charts` | 🔬 experimental |
| `ActivityFeed` | Activity timeline feed | `oridecon.ui.organisms.charts` | 🔬 experimental |
| `SlideOver` | Slide-over panel | `oridecon.ui.organisms.slide_over` | 🔬 experimental |

---

## Layouts

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `LayoutBase` | Base class for layout components | `oridecon.ui.layouts.base_layout` | ✓ stable |
| `BaseLayoutContext` | Render context for layout execution | `oridecon.ui.layouts.base_layout` | ✓ stable |
| `CSSManager` | Manages CSS resource inclusion | `oridecon.ui.layouts.base_layout` | ✓ stable |
| `JSManager` | Manages JS resource inclusion | `oridecon.ui.layouts.base_layout` | ✓ stable |
| `HTMLDocument` | Full HTML document shell | `oridecon.ui.layouts.html_document` | ✓ stable |
| `FooterLink` | Link data for footer rendering | `oridecon.ui.layouts.footer` | ✓ stable |
| `FooterRenderer` | Footer section renderer | `oridecon.ui.layouts.footer` | ✓ stable |
| `HeadRenderer` | Head section renderer | `oridecon.ui.layouts.head` | ✓ stable |

---

## CLI / Registry

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `COMPONENT_REGISTRY` | Dict of 12 registerable component entries | `oridecon.ui.cli.registry` | ✓ stable |
| `ComponentEntry` | Dataclass: name, description, source_path, dependencies, requires | `oridecon.ui.cli.registry` | ✓ stable |

---

## Performance

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `RenderCache` | LRU cache for rendered components | `oridecon.ui.performance.performance` | ✓ stable |
| `RequestCoalescer` | Coalesce duplicate render requests | `oridecon.ui.performance.performance` | 🔬 experimental |
| `ResponseOptimizer` | ETag-based HTMX response optimization | `oridecon.ui.performance.performance` | ✓ stable |
| `add_htmx_timing_header` | Add server-timing headers to HTMX responses | `oridecon.ui.performance.performance` | ✓ stable |
| `cached_render` | Decorator for cached component rendering | `oridecon.ui.performance.performance` | 🔬 experimental |
| `debounced_search_attrs` | Generate debounced HTMX search attributes | `oridecon.ui.performance.performance` | ✓ stable |
| `infinite_scroll_trigger` | Generate infinite scroll HTMX attributes | `oridecon.ui.performance.performance` | ✓ stable |
| `lazy_load_placeholder` | Generate lazy-load placeholder | `oridecon.ui.performance.performance` | ✓ stable |
| `measure_render_time` | Decorator to measure component render time | `oridecon.ui.performance.performance` | 🔬 experimental |
| `optimize_htmx_response` | Apply ETag and timing to HTMX responses | `oridecon.ui.performance.performance` | 🔬 experimental |

---

## Observability

| Symbol | Description | Module | Stability |
|--------|-------------|--------|-----------|
| `MetricsCollector` | In-memory UI metrics collector | `oridecon.ui.performance.observability` | ✓ stable |
| `MetricProtocol` | Protocol for metric implementations | `oridecon.ui.performance.observability` | ✓ stable |
| `MetricType` | Enum of metric types (counter, gauge, histogram) | `oridecon.ui.performance.observability` | ✓ stable |
