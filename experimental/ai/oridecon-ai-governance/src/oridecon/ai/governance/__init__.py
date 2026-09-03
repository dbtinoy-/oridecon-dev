"""AI Governance sub-package."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from typing import TYPE_CHECKING, Any

try:
    __version__ = version("oridecon-ai-governance")
except PackageNotFoundError:
    __version__ = "0.0.0"

if TYPE_CHECKING:
    from oridecon.ai.governance.audit import (
        AIAuditEvent,
        AIAuditStore,
        AuditEventType,
        AuditQuery,
        AuditSummary,
        InMemoryAuditStore,
    )
    from oridecon.ai.governance.config import GovernanceConfig
    from oridecon.ai.governance.content_gate import (
        AlwaysAllowGate,
        CompositeGate,
        ContentPolicyGateProtocol,
        ContentPolicyService,
        PolicyDecision,
        PolicyObserverProtocol,
        PolicyOutcome,
        PolicyRequest,
    )
    from oridecon.ai.governance.di.provider import GovernanceProvider
    from oridecon.ai.governance.exceptions import (
        BudgetExceededError,
        GovernanceError,
        ModelAccessDeniedError,
        RateLimitExceededError,
        ResourceExhaustedError,
    )
    from oridecon.ai.governance.hooks import (
        GovernanceAuditRecordedHook,
        GovernancePersistenceWrittenHook,
        GovernancePolicyEvaluatedHook,
    )
    from oridecon.ai.governance.module import GovernanceModule
    from oridecon.ai.governance.persistence import (
        GovernancePersistence,
        InMemoryGovernancePersistence,
        RedisGovernancePersistence,
    )
    from oridecon.ai.governance.resource.reconciliation import (
        GaugeReconciliationCallback,
        GaugeReconciliationWorker,
    )
    from oridecon.ai.governance.resource.registry import (
        ResourceUnitRegistry,
    )
    from oridecon.ai.governance.resource.tracker import (
        ResourceUnitTracker,
    )
    from oridecon.ai.governance.services.manager import AIGovernanceManager

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # --- Content Gate ---
    "AlwaysAllowGate": (
        "oridecon.ai.governance.content_gate",
        "AlwaysAllowGate",
    ),
    "CompositeGate": (
        "oridecon.ai.governance.content_gate",
        "CompositeGate",
    ),
    "ContentPolicyGateProtocol": (
        "oridecon.ai.governance.content_gate",
        "ContentPolicyGateProtocol",
    ),
    "ContentPolicyService": (
        "oridecon.ai.governance.content_gate",
        "ContentPolicyService",
    ),
    "PolicyDecision": (
        "oridecon.ai.governance.content_gate",
        "PolicyDecision",
    ),
    "PolicyObserverProtocol": (
        "oridecon.ai.governance.content_gate",
        "PolicyObserverProtocol",
    ),
    "PolicyOutcome": (
        "oridecon.ai.governance.content_gate",
        "PolicyOutcome",
    ),
    "PolicyRequest": (
        "oridecon.ai.governance.content_gate",
        "PolicyRequest",
    ),
    # --- Audit ---
    "AIAuditEvent": ("oridecon.ai.governance.audit", "AIAuditEvent"),
    "AIAuditStore": ("oridecon.ai.governance.audit", "AIAuditStore"),
    "AuditEventType": ("oridecon.ai.governance.audit", "AuditEventType"),
    "AuditQuery": ("oridecon.ai.governance.audit", "AuditQuery"),
    "AuditSummary": ("oridecon.ai.governance.audit", "AuditSummary"),
    "InMemoryAuditStore": ("oridecon.ai.governance.audit", "InMemoryAuditStore"),
    # --- Config ---
    "GovernanceConfig": ("oridecon.ai.governance.config", "GovernanceConfig"),
    # --- DI ---
    "GovernanceProvider": ("oridecon.ai.governance.di.provider", "GovernanceProvider"),
    "GovernanceModule": ("oridecon.ai.governance.module", "GovernanceModule"),
    # --- Exceptions ---
    "GovernanceError": ("oridecon.ai.governance.exceptions", "GovernanceError"),
    "BudgetExceededError": ("oridecon.ai.governance.exceptions", "BudgetExceededError"),
    "ModelAccessDeniedError": (
        "oridecon.ai.governance.exceptions",
        "ModelAccessDeniedError",
    ),
    "RateLimitExceededError": (
        "oridecon.ai.governance.exceptions",
        "RateLimitExceededError",
    ),
    # --- Hooks ---
    "GovernanceAuditRecordedHook": (
        "oridecon.ai.governance.hooks",
        "GovernanceAuditRecordedHook",
    ),
    "GovernancePersistenceWrittenHook": (
        "oridecon.ai.governance.hooks",
        "GovernancePersistenceWrittenHook",
    ),
    "GovernancePolicyEvaluatedHook": (
        "oridecon.ai.governance.hooks",
        "GovernancePolicyEvaluatedHook",
    ),
    # --- Persistence ---
    "GovernancePersistence": (
        "oridecon.ai.governance.persistence",
        "GovernancePersistence",
    ),
    "InMemoryGovernancePersistence": (
        "oridecon.ai.governance.persistence",
        "InMemoryGovernancePersistence",
    ),
    "RedisGovernancePersistence": (
        "oridecon.ai.governance.persistence",
        "RedisGovernancePersistence",
    ),
    # --- Resource ---
    "ResourceExhaustedError": (
        "oridecon.ai.governance.exceptions",
        "ResourceExhaustedError",
    ),
    "ResourceUnitRegistry": (
        "oridecon.ai.governance.resource.registry",
        "ResourceUnitRegistry",
    ),
    "ResourceUnitTracker": (
        "oridecon.ai.governance.resource.tracker",
        "ResourceUnitTracker",
    ),
    "GaugeReconciliationCallback": (
        "oridecon.ai.governance.resource.reconciliation",
        "GaugeReconciliationCallback",
    ),
    "GaugeReconciliationWorker": (
        "oridecon.ai.governance.resource.reconciliation",
        "GaugeReconciliationWorker",
    ),
    # --- Services ---
    "AIGovernanceManager": (
        "oridecon.ai.governance.services.manager",
        "AIGovernanceManager",
    ),
    # --- Protocols ---
    "AIAuditStoreProtocol": (
        "oridecon.ai.governance.protocols",
        "AIAuditStoreProtocol",
    ),
    "AIGovernanceProtocol": (
        "oridecon.ai.governance.protocols",
        "AIGovernanceProtocol",
    ),
    "CostTrackingProtocol": (
        "oridecon.ai.governance.protocols",
        "CostTrackingProtocol",
    ),
    # --- Events ---
    "PolicyEvaluatedEvent": ("oridecon.ai.governance.events", "PolicyEvaluatedEvent"),
}


def __getattr__(name: str) -> Any:
    """Lazy-load symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """Enumerate available attributes for IDE support."""
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = [
    "AIAuditEvent",
    "AIAuditStore",
    "AIAuditStoreProtocol",
    "AIGovernanceManager",
    "AIGovernanceProtocol",
    "AlwaysAllowGate",
    "AuditEventType",
    "AuditQuery",
    "AuditSummary",
    "BudgetExceededError",
    "CompositeGate",
    "ContentPolicyGateProtocol",
    "ContentPolicyService",
    "CostTrackingProtocol",
    "GaugeReconciliationCallback",
    "GaugeReconciliationWorker",
    "GovernanceAuditRecordedHook",
    "GovernanceConfig",
    "GovernanceError",
    "GovernanceModule",
    "GovernancePersistence",
    "GovernancePersistenceWrittenHook",
    "GovernancePolicyEvaluatedHook",
    "GovernanceProvider",
    "InMemoryAuditStore",
    "InMemoryGovernancePersistence",
    "ModelAccessDeniedError",
    "PolicyDecision",
    "PolicyEvaluatedEvent",
    "PolicyObserverProtocol",
    "PolicyOutcome",
    "PolicyRequest",
    "RateLimitExceededError",
    "RedisGovernancePersistence",
    "ResourceExhaustedError",
    "ResourceUnitRegistry",
    "ResourceUnitTracker",
]
