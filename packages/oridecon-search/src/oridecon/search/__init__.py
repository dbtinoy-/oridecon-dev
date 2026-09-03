"""Oridecon Search Package."""

from __future__ import annotations

import importlib.metadata

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from typing import TYPE_CHECKING, Any

from oridecon.search.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.search.analytics import (
        InMemorySearchAnalyticsRecorder,
        SearchAnalyticsRecorder,
    )
    from oridecon.search.config import (
        BackendType,
        IndexConfig,
        NamedSearchConfig,
        SearchConfig,
    )
    from oridecon.search.di.provider import SearchProvider
    from oridecon.search.engine import (
        FederatedResults,
        FederatedSearchEngine,
        SearchableModel,
        SearchEngine,
    )
    from oridecon.search.exceptions import (
        BackendError,
        ConfigurationError,
        QueryError,
        SearchError,
        SearchIndexError,
    )
    from oridecon.search.filterset import (
        FilterCondition,
        FilterOperator,
        FilterSet,
        FilterSetTranslator,
    )
    from oridecon.search.query import (
        Suggestion,
        SuggestionEngine,
        SuggestionResult,
    )
    from oridecon.search.repository import SearchEntityRepository
    from oridecon.search.types import (
        RAGSearchResult,
        SearchQuery,
        SearchResponse,
        SearchStrategy,
    )
    from oridecon.search.validation import (
        SearchQueryValidator,
        sanitize_search_filters,
        sanitize_search_query,
        validate_index_name,
        validate_search_filters,
        validate_search_query,
        validate_search_sort,
    )

_LAZY_IMPORTS = {
    # FilterSet translator
    "FilterCondition": "oridecon.search.filterset",
    "FilterOperator": "oridecon.search.filterset",
    "FilterSet": "oridecon.search.filterset",
    "FilterSetTranslator": "oridecon.search.filterset",
    # Module
    "SearchModule": "oridecon.search.module",
    "BackendType": "oridecon.search.config",
    "NamedSearchConfig": "oridecon.search.config",
    "SearchConfig": "oridecon.search.config",
    "SearchableModel": "oridecon.search.engine",
    "SearchEngine": "oridecon.search.engine",
    "FederatedSearchEngine": "oridecon.search.engine",
    "FederatedResults": "oridecon.search.engine",
    "BackendError": "oridecon.search.exceptions",
    "ConfigurationError": "oridecon.search.exceptions",
    "QueryError": "oridecon.search.exceptions",
    "SearchError": "oridecon.search.exceptions",
    "SearchIndexError": "oridecon.search.exceptions",
    "SearchProvider": "oridecon.search.di.provider",
    "SearchEntityRepository": "oridecon.search.repository",
    "IndexConfig": "oridecon.search.config",
    "RAGSearchResult": "oridecon.search.types",
    "SearchQuery": "oridecon.search.types",
    "SearchResponse": "oridecon.search.types",
    "SearchResult": "oridecon.search.types",
    "SearchStrategy": "oridecon.search.types",
    "SearchQueryValidator": "oridecon.search.validation",
    "sanitize_search_filters": "oridecon.search.validation",
    "sanitize_search_query": "oridecon.search.validation",
    "validate_index_name": "oridecon.search.validation",
    "validate_search_filters": "oridecon.search.validation",
    "validate_search_query": "oridecon.search.validation",
    "validate_search_sort": "oridecon.search.validation",
    "InMemorySearchAnalyticsRecorder": "oridecon.search.analytics",
    "SearchAnalyticsRecorder": "oridecon.search.analytics",
    "Suggestion": "oridecon.search.query",
    "SuggestionEngine": "oridecon.search.query",
    "SuggestionResult": "oridecon.search.query",
    # Events
    "IndexingCompletedEvent": "oridecon.search.events",
    "SearchExecutedEvent": "oridecon.search.events",
    # Hooks
    "SearchIndexedHook": "oridecon.search.hooks",
    "SearchQueryExecutedHook": "oridecon.search.hooks",
}


def __getattr__(name: str) -> Any:
    if name == "__version__":
        return __version__
    if name in _LAZY_IMPORTS:
        import importlib

        module_path = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__} has no attribute {name}")


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = [*list(_LAZY_IMPORTS.keys()), "__version__"]
