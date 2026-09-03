"""Exceptions for the core subsystem.

All exceptions derive from :class:`OrideconError` so they can be caught
uniformly at the framework level.
"""

from __future__ import annotations

from oridecon.contracts.exceptions import OrideconError


class CoreError(OrideconError):
    """Base exception for all core errors."""

    _code: str = "ORI_ERR_CORE_005"


__all__ = [
    "CoreError",
]
