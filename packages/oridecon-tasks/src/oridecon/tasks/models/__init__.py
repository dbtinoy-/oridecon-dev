"""Task models and data structures."""

from __future__ import annotations

from oridecon.contracts.infra.tasks import JobStatus
from oridecon.tasks.models.job import JobProtocol, JobResult

__all__ = ["JobProtocol", "JobResult", "JobStatus"]
