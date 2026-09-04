"""Canonical Alpine.js attribute construction.

Python keyword arguments cannot spell Alpine's colon-delimited directives.
These helpers validate directive tokens and return dictionaries that can be
expanded into ``el(...)`` without silently converting colons to hyphens.
"""

from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Final

_ARGUMENT: Final = re.compile(r"^[a-z][a-z0-9:_-]*$")
_MODIFIER: Final = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
_TRANSITION_PHASES: Final = frozenset(
    ("enter", "enter-start", "enter-end", "leave", "leave-start", "leave-end")
)


@dataclass(frozen=True, slots=True)
class AlpineExpression:
    """An authored Alpine expression, distinct from ordinary display text."""

    value: str

    def __post_init__(self) -> None:
        if not self.value.strip():
            raise ValueError("Alpine expression must not be empty")
        if "\x00" in self.value:
            raise ValueError("Alpine expression must not contain NUL")

    def __str__(self) -> str:
        return self.value


def expression(value: str) -> AlpineExpression:
    """Mark an authored string as Alpine executable syntax."""
    return AlpineExpression(value)


def _argument(value: str, *, kind: str) -> str:
    if not _ARGUMENT.fullmatch(value):
        raise ValueError(f"Invalid Alpine {kind}: {value!r}")
    return value


def _modifiers(values: tuple[str, ...]) -> str:
    if len(set(values)) != len(values):
        raise ValueError("Alpine directive modifiers must be unique")
    for value in values:
        if not _MODIFIER.fullmatch(value):
            raise ValueError(f"Invalid Alpine modifier: {value!r}")
    return "".join(f".{value}" for value in values)


class AlpineAttributes:
    """Namespace for validated, canonical Alpine attributes."""

    @staticmethod
    def expr(value: str) -> AlpineExpression:
        return expression(value)

    @staticmethod
    def data(value: AlpineExpression) -> dict[str, str]:
        return {"x-data": str(value)}

    @staticmethod
    def on(
        event: str,
        value: AlpineExpression,
        *modifiers: str,
    ) -> dict[str, str]:
        event = _argument(event, kind="event name")
        return {f"x-on:{event}{_modifiers(modifiers)}": str(value)}

    @staticmethod
    def bind(attribute: str, value: AlpineExpression) -> dict[str, str]:
        attribute = _argument(attribute, kind="bound attribute")
        return {f"x-bind:{attribute}": str(value)}

    @staticmethod
    def model(value: AlpineExpression, *modifiers: str) -> dict[str, str]:
        return {f"x-model{_modifiers(modifiers)}": str(value)}

    @staticmethod
    def show(value: AlpineExpression) -> dict[str, str]:
        return {"x-show": str(value)}

    @staticmethod
    def transition(phase: str, value: AlpineExpression) -> dict[str, str]:
        if phase not in _TRANSITION_PHASES:
            raise ValueError(f"Invalid Alpine transition phase: {phase!r}")
        return {f"x-transition:{phase}": str(value)}


alpine: Final = AlpineAttributes()

__all__ = ["AlpineAttributes", "AlpineExpression", "alpine", "expression"]
