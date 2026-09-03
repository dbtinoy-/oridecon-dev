"""Exceptions for the oridecon-ai-safety package."""

from __future__ import annotations

from oridecon.contracts.ai.exceptions import GuardError as _ContractsGuardError


class GuardError(_ContractsGuardError):
    """Base exception for all guard-related errors."""

    _code: str = "ORI_ERR_GUARD_004"


class GuardConfigurationError(GuardError):
    """Raised when a guard is misconfigured at boot time."""

    _code: str = "ORI_ERR_GUARD_005"


class GuardPipelineError(GuardError):
    """Raised when the guard pipeline encounters an unrecoverable error."""

    _code: str = "ORI_ERR_GUARD_006"


__all__ = [
    "GuardConfigurationError",
    "GuardError",
    "GuardPipelineError",
]
