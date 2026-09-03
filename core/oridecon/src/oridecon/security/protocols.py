"""Re-exports for the security subsystem.

Re-exports ``GuardError`` from contracts.  The ``GuardProtocol``
is imported from ``oridecon.contracts.web.guard``.
"""

from __future__ import annotations

from oridecon.contracts.ai.exceptions import (
    GuardError as GuardError,  # re-export
)

__all__ = [
    "GuardError",
]
