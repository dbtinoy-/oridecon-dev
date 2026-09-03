"""Workflow orchestration package for Oridecon Framework.

Provides pipeline execution, transformation pipes, bulk operations,
saga coordination, and directed-graph workflow execution.
"""

from __future__ import annotations

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import importlib
import importlib.metadata
from typing import TYPE_CHECKING, Any

from oridecon.workflow.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.workflow.bulk.models import (
        BulkBatchResult,
        BulkItemError,
        BulkOperationMetrics,
        BulkOperationState,
    )
    from oridecon.workflow.bulk.operation import BulkOperation
    from oridecon.workflow.checkpoint.store_cache import CacheContentCheckpointStore
    from oridecon.workflow.checkpoint.store_database import (
        DatabaseContentCheckpointStore,
    )
    from oridecon.workflow.checkpoint.store_memory import InMemoryContentCheckpointStore
    from oridecon.workflow.config import (
        BulkOperationConfig,
        ContentCheckpointConfig,
        GraphConfig,
    )
    from oridecon.workflow.core.definition import WorkflowDefinition
    from oridecon.workflow.core.instance import WorkflowInstance
    from oridecon.workflow.core.pipe import TransformPipe
    from oridecon.workflow.decorators import saga_step, workflow
    from oridecon.workflow.di.provider import WorkflowProvider
    from oridecon.workflow.exceptions import (
        BulkOperationCancelledError,
        BulkOperationError,
        BulkOperationTimeoutError,
        CycleDetectedError,
        GraphExecutionError,
        GraphTimeoutError,
        GraphValidationError,
        HumanInputRequiredError,
        NodeExecutionError,
        PipelineExecutionError,
        PipelineStepError,
        WorkflowCompensationError,
        WorkflowError,
        WorkflowNotFoundError,
        WorkflowStateError,
        WorkflowStepError,
        WorkflowTimeoutError,
        WorkflowVersionMismatchError,
    )
    from oridecon.workflow.execution.checkpoint import WorkflowCheckpoint
    from oridecon.workflow.execution.history import ExecutionHistory
    from oridecon.workflow.execution.runner import WorkflowRunner
    from oridecon.workflow.graph.builder import WorkflowBuilder
    from oridecon.workflow.graph.edge import WorkflowEdge
    from oridecon.workflow.graph.engine import WorkflowEngine
    from oridecon.workflow.graph.node import AbstractWorkflowNode, NodeType
    from oridecon.workflow.graph.state import WorkflowState
    from oridecon.workflow.module import WorkflowModule
    from oridecon.workflow.nodes.agent_node import AgentNode
    from oridecon.workflow.nodes.gate_node import GateNode
    from oridecon.workflow.nodes.human_node import HumanNode
    from oridecon.workflow.nodes.llm_node import LLMNode
    from oridecon.workflow.nodes.subworkflow_node import SubworkflowNode
    from oridecon.workflow.nodes.tool_node import ToolNode
    from oridecon.workflow.pipeline import (
        ConditionalStep,
        FunctionStep,
        ParallelStep,
        Pipeline,
        PipelineContext,
        PipelineStep,
        conditional,
        parallel,
        pipeline_step,
        step,
    )
    from oridecon.workflow.saga import (
        AbstractSaga,
        ContentAddressedSaga,
        ContentAddressedStage,
    )
    from oridecon.workflow.types import GraphResult, NodeResult

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # Bulk
    "BulkOperation": ("oridecon.workflow.bulk.operation", "BulkOperation"),
    "BulkBatchResult": ("oridecon.workflow.bulk.models", "BulkBatchResult"),
    "BulkItemError": ("oridecon.workflow.bulk.models", "BulkItemError"),
    "BulkOperationMetrics": ("oridecon.workflow.bulk.models", "BulkOperationMetrics"),
    "BulkOperationState": ("oridecon.workflow.bulk.models", "BulkOperationState"),
    # Pipeline
    "TransformPipe": ("oridecon.workflow.core.pipe", "TransformPipe"),
    # Core
    "WorkflowDefinition": ("oridecon.workflow.core.definition", "WorkflowDefinition"),
    "WorkflowInstance": ("oridecon.workflow.core.instance", "WorkflowInstance"),
    "ConditionalStep": ("oridecon.workflow.pipeline", "ConditionalStep"),
    "FunctionStep": ("oridecon.workflow.pipeline", "FunctionStep"),
    "ParallelStep": ("oridecon.workflow.pipeline", "ParallelStep"),
    "Pipeline": ("oridecon.workflow.pipeline", "Pipeline"),
    "PipelineContext": ("oridecon.workflow.pipeline", "PipelineContext"),
    "PipelineStep": ("oridecon.workflow.pipeline", "PipelineStep"),
    "conditional": ("oridecon.workflow.pipeline", "conditional"),
    "parallel": ("oridecon.workflow.pipeline", "parallel"),
    "pipeline_step": ("oridecon.workflow.pipeline", "pipeline_step"),
    "step": ("oridecon.workflow.pipeline", "step"),
    # SagaProtocol
    "AbstractSaga": ("oridecon.workflow.saga", "AbstractSaga"),
    "ContentAddressedSaga": ("oridecon.workflow.saga", "ContentAddressedSaga"),
    "ContentAddressedStage": ("oridecon.workflow.saga", "ContentAddressedStage"),
    # Types
    "SagaStep": ("oridecon.workflow.types", "SagaStep"),
    "StepExecutionResult": ("oridecon.workflow.types", "StepExecutionResult"),
    "StepStatus": ("oridecon.workflow.types", "StepStatus"),
    # Graph types
    "NodeResult": ("oridecon.workflow.types", "NodeResult"),
    "GraphResult": ("oridecon.workflow.types", "GraphResult"),
    # Graph config
    "GraphConfig": ("oridecon.workflow.config", "GraphConfig"),
    "BulkOperationConfig": ("oridecon.workflow.config", "BulkOperationConfig"),
    "ContentCheckpointConfig": ("oridecon.workflow.config", "ContentCheckpointConfig"),
    # Exceptions (existing)
    "BulkOperationCancelledError": (
        "oridecon.workflow.exceptions",
        "BulkOperationCancelledError",
    ),
    "BulkOperationError": ("oridecon.workflow.exceptions", "BulkOperationError"),
    "BulkOperationTimeoutError": (
        "oridecon.workflow.exceptions",
        "BulkOperationTimeoutError",
    ),
    "PipelineExecutionError": (
        "oridecon.workflow.exceptions",
        "PipelineExecutionError",
    ),
    "PipelineStepError": ("oridecon.workflow.exceptions", "PipelineStepError"),
    "WorkflowError": ("oridecon.workflow.exceptions", "WorkflowError"),
    "WorkflowNotFoundError": (
        "oridecon.workflow.exceptions",
        "WorkflowNotFoundError",
    ),
    "WorkflowStateError": ("oridecon.workflow.exceptions", "WorkflowStateError"),
    "WorkflowStepError": ("oridecon.workflow.exceptions", "WorkflowStepError"),
    "WorkflowTimeoutError": (
        "oridecon.workflow.exceptions",
        "WorkflowTimeoutError",
    ),
    "WorkflowCompensationError": (
        "oridecon.workflow.exceptions",
        "WorkflowCompensationError",
    ),
    # Graph exceptions
    "GraphExecutionError": ("oridecon.workflow.exceptions", "GraphExecutionError"),
    "NodeExecutionError": ("oridecon.workflow.exceptions", "NodeExecutionError"),
    "CycleDetectedError": ("oridecon.workflow.exceptions", "CycleDetectedError"),
    "GraphTimeoutError": ("oridecon.workflow.exceptions", "GraphTimeoutError"),
    "GraphValidationError": ("oridecon.workflow.exceptions", "GraphValidationError"),
    "HumanInputRequiredError": (
        "oridecon.workflow.exceptions",
        "HumanInputRequiredError",
    ),
    "WorkflowVersionMismatchError": (
        "oridecon.workflow.exceptions",
        "WorkflowVersionMismatchError",
    ),
    # Graph engine
    "WorkflowEngine": ("oridecon.workflow.graph.engine", "WorkflowEngine"),
    "WorkflowBuilder": ("oridecon.workflow.graph.builder", "WorkflowBuilder"),
    "WorkflowState": ("oridecon.workflow.graph.state", "WorkflowState"),
    "WorkflowEdge": ("oridecon.workflow.graph.edge", "WorkflowEdge"),
    "AbstractWorkflowNode": ("oridecon.workflow.graph.node", "AbstractWorkflowNode"),
    "NodeType": ("oridecon.workflow.graph.node", "NodeType"),
    # Nodes
    "AgentNode": ("oridecon.workflow.nodes.agent_node", "AgentNode"),
    "LLMNode": ("oridecon.workflow.nodes.llm_node", "LLMNode"),
    "ToolNode": ("oridecon.workflow.nodes.tool_node", "ToolNode"),
    "HumanNode": ("oridecon.workflow.nodes.human_node", "HumanNode"),
    "GateNode": ("oridecon.workflow.nodes.gate_node", "GateNode"),
    "SubworkflowNode": ("oridecon.workflow.nodes.subworkflow_node", "SubworkflowNode"),
    # Execution
    "WorkflowRunner": ("oridecon.workflow.execution.runner", "WorkflowRunner"),
    "WorkflowCheckpoint": (
        "oridecon.workflow.execution.checkpoint",
        "WorkflowCheckpoint",
    ),
    "ExecutionHistory": ("oridecon.workflow.execution.history", "ExecutionHistory"),
    # Checkpoint
    "InMemoryContentCheckpointStore": (
        "oridecon.workflow.checkpoint.store_memory",
        "InMemoryContentCheckpointStore",
    ),
    "CacheContentCheckpointStore": (
        "oridecon.workflow.checkpoint.store_cache",
        "CacheContentCheckpointStore",
    ),
    "DatabaseContentCheckpointStore": (
        "oridecon.workflow.checkpoint.store_database",
        "DatabaseContentCheckpointStore",
    ),
    # Decorators
    "workflow": ("oridecon.workflow.decorators", "workflow"),
    "saga_step": ("oridecon.workflow.decorators", "saga_step"),
    # DI
    "WorkflowModule": ("oridecon.workflow.module", "WorkflowModule"),
    "WorkflowProvider": ("oridecon.workflow.di.provider", "WorkflowProvider"),
    # Events
    "WorkflowStartedEvent": ("oridecon.workflow.events", "WorkflowStartedEvent"),
    "WorkflowCompletedEvent": ("oridecon.workflow.events", "WorkflowCompletedEvent"),
    "WorkflowFailedEvent": ("oridecon.workflow.events", "WorkflowFailedEvent"),
    # Hooks
    "WorkflowCompletedHook": ("oridecon.workflow.hooks", "WorkflowCompletedHook"),
    "WorkflowStartedHook": ("oridecon.workflow.hooks", "WorkflowStartedHook"),
    "WorkflowStateTransitionedHook": (
        "oridecon.workflow.hooks",
        "WorkflowStateTransitionedHook",
    ),
}


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        module_path, attr = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = [
    "AbstractSaga",
    "AbstractWorkflowNode",
    "AgentNode",
    "BulkBatchResult",
    "BulkItemError",
    "BulkOperation",
    "BulkOperationCancelledError",
    "BulkOperationConfig",
    "BulkOperationError",
    "BulkOperationMetrics",
    "BulkOperationState",
    "BulkOperationTimeoutError",
    "CacheContentCheckpointStore",
    "ConditionalStep",
    "ContentAddressedSaga",
    "ContentAddressedStage",
    "ContentCheckpointConfig",
    "CycleDetectedError",
    "DatabaseContentCheckpointStore",
    "ExecutionHistory",
    "FunctionStep",
    "GateNode",
    "GraphConfig",
    "GraphExecutionError",
    "GraphResult",
    "GraphTimeoutError",
    "GraphValidationError",
    "HumanInputRequiredError",
    "HumanNode",
    "InMemoryContentCheckpointStore",
    "LLMNode",
    "NodeExecutionError",
    "NodeResult",
    "NodeType",
    "ParallelStep",
    "Pipeline",
    "PipelineContext",
    "PipelineExecutionError",
    "PipelineStep",
    "PipelineStepError",
    "SagaStep",
    "StepExecutionResult",
    "StepStatus",
    "SubworkflowNode",
    "ToolNode",
    "TransformPipe",
    "WorkflowBuilder",
    "WorkflowCheckpoint",
    "WorkflowCompensationError",
    "WorkflowCompletedEvent",
    "WorkflowCompletedHook",
    "WorkflowDefinition",
    "WorkflowEdge",
    "WorkflowEngine",
    "WorkflowError",
    "WorkflowFailedEvent",
    "WorkflowInstance",
    "WorkflowModule",
    "WorkflowNotFoundError",
    "WorkflowProvider",
    "WorkflowRunner",
    "WorkflowStartedEvent",
    "WorkflowStartedHook",
    "WorkflowState",
    "WorkflowStateError",
    "WorkflowStateTransitionedHook",
    "WorkflowStepError",
    "WorkflowTimeoutError",
    "WorkflowVersionMismatchError",
    "conditional",
    "parallel",
    "pipeline_step",
    "saga_step",
    "step",
    "workflow",
]
