"""NoSQL backends."""

from __future__ import annotations

from oridecon.nosql.backends.dynamodb.backend import DynamoDBBackend
from oridecon.nosql.backends.firestore.backend import FirestoreBackend

__all__ = ["DynamoDBBackend", "FirestoreBackend"]
