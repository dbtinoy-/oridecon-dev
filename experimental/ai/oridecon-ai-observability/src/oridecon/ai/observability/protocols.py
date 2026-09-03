"""Re-export observability protocols for consumer convenience.

Consumers use these contracts to depend on observability abstractions
without importing the full oridecon-ai-observability implementation.
"""

from __future__ import annotations

from oridecon.contracts.observability.ai import (
    AIHealthMonitorProtocol as AIHealthMonitorProtocol,
)
from oridecon.contracts.observability.ai import (
    AIMetricsProtocol as AIMetricsProtocol,
)
from oridecon.contracts.observability.ai import (
    AITracerProtocol as AITracerProtocol,
)
from oridecon.contracts.observability.ai import (
    ObservabilityProtocol as ObservabilityProtocol,
)

__all__ = [
    "AIHealthMonitorProtocol",
    "AIMetricsProtocol",
    "AITracerProtocol",
    "ObservabilityProtocol",
]
