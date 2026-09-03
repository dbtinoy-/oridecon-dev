from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from oridecon.ai.rag.cache.base import CacheType, RAGCacheConfig
    from oridecon.ai.rag.cache.keys import CacheKeyBuilder
    from oridecon.ai.rag.cache.manager import RAGCache
    from oridecon.ai.rag.cache.stats import RAGCacheStats

_LAZY_IMPORTS = {
    "CacheType": "oridecon.ai.rag.cache.base",
    "RAGCacheConfig": "oridecon.ai.rag.cache.base",
    "CacheKeyBuilder": "oridecon.ai.rag.cache.keys",
    "RAGCacheStats": "oridecon.ai.rag.cache.stats",
    "RAGCache": "oridecon.ai.rag.cache.manager",
}


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib

        module_path = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path, __package__)
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__} has no attribute {name}")


def __dir__() -> list[str]:
    return list(_LAZY_IMPORTS.keys())


__all__ = list(_LAZY_IMPORTS.keys())
