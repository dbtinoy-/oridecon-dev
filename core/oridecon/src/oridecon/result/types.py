"""Result type — backward-compatible re-export.

Canonical location: oridecon.contracts.core.result
"""

from __future__ import annotations

from oridecon.contracts.core.result import Err as Err
from oridecon.contracts.core.result import Ok as Ok
from oridecon.contracts.core.result import Result as Result
from oridecon.contracts.core.result import UnwrapError as UnwrapError

__all__ = ["Err", "Ok", "Result"]
