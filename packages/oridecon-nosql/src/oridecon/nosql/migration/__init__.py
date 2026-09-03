"""Migration package for NoSQL schema management."""

from __future__ import annotations

from oridecon.nosql.migration.manager import MigrationManager, MigrationRecord
from oridecon.nosql.migration.operations import (
    AddField,
    CreateIndex,
    DropCollection,
    DropIndex,
    RenameField,
)

__all__ = [
    "AddField",
    "CreateIndex",
    "DropCollection",
    "DropIndex",
    "MigrationManager",
    "MigrationRecord",
    "RenameField",
]
