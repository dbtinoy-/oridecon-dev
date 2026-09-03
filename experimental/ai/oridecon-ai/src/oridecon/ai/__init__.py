"""Oridecon AI — Unified AI/ML Layer.

Install `oridecon-ai` to get the full AI subsystem.
Import from sub-packages for granular control.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from oridecon.ai.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.ai.config import AIConfig, ClientConfig, RAGConfig, VectorConfig
    from oridecon.ai.di.provider import AIProvider
    from oridecon.ai.module import AIModule

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "AIConfig": ("oridecon.ai.config", "AIConfig"),
    "AIModule": ("oridecon.ai.module", "AIModule"),
    "AIProvider": ("oridecon.ai.di.provider", "AIProvider"),
    "ClientConfig": ("oridecon.ai.config", "ClientConfig"),
    "RAGConfig": ("oridecon.ai.config", "RAGConfig"),
    "VectorConfig": ("oridecon.ai.config", "VectorConfig"),
}

__all__ = list(_LAZY_IMPORTS)


def __getattr__(name: str) -> object:
    """Lazy-load public symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr = _LAZY_IMPORTS[name]
        mod = importlib.import_module(module_path)
        value = getattr(mod, attr)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """Expose lazy-loaded names for tab completion and dir()."""
    return list(_LAZY_IMPORTS)
