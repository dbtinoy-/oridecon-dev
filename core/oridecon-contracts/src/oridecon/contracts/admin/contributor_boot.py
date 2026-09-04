"""Contributor boot failure classification — distinguishes expected
missing-dependency failures from genuine errors."""

from __future__ import annotations

from dataclasses import dataclass

from oridecon.contracts.exceptions.base import OrideconError


@dataclass(frozen=True, slots=True)
class ContributorBootFailure:
    """Structured summary of a contributor boot failure."""

    expected: bool
    reason: str
    summary: str


def summarize_contributor_boot_failure(exc: Exception) -> ContributorBootFailure:
    """Classify a contributor boot exception as expected or genuine.

    ``ModuleNotFoundError`` and ``ImportError`` raised during contributor
    boot are typically expected when an optional backing service is not
    registered in this deployment.  All other errors are treated as
    genuine failures.
    """
    if isinstance(exc, (ModuleNotFoundError, ImportError)):
        name = getattr(exc, "name", "") or str(exc)
        return ContributorBootFailure(
            expected=True,
            reason=f"optional dependency not installed: {name}",
            summary=str(exc),
        )

    if isinstance(exc, OrideconError):
        code = getattr(exc, "_code", "")
        return ContributorBootFailure(
            expected=False,
            reason=f"{code} {type(exc).__name__}",
            summary=str(exc),
        )

    return ContributorBootFailure(
        expected=False,
        reason=type(exc).__name__,
        summary=str(exc),
    )


__all__ = [
    "ContributorBootFailure",
    "summarize_contributor_boot_failure",
]
