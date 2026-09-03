"""Request-scoped caching — local implementation removed.

All request-scoped caching is now provided by ``oridecon.cache``.

Migration guide
---------------
Replace imports from this module as follows:

    # Before
    from oridecon.admin.services.request_cache import cache_in_request, get_request_cache

    # After
    from oridecon.cache import cache_in_request, get_request_cache

``get_request_cache()`` returns a plain ``dict[str, Any]`` backed by a
``contextvars.ContextVar``, providing automatic per-request isolation with
no additional locking.
"""

from __future__ import annotations
