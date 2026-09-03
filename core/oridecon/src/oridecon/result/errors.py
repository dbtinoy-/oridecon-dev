"""Result-specific exception types."""

from __future__ import annotations

from oridecon.contracts.core.result import UnwrapError as UnwrapError

ResultError: type = UnwrapError

__all__ = ["ResultError", "UnwrapError"]
