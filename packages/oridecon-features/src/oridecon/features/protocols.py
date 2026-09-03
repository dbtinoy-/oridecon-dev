"""Re-export feature flag protocols for consumer convenience.

Consumers use these contracts to depend on feature flag abstractions
without importing the full oridecon-features implementation.
"""

from __future__ import annotations

from oridecon.contracts.feature_flags.protocols import (
    FlagManagerProtocol as FlagManagerProtocol,
)
from oridecon.contracts.feature_flags.protocols import (
    FlagProviderProtocol as FlagProviderProtocol,
)
from oridecon.contracts.feature_flags.protocols import (
    MutableFlagProviderProtocol as MutableFlagProviderProtocol,
)

__all__ = [
    "FlagManagerProtocol",
    "FlagProviderProtocol",
    "MutableFlagProviderProtocol",
]
