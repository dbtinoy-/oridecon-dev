"""Feedback loop module for continuous learning."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from typing import TYPE_CHECKING, Any

try:
    __version__ = version("oridecon-ai-safety")
except PackageNotFoundError:
    __version__ = "0.0.0"

if TYPE_CHECKING:
    from oridecon.ai.feedback.config import FeedbackConfig
    from oridecon.ai.feedback.di.provider import FeedbackProvider
    from oridecon.ai.feedback.exceptions import (
        FeedbackAuthorizationError,
        FeedbackError,
        FeedbackProcessingError,
        FeedbackTooLargeError,
        FeedbackValidationError,
    )
    from oridecon.ai.feedback.hooks import (
        FeedbackProcessedHook,
        FeedbackStoredHook,
        FeedbackSubmittedHook,
    )
    from oridecon.ai.feedback.middleware import (
        FeedbackContext,
        FeedbackMiddleware,
    )
    from oridecon.ai.feedback.module import FeedbackModule
    from oridecon.ai.feedback.services.collector import FeedbackCollector
    from oridecon.ai.feedback.services.feedback_service import FeedbackService
    from oridecon.ai.feedback.storage import (
        CachedFeedbackStore,
        DatabaseFeedbackStore,
        FeedbackStoreProtocol,
        FeedbackSummary,
    )
    from oridecon.ai.feedback.types import FeedbackItem, FeedbackType

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # --- Config ---
    "FeedbackConfig": ("oridecon.ai.feedback.config", "FeedbackConfig"),
    # --- DI ---
    "FeedbackProvider": ("oridecon.ai.feedback.di.provider", "FeedbackProvider"),
    "FeedbackModule": ("oridecon.ai.feedback.module", "FeedbackModule"),
    # --- Exceptions ---
    "FeedbackAuthorizationError": (
        "oridecon.ai.feedback.exceptions",
        "FeedbackAuthorizationError",
    ),
    "FeedbackError": ("oridecon.ai.feedback.exceptions", "FeedbackError"),
    "FeedbackProcessingError": (
        "oridecon.ai.feedback.exceptions",
        "FeedbackProcessingError",
    ),
    "FeedbackTooLargeError": (
        "oridecon.ai.feedback.exceptions",
        "FeedbackTooLargeError",
    ),
    "FeedbackValidationError": (
        "oridecon.ai.feedback.exceptions",
        "FeedbackValidationError",
    ),
    # --- Hooks ---
    "FeedbackProcessedHook": (
        "oridecon.ai.feedback.hooks",
        "FeedbackProcessedHook",
    ),
    "FeedbackStoredHook": ("oridecon.ai.feedback.hooks", "FeedbackStoredHook"),
    "FeedbackSubmittedHook": ("oridecon.ai.feedback.hooks", "FeedbackSubmittedHook"),
    # --- Middleware ---
    "FeedbackContext": ("oridecon.ai.feedback.middleware", "FeedbackContext"),
    "FeedbackMiddleware": ("oridecon.ai.feedback.middleware", "FeedbackMiddleware"),
    # --- Services ---
    "FeedbackCollector": (
        "oridecon.ai.feedback.services.collector",
        "FeedbackCollector",
    ),
    "FeedbackService": (
        "oridecon.ai.feedback.services.feedback_service",
        "FeedbackService",
    ),
    # --- Storage ---
    "CachedFeedbackStore": ("oridecon.ai.feedback.storage", "CachedFeedbackStore"),
    "DatabaseFeedbackStore": ("oridecon.ai.feedback.storage", "DatabaseFeedbackStore"),
    "FeedbackSummary": ("oridecon.ai.feedback.storage", "FeedbackSummary"),
    # --- Types ---
    "FeedbackItem": ("oridecon.ai.feedback.types", "FeedbackItem"),
    "FeedbackType": ("oridecon.ai.feedback.types", "FeedbackType"),
    # --- Protocols ---
    "FeedbackProtocol": ("oridecon.ai.feedback.protocols", "FeedbackProtocol"),
    "FeedbackStoreProtocol": (
        "oridecon.ai.feedback.protocols",
        "FeedbackStoreProtocol",
    ),
    # --- Events ---
    "FeedbackSubmittedEvent": ("oridecon.ai.feedback.events", "FeedbackSubmittedEvent"),
}


def __getattr__(name: str) -> Any:
    """Lazy-load symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """Enumerate available attributes for IDE support."""
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = [
    "CachedFeedbackStore",
    "DatabaseFeedbackStore",
    "FeedbackAuthorizationError",
    "FeedbackCollector",
    "FeedbackConfig",
    "FeedbackContext",
    "FeedbackError",
    "FeedbackItem",
    "FeedbackMiddleware",
    "FeedbackModule",
    "FeedbackProcessedHook",
    "FeedbackProcessingError",
    "FeedbackProtocol",
    "FeedbackProvider",
    "FeedbackService",
    "FeedbackStoreProtocol",
    "FeedbackStoredHook",
    "FeedbackSubmittedEvent",
    "FeedbackSubmittedHook",
    "FeedbackSummary",
    "FeedbackTooLargeError",
    "FeedbackType",
    "FeedbackValidationError",
]
