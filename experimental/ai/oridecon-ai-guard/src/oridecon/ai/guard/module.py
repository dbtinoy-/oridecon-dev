"""GuardProtocol module for Oridecon."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from oridecon.contracts.ai.guards import (
    GuardPipelineProtocol,
    InputGuardProtocol,
    OutputGuardProtocol,
)
from oridecon.di.module import DynamicModule, Module, module

if TYPE_CHECKING:
    from oridecon.ai.guard.config import GuardConfig


@module()
class GuardModule(Module):
    """Module for content safety guard pipeline.

    Registers the :class:`~oridecon.ai.guard.di.provider.GuardProvider`
    which builds and wires the configured guard pipeline into the container.

    Usage::

        app = OrideconApplication(
            modules=[..., GuardModule()],
        )

    Or with custom config::

        app = OrideconApplication(
            modules=[
                ...,
                GuardModule(
                    config=GuardConfig(
                        injection_detection=True,
                        pii_action="redact",
                        max_input_chars=8000,
                    )
                )
            ]
        )
    """

    @classmethod
    def configure(
        cls,
        config: GuardConfig | None = None,
        enable_audit_logging: bool = True,
        **kwargs: Any,
    ) -> DynamicModule:
        """Create a GuardModule with explicit configuration.

        Args:
            config: :class:`~oridecon.ai.guard.config.GuardConfig` or ``None``
                for defaults.
            enable_audit_logging: Emit structured audit log entries for every
                guard decision (allow, block, redact). Defaults to ``True``;
                set to ``False`` to reduce log volume in high-throughput
                environments.
            **kwargs: Additional keyword arguments forwarded to
                :class:`~oridecon.ai.guard.di.provider.GuardProvider`.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.ai.guard.di.provider import GuardProvider

        return DynamicModule(
            module=cls,
            providers=[
                GuardProvider(
                    config=config,
                    enable_audit_logging=enable_audit_logging,
                    **kwargs,
                )
            ],
            exports=[
                GuardPipelineProtocol,
                InputGuardProtocol,
                OutputGuardProtocol,
            ],
        )

    @classmethod
    def stub(cls, config: GuardConfig | None = None) -> DynamicModule:
        """Create a GuardModule suitable for unit and integration testing.

        Uses a pass-through (allow-all) guard pipeline with no external API
        calls. Audit logging is disabled by default to keep test output clean.

        Args:
            config: Optional :class:`~oridecon.ai.guard.config.GuardConfig`
                override. Uses safe test defaults when ``None``.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.ai.guard.di.provider import GuardProvider

        return DynamicModule(
            module=cls,
            providers=[GuardProvider(config=config, enable_audit_logging=False)],
            exports=[
                GuardPipelineProtocol,
                InputGuardProtocol,
                OutputGuardProtocol,
            ],
        )


__all__ = ["GuardModule"]
