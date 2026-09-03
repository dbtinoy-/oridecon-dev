"""Workflow contracts — pipeline, bulk, and saga orchestration protocols."""

from __future__ import annotations

from oridecon.contracts.workflow.content_checkpoint import (
    ContentCheckpointEntry,
    ContentCheckpointKey,
    ContentCheckpointStoreProtocol,
)
from oridecon.contracts.workflow.errors import SagaVersionMismatchError
from oridecon.contracts.workflow.protocols import (
    ApprovalProtocol,
    BulkProcessorProtocol,
    ExecutionProtocol,
    PipelineContextProtocol,
    PipelineProtocol,
    PipelineStepProtocol,
    SagaManagerProtocol,
    SagaProtocol,
    SagaState,
    SagaStoreProtocol,
    StateMachineProtocol,
    StatePersistenceProtocol,
    StateTransitionRecord,
    WorkflowGraphProtocol,
    WorkflowNodeProtocol,
)
from oridecon.contracts.workflow.steps import SagaStep, SagaStepError

__all__ = [
    "ApprovalProtocol",
    "BulkProcessorProtocol",
    "ContentCheckpointEntry",
    "ContentCheckpointKey",
    "ContentCheckpointStoreProtocol",
    "ExecutionProtocol",
    "PipelineContextProtocol",
    "PipelineProtocol",
    "PipelineStepProtocol",
    "SagaManagerProtocol",
    "SagaProtocol",
    "SagaState",
    "SagaStep",
    "SagaStepError",
    "SagaStoreProtocol",
    "SagaVersionMismatchError",
    "StateMachineProtocol",
    "StatePersistenceProtocol",
    "StateTransitionRecord",
    "WorkflowGraphProtocol",
    "WorkflowNodeProtocol",
]
