"""CLI contributor exports for the oridecon-tasks package."""

from __future__ import annotations

from oridecon.tasks.cli.contributor import TasksCliContributor
from oridecon.tasks.cli.generators.task import TaskGenerator

__all__ = ["TaskGenerator", "TasksCliContributor"]
