from __future__ import annotations

from oridecon.contracts.core.clock import ClockProtocol, Duration
from oridecon.contracts.core.concurrency_enums import (
    ConcurrencyStrategy,
    ExecutionStrategy,
)
from oridecon.contracts.core.concurrency_protocols import (
    ChannelProtocol,
    DispatcherProtocol,
    ParallelProtocol,
    TaskManagerProtocol,
)
from oridecon.contracts.core.config import ConfigIssue, ConfigProtocol, Environment
from oridecon.contracts.core.constants import (
    ALL_ENTRY_POINT_GROUPS,
    EP_AI_SUBSYSTEMS,
    EP_PROVIDERS,
)
from oridecon.contracts.core.context import (
    ContextProtocol,
    RequestContextProtocol,
)
from oridecon.contracts.core.di import (
    ContainerProtocol,
    ContainerRegistrarProtocol,
    ContainerResolverProtocol,
)
from oridecon.contracts.core.disposable import AsyncDisposableProtocol
from oridecon.contracts.core.health import (
    AggregateHealthResult,
    HealthCheckableProtocol,
    HealthCheckAggregatorProtocol,
    HealthCheckCategory,
    HealthCheckProtocol,
    HealthCheckResult,
    HealthStatus,
)
from oridecon.contracts.core.hooks import HookPriority, HookRegistryProtocol
from oridecon.contracts.core.idempotency import IdempotencyStoreProtocol
from oridecon.contracts.core.identity import IdGeneratorProtocol, IdStrategy
from oridecon.contracts.core.invocation import (
    InvocationContextProtocol,
    InvocationHandlerProtocol,
    InvocationMiddlewareProtocol,
    InvocationPipelineProtocol,
)
from oridecon.contracts.core.lifecycle import (
    GracefulShutdownProtocol,
    OnApplicationBootstrapProtocol,
    OnApplicationShutdownProtocol,
    OnBeforeShutdownProtocol,
    OnConfigReloadProtocol,
    OnModuleInitProtocol,
)
from oridecon.contracts.core.lock import (
    AsyncLockProtocol,
    DistributedLockProtocol,
    LockInfo,
    LockManagerProtocol,
)
from oridecon.contracts.core.logging import LoggerProtocol
from oridecon.contracts.core.middleware import (
    ExceptionFilterChainProtocol,
    Middleware,
    MiddlewarePipelineProtocol,
    MiddlewareProtocol,
)
from oridecon.contracts.core.provider import (
    Lifecycle,
    ProviderPriority,
    ProviderProtocol,
)
from oridecon.contracts.core.registry import (
    BackendRegistryProtocol,
    RegistryProtocol,
    StrategyRegistryProtocol,
)
from oridecon.contracts.core.result import Err, Ok, Result
from oridecon.contracts.core.scopes import ServiceScope
from oridecon.contracts.core.serialization import (
    AsyncStringSerializerProtocol,
    JsonSerializerProtocol,
    SerializerProtocol,
)
from oridecon.contracts.core.stores import LockStoreProtocol as LockStoreProtocol
from oridecon.contracts.core.trace_context import (
    new_span_id,
    new_trace_id,
    span_id_var,
    trace_flags_var,
    trace_id_var,
)
from oridecon.contracts.core.types import (
    JSON,
    EntityId,
    Headers,
    Metadata,
    QueryParams,
    Timestamp,
    TokenPayload,
    Version,
)
from oridecon.contracts.core.validation import ValidationError
from oridecon.contracts.exceptions.container import OrphanedRegistration
from oridecon.contracts.infra.resilience import CircuitState

__all__ = [
    "JSON",
    "AggregateHealthResult",
    "AsyncDisposableProtocol",
    "AsyncLockProtocol",
    "AsyncStringSerializerProtocol",
    "BackendRegistryProtocol",
    "CircuitState",
    "ClockProtocol",
    "ConcurrencyStrategy",
    "ConfigIssue",
    "ConfigProtocol",
    "ContainerProtocol",
    "ContainerRegistrarProtocol",
    "ContainerResolverProtocol",
    "ContextProtocol",
    "DispatcherProtocol",
    "DistributedLockProtocol",
    "Duration",
    "EntityId",
    "Environment",
    "Err",
    "ExceptionFilterChainProtocol",
    "ExecutionStrategy",
    "GracefulShutdownProtocol",
    "Headers",
    "HealthCheckAggregatorProtocol",
    "HealthCheckCategory",
    "HealthCheckProtocol",
    "HealthCheckResult",
    "HealthCheckableProtocol",
    "HealthStatus",
    "HookPriority",
    "HookRegistryProtocol",
    "IdGeneratorProtocol",
    "IdStrategy",
    "IdempotencyStoreProtocol",
    "InvocationContextProtocol",
    "InvocationHandlerProtocol",
    "InvocationMiddlewareProtocol",
    "InvocationPipelineProtocol",
    "JsonSerializerProtocol",
    "Lifecycle",
    "LockInfo",
    "LockManagerProtocol",
    "LockStoreProtocol",
    "LoggerProtocol",
    "Metadata",
    "Middleware",
    "MiddlewarePipelineProtocol",
    "MiddlewareProtocol",
    "Ok",
    "OnApplicationBootstrapProtocol",
    "OnApplicationShutdownProtocol",
    "OnBeforeShutdownProtocol",
    "OnConfigReloadProtocol",
    "OnModuleInitProtocol",
    "OrphanedRegistration",
    "ParallelProtocol",
    "ProviderPriority",
    "ProviderProtocol",
    "QueryParams",
    "RegistryProtocol",
    "RequestContextProtocol",
    "Result",
    "SerializerProtocol",
    "ServiceScope",
    "StrategyRegistryProtocol",
    "TaskManagerProtocol",
    "Timestamp",
    "TokenPayload",
    "ValidationError",
    "Version",
    "new_span_id",
    "new_trace_id",
    "span_id_var",
    "trace_flags_var",
    "trace_id_var",
]
