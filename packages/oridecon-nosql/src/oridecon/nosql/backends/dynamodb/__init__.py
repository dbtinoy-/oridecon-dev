"""DynamoDB document store backend for oridecon-nosql."""

from __future__ import annotations

from oridecon.nosql.backends.dynamodb.backend import DynamoDBBackend
from oridecon.nosql.backends.dynamodb.collection import DynamoDBCollection

__all__ = ["DynamoDBBackend", "DynamoDBCollection"]
