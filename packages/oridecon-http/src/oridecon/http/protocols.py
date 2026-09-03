"""Re-export HTTP protocols for consumer convenience.

Consumers use these contracts to depend on HTTP abstractions without
importing the full oridecon-http implementation.
"""

from __future__ import annotations

from oridecon.contracts.web.http_protocols import (
    HTTPClientProtocol as HTTPClientProtocol,
)
from oridecon.contracts.web.http_protocols import (
    InterceptorChainProtocol as InterceptorChainProtocol,
)
from oridecon.contracts.web.http_protocols import (
    InterceptorProtocol as InterceptorProtocol,
)

__all__ = [
    "HTTPClientProtocol",
    "InterceptorChainProtocol",
    "InterceptorProtocol",
]
