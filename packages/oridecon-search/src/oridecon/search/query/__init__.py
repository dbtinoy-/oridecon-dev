"""Search Query Building and Validation"""

from __future__ import annotations

from oridecon.search.query.builder import SearchQueryBuilder
from oridecon.search.query.safe_query import (
    AlgoliaBackend,
    ElasticsearchBackend,
    QueryBackend,
    SafeQueryBuilder,
    create_algolia_builder,
    create_elasticsearch_builder,
)
from oridecon.search.query.suggestions import (
    Suggestion,
    SuggestionEngine,
    SuggestionResult,
)
from oridecon.search.query.types import (
    AggregationSpec,
    FilterCondition,
    QueryOperator,
    SafeSearchQuery,
    SortDirection,
    SortField,
)

__all__ = [
    "AggregationSpec",
    "AlgoliaBackend",
    "ElasticsearchBackend",
    "FilterCondition",
    "QueryBackend",
    "QueryOperator",
    "SafeQueryBuilder",
    "SafeSearchQuery",
    "SearchQueryBuilder",
    "SortDirection",
    "SortField",
    "Suggestion",
    "SuggestionEngine",
    "SuggestionResult",
]
