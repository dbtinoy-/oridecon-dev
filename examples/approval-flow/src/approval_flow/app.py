"""Composition root for the single-niche Approval Flow demo."""

from __future__ import annotations

from approval_flow.controllers.api import ApprovalFlowApiController
from approval_flow.di.provider import ApprovalFlowProvider
from approval_flow.services.flow import build_approval_state_machine
from approval_flow.ui.pages import ApprovalFlowPageController
from oridecon.app.base import Application
from oridecon.config.main import OrideconConfig
from oridecon.di.provider import Provider
from oridecon.web.module import WebModule
from oridecon.workflow.module import WorkflowModule


def build_modules() -> list[object]:
    """Build the Oridecon modules required by the approval flow demo."""
    return [
        WorkflowModule.configure(state_machine=build_approval_state_machine()),
        WebModule.configure(
            controllers=[ApprovalFlowApiController, ApprovalFlowPageController],
        ),
    ]


def build_providers() -> list[Provider]:
    """Build the DI providers for the approval flow demo."""
    return [ApprovalFlowProvider()]


def create_app(config: OrideconConfig | None = None) -> Application:
    """Create and configure the approval flow application."""
    app = Application(name="approval-flow", config=config)
    app.add_modules(build_modules())
    app.add_providers(build_providers())
    return app


__all__ = ["build_modules", "build_providers", "create_app"]
