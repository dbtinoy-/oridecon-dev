"""Relay gateway module for dependency injection."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.contracts.ai.relay import RelayGatewayProtocol
from oridecon.di.module import DynamicModule, Module, module

if TYPE_CHECKING:
    from oridecon.ai.relay.gateway.config import RelayGatewayConfig

__all__ = ["RelayGatewayModule"]


@module
class RelayGatewayModule(Module):
    """Protocol-facing relay gateway module for Oridecon applications.

    Provides the relay gateway behind the :class:`RelayGatewayProtocol`
    contract: channel selection, orchestration, upstream I/O, and SSE
    handling.  The :class:`RelayGatewayProvider` composes the gateway
    from caller-owned config, conversion engine, and HTTP client.

    Usage::

        from oridecon.ai.relay.gateway import RelayGatewayModule

        @module(
            imports=[RelayGatewayModule.configure()]
        )
        class AppModule(Module):
            pass
    """

    @classmethod
    def configure(cls, config: RelayGatewayConfig | None = None) -> DynamicModule:
        """Create a RelayGatewayModule with the built-in gateway routes.

        Args:
            config: Static gateway configuration (channel table, model
                suffixes, auto-test flags, job TTL). Defaults to an empty
                configuration when omitted.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.ai.relay.gateway.di.provider import RelayGatewayProvider
        from oridecon.ai.relay.gateway.operations.controls import RelayControlsService
        from oridecon.ai.relay.gateway.operations.health import RelayHealthService
        from oridecon.ai.relay.gateway.operations.metrics import RelayMetricsService

        return DynamicModule(
            module=cls,
            providers=[RelayGatewayProvider(config=config)],
            exports=[
                RelayGatewayProtocol,
                RelayHealthService,
                RelayMetricsService,
                RelayControlsService,
            ],
        )
