"""Verification DI provider: registers HMAC signature verifier."""

from __future__ import annotations

from oridecon.contracts.core.di import (
    BootContainerProtocol,
    ContainerRegistrarProtocol,
)
from oridecon.contracts.core.provider import ProviderPriority
from oridecon.di.provider import Provider

__all__ = ["WebhookVerificationProvider"]


class WebhookVerificationProvider(Provider):
    """Registers HMAC signature verification services."""

    def __init__(self) -> None:
        """Initialize the verification provider."""
        super().__init__(name="webhook_verification", priority=ProviderPriority.COMMS)

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        """Register the HMAC signature verifier.

        Args:
            container: DI container registrar.
        """
        from oridecon.webhook.verification.hmac import HMACSignatureVerifier

        container.singleton(HMACSignatureVerifier, HMACSignatureVerifier)

    async def boot(self, container: BootContainerProtocol) -> None:
        pass
