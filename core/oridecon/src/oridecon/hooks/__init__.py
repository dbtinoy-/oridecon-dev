"""General-purpose hook registry for framework extensibility.

Provides action hooks (fire-and-forget, error-isolated) and filter hooks
(value-pipeline, error-propagating) with priority ordering.
"""

from __future__ import annotations

from oridecon.contracts.core.hooks import HookPriority, HookRegistryProtocol
from oridecon.hooks.registry import HookRegistry

__all__ = [
    "HookPriority",
    "HookRegistry",
    "HookRegistryProtocol",
]
