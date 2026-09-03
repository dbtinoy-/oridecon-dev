"""Feature flag subsystem for the Oridecon framework.

Provides a full-featured, async-first feature flag system with TTL caching,
runtime overrides, variant A/B testing, and DI integration.

Exports:
    Flag: Full flag definition including evaluation rules.
    FlagType: Evaluation strategy enum (BOOLEAN, PERCENTAGE, USER_LIST, etc.).
    FlagContext: Evaluation context (user ID, attributes, session).
    FlagEvaluation: Result of evaluating a flag for a given context.
    FlagValue: Type alias for boolean or variant-name evaluation result.
    FeatureFlagError: Base exception for all feature-flag errors.
    FlagNotFoundError: Raised when a requested flag does not exist.
    FlagEvaluationError: Raised when a provider fails during flag evaluation.
    FeatureFlagDisabledError: Raised when a feature-guarded path is called disabled.
    AbstractFlagProvider: Rich abstract base with full evaluation logic.
    LocalProvider: In-memory, code-defined flag store.
    EnvProvider: Reads flags from environment variables.
    ChainedProvider: Layered lookup across multiple providers.
    MemoryProvider: Lightweight test double with override support.
    FlagManager: Central manager with caching, overrides, and variant support.
    FlagChangeListener: Sync callback type for flag override change notifications.
    AsyncFlagChangeListener: Async callback type for flag override change notifications.
    ManagerConfig: Configuration dataclass for FlagManager.
    FeatureFlagsConfig: Runtime configuration for the DI provider.
    FeatureFlagsProvider: DI provider registering flag infrastructure.
    feature_flag: Decorator for async flag-gated functions.
    feature_flag_sync: Decorator for sync flag-gated functions.
    require_flag: Decorator that raises when a flag is disabled (async).
    require_flag_sync: Decorator that raises when a flag is disabled (sync).
    CacheBackendFlagProvider: Cache-backed flag provider (Redis, Memcached, etc.).
    FlagProviderProtocol: Contract for feature flag providers.
    MutableFlagProviderProtocol: Contract for mutable feature flag providers.
    FlagManagerProtocol: Contract for feature flag managers.
"""

from __future__ import annotations

import importlib.metadata
from typing import TYPE_CHECKING

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

# -- Version -------------------------------------------------------------------

from oridecon.features.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.features.backends.base import AbstractFlagProvider
    from oridecon.features.backends.cache import CacheBackendFlagProvider
    from oridecon.features.backends.chained import ChainedProvider
    from oridecon.features.backends.env import EnvProvider
    from oridecon.features.backends.local import LocalProvider
    from oridecon.features.backends.testing import MemoryProvider
    from oridecon.features.config import FeatureFlagsConfig
    from oridecon.features.decorators import (
        feature_flag,
        feature_flag_sync,
        require_flag,
        require_flag_sync,
    )
    from oridecon.features.di.provider import FeatureFlagsProvider
    from oridecon.features.events import FlagChangeEvent
    from oridecon.features.exceptions import (
        FeatureFlagDisabledError,
        FeatureFlagError,
        FlagEvaluationError,
        FlagNotFoundError,
    )
    from oridecon.features.manager import (
        AsyncFlagChangeListener,
        FlagChangeListener,
        FlagManager,
        ManagerConfig,
    )
    from oridecon.features.protocols import (
        FlagManagerProtocol,
        FlagProviderProtocol,
        MutableFlagProviderProtocol,
    )
    from oridecon.features.types import (
        Flag,
        FlagContext,
        FlagEvaluation,
        FlagType,
        FlagValue,
    )

_LAZY_IMPORTS: dict[str, str] = {
    # module
    "FeatureFlagsModule": "oridecon.features.module",
    # protocols
    "FlagProviderProtocol": "oridecon.features.protocols",
    "MutableFlagProviderProtocol": "oridecon.features.protocols",
    "FlagManagerProtocol": "oridecon.features.protocols",
    # types
    "Flag": "oridecon.features.types",
    "FlagContext": "oridecon.features.types",
    "FlagEvaluation": "oridecon.features.types",
    "FlagType": "oridecon.features.types",
    "FlagValue": "oridecon.features.types",
    # exceptions
    "FeatureFlagDisabledError": "oridecon.features.exceptions",
    "FeatureFlagError": "oridecon.features.exceptions",
    "FlagEvaluationError": "oridecon.features.exceptions",
    "FlagNotFoundError": "oridecon.features.exceptions",
    # backends
    "AbstractFlagProvider": "oridecon.features.backends.base",
    "CacheBackendFlagProvider": "oridecon.features.backends.cache",
    "LocalProvider": "oridecon.features.backends.local",
    "EnvProvider": "oridecon.features.backends.env",
    "ChainedProvider": "oridecon.features.backends.chained",
    "MemoryProvider": "oridecon.features.backends.testing",
    # manager
    "FlagManager": "oridecon.features.manager",
    "AsyncFlagChangeListener": "oridecon.features.manager",
    "FlagChangeListener": "oridecon.features.manager",
    "ManagerConfig": "oridecon.features.manager",
    # events
    "FlagChangeEvent": "oridecon.features.events",
    # decorators
    "feature_flag": "oridecon.features.decorators",
    "feature_flag_sync": "oridecon.features.decorators",
    "require_flag": "oridecon.features.decorators",
    "require_flag_sync": "oridecon.features.decorators",
    # config
    "FeatureFlagsConfig": "oridecon.features.config",
    # integration
    "FeatureFlagsProvider": "oridecon.features.di.provider",
    # Hooks
    "FeatureFlagEvaluatedHook": "oridecon.features.hooks",
    "FeatureFlagUpdatedHook": "oridecon.features.hooks",
}


def __getattr__(name: str) -> object:
    if name in _LAZY_IMPORTS:
        import importlib

        module = importlib.import_module(_LAZY_IMPORTS[name])
        value = getattr(module, name)
        globals()[name] = value
        return value
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = list(_LAZY_IMPORTS.keys())
