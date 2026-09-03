"""Content Security Policy package for oridecon-web."""

from __future__ import annotations

from oridecon.web.security.config import CSPConfig
from oridecon.web.security.csp.builder import CSPPolicy

__all__ = ["CSPConfig", "CSPPolicy"]
