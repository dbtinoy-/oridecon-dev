"""Protocol re-exports for guard — convenience surface for consumers."""

from __future__ import annotations

from oridecon.contracts.ai.guards import GuardPipelineProtocol as GuardPipelineProtocol
from oridecon.contracts.ai.guards import GuardResultProtocol as GuardResultProtocol
from oridecon.contracts.ai.guards import InputGuardProtocol as InputGuardProtocol
from oridecon.contracts.ai.guards import OutputGuardProtocol as OutputGuardProtocol

__all__ = [
    "GuardPipelineProtocol",
    "GuardResultProtocol",
    "InputGuardProtocol",
    "OutputGuardProtocol",
]
