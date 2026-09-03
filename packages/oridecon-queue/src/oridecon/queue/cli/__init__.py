"""CLI contributor exports for the oridecon-queue package."""

from __future__ import annotations

from oridecon.queue.cli.contributor import QueueCliContributor
from oridecon.queue.cli.generators.message_consumer import MessageConsumerGenerator

__all__ = ["MessageConsumerGenerator", "QueueCliContributor"]
