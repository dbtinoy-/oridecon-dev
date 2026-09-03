"""Composition utilities for chaining, routing, and parallelising skills."""

from __future__ import annotations

from oridecon.ai.skills.composition.chain import SkillChain
from oridecon.ai.skills.composition.conditional import ConditionalSkill
from oridecon.ai.skills.composition.parallel import ParallelSkills
from oridecon.ai.skills.composition.pipeline import SkillPipeline
from oridecon.ai.skills.composition.router import SkillRouter

__all__ = [
    "ConditionalSkill",
    "ParallelSkills",
    "SkillChain",
    "SkillPipeline",
    "SkillRouter",
]
