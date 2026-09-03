"""MongoDB backend for oridecon-nosql."""

from __future__ import annotations

from oridecon.nosql.backends.mongodb.backend import MongoDBDocumentStore
from oridecon.nosql.backends.mongodb.collection import MongoDBCollection

__all__ = ["MongoDBCollection", "MongoDBDocumentStore"]
