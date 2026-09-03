"""Data caching layer — local implementations removed.

All caching is now provided by ``oridecon-cache``.  Inject
``CacheBackendProtocol`` from ``oridecon.contracts.infra.cache`` into data
sources that need caching, and use ``MemoryCacheBackend`` from
``oridecon.cache`` as the in-process backend.
"""

from __future__ import annotations
