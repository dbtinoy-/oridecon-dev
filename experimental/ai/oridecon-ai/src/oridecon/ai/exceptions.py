"""Oridecon AI package exceptions."""

from __future__ import annotations

from oridecon.contracts.ai.exceptions import AIError as _ContractsAIError


class AIError(_ContractsAIError):
    """Base exception for oridecon-ai."""

    _code: str = "ORI_ERR_AI_005"
