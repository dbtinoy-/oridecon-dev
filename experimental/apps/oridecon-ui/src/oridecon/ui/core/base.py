from __future__ import annotations

from collections.abc import Callable, Iterable
from contextvars import ContextVar, Token
from copy import copy
import html
import importlib
import re
from types import TracebackType
from typing import Any, Self, cast
import warnings

from markupsafe import Markup

from oridecon.logging import get_logger
from oridecon.ui.core.render_context import ensure_render_context, get_render_context
from oridecon.ui.core.trusted_html import TrustedHTML

logger = get_logger(__name__)

#: Declared minor release in which the legacy trust/deprecation shims are
#: removed. All framework call sites must migrate in this release; the shims
#: below are the only temporary rollback mechanism and always warn.
_LEGACY_TEARDOWN_VERSION = "0.2.0"

#: (name, replacement) pairs already warned — deduplicates the warning emitted
#: per framework call site so a table of 50 rows does not flood the log.
_deprecation_warned: set[tuple[str, str]] = set()


def _warn_deprecated(name: str, replacement: str) -> None:
    """Emit one deduplicated DeprecationWarning for a legacy render API."""
    key = (name, replacement)
    if key in _deprecation_warned:
        return
    _deprecation_warned.add(key)
    warnings.warn(
        f"oridecon.ui: {name} is deprecated and will be removed in "
        f"v{_LEGACY_TEARDOWN_VERSION}; use {replacement}",
        DeprecationWarning,
        stacklevel=3,
    )


def _legacy_markup(value: Markup) -> TrustedHTML:
    """Convert a markupsafe ``Markup`` into an attributed trust grant.

    ``Markup`` is a plain-string subclass that previously bypassed escaping
    anywhere it was rendered. It is kept working for one migration window as a
    deduplicated deprecation adapter; the string is never re-sanitized here.
    """
    _warn_deprecated(
        "markupsafe.Markup",
        "trusted_html(value, source=...) after sanitizing the markup",
    )
    return TrustedHTML(
        value=str(value),
        source="legacy markupsafe.Markup compatibility adapter",
    )

_ALPINE_ARGUMENT_RE = re.compile(r"^[a-z][a-z0-9:_-]*$")
_ALPINE_MODIFIER_RE = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
_ALPINE_COLON_FAMILIES = ("x-on", "x-bind", "x-transition")


def _validate_alpine_attribute_name(name: str) -> None:
    """Reject Alpine spellings that browsers retain but Alpine ignores."""
    if not name.startswith("x-"):
        return
    if name != name.lower():
        raise ValueError(f"Alpine attribute names must be lowercase: {name!r}")
    if "--" in name:
        raise ValueError(f"Malformed Alpine attribute name: {name!r}")

    for family in _ALPINE_COLON_FAMILIES:
        if name.startswith(f"{family}-"):
            raise ValueError(
                f"Malformed Alpine attribute {name!r}; use {family}:<argument>"
            )
        if name.startswith(f"{family}:"):
            directive, *modifiers = name[len(family) + 1 :].split(".")
            if not _ALPINE_ARGUMENT_RE.fullmatch(directive):
                raise ValueError(f"Invalid Alpine directive argument in {name!r}")
            if any(
                not _ALPINE_MODIFIER_RE.fullmatch(item) for item in modifiers
            ) or len(set(modifiers)) != len(modifiers):
                raise ValueError(f"Invalid Alpine directive modifiers in {name!r}")
            return

    if name in {"x-on", "x-bind"} or name.startswith(("x-on.", "x-bind.")):
        raise ValueError(f"Alpine attribute {name!r} requires a directive argument")
    if name.startswith("x-transition."):
        modifiers = name.removeprefix("x-transition.").split(".")
        if any(not _ALPINE_MODIFIER_RE.fullmatch(item) for item in modifiers) or len(
            set(modifiers)
        ) != len(modifiers):
            raise ValueError(f"Invalid Alpine transition modifiers in {name!r}")


# Prefer a real `htpy` module when available, but tolerate environments
# without it (tests, minimal installs). We expose an `el` factory that
# constructs a real htpy element when possible, otherwise falls back to
# our lightweight `Element` implementation.

try:
    _htpy = importlib.import_module("htpy")
except ImportError:  # pragma: no cover - networks / minimal envs
    _htpy = None  # type: ignore[assignment]


def _load_htpy_structure_types() -> tuple[type[Any], ...]:
    """Load the concrete public htpy node types supported by this adapter.

    Trust is based on library types, never on an object's module name or the
    mere presence of ``__html__``. Dynamic lookup keeps htpy optional and lets
    older supported releases omit node categories they do not expose.
    """
    if _htpy is None:
        return ()
    candidates = (
        getattr(_htpy, name, None)
        for name in ("BaseElement", "Fragment", "ContextConsumer", "ContextProvider")
    )
    return tuple(candidate for candidate in candidates if isinstance(candidate, type))


_HTPY_STRUCTURE_TYPES = _load_htpy_structure_types()


def _is_html_structure(value: Any) -> bool:
    """Return whether ``value`` has an explicitly supported HTML provenance."""
    return isinstance(
        value,
        (Element, RawHTML, TrustedHTML, *_HTPY_STRUCTURE_TYPES),
    )


def _declared_renderer(value: Any) -> Callable[[], Any] | None:
    """Return a render method declared by the value's concrete type.

    Instance-level ``__getattr__`` fallbacks (notably mocks) must not create an
    accidental render protocol: calling a dynamically fabricated ``render``
    can recurse forever and bypass the typed structure boundary.
    """
    if not callable(getattr(type(value), "render", None)):
        return None
    renderer = value.render
    return renderer if callable(renderer) else None


class Element:
    """A lightweight, structured HTML element compatible with htpy.

    This provides a small subset of behaviour we need: HTML attribute
    escaping, boolean attributes, self-closing tag handling and a stable
    `__html__`/`__str__` API so our `render_to_string` function can
    consistently produce HTML regardless of whether `htpy` is present.
    """

    SELF_CLOSING = {"input", "img", "br", "hr", "meta", "link"}

    def __init__(self, tag: str, *children: Any, **attrs: Any) -> None:
        self.tag = tag
        self.children = list(children)
        self.attrs = attrs

        # If leading children are dicts, use them as attributes (htpy-style)
        while self.children and isinstance(self.children[0], dict):
            self.attrs.update(self.children.pop(0))

        if "children" in self.attrs:
            raise TypeError(
                "Element/el() do not accept children=; pass children "
                "positionally or use fragment(...) for a pre-existing sequence"
            )

        # Auto-add type="button" for HTMX-enabled buttons to avoid accidental form submits
        if self.tag == "button":
            if "type" not in self.attrs:
                # Detect HTMX-style attributes (pythonic `hx_` names)
                if any(k.startswith("hx") for k in self.attrs):
                    self.attrs["type"] = "button"

            # Remove automatic `hx_trigger="load"` to prefer manual checks
            for k in list(self.attrs.keys()):
                if k in ("hx_trigger", "hx-trigger"):
                    if str(self.attrs[k]) == "load":
                        del self.attrs[k]

        # Support Streamlit-like `with` usage by adding ourselves to the current context
        add_child_to_current(self)

    def __enter__(self) -> Self:
        _enter_composition_context(self)
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        _exit_composition_context(self)

    def __html__(self) -> str:
        if get_render_context() is None:
            with ensure_render_context():
                return self.__html__()

        parts: list[str] = [f"<{self.tag}"]
        for k, v in self.attrs.items():
            # Map pythonic kwarg names like `class_` to `class`, `for_` to `for`,
            # and convert internal underscores to hyphens so `hx_post` -> `hx-post`.
            if k == "class_":
                attr_name = "class"
            elif k.endswith("_") and "_" not in k[:-1]:
                # Handles `for_`, `id_` (reserved words or trailing underscores)
                attr_name = k[:-1]
            else:
                attr_name = k.replace("_", "-")

            _validate_alpine_attribute_name(attr_name)

            if v is True:
                parts.append(f" {attr_name}")
            elif v is False or v is None:
                continue
            else:
                parts.append(f' {attr_name}="{html.escape(str(v), quote=True)}"')

        if self.tag in self.SELF_CLOSING:
            parts.append(" />")
            return "".join(parts)

        parts.append(">")

        for c in self.children:
            parts.append(_render_child(c))

        parts.append(f"</{self.tag}>")
        return "".join(parts)

    def __str__(self) -> str:  # pragma: no cover - exercised indirectly
        return self.__html__()


class RawHTML(TrustedHTML):
    """Compatibility wrapper for the legacy unattributed ``raw()`` API."""

    __slots__ = ()

    def __new__(cls, value: str) -> "RawHTML":
        _warn_deprecated(
            "raw()/RawHTML",
            "trusted_html(value, source=...) after sanitizing the markup",
        )
        return TrustedHTML.__new__(cls, value, "legacy raw() compatibility adapter")


def raw(value: str) -> RawHTML:
    return RawHTML(value)


def el(tag: str, *children: Any, **attrs: Any) -> Any:
    """Construct an element using `htpy` when available, otherwise
    return an `Element` fallback that implements `__html__`.

    For self-closing tags we prefer our local Element to ensure consistent
    output (including trailing slash), even when `htpy` is installed.
    """
    # Ensure deterministic, self-closing rendering for known empty tags
    if tag in Element.SELF_CLOSING:
        return Element(tag, *children, **attrs)

    # We always use our local Element for blocks that might be used with `with`,
    # even if htpy is present, to ensure they support the context manager protocol.
    return Element(tag, *children, **attrs)


def _render_child(child: Any) -> str:
    """Render one Element child under the framework's escaping policy.

    Policy — *strings are data, elements are structure*:

    - Plain strings are escaped (they are text content). This includes
      plain strings returned by ``Component.render()``: a component is
      resolved first and its string result is treated as data.
    - ``TrustedHTML`` (including source-attributed grants) and framework
      ``Element`` / concrete supported htpy nodes pass through verbatim.
      ``markupsafe.Markup`` and legacy ``raw()`` pass through during one
      documented migration window through an attributed compatibility
      adapter that warns. An arbitrary ``__html__`` method does not grant
      markup trust.
    - Iterables are rendered element-wise under the same policy.

    This closes the previous inconsistency where a ``Component`` child
    bypassed escaping entirely (``render_to_string`` returns strings
    verbatim), so a component whose ``render()`` returned
    ``"<b>" + user_input + "</b>"`` injected unescaped markup.
    """
    if child is None:
        return ""
    if isinstance(child, Markup):
        return _render_child(_legacy_markup(child))
    # Explicit framework/trusted/htpy values are structure — checked before
    # the plain-string branch because TrustedHTML is a str subclass.
    if _is_html_structure(child):
        return render_to_string(child)
    if isinstance(child, str):
        return html.escape(child, quote=False)
    if isinstance(child, Component):
        as_child_result = child._render_as_child()
        if as_child_result is not None:
            return _render_child(as_child_result)
        return _render_child(child.render())
    renderer = _declared_renderer(child)
    if renderer is not None:
        return _render_child(renderer())
    if isinstance(child, Iterable) and not isinstance(child, (bytes, dict)):
        return "".join(_render_child(item) for item in child)
    return render_to_string(child)


def render_child_to_string(value: Any) -> str:
    """Render one nested value for wrappers that must inspect owned markup.

    This boundary always treats plain strings and plain component results as
    text — the same policy as the top-level renderer since the unified trust
    boundary landed. New wrappers should preserve nodes directly; this adapter
    exists for the small set that must inspect or transform form structure
    before rendering.
    """
    if get_render_context() is None:
        with ensure_render_context():
            return render_child_to_string(value)
    return _render_child(value)


def fragment(*values: Any) -> tuple[Any, ...]:
    """Build an ordered render sequence from a pre-existing iterable.

    Positional children remain canonical for ``el``/``Component``. This helper
    exists for the case where a child sequence already lives in a list and
    must be spread without inventing a ``children=`` keyword. Tuples render
    element-wise under the same escaping policy.
    """
    return tuple(values)


# Compatibility state for Streamlit-like ``with`` composition. ContextVars
# keep implicit parents task-local while immutable tuples prevent child tasks
# from sharing and mutating one process-wide stack.
_CompositionStack = tuple[Any, ...]
_CompositionEntry = tuple[Any, Token[_CompositionStack]]
_NoContextEntry = tuple[Any, Token[bool]]

_context_stack: ContextVar[_CompositionStack] = ContextVar(
    "oridecon_ui_composition_stack", default=()
)
_context_entries: ContextVar[tuple[_CompositionEntry, ...]] = ContextVar(
    "oridecon_ui_composition_entries", default=()
)
_no_context: ContextVar[bool] = ContextVar(
    "oridecon_ui_composition_disabled", default=False
)
_no_context_entries: ContextVar[tuple[_NoContextEntry, ...]] = ContextVar(
    "oridecon_ui_no_context_entries", default=()
)


def _enter_composition_context(parent: Any) -> None:
    """Push ``parent`` in the current task and retain its reset token."""
    token = _context_stack.set((*_context_stack.get(), parent))
    _context_entries.set((*_context_entries.get(), (parent, token)))


def _exit_composition_context(parent: Any) -> None:
    """Pop ``parent`` with strict LIFO validation and deterministic cleanup."""
    entries = _context_entries.get()
    matching_index = next(
        (
            index
            for index in range(len(entries) - 1, -1, -1)
            if entries[index][0] is parent
        ),
        None,
    )
    if matching_index is None:
        raise RuntimeError("Composition context is not active in this task")

    _, token = entries[matching_index]
    is_lifo = matching_index == len(entries) - 1 and (
        bool(_context_stack.get()) and _context_stack.get()[-1] is parent
    )
    # Resetting the token restores the exact stack from before this parent was
    # entered. On a mismatched exit this also removes any poisoned descendants.
    _context_stack.reset(token)
    _context_entries.set(entries[:matching_index])
    if not is_lifo:
        raise RuntimeError("Composition contexts must exit in LIFO order")


class NoContext:
    """Temporarily disable implicit child registration in the current task."""

    def __enter__(self) -> Self:
        token = _no_context.set(True)
        _no_context_entries.set((*_no_context_entries.get(), (self, token)))
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        entries = _no_context_entries.get()
        matching_index = next(
            (
                index
                for index in range(len(entries) - 1, -1, -1)
                if entries[index][0] is self
            ),
            None,
        )
        if matching_index is None:
            raise RuntimeError("NoContext is not active in this task")

        _, token = entries[matching_index]
        is_lifo = matching_index == len(entries) - 1
        _no_context.reset(token)
        _no_context_entries.set(entries[:matching_index])
        if not is_lifo:
            raise RuntimeError("NoContext managers must exit in LIFO order")


def add_child_to_current(child: Any) -> None:
    """Append ``child`` to the current task's implicit composition parent."""
    stack = _context_stack.get()
    if stack and not _no_context.get():
        stack[-1].children.append(child)


class Component:
    """Base UI Component for oridecon-admin (HTPy-backed).

    Subclasses implement `render()` which returns either a string
    or an htpy element. `render_to_string` converts to HTML.

    Components support Streamlit-style `with` usage via context manager
    methods: entering the context makes the component the current parent
    for subsequent calls to `add_child_to_current` or manual appends.
    """

    def __init__(self, *children: Any, as_child: bool = False, **props: Any) -> None:
        if as_child:
            _warn_deprecated(
                f"{type(self).__name__}(as_child=True)",
                "Slot(child, attrs=...) for explicit polymorphic composition",
            )
        self.as_child = as_child
        self.props = props
        if children:
            self.children: list[Any] = list(children)
        elif "children" in props:
            _warn_deprecated(
                f"{type(self).__name__}(children=...)",
                "positional children or fragment(...)",
            )
            self.children = list(props.pop("children", []))
        else:
            self.children = []
        # Support Streamlit-like `with` usage by adding ourselves to the current context
        add_child_to_current(self)
        self.on_mount()

    def _render_as_child(self) -> str | Any:
        """Render by delegating to the first child when ``as_child`` is True."""
        if not self.as_child or not self.children:
            return None  # signal to fall through to normal render

        child = self.children[0]
        # Local import to avoid circular import (slot.py imports Component from here)
        from oridecon.ui.core.slot import Slot

        if isinstance(child, Slot):
            return child.render()

        if isinstance(child, Component):
            # Render a shallow structural clone so polymorphic composition never
            # leaks parent attributes into a caller-owned component. Child
            # values retain the established precedence over parent defaults.
            cloned_child = copy(child)
            cloned_child.props = {**self.props, **child.props}
            cloned_child.children = list(child.children)
            return cloned_child.render()

        return child

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        # Handle auto-registration if @Injectable was used
        if hasattr(cls, "_injectable_config"):
            # Registration will happen during provider discovery
            pass

    def on_mount(self) -> None:
        """Lifecycle hook called when component is instantiated."""

    def __enter__(self) -> Self:
        _enter_composition_context(self)
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        _exit_composition_context(self)

    def add(self, *children: Any) -> Component:
        """Fluent API to add children to this component."""
        self.children.extend(children)
        return self

    def render(self) -> str | Any:
        raise NotImplementedError

    def __html__(self) -> str:
        if get_render_context() is None:
            with ensure_render_context():
                return self.__html__()

        # Check asChild delegation first
        as_child_result = self._render_as_child()
        if as_child_result is not None:
            rendered = as_child_result
        else:
            from oridecon.ui.config import (
                UIConfig,  # lazy to avoid circular at import time
            )

            try:
                cfg = UIConfig()  # use defaults; provider may supply a richer instance
            except Exception as e:  # noqa: BLE001
                logger.debug("ui_config_load_failed", error=str(e))
                cfg = None

            rendered = self.render()
            debug = getattr(cfg, "debug_components", False)
            if debug:
                component_name = type(self).__name__
                logger.debug("component.render", component=component_name)
                # Inject data-component attribute on the outermost element.
                html_str = render_to_string(rendered)
                # Prepend data-component as an HTML comment marker that
                # does not mutate the element tree (safe, non-intrusive).
                return (
                    f'<!-- data-component="{html.escape(component_name)}" -->{html_str}'
                )
        return render_to_string(rendered)

    def __str__(self) -> str:
        return self.__html__()


def render_to_string(value: str | Any) -> str:
    """Render a component or htpy element to an HTML string.

    A plain Python string is **text at every render depth**, including
    top-level values and ``Component.render()`` results. HTML structure is a
    typed value (``Element`` / supported htpy nodes); verbatim markup requires
    an explicit source-attributed ``TrustedHTML`` grant. The legacy
    ``markupsafe.Markup`` and ``raw()`` values survive this migration window
    through warning compatibility adapters and are removed in
    ``v{_LEGACY_TEARDOWN_VERSION}``.
    """
    if get_render_context() is None:
        with ensure_render_context():
            return render_to_string(value)

    # None becomes empty string
    if value is None:
        return ""

    if isinstance(value, Markup):
        return render_to_string(_legacy_markup(value))

    # Note: we check for Component first to avoid infinite recursion if
    # Component implements __html__ (which it does, calling this function).
    if isinstance(value, Component):
        return render_to_string(value.render())

    # Explicit framework/trusted/htpy values are structure — checked before
    # the plain-string branch because TrustedHTML is a str subclass, and
    # before Iterable because htpy elements support iteration (``with`` use).
    if _is_html_structure(value):
        # Rendering errors are correctness failures. Falling back to ``str``
        # or ``repr`` can hide a broken form/component behind object text and
        # can invoke the same failing renderer more than once.
        return cast("str", value.__html__())

    # Strings are data: they are escaped here, exactly as they are at every
    # other render boundary.
    if isinstance(value, str):
        return html.escape(value, quote=False)

    # Iterables (lists/tuples/generators) are rendered element-wise. We
    # explicitly exclude `bytes`/`dict` as they are not HTML sequences.
    if isinstance(value, Iterable) and not isinstance(value, (str, bytes, dict)):
        # Check if the value has iter_chunks method (deprecation path)
        if hasattr(value, "iter_chunks"):
            return "".join(render_to_string(chunk) for chunk in value.iter_chunks())
        return "".join(render_to_string(v) for v in value)

    # Fallback for objects with a concrete render method but not inheriting
    # from Component. Dynamic instance attributes do not establish a protocol.
    renderer = _declared_renderer(value)
    if renderer is not None:
        return render_to_string(renderer())

    return html.escape(str(value))


# ---------------------------------------------------------------------------
# Developer-experience helpers for the "raw HTML" failure mode.
#
# The most common admin bug: a custom renderer (e.g. a ``Column.render()``
# override) returns a pre-built HTML *string*. Under the escaping policy
# above that string is treated as data and escaped, so the browser shows
# the markup as literal text (``&lt;span class=...&gt;...``). These helpers
# detect that situation at the render boundaries and log a one-time warning
# telling the developer exactly what to change.
# ---------------------------------------------------------------------------

_HTML_TAG_RE = re.compile(r"</?[a-zA-Z][a-zA-Z0-9-]*\b[^>]*>")

#: (origin, snippet-prefix) pairs already warned about — avoids log spam on
#: every cell of every request.
_warned_html_strings: set[tuple[str, str]] = set()

#: Cached debug_components flag; see _debug_components_enabled.
_debug_components_cache: bool | None = None


def looks_like_html(value: Any) -> bool:
    """Heuristic: does this string look like it contains an HTML tag?

    ``TrustedHTML`` values are (str subclass) explicitly trusted markup, not a
    renderer mistake, so they never match.
    """
    if not isinstance(value, str):
        return False
    if isinstance(value, (TrustedHTML,)):
        return False
    return bool(_HTML_TAG_RE.search(value))


def warn_html_string_render(
    origin: str,
    snippet: Any,
    *,
    fix: str = (
        "return an element built with el(...), or use "
        "trusted_html(markup, source=...) after sanitizing pre-rendered HTML"
    ),
) -> None:
    """Warn (once per origin/snippet) that a renderer returned an HTML string.

    The string will be escaped by the element layer, so the browser shows
    literal markup instead of rendered HTML. Emitting a warning here turns a
    confusing UI bug into an actionable log message.

    Args:
        origin: Where the string came from (e.g. ``Column.render() 'name'``).
        snippet: The offending string (only a prefix is kept for dedup).
        fix: Developer guidance included in the warning.
    """
    if not looks_like_html(snippet):
        return
    key = (origin, str(snippet)[:80])
    if key in _warned_html_strings:
        return
    _warned_html_strings.add(key)
    logger.warning(
        "renderer_returned_html_string origin=%r snippet=%r fix=%r",
        origin,
        str(snippet)[:120],
        fix,
    )


def _debug_components_enabled() -> bool:
    """Whether component debugging is on for this process.

    Cached because it is consulted per cell: a table of 50 rows by 8
    columns would otherwise rebuild the config 400 times per request.
    """
    global _debug_components_cache
    if _debug_components_cache is None:
        from oridecon.ui.config import UIConfig  # lazy: circular at import time

        try:
            _debug_components_cache = bool(UIConfig().debug_components)
        except Exception as e:  # noqa: BLE001
            logger.debug("ui_config_load_failed", error=str(e))
            _debug_components_cache = False
    return _debug_components_cache


def html_string_notice(value: Any, origin: str = "") -> Any:
    """Render an escaped HTML string so it reads as text, not broken markup.

    A renderer that returns an HTML *string* has its output escaped by the
    element layer, so the browser shows ``&lt;span&gt;...`` where a widget
    was intended. The escaping is correct -- strings are data -- but the
    result looks like corrupted output rather than a mistake in the code.

    This presents the value as what it actually is: literal text. The
    monospace treatment signals "not rendered markup" on its own, and when
    ``debug_components`` is enabled a short label names the origin so the
    developer can find the renderer.

    The label is gated on the debug flag rather than shown always because
    ``looks_like_html`` is a heuristic: values such as ``List<String>`` or
    ``Widget <Pro> Edition`` match it, and captioning genuine product data
    as a developer error in front of end users would be worse than the
    problem it reports.

    Args:
        value: The offending string, rendered escaped by the element layer.
        origin: Where the string came from, shown only in debug mode.

    Returns:
        An element wrapping ``value``.
    """
    code = el(
        "code",
        value,
        class_=(
            "font-mono text-xs break-all rounded bg-muted px-1 py-0.5 "
            "text-muted-foreground"
        ),
    )
    if not _debug_components_enabled():
        return code

    return el(
        "span",
        code,
        el(
            "span",
            "unrendered HTML string" + (f" from {origin}" if origin else ""),
            class_=(
                "ml-1.5 inline-flex items-center rounded border "
                "border-warning/30 bg-warning/10 px-1.5 py-0.5 text-[10px] "
                "font-medium uppercase tracking-wide text-warning"
            ),
        ),
        class_="inline-flex items-center gap-0.5 align-middle",
        title=(
            "This renderer returned an HTML string, which is escaped and "
            "shown as text. Return el(...) or use source-attributed TrustedHTML."
        ),
    )
