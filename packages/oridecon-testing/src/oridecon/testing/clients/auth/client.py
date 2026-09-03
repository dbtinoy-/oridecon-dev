"""Testing client for oridecon-auth package.

This module provides testing utilities and clients for the oridecon-auth package,
integrating with the oridecon.testing infrastructure.

Note: This module now re-exports from the refactored testing package for backward compatibility.
"""

from __future__ import annotations

from oridecon.testing.clients.auth.bed import AuthTestBed
from oridecon.testing.clients.auth.test_client import (  # type: ignore[import-untyped]
    AuthTestClient,
)
from oridecon.testing.clients.auth.types import AuthTestToken, AuthTestUser

__all__ = [
    "AuthTestBed",
    "AuthTestClient",
    "AuthTestToken",
    "AuthTestUser",
]
