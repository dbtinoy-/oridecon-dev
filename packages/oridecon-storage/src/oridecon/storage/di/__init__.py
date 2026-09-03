"""Framework integration for oridecon-storage."""

from __future__ import annotations

from oridecon.storage.di.provider import StorageProvider
from oridecon.storage.module import StorageModule

__all__ = ["StorageModule", "StorageProvider"]
