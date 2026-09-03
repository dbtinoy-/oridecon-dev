"""Evaluation module for dependency injection."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.contracts.ai.evaluation import (
    EvaluationHarnessProtocol,
    EvaluatorProtocol,
)
from oridecon.contracts.ai.experiment import (
    CheckpointStoreProtocol,
    ExperimentTrackerProtocol,
)
from oridecon.di.module import DynamicModule, Module, module

if TYPE_CHECKING:
    from oridecon.ai.evaluation.config import EvaluationConfig


@module
class EvaluationModule(Module):
    """Evaluation module for Oridecon applications.

    Provides evaluator and harness support for AI model evaluation.

    Usage::

        from oridecon.ai.evaluation import EvaluationModule
        from oridecon.ai.evaluation.config import EvaluationConfig

        @module(
            imports=[EvaluationModule.configure(EvaluationConfig(...))]
        )
        class AppModule(Module):
            pass
    """

    @classmethod
    def configure(cls, config: EvaluationConfig | None = None) -> DynamicModule:
        """Create an EvaluationModule with explicit configuration.

        Args:
            config: :class:`~oridecon.ai.evaluation.config.EvaluationConfig` or
                ``None`` for defaults.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.ai.evaluation.di.provider import EvaluationProvider

        return DynamicModule(
            module=cls,
            providers=[EvaluationProvider(config=config)],
            exports=[
                EvaluatorProtocol,
                EvaluationHarnessProtocol,
                ExperimentTrackerProtocol,
                CheckpointStoreProtocol,
            ],
        )

    @classmethod
    def stub(cls, config: EvaluationConfig | None = None) -> DynamicModule:
        """Create an EvaluationModule suitable for unit and integration testing.

        Uses in-memory or no-op evaluator implementations with minimal side
        effects.

        Args:
            config: Optional :class:`~oridecon.ai.evaluation.config.EvaluationConfig`
                override. Uses safe test defaults when ``None``.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.ai.evaluation.di.provider import EvaluationProvider

        return DynamicModule(
            module=cls,
            providers=[EvaluationProvider(config=config)],
            exports=[
                EvaluatorProtocol,
                EvaluationHarnessProtocol,
                ExperimentTrackerProtocol,
                CheckpointStoreProtocol,
            ],
        )


__all__ = ["EvaluationModule"]
