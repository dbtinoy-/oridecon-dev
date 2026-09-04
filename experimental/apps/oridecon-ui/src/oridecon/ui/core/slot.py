"""Strict, non-mutating Slot composition for one structural child."""

from __future__ import annotations

from collections.abc import Collection, Mapping
from copy import copy
from typing import Any

from oridecon.ui.attributes import AlpineExpression
from oridecon.ui.core.base import Component, Element

_CONFLICT_ATTRS = frozenset({"href", "id", "name", "type", "value"})
_TOKEN_ARIA_ATTRS = frozenset({"aria-describedby", "aria-labelledby"})
_REF_ATTRS = frozenset({"ref", "x-ref"})


def _attribute_name(name: str) -> str:
    """Normalize Python-friendly attribute aliases to their rendered name."""
    if name == "class_":
        return "class"
    if name.endswith("_") and "_" not in name[:-1]:
        return name[:-1]
    return name.replace("_", "-")


def _canonical_attrs(attrs: Mapping[str, Any]) -> dict[str, Any]:
    canonical: dict[str, Any] = {}
    for raw_name, value in attrs.items():
        if not isinstance(raw_name, str) or not raw_name:
            raise TypeError("Slot attribute names must be non-empty strings")
        name = _attribute_name(raw_name)
        if name in canonical and canonical[name] != value:
            raise ValueError(f"Conflicting Slot aliases for attribute {name!r}")
        canonical[name] = value
    return canonical


def _tokens(*values: Any) -> str:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value is None:
            continue
        for token in str(value).split():
            if token not in seen:
                seen.add(token)
                result.append(token)
    return " ".join(result)


def _serialize_style(value: Mapping[Any, Any]) -> str:
    declarations: list[str] = []
    for name, item in value.items():
        if not isinstance(name, str) or not name.strip():
            raise TypeError("Slot style property names must be non-empty strings")
        declarations.append(f"{name.strip()}: {item}")
    return "; ".join(declarations)


def _merge_style(child: Any, parent: Any) -> Any:
    if child is None:
        return _serialize_style(parent) if isinstance(parent, Mapping) else parent
    if parent is None:
        return _serialize_style(child) if isinstance(child, Mapping) else child
    if isinstance(child, Mapping) and isinstance(parent, Mapping):
        merged = dict(parent)
        merged.update(child)
        return _serialize_style(merged)
    if isinstance(child, str) and isinstance(parent, str) and child == parent:
        return child
    raise ValueError(
        "Slot cannot merge conflicting style strings or mixed style representations"
    )


def _event_attribute(name: str) -> str:
    if name.startswith(("x-on:", "@")):
        return name
    return f"x-on:{name}"


def _resolve_element(child: Any) -> Element:
    """Resolve a component chain to exactly one local Element root."""
    candidate = child
    seen: set[int] = set()
    while isinstance(candidate, Component):
        identity = id(candidate)
        if identity in seen:
            raise TypeError("Slot child component rendering contains a cycle")
        seen.add(identity)
        delegated = candidate._render_as_child()
        candidate = delegated if delegated is not None else candidate.render()
    if not isinstance(candidate, Element):
        raise TypeError(
            "Slot requires exactly one Element root; text, fragments, and trusted HTML "
            "cannot receive attributes"
        )
    return candidate


class Slot(Component):
    """Merge attributes into one Element without mutating caller-owned values.

    Child attributes win by default. Identity/navigation/form conflicts are
    rejected unless their rendered attribute name is listed in ``overrides``.
    Event composition accepts only :class:`AlpineExpression` values so raw
    JavaScript strings are never concatenated implicitly.
    """

    def __init__(
        self,
        child: Any,
        *,
        attrs: Mapping[str, Any] | None = None,
        class_name: str = "",
        events: Mapping[str, AlpineExpression] | None = None,
        ref: str | None = None,
        overrides: Collection[str] = (),
    ) -> None:
        super().__init__()
        self._slot_child = child
        self._slot_attrs = dict(attrs or {})
        self._slot_class_name = class_name
        self._slot_events = dict(events or {})
        self._slot_ref = ref
        self._slot_overrides = frozenset(_attribute_name(name) for name in overrides)

    def render(self) -> Element:
        """Return a shallow structural clone with deterministic merged attrs."""
        child = _resolve_element(self._slot_child)
        child_attrs = _canonical_attrs(child.attrs)
        slot_attrs = _canonical_attrs(self._slot_attrs)

        for name in slot_attrs:
            if name.startswith(("x-on:", "@")):
                raise TypeError("Pass Slot event handlers through events=, not attrs=")
            if name in _REF_ATTRS:
                raise TypeError("Pass a Slot reference through ref=, not attrs=")

        child_class = child_attrs.pop("class", None)
        slot_class = slot_attrs.pop("class", None)
        classes = _tokens(child_class, slot_class, self._slot_class_name)

        child_style = child_attrs.pop("style", None)
        slot_style = slot_attrs.pop("style", None)
        style = _merge_style(child_style, slot_style)

        merged = dict(child_attrs)
        for name, value in slot_attrs.items():
            if name not in merged:
                merged[name] = value
                continue
            if merged[name] == value:
                continue
            if name in _TOKEN_ARIA_ATTRS:
                merged[name] = _tokens(merged[name], value)
            elif name.startswith("aria-"):
                raise ValueError(f"Conflicting scalar accessibility attribute {name!r}")
            elif name in _CONFLICT_ATTRS and name not in self._slot_overrides:
                raise ValueError(
                    f"Conflicting Slot attribute {name!r}; declare an explicit override"
                )
            elif name in self._slot_overrides:
                merged[name] = value
            # All other ordinary attributes are child-wins.

        child_refs = [merged.pop(name) for name in _REF_ATTRS if name in merged]
        if len({str(value) for value in child_refs}) > 1:
            raise ValueError("Slot child declares multiple refs")
        child_ref = child_refs[0] if child_refs else None
        if self._slot_ref is not None:
            if not self._slot_ref.strip():
                raise ValueError("Slot ref must not be blank")
            if child_ref is not None and child_ref != self._slot_ref:
                raise ValueError("Slot cannot merge multiple refs")
            merged["x-ref"] = self._slot_ref
        elif child_ref is not None:
            merged["x-ref"] = child_ref

        for event, expression in self._slot_events.items():
            if not isinstance(expression, AlpineExpression):
                raise TypeError("Slot events must use AlpineExpression values")
            name = _event_attribute(event)
            existing = merged.get(name)
            if existing is None:
                merged[name] = expression
            elif isinstance(existing, AlpineExpression):
                merged[name] = AlpineExpression(f"{existing}; {expression}")
            else:
                raise TypeError(
                    f"Slot cannot compose untyped string event handler {name!r}"
                )

        if classes:
            merged["class"] = classes
        if style is not None:
            merged["style"] = style

        clone = copy(child)
        clone.attrs = merged
        clone.children = list(child.children)
        return clone


__all__ = ["Slot"]
