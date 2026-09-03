"""Feedback module for dependency injection."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.contracts.ai.feedback import FeedbackProtocol
from oridecon.di.module import DynamicModule, Module, module

if TYPE_CHECKING:
    from oridecon.ai.feedback.config import FeedbackConfig


@module()
class FeedbackModule(Module):
    """AI Feedback collection and processing integration.

    Call :meth:`configure` to register a
    :class:`~oridecon.contracts.ai.feedback.FeedbackProtocol` implementation
    along with the processor registry and storage backend for injection.

    Usage::

        from oridecon.ai.feedback.config import FeedbackConfig

        @module(
            imports=[
                FeedbackModule.configure(
                    FeedbackConfig(async_processing=False)
                )
            ]
        )
        class AppModule(Module):
            pass

    Error Handling::

        The feedback services use the Result pattern for expected failures.
        Domain errors are available via the exported exception hierarchy::

            from oridecon.ai.feedback.exceptions import (
                FeedbackError,           # base — catch-all
                FeedbackProcessingError, # processor pipeline failure
                FeedbackValidationError, # schema / data-validation failure
            )

    Exports:
        :class:`~oridecon.contracts.ai.feedback.FeedbackProtocol`,
        :class:`~oridecon.ai.feedback.exceptions.FeedbackError`,
        :class:`~oridecon.ai.feedback.exceptions.FeedbackProcessingError`,
        :class:`~oridecon.ai.feedback.exceptions.FeedbackValidationError`
    """

    @classmethod
    def configure(cls, config: FeedbackConfig | None = None) -> DynamicModule:
        """Create a FeedbackModule with the given configuration.

        Args:
            config: :class:`~oridecon.ai.feedback.config.FeedbackConfig`, a
                plain ``dict`` of the same keys, or ``None`` for framework
                defaults.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.ai.feedback.di.provider import FeedbackProvider

        return DynamicModule(
            module=cls,
            providers=[FeedbackProvider(config=config)],
            exports=[
                FeedbackProtocol,
            ],
        )

    @classmethod
    def stub(cls, config: FeedbackConfig | None = None) -> DynamicModule:
        """Create a FeedbackModule suitable for unit and integration testing.

        Uses in-memory or no-op implementations with minimal side effects.

        Args:
            config: Optional config override. Uses safe test defaults when None.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.ai.feedback.di.provider import FeedbackProvider

        return DynamicModule(
            module=cls,
            providers=[FeedbackProvider(config=config)],
            exports=[
                FeedbackProtocol,
            ],
        )


__all__ = ["FeedbackModule"]
