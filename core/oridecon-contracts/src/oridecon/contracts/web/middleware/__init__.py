"""Web middleware protocols."""

from __future__ import annotations

from oridecon.contracts.web.guard import GuardProtocol
from oridecon.contracts.web.middleware.protocols import ASGIMiddlewareProtocol
from oridecon.contracts.web.middleware.registry_protocol import (
    MiddlewareRegistryProtocol,
)

__all__ = ["ASGIMiddlewareProtocol", "GuardProtocol", "MiddlewareRegistryProtocol"]
