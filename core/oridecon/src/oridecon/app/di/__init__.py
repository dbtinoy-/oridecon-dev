"""Integration layer for the app package.

Exports the :class:`CoreProvider` DI provider that bootstraps all
Oridecon framework sub-providers.
"""

from __future__ import annotations

from oridecon.app.di.provider import CoreProvider

__all__ = ["CoreProvider"]
