"""GuardProtocol chain and decorator for authorization."""

from __future__ import annotations

from oridecon.security.guards.chain import GuardChainImpl
from oridecon.security.guards.decorator import use_guards

__all__ = ["GuardChainImpl", "use_guards"]
