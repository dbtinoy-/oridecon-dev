"""Search Engine Abstractions & Validation."""

from __future__ import annotations

from oridecon.search.config import SearchConfig
from oridecon.search.engine.base import SearchEngine
from oridecon.search.engine.engine import (
    BulkOperationResult,
    BulkResult,
    DefaultSearchEngine,
    SearchQuery,
)
from oridecon.search.engine.federation import (
    FederatedResults,
    FederatedSearchEngine,
    FederatedSearchResult,
)
from oridecon.search.engine.models import SearchableModel
from oridecon.search.engine.validation import MAX_QUERY_LENGTH, validate_search_query
from oridecon.search.types import SearchResponse

__all__ = [
    "MAX_QUERY_LENGTH",
    "BulkOperationResult",
    "BulkResult",
    "DefaultSearchEngine",
    "FederatedResults",
    "FederatedSearchEngine",
    "FederatedSearchResult",
    "SearchConfig",
    "SearchEngine",
    "SearchQuery",
    "SearchResponse",
    "SearchableModel",
    "validate_search_query",
]
