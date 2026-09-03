"""Prompt module for Oridecon."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from oridecon.contracts.ai.llm import PromptTemplateProtocol
from oridecon.di.module import DynamicModule, Module, module

if TYPE_CHECKING:
    from oridecon.ai.prompt.config import PromptConfig


@module()
class PromptModule(Module):
    """Prompt template management and rendering integration.

    Registers the :class:`~oridecon.ai.prompt.di.provider.PromptProvider`
    which wires a :class:`~oridecon.ai.prompt.registry.registry.PromptRegistry`
    into the container and exposes it as
    :class:`~oridecon.contracts.ai.llm.PromptTemplateProtocol`.

    Usage::

        from oridecon.ai.prompt import PromptModule
        from oridecon.ai.prompt.config import PromptConfig

        @module(
            imports=[
                PromptModule.configure(
                    PromptConfig(default_format="jinja2")
                )
            ]
        )
        class AppModule(Module):
            pass

    Error Handling::

        Prompt rendering and registry lookups surface typed exceptions that
        can be caught directly or handled via the Result pattern::

            from oridecon.ai.prompt.exceptions import (
                PromptError,          # base — catch-all
                PromptRenderError,    # template rendering failure
                PromptValidationError,# variable type / value validation
                PromptNotFoundError,  # named template not in registry
                PromptVersionError,   # version conflict or invalid rollback
            )

    Exports:
        :class:`~oridecon.contracts.ai.llm.PromptTemplateProtocol`,
        :class:`~oridecon.ai.prompt.exceptions.PromptError`,
        :class:`~oridecon.ai.prompt.exceptions.PromptRenderError`,
        :class:`~oridecon.ai.prompt.exceptions.PromptValidationError`,
        :class:`~oridecon.ai.prompt.exceptions.PromptNotFoundError`,
        :class:`~oridecon.ai.prompt.exceptions.PromptVersionError`
    """

    @classmethod
    def configure(
        cls, config: PromptConfig | None = None, **kwargs: Any
    ) -> DynamicModule:
        """Create a PromptModule with explicit configuration.

        Args:
            config: :class:`~oridecon.ai.prompt.config.PromptConfig` or ``None``
                to use defaults.
            **kwargs: Additional keyword arguments forwarded to
                :class:`~oridecon.ai.prompt.di.provider.PromptProvider`.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.ai.prompt.di.provider import PromptProvider

        return DynamicModule(
            module=cls,
            providers=[PromptProvider(config=config, **kwargs)],
            exports=[
                PromptTemplateProtocol,
            ],
        )

    @classmethod
    def stub(cls, config: PromptConfig | None = None) -> DynamicModule:
        """Create a PromptModule suitable for unit and integration testing.

        Uses in-memory or no-op implementations with minimal side effects.

        Args:
            config: Optional config override. Uses safe test defaults when None.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.ai.prompt.di.provider import PromptProvider

        return DynamicModule(
            module=cls,
            providers=[PromptProvider(config=config)],
            exports=[
                PromptTemplateProtocol,
            ],
        )


__all__ = ["PromptModule"]
