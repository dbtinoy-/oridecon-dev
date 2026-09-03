"""Demo configuration — ``demo:`` section of application.yaml.

Convention followed: **Yaml-first config** — ``OrideconConfig`` /
``from_yaml`` auto-discovers ``application.yaml`` from the working
directory.  ``ORI_DEMO__*`` overrides and ``ORI_PROFILE`` overlays apply
via the loader.

The ``RatesConfig`` dataclass declares the typed ``demo:`` section with
field-level defaults.  Environment variable overrides use the double-
underscore convention: ``ORI_DEMO__UPSTREAM_SCENARIO=down`` sets
``upstream_scenario = "down"``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from oridecon.config import BaseConfig
from oridecon.contracts.core.config import Environment
from oridecon.validation import Field


@dataclass(init=False)
class RatesConfig(BaseConfig):
    """Typed ``demo:`` section of the resilient-rates application.yaml."""

    config_section: ClassVar[str] = "demo"
    name: str = "demo"
    enabled: bool = True
    env: Environment | None = Field(None, description="Deployment environment")

    upstream_scenario: str = Field(
        "healthy",
        description="Initial upstream scenario (healthy|flaky|down|slow)",
    )


__all__ = ["RatesConfig"]
