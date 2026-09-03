"""Routing strategies for multi-provider LLM inference.

Provides a ``RoutingStrategyProtocol`` protocol and concrete implementations:

* ``SequentialCascadeStrategy``: Try providers one at a time in priority order.
* ``ParallelRaceStrategy``: Fire requests in parallel, return the first success.
* ``CostOptimizedStrategy``: Sort providers by token cost, try cheapest first.
* ``LatencyOptimizedStrategy``: Route to the provider with the lowest recent latency.

The ``LLMRouter`` delegates to whichever strategy is configured via
``LLMConfig.strategy``.
"""

from __future__ import annotations

from oridecon.ai.llm.routing.strategies.cost import CostOptimizedStrategy
from oridecon.ai.llm.routing.strategies.latency import LatencyOptimizedStrategy
from oridecon.ai.llm.routing.strategies.parallel import ParallelRaceStrategy
from oridecon.ai.llm.routing.strategies.sequential import SequentialCascadeStrategy
from oridecon.contracts.ai.routing import RoutingStrategyProtocol

__all__ = [
    "CostOptimizedStrategy",
    "LatencyOptimizedStrategy",
    "ParallelRaceStrategy",
    "RoutingStrategyProtocol",
    "SequentialCascadeStrategy",
]
