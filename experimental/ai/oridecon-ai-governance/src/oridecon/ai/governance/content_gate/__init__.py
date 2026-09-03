"""Content policy gate sub-package.

Provides the seam for "should this request reach the LLM?" decisions:
abuse detection, quota enforcement, content policy, age-gating, and
jurisdictional restrictions.

Public API
----------
.. code-block:: python

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
"""

from __future__ import annotations

from oridecon.ai.governance.content_gate.gates import AlwaysAllowGate, CompositeGate
from oridecon.ai.governance.content_gate.models import (
    PolicyDecision,
    PolicyOutcome,
    PolicyRequest,
)
from oridecon.ai.governance.content_gate.protocol import (
    ContentPolicyGateProtocol,
    PolicyObserverProtocol,
)
from oridecon.ai.governance.content_gate.service import ContentPolicyService

__all__ = [
    "AlwaysAllowGate",
    "CompositeGate",
    "ContentPolicyGateProtocol",
    "ContentPolicyService",
    "PolicyDecision",
    "PolicyObserverProtocol",
    "PolicyOutcome",
    "PolicyRequest",
]
