"""CSRF protection package for oridecon-web."""

from __future__ import annotations

from oridecon.web.security.config import CSRFConfig
from oridecon.web.security.csrf.middleware import CSRFProtectionMiddleware

__all__ = ["CSRFConfig", "CSRFProtectionMiddleware"]
