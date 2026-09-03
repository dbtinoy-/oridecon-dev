"""Domain events for oridecon-multimedia — immutable facts emitted per generation call.

Mirrors oridecon-ai-llm's LLMCompletionEvent: published through
EventBusProtocol when bound, consumed by cost accounting / dashboards.
No hard dependency on oridecon-monitor — see design spec 'Observability'.
"""

from __future__ import annotations

from dataclasses import dataclass

from oridecon.contracts.domain.events import DomainEvent

__all__ = ["MultimediaGenerationEvent"]


@dataclass(frozen=True, init=False)
class MultimediaGenerationEvent(DomainEvent):
    """Emitted after a generate()/submit() call completes (success or failure)."""

    media_type: str
    provider: str
    size_bytes: int | None
    duration_seconds: float | None
