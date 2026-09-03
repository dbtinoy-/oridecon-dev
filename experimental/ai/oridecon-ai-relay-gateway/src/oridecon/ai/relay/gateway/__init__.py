"""Protocol-facing relay gateway: channel selection, orchestration, upstream I/O, and SSE handling.

The gateway composes the :class:`RelayGatewayService` from a channel
registry, payload codec, upstream HTTP adapter, and the conversion engine,
and exposes it behind :class:`~oridecon.contracts.ai.relay.RelayGatewayProtocol`
through :class:`RelayGatewayModule` / :class:`RelayGatewayProvider`.
"""

from __future__ import annotations

from oridecon.ai.relay.gateway.catalog import ModelCatalogService
from oridecon.ai.relay.gateway.channels import RelayChannelRegistry
from oridecon.ai.relay.gateway.codec import RelayPayloadCodec
from oridecon.ai.relay.gateway.config import RelayGatewayConfig
from oridecon.ai.relay.gateway.credentials import (
    CredentialInjectingHTTPClient,
    NullChannelCredentialProvider,
    RelayChannelCredentialProvider,
)
from oridecon.ai.relay.gateway.di.provider import RelayGatewayProvider
from oridecon.ai.relay.gateway.module import RelayGatewayModule
from oridecon.ai.relay.gateway.operations import (
    InMemoryRelayPolicyStore,
    RelayChannelAutoTester,
    RelayChannelCheckerProtocol,
    RelayChannelProbeResult,
    RelayControlsService,
    RelayFailoverTracker,
    RelayHealthService,
    RelayMetricsService,
    RelayRouteEvent,
    RelayRouteEventSourceProtocol,
    RelayStreamRegistry,
)
from oridecon.ai.relay.gateway.passthrough import PassthroughService
from oridecon.ai.relay.gateway.service import RelayGatewayService
from oridecon.ai.relay.gateway.stream import UpstreamEventParser, relay_stream
from oridecon.ai.relay.gateway.upstream import HTTPUpstreamAdapter

__all__ = [
    "CredentialInjectingHTTPClient",
    "HTTPUpstreamAdapter",
    "InMemoryRelayPolicyStore",
    "ModelCatalogService",
    "NullChannelCredentialProvider",
    "PassthroughService",
    "RelayChannelAutoTester",
    "RelayChannelCheckerProtocol",
    "RelayChannelCredentialProvider",
    "RelayChannelProbeResult",
    "RelayChannelRegistry",
    "RelayControlsService",
    "RelayFailoverTracker",
    "RelayGatewayConfig",
    "RelayGatewayModule",
    "RelayGatewayProvider",
    "RelayGatewayService",
    "RelayHealthService",
    "RelayMetricsService",
    "RelayPayloadCodec",
    "RelayRouteEvent",
    "RelayRouteEventSourceProtocol",
    "RelayStreamRegistry",
    "UpstreamEventParser",
    "relay_stream",
]
