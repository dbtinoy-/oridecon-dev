"""Task-local render context and deterministic DOM identity scopes."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass, field
from hashlib import blake2s
import re
from typing import Any

from oridecon.logging import get_logger

logger = get_logger(__name__)

_SAFE_SEGMENT = re.compile(r"^[a-z][a-z0-9-]*$")
_UNSAFE_SEGMENT = re.compile(r"[^a-z0-9-]+")
_MAX_READABLE_SEGMENT = 48


def _segment(value: str, *, kind: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"RenderScope {kind} must be a string")
    raw = value.strip()
    if not raw:
        raise ValueError(f"RenderScope {kind} must not be blank")

    normalized = _UNSAFE_SEGMENT.sub("-", raw.lower()).strip("-")
    if not normalized:
        normalized = "id"
    if not normalized[0].isalpha():
        normalized = f"x-{normalized}"

    changed = normalized != raw or len(normalized) > _MAX_READABLE_SEGMENT
    if len(normalized) > _MAX_READABLE_SEGMENT:
        normalized = normalized[:_MAX_READABLE_SEGMENT].rstrip("-")
    if changed:
        digest = blake2s(raw.encode("utf-8"), digest_size=3).hexdigest()
        normalized = f"{normalized}-{digest}"
    if not _SAFE_SEGMENT.fullmatch(normalized):  # pragma: no cover - invariant guard
        raise ValueError(f"RenderScope could not normalize {kind} {value!r}")
    return normalized


@dataclass
class _ScopeState:
    issued: dict[str, int] = field(default_factory=dict)
    counters: defaultdict[tuple[str, ...], int] = field(
        default_factory=lambda: defaultdict(int)
    )


class RenderScope:
    """Allocate readable, deterministic, response-local HTML IDs.

    A scope is intentionally stateful for one render response. Child scopes
    share its issuance registry so duplicate IDs cannot hide in separate
    component subtrees. Construct a fresh root scope to reproduce IDs for a
    later full or partial render.
    """

    __slots__ = ("_segments", "_state", "strict")

    def __init__(
        self,
        namespace: str = "oridecon",
        *,
        strict: bool = True,
        _segments: tuple[str, ...] | None = None,
        _state: _ScopeState | None = None,
    ) -> None:
        self._segments = _segments or (_segment(namespace, kind="namespace"),)
        self._state = _state or _ScopeState()
        self.strict = strict

    @property
    def prefix(self) -> str:
        """Return the rendered namespace prefix for diagnostics."""
        return "-".join(self._segments)

    def child(self, namespace: str) -> RenderScope:
        """Create a namespaced view that shares response-wide uniqueness."""
        return RenderScope(
            strict=self.strict,
            _segments=(*self._segments, _segment(namespace, kind="namespace")),
            _state=self._state,
        )

    def id(self, role: str, *, key: str | None = None) -> str:
        """Allocate one deterministic ID for ``role`` and an optional stable key."""
        role_segment = _segment(role, kind="role")
        parts = (*self._segments, role_segment)
        if key is None:
            self._state.counters[parts] += 1
            proposed = "-".join((*parts, str(self._state.counters[parts])))
        else:
            proposed = "-".join((*parts, _segment(key, kind="key")))

        if proposed not in self._state.issued:
            self._state.issued[proposed] = 1
            return proposed

        if self.strict:
            raise ValueError(
                f"Duplicate RenderScope ID {proposed!r}; use a unique stable key or "
                "reuse the first allocated value"
            )

        occurrence = self._state.issued[proposed] + 1
        candidate = f"{proposed}-{occurrence}"
        while candidate in self._state.issued:
            occurrence += 1
            candidate = f"{proposed}-{occurrence}"
        self._state.issued[proposed] = occurrence
        self._state.issued[candidate] = 1
        logger.warning(
            "render_scope_duplicate_id",
            proposed=proposed,
            emitted=candidate,
        )
        return candidate

    def __repr__(self) -> str:
        return f"RenderScope(prefix={self.prefix!r}, strict={self.strict!r})"


@dataclass(frozen=True, slots=True)
class RenderContext:
    """Policy and identity state shared by one render tree."""

    scope: RenderScope
    settings: Any = None


_current_render_context: ContextVar[RenderContext | None] = ContextVar(
    "oridecon_ui_render_context",
    default=None,
)


def get_render_context() -> RenderContext | None:
    """Return the current task's render context, if rendering is active."""
    return _current_render_context.get()


def get_render_scope() -> RenderScope:
    """Return the active scope or a deterministic standalone fallback."""
    context = get_render_context()
    return context.scope if context is not None else RenderScope()


@contextmanager
def render_context(context: RenderContext | None = None) -> Iterator[RenderContext]:
    """Activate ``context`` in this async task and restore the previous value."""
    active = context or RenderContext(scope=RenderScope())
    token = _current_render_context.set(active)
    try:
        yield active
    finally:
        _current_render_context.reset(token)


@contextmanager
def ensure_render_context() -> Iterator[RenderContext]:
    """Reuse an active context or create one around a standalone render."""
    current = get_render_context()
    if current is not None:
        yield current
        return
    with render_context() as created:
        yield created


__all__ = [
    "RenderContext",
    "RenderScope",
    "ensure_render_context",
    "get_render_context",
    "get_render_scope",
    "render_context",
]
