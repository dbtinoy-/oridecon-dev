from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from oridecon.domain import DomainModel
from oridecon.validation import Field


@dataclass(init=False)
class ExtractionResult(DomainModel):
    text: str
    entities: list[dict[str, Any]] = Field(default_factory=list)
    relationships: list[dict[str, Any]] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
