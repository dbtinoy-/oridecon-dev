"""Type definitions for oridecon core security."""

from __future__ import annotations

from oridecon.contracts.security.rotation import (
    SecretRotationPolicy as SecretRotationPolicy,  # re-export
)

__all__ = ["SecretRotationPolicy"]
