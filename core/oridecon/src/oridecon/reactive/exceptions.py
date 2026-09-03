"""Reactive layer exceptions."""

from __future__ import annotations

from oridecon.contracts.exceptions.base import OrideconError


class ReactiveError(OrideconError):
    """Base exception for the reactive stream layer."""


class BackpressureError(ReactiveError):
    """Raised when a subscriber channel overflows under a non-blocking policy."""
