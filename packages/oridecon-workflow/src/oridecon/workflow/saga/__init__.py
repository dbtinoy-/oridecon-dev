"""SagaProtocol orchestration primitives for oridecon-workflow."""

from __future__ import annotations

from oridecon.contracts.workflow.protocols import SagaState, SagaStoreProtocol
from oridecon.contracts.workflow.steps import SagaStepError
from oridecon.workflow.saga.base import AbstractSaga, SagaError, SagaStep
from oridecon.workflow.saga.batch import SagaBatchProcessor
from oridecon.workflow.saga.content_addressed import (
    ContentAddressedSaga,
    ContentAddressedStage,
)
from oridecon.workflow.saga.hooks import (
    SagaCompensationCompletedHook,
    SagaCompensationContext,
    SagaCompensationTriggeredHook,
    SagaStepContext,
    SagaStepExecutedHook,
    SagaStepFailedHook,
)

__all__ = [
    "AbstractSaga",
    "ContentAddressedSaga",
    "ContentAddressedStage",
    "SagaBatchProcessor",
    "SagaCompensationCompletedHook",
    "SagaCompensationContext",
    "SagaCompensationTriggeredHook",
    "SagaError",
    "SagaState",
    "SagaStep",
    "SagaStepContext",
    "SagaStepError",
    "SagaStepExecutedHook",
    "SagaStepFailedHook",
    "SagaStoreProtocol",
]
