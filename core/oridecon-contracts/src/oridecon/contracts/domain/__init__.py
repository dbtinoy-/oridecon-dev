"""Domain-driven design primitives package.

Organized into focused submodules:

* ``base`` – DomainModelProtocol and ID type variable
* ``events`` – DomainEvent and related helpers
* ``aggregates`` – AggregateRootProtocol (protocol only; implementation in ``oridecon.domain``)
* ``specification`` – SpecificationProtocol protocol

Note: DomainModel, Entity, and ValueObject implementations have moved to
``oridecon.domain.base``. Import from there instead.
Note: The concrete ``AggregateRoot`` base class lives in ``oridecon.domain.models.aggregate``.
"""

from __future__ import annotations

# re-export core domain primitives for convenience
from oridecon.contracts.domain.aggregates import AggregateRootProtocol
from oridecon.contracts.domain.base import (
    ID,
    DomainModelProtocol,
)
from oridecon.contracts.domain.events import DomainEvent
from oridecon.contracts.domain.idempotency import (
    IdempotencyRecord,
    IdempotencyStatus,
)
from oridecon.contracts.domain.pagination import (
    CursorPage,
    CursorPageProtocol,
    OffsetPageProtocol,
)
from oridecon.contracts.domain.specification import SpecificationProtocol

__all__: list[str] = [
    "ID",
    "AggregateRootProtocol",
    "CursorPage",
    "CursorPageProtocol",
    "DomainEvent",
    "DomainModelProtocol",
    "IdempotencyRecord",
    "IdempotencyStatus",
    "OffsetPageProtocol",
    "SpecificationProtocol",
]
