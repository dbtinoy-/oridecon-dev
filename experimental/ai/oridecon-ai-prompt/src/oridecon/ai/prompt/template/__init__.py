"""template sub-package."""

from __future__ import annotations

from oridecon.ai.prompt.template.base import AbstractPromptTemplate
from oridecon.ai.prompt.template.chat import ChatPromptTemplate
from oridecon.ai.prompt.template.few_shot import (
    FewShotPromptTemplate,
    InMemoryExampleSelector,
)
from oridecon.ai.prompt.template.partial import PartialPromptTemplate
from oridecon.ai.prompt.template.string import StringPromptTemplate

__all__ = [
    "AbstractPromptTemplate",
    "ChatPromptTemplate",
    "FewShotPromptTemplate",
    "InMemoryExampleSelector",
    "PartialPromptTemplate",
    "StringPromptTemplate",
]
