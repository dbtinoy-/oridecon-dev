"""Custom GraphQL scalars."""

from __future__ import annotations

from oridecon.graphql.scalars.date import Date
from oridecon.graphql.scalars.datetime import DateTime
from oridecon.graphql.scalars.json import JSON
from oridecon.graphql.scalars.misc import URL, UUID, BigInt, Email, Void
from oridecon.graphql.scalars.time import Time
from oridecon.graphql.scalars.timestamp import Timestamp

__all__ = [
    "JSON",
    "URL",
    "UUID",
    "BigInt",
    "Date",
    "DateTime",
    "Email",
    "Time",
    "Timestamp",
    "Void",
]
