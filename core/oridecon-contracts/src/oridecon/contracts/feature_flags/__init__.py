"""Contracts for the feature flags subsystem.

Exports protocols, models, and exceptions so other packages can use
``from oridecon.contracts.feature_flags import FlagProviderProtocol``.
"""

from __future__ import annotations

from oridecon.contracts.exceptions.feature_flags import (
    FeatureFlagError,
)
from oridecon.contracts.feature_flags.models import (
    FlagEvaluation,
    FlagType,
    FlagValue,
)
from oridecon.contracts.feature_flags.protocols import (
    FlagManagerProtocol,
    FlagProviderProtocol,
    MutableFlagProviderProtocol,
)

__all__ = [
    "FeatureFlagError",
    "FlagEvaluation",
    "FlagManagerProtocol",
    "FlagProviderProtocol",
    "FlagType",
    "FlagValue",
    "MutableFlagProviderProtocol",
]
