"""Idempotent task submission value types.

Value types live here (not in ``protocols.py``) because they appear in
protocol method signatures and cross package boundaries —
``IdempotencyResult`` is consumed by ``oridecon-multimedia`` and produced
by ``oridecon-tasks``. The task idempotency protocols live in
``oridecon.contracts.infra.tasks.protocols`` and the underlying store
contract is ``oridecon.contracts.core.idempotency``.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any


class IdempotencyResultStatus(str, Enum):
    """Lifecycle status of an idempotent task submission.

    Members compare equal to their string values and serialize naturally
    to JSON.
    """

    SUBMITTED = "submitted"
    DUPLICATE = "duplicate"
    COMPLETED = "completed"


@dataclass(frozen=True)
class IdempotencyResult:
    """Outcome of an idempotent task submission.

    Attributes:
        task_id: Identifier of the submitted (or previously submitted) task.
        idempotency_key: The idempotency key used for the submission.
        status: Submission lifecycle status.
        created_at: UTC timestamp of the original submission.
        result: Stored result payload on duplicate/completed lookups.
    """

    task_id: str
    idempotency_key: str
    status: IdempotencyResultStatus
    created_at: datetime
    result: Any | None = None


__all__ = ["IdempotencyResult", "IdempotencyResultStatus"]
