"""Governance error classes."""

from __future__ import annotations

from oridecon.contracts.exceptions import OrideconError


class GovernanceError(OrideconError):
    """Base class for governance-related errors."""

    _code = "ORI_ERR_GOV_001"


class BudgetExceededError(GovernanceError):
    """Error raised when budget is exceeded."""

    _code = "ORI_ERR_GOV_002"


class PolicyViolationError(GovernanceError):
    """Error raised when policy is violated."""

    _code = "ORI_ERR_GOV_003"


__all__ = [
    "BudgetExceededError",
    "GovernanceError",
    "PolicyViolationError",
]
