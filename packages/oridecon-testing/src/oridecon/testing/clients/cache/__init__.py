"""
Testing infrastructure for oridecon-cache.

This module provides comprehensive testing utilities for the Oridecon cache framework,
including test clients, test beds, fixtures, and mock implementations.

Components:
    - CacheTestClient: High-level testing client for cache operations
    - CacheTestBed: Async context manager with cache providers
    - CacheTestData: Test data models for cache testing
    - Fixtures: Pytest fixtures for various cache testing scenarios

Example:
    >>> import pytest
    >>> from oridecon.testing.clients.cache import CacheTestBed, CacheTestClient
    >>>
    >>> @pytest.mark.asyncio
    >>> async def test_cache_operations(cache_bed, cache_client):
    ...     async with cache_bed as bed:
    ...         client = CacheTestClient(bed)
    ...         await client.set_cache_value("key", "value")
    ...         value = await client.get_cache_value("key")
    ...         assert value == "value"
"""

from __future__ import annotations

from oridecon.testing.clients.cache.bed import CacheTestBed
from oridecon.testing.clients.cache.client_core import CacheTestClient
from oridecon.testing.clients.cache.data import CacheTestData
from oridecon.testing.clients.cache.fixtures import (
    backend_failure_scenarios,
    # Client fixtures
    cache_client,
    # Error fixtures
    cache_error_scenarios,
    # Test bed fixtures
    cache_test_bed,
    # Data fixtures
    cache_test_data,
    complex_cache_data,
    complex_keys,
    dict_values,
    list_values,
    long_ttl,
    medium_ttl,
    # Backend fixtures
    memory_backend,
    memory_cache_bed,
    memory_cache_client,
    mixed_values,
    namespaced_keys,
    redis_backend,
    redis_cache_bed,
    redis_cache_client,
    # TTL fixtures
    short_ttl,
    simple_cache_data,
    # Key fixtures
    simple_keys,
    # Value fixtures
    string_values,
)

__all__ = [
    "CacheTestBed",
    # Main classes
    "CacheTestClient",
    "CacheTestData",
    "backend_failure_scenarios",
    # Client fixtures
    "cache_client",
    # Error fixtures
    "cache_error_scenarios",
    # Test bed fixtures
    "cache_test_bed",
    # Data fixtures
    "cache_test_data",
    "complex_cache_data",
    "complex_keys",
    "dict_values",
    "list_values",
    "long_ttl",
    "medium_ttl",
    # Backend fixtures
    "memory_backend",
    "memory_cache_bed",
    "memory_cache_client",
    "mixed_values",
    "namespaced_keys",
    "redis_backend",
    "redis_cache_bed",
    "redis_cache_client",
    # TTL fixtures
    "short_ttl",
    "simple_cache_data",
    # Key fixtures
    "simple_keys",
    # Value fixtures
    "string_values",
]
