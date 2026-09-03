"""SagaProtocol orchestration — SagaBase, SagaStep, SagaManagerProtocol, InMemorySagaStore.

A saga coordinates multi-step distributed transactions with compensation on failure.
"""

from __future__ import annotations

from oridecon.events.sagas.base import SagaBase, SagaStep, saga_step
from oridecon.events.sagas.context import SagaContext, SagaStepResult
from oridecon.events.sagas.manager import SagaManagerProtocol
from oridecon.events.sagas.sql import SqlSagaStore
from oridecon.events.sagas.store import InMemorySagaStore, SagaStore
from oridecon.events.sagas.types import (
    SagaRecord,
    SagaStatus,
    SagaStepRecord,
    SagaStepStatus,
)

__all__ = [
    "InMemorySagaStore",
    "SagaBase",
    "SagaContext",
    "SagaManagerProtocol",
    "SagaRecord",
    "SagaStatus",
    "SagaStep",
    "SagaStepRecord",
    "SagaStepResult",
    "SagaStepStatus",
    "SagaStore",
    "SqlSagaStore",
    "saga_step",
]
