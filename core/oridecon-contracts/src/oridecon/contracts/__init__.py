"""Oridecon Unified Types.

This package provides a centralized location for all framework-wide
type definitions, protocols, and data classes.
"""

from __future__ import annotations

import pkgutil
from typing import TYPE_CHECKING, Any

__path__ = pkgutil.extend_path(__path__, __name__)

# -- Version ---------------------------------------------------------------

import importlib.metadata

from oridecon.contracts.core.constants import __version__ as __version__

# ---------------------------------------------------------------------------
# Lazy Imports (deferred until first attribute access)
# ---------------------------------------------------------------------------
if TYPE_CHECKING:
    from oridecon.contracts import (
        admin,
        ai,
        auth,
        core,
        data,
        domain,
        events,
        exceptions,
        feature_flags,
        graphql,
        infra,
        mapping,
        mcp,
        monitor,
        observability,
        search,
        security,
        tenancy,
        web,
        workflow,
    )
    from oridecon.contracts.ai import (
        AgentError,
        AgentExecutorProtocol,
        AgentProtocol,
        AgentResponse,
        AIProviderProtocol,
        ChatMessage,
        ContextPrunerProtocol,
        DocumentVectorStoreProtocol,
        EmbeddingClientProtocol,
        EpisodicMemoryProtocol,
        LLMClientProtocol,
        MemoryConsolidatorProtocol,
        MemoryProtocol,
        MemoryStoreProtocol,
        PromptAssemblerProtocol,
        PromptCompressorProtocol,
        SemanticCacheProtocol,
        SemanticMemoryProtocol,
        StrategyError,
        StrategyProtocol,
        TokenBudget,
        TokenCounterProtocol,
        ToolError,
        ToolProtocol,
        ToolRegistryProtocol,
        WorkingMemoryProtocol,
    )
    from oridecon.contracts.ai.workflow import AIWorkflowNodeProtocol
    from oridecon.contracts.audit import AuditEntry
    from oridecon.contracts.auth import (
        AuthenticatedUserProtocol,
        AuthorizerProtocol,
        AuthProviderProtocol,
        PasswordHasherProtocol,
        TokenManagerProtocol,
        UserProtocol,
    )
    from oridecon.contracts.cli import (
        CliContributorProtocol,
        GeneratorDefinition,
        GeneratorOption,
    )
    from oridecon.contracts.core import (
        JSON,
        AggregateHealthResult,
        AsyncStringSerializerProtocol,
        ClockProtocol,
        ConfigProtocol,
        ContainerProtocol,
        ContainerRegistrarProtocol,
        ContainerResolverProtocol,
        Duration,
        GracefulShutdownProtocol,
        HealthCheckAggregatorProtocol,
        HealthCheckProtocol,
        HealthCheckResult,
        HealthStatus,
        IdGeneratorProtocol,
        IdStrategy,
        Lifecycle,
        LockStoreProtocol,
        Metadata,
        OnApplicationBootstrapProtocol,
        OnApplicationShutdownProtocol,
        OnBeforeShutdownProtocol,
        OnModuleInitProtocol,
        ProviderPriority,
        ProviderProtocol,
        Result,
        SerializerProtocol,
        ServiceScope,
        TokenPayload,
    )
    from oridecon.contracts.core.idempotency import (
        IdempotencyMiddlewareProtocol,
        IdempotencyStoreProtocol,
    )
    from oridecon.contracts.core.lock import (
        AsyncLockProtocol,
        DistributedLockProtocol,
        LockInfo,
        LockManagerProtocol,
    )
    from oridecon.contracts.core.validation import ValidationError
    from oridecon.contracts.data import (
        ConnectionPoolProtocol,
        ConnectionProtocol,
        DatabaseProviderProtocol,
        DeleteResult,
        InsertResult,
        MigrationManagerProtocol,
        MigrationRecord,
        QueryLogEntry,
        QueryLoggerProtocol,
        QueryResult,
        ReadOnlyRepositoryProtocol,
        RepositoryProtocol,
        UnitOfWorkProtocol,
        UpdateResult,
    )
    from oridecon.contracts.data.sql.migrations import MigrationRunnerProtocol
    from oridecon.contracts.data.vector.protocols import VectorStoreProtocol
    from oridecon.contracts.domain.aggregates import AggregateRootProtocol
    from oridecon.contracts.domain.events import DomainEvent
    from oridecon.contracts.domain.pagination import (
        CursorPage,
        CursorPageProtocol,
        OffsetPageProtocol,
    )
    from oridecon.contracts.domain.specification import SpecificationProtocol
    from oridecon.contracts.events import (
        CommandBusProtocol,
        DomainEventPublisherProtocol,
        EventBusProtocol,
        EventHandlerProtocol,
        EventStoreProtocol,
        QueryBusProtocol,
        WebhookSignatureVerifierProtocol,
    )
    from oridecon.contracts.exceptions.components import (
        SecretNotFoundError,
    )
    from oridecon.contracts.exceptions.events import (
        DuplicateHandlerError,
        HandlerNotFoundError,
    )
    from oridecon.contracts.exceptions.security import (
        SecretAccessError,
    )
    from oridecon.contracts.feature_flags import (
        FlagEvaluation,
        FlagType,
        FlagValue,
    )
    from oridecon.contracts.infra.cache import (
        CacheBackendProtocol,
        CacheProviderProtocol,
    )
    from oridecon.contracts.infra.resilience import (
        CircuitBreakerConfig,
        RetryConfig,
    )
    from oridecon.contracts.infra.resources import (
        PoolManagerProtocol,
        PoolProtocol,
        PoolStatsProtocol,
    )
    from oridecon.contracts.infra.state import StateStoreProtocol
    from oridecon.contracts.infra.storage import BlobStoreProtocol
    from oridecon.contracts.infra.tasks import (
        JobProtocol,
        JobStatus,
        TaskExecutorProtocol,
        TaskProviderProtocol,
        TaskQueueProtocol,
    )
    from oridecon.contracts.mapping import ObjectMapperProtocol
    from oridecon.contracts.mcp import (
        MCPError,
        MCPInitializationError,
        MCPMethodNotFoundError,
        MCPPromptError,
        MCPProtocolError,
        MCPResourceError,
        MCPServerProtocol,
        MCPToolCallError,
        MCPToolProviderProtocol,
        MCPTransportProtocol,
    )
    from oridecon.contracts.observability.metrics import HealthCheckRegistryProtocol
    from oridecon.contracts.search import SearchEngineProtocol
    from oridecon.contracts.security import (
        AsyncSecretStoreProtocol,
        HasherProtocol,
        KeyDerivationProtocol,
    )
    from oridecon.contracts.security.secrets import SecretStoreProtocol
    from oridecon.contracts.tenancy import (
        TenantConfigError,
        TenantConfigProviderProtocol,
        TenantError,
        TenantInactiveError,
        TenantInfo,
        TenantIsolationStrategyProtocol,
        TenantNotFoundError,
        TenantProviderProtocol,
        TenantProvisioningError,
        TenantResolutionContext,
        TenantResolutionError,
        TenantResolverProtocol,
        TenantSlugConflictError,
        TenantStatus,
        TenantSuspendedError,
    )
    from oridecon.contracts.web import (
        CORSPolicyProtocol,
        ErrorDetail,
        ErrorResponseDTO,
        HttpRequestLoggerProtocol,
        PaginatedResponseDTO,
    )
    from oridecon.contracts.workflow import (
        SagaManagerProtocol,
        SagaProtocol,
    )

_SUBMODULE_NAMES: frozenset[str] = frozenset(
    {
        "admin",
        "ai",
        "auth",
        "cli",
        "codegen",
        "core",
        "data",
        "domain",
        "events",
        "exceptions",
        "feature_flags",
        "graphql",
        "infra",
        "lib",
        "lifecycle",
        "mailer",
        "mapping",
        "mcp",
        "monitor",
        "notification",
        "observability",
        "search",
        "security",
        "tenancy",
        "web",
        "workflow",
    }
)

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # lifecycle
    "AuditableProtocol": ("oridecon.contracts.lifecycle", "AuditableProtocol"),
    "CacheAwareProtocol": ("oridecon.contracts.lifecycle", "CacheAwareProtocol"),
    "ExportableProtocol": ("oridecon.contracts.lifecycle", "ExportableProtocol"),
    "TransactionalProtocol": ("oridecon.contracts.lifecycle", "TransactionalProtocol"),
    "ValidatableProtocol": ("oridecon.contracts.lifecycle", "ValidatableProtocol"),
    # cli
    "CliContributorProtocol": ("oridecon.contracts.cli", "CliContributorProtocol"),
    "GeneratorDefinition": ("oridecon.contracts.cli", "GeneratorDefinition"),
    "GeneratorOption": ("oridecon.contracts.cli", "GeneratorOption"),
    # agents (merged into ai/)
    "AgentError": ("oridecon.contracts.ai", "AgentError"),
    "AgentExecutorProtocol": ("oridecon.contracts.ai", "AgentExecutorProtocol"),
    "AgentProtocol": ("oridecon.contracts.ai", "AgentProtocol"),
    "AgentResponse": ("oridecon.contracts.ai", "AgentResponse"),
    "StrategyError": ("oridecon.contracts.ai", "StrategyError"),
    "StrategyProtocol": ("oridecon.contracts.ai", "StrategyProtocol"),
    "ToolError": ("oridecon.contracts.ai", "ToolError"),
    "ToolProtocol": ("oridecon.contracts.ai", "ToolProtocol"),
    "ToolRegistryProtocol": ("oridecon.contracts.ai", "ToolRegistryProtocol"),
    # ai
    "AIProviderProtocol": ("oridecon.contracts.ai", "AIProviderProtocol"),
    "ChatMessage": ("oridecon.contracts.ai.llm", "ChatMessage"),
    "ContextPrunerProtocol": ("oridecon.contracts.ai.session", "ContextPrunerProtocol"),
    "EmbeddingClientProtocol": ("oridecon.contracts.ai", "EmbeddingClientProtocol"),
    "EpisodicMemoryProtocol": ("oridecon.contracts.ai", "EpisodicMemoryProtocol"),
    "LLMClientProtocol": ("oridecon.contracts.ai", "LLMClientProtocol"),
    "MemoryConsolidatorProtocol": (
        "oridecon.contracts.ai",
        "MemoryConsolidatorProtocol",
    ),
    "MemoryProtocol": ("oridecon.contracts.ai", "MemoryProtocol"),
    "MemoryStoreProtocol": ("oridecon.contracts.ai", "MemoryStoreProtocol"),
    "PromptAssemblerProtocol": ("oridecon.contracts.ai.llm", "PromptAssemblerProtocol"),
    "PromptCompressorProtocol": (
        "oridecon.contracts.ai.rag",
        "PromptCompressorProtocol",
    ),
    "SemanticCacheProtocol": ("oridecon.contracts.ai.llm", "SemanticCacheProtocol"),
    "SemanticMemoryProtocol": ("oridecon.contracts.ai", "SemanticMemoryProtocol"),
    "TokenBudget": ("oridecon.contracts.ai.llm", "TokenBudget"),
    "TokenCounterProtocol": ("oridecon.contracts.ai.llm", "TokenCounterProtocol"),
    "DocumentVectorStoreProtocol": (
        "oridecon.contracts.ai.vector",
        "DocumentVectorStoreProtocol",
    ),
    "VectorStoreProtocol": (
        "oridecon.contracts.data.vector.protocols",
        "VectorStoreProtocol",
    ),
    "WorkingMemoryProtocol": ("oridecon.contracts.ai", "WorkingMemoryProtocol"),
    # auth
    "AuthProviderProtocol": ("oridecon.contracts.auth", "AuthProviderProtocol"),
    "AuthenticatedUserProtocol": (
        "oridecon.contracts.auth",
        "AuthenticatedUserProtocol",
    ),
    "AuthorizerProtocol": ("oridecon.contracts.auth", "AuthorizerProtocol"),
    "PasswordHasherProtocol": ("oridecon.contracts.auth", "PasswordHasherProtocol"),
    "TokenManagerProtocol": ("oridecon.contracts.auth", "TokenManagerProtocol"),
    "UserProtocol": ("oridecon.contracts.auth", "UserProtocol"),
    # cache
    "CacheBackendProtocol": ("oridecon.contracts.infra.cache", "CacheBackendProtocol"),
    "CacheProviderProtocol": (
        "oridecon.contracts.infra.cache",
        "CacheProviderProtocol",
    ),
    # core
    "AggregateHealthResult": ("oridecon.contracts.core", "AggregateHealthResult"),
    "ConfigProtocol": ("oridecon.contracts.core", "ConfigProtocol"),
    "ClockProtocol": ("oridecon.contracts.core", "ClockProtocol"),
    "ContainerProtocol": ("oridecon.contracts.core", "ContainerProtocol"),
    "ContainerRegistrarProtocol": (
        "oridecon.contracts.core",
        "ContainerRegistrarProtocol",
    ),
    "ContainerResolverProtocol": (
        "oridecon.contracts.core",
        "ContainerResolverProtocol",
    ),
    "GracefulShutdownProtocol": ("oridecon.contracts.core", "GracefulShutdownProtocol"),
    "HealthCheckAggregatorProtocol": (
        "oridecon.contracts.core",
        "HealthCheckAggregatorProtocol",
    ),
    "HealthCheckProtocol": ("oridecon.contracts.core", "HealthCheckProtocol"),
    "HealthCheckRegistryProtocol": (
        "oridecon.contracts.observability.metrics",
        "HealthCheckRegistryProtocol",
    ),
    "HealthCheckResult": ("oridecon.contracts.core", "HealthCheckResult"),
    "HealthStatus": ("oridecon.contracts.core", "HealthStatus"),
    "Duration": ("oridecon.contracts.core", "Duration"),
    "IdGeneratorProtocol": ("oridecon.contracts.core", "IdGeneratorProtocol"),
    "IdStrategy": ("oridecon.contracts.core", "IdStrategy"),
    "JSON": ("oridecon.contracts.core", "JSON"),
    "Lifecycle": ("oridecon.contracts.core", "Lifecycle"),
    "LockStoreProtocol": ("oridecon.contracts.core", "LockStoreProtocol"),
    "Metadata": ("oridecon.contracts.core", "Metadata"),
    "OnApplicationBootstrapProtocol": (
        "oridecon.contracts.core",
        "OnApplicationBootstrapProtocol",
    ),
    "OnApplicationShutdownProtocol": (
        "oridecon.contracts.core",
        "OnApplicationShutdownProtocol",
    ),
    "OnBeforeShutdownProtocol": ("oridecon.contracts.core", "OnBeforeShutdownProtocol"),
    "OnModuleInitProtocol": ("oridecon.contracts.core", "OnModuleInitProtocol"),
    "ProviderPriority": ("oridecon.contracts.core", "ProviderPriority"),
    "ProviderProtocol": ("oridecon.contracts.core", "ProviderProtocol"),
    "Result": ("oridecon.contracts.core", "Result"),
    "AsyncStringSerializerProtocol": (
        "oridecon.contracts.core",
        "AsyncStringSerializerProtocol",
    ),
    "SerializerProtocol": ("oridecon.contracts.core", "SerializerProtocol"),
    "ServiceScope": ("oridecon.contracts.core", "ServiceScope"),
    "TokenPayload": ("oridecon.contracts.core", "TokenPayload"),
    # idempotency
    "IdempotencyMiddlewareProtocol": (
        "oridecon.contracts.core.idempotency",
        "IdempotencyMiddlewareProtocol",
    ),
    "IdempotencyStoreProtocol": (
        "oridecon.contracts.core.idempotency",
        "IdempotencyStoreProtocol",
    ),
    # lock
    "AsyncLockProtocol": ("oridecon.contracts.core.lock", "AsyncLockProtocol"),
    "DistributedLockProtocol": (
        "oridecon.contracts.core.lock",
        "DistributedLockProtocol",
    ),
    "LockInfo": ("oridecon.contracts.core.lock", "LockInfo"),
    "LockManagerProtocol": ("oridecon.contracts.core.lock", "LockManagerProtocol"),
    # validation
    "ValidationError": ("oridecon.contracts.core.validation", "ValidationError"),
    # data
    "ConnectionPoolProtocol": ("oridecon.contracts.data", "ConnectionPoolProtocol"),
    "ConnectionProtocol": ("oridecon.contracts.data", "ConnectionProtocol"),
    "DatabaseProviderProtocol": ("oridecon.contracts.data", "DatabaseProviderProtocol"),
    "DeleteResult": ("oridecon.contracts.data", "DeleteResult"),
    "InsertResult": ("oridecon.contracts.data", "InsertResult"),
    "MigrationManagerProtocol": ("oridecon.contracts.data", "MigrationManagerProtocol"),
    "MigrationRecord": ("oridecon.contracts.data", "MigrationRecord"),
    "QueryLogEntry": ("oridecon.contracts.data", "QueryLogEntry"),
    "QueryLoggerProtocol": ("oridecon.contracts.data", "QueryLoggerProtocol"),
    "QueryResult": ("oridecon.contracts.data", "QueryResult"),
    "ReadOnlyRepositoryProtocol": (
        "oridecon.contracts.data",
        "ReadOnlyRepositoryProtocol",
    ),
    "RepositoryProtocol": ("oridecon.contracts.data", "RepositoryProtocol"),
    "UnitOfWorkProtocol": ("oridecon.contracts.data", "UnitOfWorkProtocol"),
    "UpdateResult": ("oridecon.contracts.data", "UpdateResult"),
    # migrations
    "MigrationRunnerProtocol": (
        "oridecon.contracts.data.sql.migrations",
        "MigrationRunnerProtocol",
    ),
    # aggregates
    "AggregateRootProtocol": (
        "oridecon.contracts.domain.aggregates",
        "AggregateRootProtocol",
    ),
    # events
    "DomainEvent": ("oridecon.contracts.domain.events", "DomainEvent"),
    # specification
    "SpecificationProtocol": (
        "oridecon.contracts.domain.specification",
        "SpecificationProtocol",
    ),
    # state
    "StateStoreProtocol": ("oridecon.contracts.infra.state", "StateStoreProtocol"),
    # events
    "CommandBusProtocol": ("oridecon.contracts.events", "CommandBusProtocol"),
    "DomainEventPublisherProtocol": (
        "oridecon.contracts.events",
        "DomainEventPublisherProtocol",
    ),
    "EventBusProtocol": ("oridecon.contracts.events", "EventBusProtocol"),
    "EventHandlerProtocol": ("oridecon.contracts.events", "EventHandlerProtocol"),
    "EventStoreProtocol": ("oridecon.contracts.events", "EventStoreProtocol"),
    "QueryBusProtocol": ("oridecon.contracts.events", "QueryBusProtocol"),
    # components
    "SecretNotFoundError": (
        "oridecon.contracts.exceptions.components",
        "SecretNotFoundError",
    ),
    # security
    "SecretAccessError": (
        "oridecon.contracts.exceptions.security",
        "SecretAccessError",
    ),
    # events
    "DuplicateHandlerError": (
        "oridecon.contracts.exceptions.events",
        "DuplicateHandlerError",
    ),
    "HandlerNotFoundError": (
        "oridecon.contracts.exceptions.events",
        "HandlerNotFoundError",
    ),
    # mapping
    "ObjectMapperProtocol": ("oridecon.contracts.mapping", "ObjectMapperProtocol"),
    # mcp
    "MCPError": ("oridecon.contracts.mcp", "MCPError"),
    "MCPInitializationError": ("oridecon.contracts.mcp", "MCPInitializationError"),
    "MCPMethodNotFoundError": ("oridecon.contracts.mcp", "MCPMethodNotFoundError"),
    "MCPPromptError": ("oridecon.contracts.mcp", "MCPPromptError"),
    "MCPProtocolError": ("oridecon.contracts.mcp", "MCPProtocolError"),
    "MCPResourceError": ("oridecon.contracts.mcp", "MCPResourceError"),
    "MCPServerProtocol": ("oridecon.contracts.mcp", "MCPServerProtocol"),
    "MCPToolCallError": ("oridecon.contracts.mcp", "MCPToolCallError"),
    "MCPToolProviderProtocol": ("oridecon.contracts.mcp", "MCPToolProviderProtocol"),
    "MCPTransportProtocol": ("oridecon.contracts.mcp", "MCPTransportProtocol"),
    # monitor
    "ProjectionTier": ("oridecon.contracts.monitor", "ProjectionTier"),
    "WebhookSignatureVerifierProtocol": (
        "oridecon.contracts.events",
        "WebhookSignatureVerifierProtocol",
    ),
    # resilience
    "CircuitBreakerConfig": (
        "oridecon.contracts.infra.resilience",
        "CircuitBreakerConfig",
    ),
    "RetryConfig": ("oridecon.contracts.infra.resilience", "RetryConfig"),
    # search
    "SearchEngineProtocol": ("oridecon.contracts.search", "SearchEngineProtocol"),
    # security
    "AsyncSecretStoreProtocol": (
        "oridecon.contracts.security",
        "AsyncSecretStoreProtocol",
    ),
    "HasherProtocol": ("oridecon.contracts.security", "HasherProtocol"),
    "KeyDerivationProtocol": (
        "oridecon.contracts.security",
        "KeyDerivationProtocol",
    ),
    # secrets
    "SecretStoreProtocol": (
        "oridecon.contracts.security.secrets",
        "SecretStoreProtocol",
    ),
    # resources
    "PoolProtocol": ("oridecon.contracts.infra.resources", "PoolProtocol"),
    "PoolManagerProtocol": (
        "oridecon.contracts.infra.resources",
        "PoolManagerProtocol",
    ),
    "PoolStatsProtocol": ("oridecon.contracts.infra.resources", "PoolStatsProtocol"),
    # storage
    "BlobStoreProtocol": ("oridecon.contracts.infra.storage", "BlobStoreProtocol"),
    # tasks
    "JobProtocol": ("oridecon.contracts.infra.tasks", "JobProtocol"),
    "JobStatus": ("oridecon.contracts.infra.tasks", "JobStatus"),
    "TaskExecutorProtocol": ("oridecon.contracts.infra.tasks", "TaskExecutorProtocol"),
    "TaskProviderProtocol": ("oridecon.contracts.infra.tasks", "TaskProviderProtocol"),
    "TaskQueueProtocol": ("oridecon.contracts.infra.tasks", "TaskQueueProtocol"),
    # web
    "CORSPolicyProtocol": ("oridecon.contracts.web", "CORSPolicyProtocol"),
    "ErrorDetail": ("oridecon.contracts.web", "ErrorDetail"),
    "ErrorResponseDTO": ("oridecon.contracts.web", "ErrorResponseDTO"),
    "HttpRequestLoggerProtocol": (
        "oridecon.contracts.web",
        "HttpRequestLoggerProtocol",
    ),
    "PaginatedResponseDTO": ("oridecon.contracts.web", "PaginatedResponseDTO"),
    # workflow
    "SagaProtocol": ("oridecon.contracts.workflow", "SagaProtocol"),
    "SagaManagerProtocol": ("oridecon.contracts.workflow", "SagaManagerProtocol"),
    "WorkflowNodeProtocol": (
        "oridecon.contracts.workflow.protocols",
        "WorkflowNodeProtocol",
    ),
    "AIWorkflowNodeProtocol": (
        "oridecon.contracts.ai.workflow",
        "AIWorkflowNodeProtocol",
    ),
    # audit
    "AuditEntry": ("oridecon.contracts.audit", "AuditEntry"),
    # feature_flags
    "FlagEvaluation": ("oridecon.contracts.feature_flags", "FlagEvaluation"),
    "FlagType": ("oridecon.contracts.feature_flags", "FlagType"),
    "FlagValue": ("oridecon.contracts.feature_flags", "FlagValue"),
    # pagination
    "CursorPage": ("oridecon.contracts.domain.pagination", "CursorPage"),
    "CursorPageProtocol": (
        "oridecon.contracts.domain.pagination",
        "CursorPageProtocol",
    ),
    "OffsetPageProtocol": (
        "oridecon.contracts.domain.pagination",
        "OffsetPageProtocol",
    ),
    # tenancy
    "TenantConfigError": ("oridecon.contracts.tenancy", "TenantConfigError"),
    "TenantConfigProviderProtocol": (
        "oridecon.contracts.tenancy",
        "TenantConfigProviderProtocol",
    ),
    "TenantError": ("oridecon.contracts.tenancy", "TenantError"),
    "TenantInactiveError": ("oridecon.contracts.tenancy", "TenantInactiveError"),
    "TenantInfo": ("oridecon.contracts.tenancy", "TenantInfo"),
    "TenantIsolationStrategyProtocol": (
        "oridecon.contracts.tenancy",
        "TenantIsolationStrategyProtocol",
    ),
    "TenantNotFoundError": ("oridecon.contracts.tenancy", "TenantNotFoundError"),
    "TenantProviderProtocol": ("oridecon.contracts.tenancy", "TenantProviderProtocol"),
    "TenantProvisioningError": (
        "oridecon.contracts.tenancy",
        "TenantProvisioningError",
    ),
    "TenantResolutionContext": (
        "oridecon.contracts.tenancy",
        "TenantResolutionContext",
    ),
    "TenantResolutionError": ("oridecon.contracts.tenancy", "TenantResolutionError"),
    "TenantResolverProtocol": ("oridecon.contracts.tenancy", "TenantResolverProtocol"),
    "TenantSlugConflictError": (
        "oridecon.contracts.tenancy",
        "TenantSlugConflictError",
    ),
    "TenantStatus": ("oridecon.contracts.tenancy", "TenantStatus"),
    "TenantSuspendedError": ("oridecon.contracts.tenancy", "TenantSuspendedError"),
}


def __getattr__(name: str) -> Any:
    """Lazy-load public symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    if name in _SUBMODULE_NAMES:
        import importlib

        return importlib.import_module(f"oridecon.contracts.{name}")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = list(_LAZY_IMPORTS)
