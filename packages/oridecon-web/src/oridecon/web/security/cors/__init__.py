"""CORS configuration and middleware package for oridecon-web."""

from __future__ import annotations

from oridecon.web.security.config import CORSConfig
from oridecon.web.security.cors.middleware import CORSMiddleware

__all__ = ["CORSConfig", "CORSMiddleware"]
