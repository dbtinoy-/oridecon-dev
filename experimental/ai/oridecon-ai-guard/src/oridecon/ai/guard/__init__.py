"""oridecon-ai-safety — Content safety and guardrails for Oridecon Framework.

Canonical import paths
-----------------------
GuardPipeline:           from oridecon.ai.guard import GuardPipeline
GuardConfig:             from oridecon.ai.guard import GuardConfig
GuardModule:             from oridecon.ai.guard import GuardModule
GuardProvider:           from oridecon.ai.guard import GuardProvider
GuardCheckResult:        from oridecon.ai.guard import GuardCheckResult
AggregateGuardResult:    from oridecon.ai.guard import AggregateGuardResult
GuardAction:             from oridecon.ai.guard import GuardAction
PromptInjectionDetector: from oridecon.ai.guard import PromptInjectionDetector
PIIDetector:             from oridecon.ai.guard import PIIDetector
InputLengthGuard:        from oridecon.ai.guard import InputLengthGuard
TopicRestrictor:         from oridecon.ai.guard import TopicRestrictor
PIIRedactor:             from oridecon.ai.guard import PIIRedactor
OutputLengthGuard:       from oridecon.ai.guard import OutputLengthGuard

Quick Start
-----------

    from oridecon.ai.guard import GuardModule, GuardConfig
    from oridecon import OrideconApplication

    app = OrideconApplication(
        modules=[
            ...,
            GuardModule(
                config=GuardConfig(
                    injection_detection=True,
                    pii_action="redact",
                    max_input_chars=8000,
                )
            ),
        ],
    )

    # In a service, inject the pipeline and use it:
    from oridecon.ai.guard import GuardPipeline
    from oridecon.result import err
    from oridecon.di import inject

    class MyLLMService:
        def __init__(self, guard: GuardPipeline) -> None:
            self._guard = guard

        async def chat(self, user_message: str) -> str:
            result = await self._guard.check_input(user_message)
            if result.blocked:
                raise ValueError(f"Input blocked: {result.blocking_result}")
            safe_input = result.final_content or user_message
            llm_response = await self._llm.complete(safe_input)
            output = await self._guard.check_output(llm_response)
            return output.final_content or llm_response
"""

from __future__ import annotations

import importlib.metadata
import pkgutil
from typing import TYPE_CHECKING

__path__ = pkgutil.extend_path(__path__, __name__)

from oridecon.ai.guard.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.ai.guard.config import GuardConfig
    from oridecon.ai.guard.decorators import guarded
    from oridecon.ai.guard.di.provider import GuardProvider
    from oridecon.ai.guard.exceptions import (
        GuardConfigurationError,
        GuardError,
        GuardPipelineError,
    )
    from oridecon.ai.guard.hooks import (
        GuardInputCheckedHook,
        GuardOutputCheckedHook,
        GuardPipelineCompletedHook,
    )
    from oridecon.ai.guard.input.base import AbstractInputGuard
    from oridecon.ai.guard.input.injection import PromptInjectionDetector
    from oridecon.ai.guard.input.length import InputLengthGuard
    from oridecon.ai.guard.input.pii import PIIDetector
    from oridecon.ai.guard.input.topic import TopicRestrictor
    from oridecon.ai.guard.module import GuardModule
    from oridecon.ai.guard.output.base import AbstractOutputGuard
    from oridecon.ai.guard.output.length import OutputLengthGuard
    from oridecon.ai.guard.output.pii_redactor import PIIRedactor
    from oridecon.ai.guard.pipeline.guard_pipeline import GuardPipeline
    from oridecon.ai.guard.pipeline.result import (
        AggregateGuardResult,
        GuardAction,
        GuardCheckResult,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "GuardInputCheckedHook": ("oridecon.ai.guard.hooks", "GuardInputCheckedHook"),
    "GuardOutputCheckedHook": ("oridecon.ai.guard.hooks", "GuardOutputCheckedHook"),
    "GuardPipelineCompletedHook": (
        "oridecon.ai.guard.hooks",
        "GuardPipelineCompletedHook",
    ),
    "GuardConfig": ("oridecon.ai.guard.config", "GuardConfig"),
    "guarded": ("oridecon.ai.guard.decorators", "guarded"),
    "GuardProvider": ("oridecon.ai.guard.di.provider", "GuardProvider"),
    "GuardError": ("oridecon.ai.guard.exceptions", "GuardError"),
    "GuardConfigurationError": (
        "oridecon.ai.guard.exceptions",
        "GuardConfigurationError",
    ),
    "GuardPipelineError": ("oridecon.ai.guard.exceptions", "GuardPipelineError"),
    "AbstractInputGuard": ("oridecon.ai.guard.input.base", "AbstractInputGuard"),
    "PromptInjectionDetector": (
        "oridecon.ai.guard.input.injection",
        "PromptInjectionDetector",
    ),
    "InputLengthGuard": ("oridecon.ai.guard.input.length", "InputLengthGuard"),
    "PIIDetector": ("oridecon.ai.guard.input.pii", "PIIDetector"),
    "TopicRestrictor": ("oridecon.ai.guard.input.topic", "TopicRestrictor"),
    "GuardModule": ("oridecon.ai.guard.module", "GuardModule"),
    "AbstractOutputGuard": ("oridecon.ai.guard.output.base", "AbstractOutputGuard"),
    "OutputLengthGuard": ("oridecon.ai.guard.output.length", "OutputLengthGuard"),
    "PIIRedactor": ("oridecon.ai.guard.output.pii_redactor", "PIIRedactor"),
    "GuardPipeline": ("oridecon.ai.guard.pipeline.guard_pipeline", "GuardPipeline"),
    "AggregateGuardResult": (
        "oridecon.ai.guard.pipeline.result",
        "AggregateGuardResult",
    ),
    "GuardAction": ("oridecon.ai.guard.pipeline.result", "GuardAction"),
    "GuardCheckResult": ("oridecon.ai.guard.pipeline.result", "GuardCheckResult"),
    # --- Protocols ---
    "GuardPipelineProtocol": ("oridecon.ai.guard.protocols", "GuardPipelineProtocol"),
    "GuardResultProtocol": ("oridecon.ai.guard.protocols", "GuardResultProtocol"),
    "InputGuardProtocol": ("oridecon.ai.guard.protocols", "InputGuardProtocol"),
    "OutputGuardProtocol": ("oridecon.ai.guard.protocols", "OutputGuardProtocol"),
    # --- Events ---
    "InputGuardTriggeredEvent": (
        "oridecon.ai.guard.events",
        "InputGuardTriggeredEvent",
    ),
    "OutputGuardTriggeredEvent": (
        "oridecon.ai.guard.events",
        "OutputGuardTriggeredEvent",
    ),
}


def __getattr__(name: str) -> object:
    """Lazily import public symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        mod_path, attr = _LAZY_IMPORTS[name]
        module = importlib.import_module(mod_path)
        value = getattr(module, attr)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = list(_LAZY_IMPORTS.keys())
