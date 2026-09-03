"""Resilience primitives for database operations.

Provides a resilience handler that wraps database operations with circuit
breaker, retry with backoff, and timeout when ``oridecon-resilience`` is
installed. Falls back to a no-op pass-through when absent.
"""

from __future__ import annotations

from oridecon.sql.resilience.core import DatabaseResilienceHandler

__all__ = [
    "DatabaseResilienceHandler",
]
