"""Fallback store implementations bound when no framework store is registered."""

from oridecon.multimedia.stores.idempotency import InMemoryIdempotencyStoreFallback

__all__ = ["InMemoryIdempotencyStoreFallback"]
