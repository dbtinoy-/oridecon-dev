"""Protocol re-exports for skills — convenience surface for consumers."""

from __future__ import annotations

from oridecon.contracts.ai.skills import SkillExecutorProtocol as SkillExecutorProtocol
from oridecon.contracts.ai.skills import SkillProtocol as SkillProtocol
from oridecon.contracts.ai.skills import SkillRegistryProtocol as SkillRegistryProtocol

__all__ = [
    "SkillExecutorProtocol",
    "SkillProtocol",
    "SkillRegistryProtocol",
]
