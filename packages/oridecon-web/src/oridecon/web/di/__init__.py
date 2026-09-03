"""Framework integration for oridecon-web."""

from __future__ import annotations

from oridecon.web.di.provider import WebProvider
from oridecon.web.di.rate_limit import RateLimitProvider
from oridecon.web.integrations.setup import lifespan

__all__ = ["RateLimitProvider", "WebProvider", "lifespan"]
