"""P2 hook surface import verification for oridecon-workflow."""

from __future__ import annotations

from dataclasses import FrozenInstanceError, is_dataclass

import pytest


def test_workflow_hooks_root_module_exists() -> None:
    import oridecon.workflow
    from oridecon.workflow.hooks import (
        WorkflowCompletedHook,
        WorkflowStartedHook,
        WorkflowStateTransitionedHook,
    )

    assert WorkflowStartedHook.__name__ == "WorkflowStartedHook"
    assert WorkflowStateTransitionedHook.__name__ == "WorkflowStateTransitionedHook"
    assert WorkflowCompletedHook.__name__ == "WorkflowCompletedHook"
    assert oridecon.workflow.WorkflowStartedHook is WorkflowStartedHook
    assert oridecon.workflow.WorkflowStateTransitionedHook is WorkflowStateTransitionedHook
    assert oridecon.workflow.WorkflowCompletedHook is WorkflowCompletedHook
    assert "WorkflowCompletedHook" in oridecon.workflow.__all__
    assert "WorkflowStartedHook" in oridecon.workflow.__all__
    assert "WorkflowStateTransitionedHook" in oridecon.workflow.__all__


def test_workflow_hook_payloads_are_frozen_and_keyword_only() -> None:
    from oridecon.workflow.hooks import WorkflowCompletedHook, WorkflowStartedHook

    started = WorkflowStartedHook(workflow_id="wf-1", workflow_type="OrderFulfillment")
    completed = WorkflowCompletedHook(
        workflow_id="wf-1", workflow_type="OrderFulfillment", succeeded=True
    )

    assert is_dataclass(started)
    assert is_dataclass(completed)

    with pytest.raises(TypeError):
        WorkflowStartedHook("wf-1", "OrderFulfillment")  # type: ignore[misc]

    with pytest.raises(FrozenInstanceError):
        started.workflow_id = "other"  # type: ignore[misc]


def test_workflow_state_transitioned_hook_fields() -> None:
    from oridecon.workflow.hooks import WorkflowStateTransitionedHook

    hook = WorkflowStateTransitionedHook(
        workflow_id="wf-1", from_state="pending", to_state="processing"
    )
    assert hook.from_state == "pending"
    assert hook.to_state == "processing"
