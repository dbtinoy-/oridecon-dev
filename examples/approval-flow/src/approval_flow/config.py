"""Typed configuration for the Approval Flow demo."""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from oridecon.config import BaseConfig
from oridecon.contracts.core.config import Environment
from oridecon.validation import ConfigDict, Field


@dataclass(init=False)
class ApprovalFlowConfig(BaseConfig):
    """Demo-owned labels; state and approval behavior come from Oridecon."""

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")
    config_section: ClassVar[str] = "approval_flow"
    name: str = "approval_flow"
    enabled: bool = True
    env: Environment | None = Field(None, description="Deployment environment")
    initial_request: str = Field(
        default="Purchase 24 laptops", description="Seed request label"
    )
    initial_amount: int = Field(default=24000, gt=0, description="Seed request amount")


__all__ = ["ApprovalFlowConfig"]
