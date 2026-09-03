"""DI provider for oridecon-auth.

This provider wires the auth subsystem with ClockProtocol, IdGeneratorProtocol,
TracerProtocol, and MetricsCollectorProtocol for testability and hardening.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from oridecon.auth.authn.password_hasher import Argon2idKeyDerivation
from oridecon.auth.config import AuthConfig
from oridecon.contracts.core import HealthCheckResult, HealthStatus, ProviderPriority
from oridecon.contracts.core.health import HealthCheckCategory
from oridecon.contracts.security.protocols import KeyDerivationProtocol
from oridecon.di.provider import Provider
from oridecon.logging import get_logger

if TYPE_CHECKING:
    from oridecon.contracts.core.di import (
        ContainerRegistrarProtocol,
        ContainerResolverProtocol,
    )

logger = get_logger(__name__)

__all__ = ["AuthProvider"]


class AuthProvider(Provider):
    """Authentication provider for Oridecon Framework.

    This provider wires:
    - ClockProtocol for token/session timestamps
    - IdGeneratorProtocol for session/token IDs
    - TracerProtocol for observability
    - MetricsCollectorProtocol for metrics
    - KeyDerivationProtocol (Argon2id) for key derivation
    """

    name = "auth"
    priority = ProviderPriority.SECURITY

    config_key: str | None = "auth"
    config_model: type | None = AuthConfig

    def __init__(self, config: AuthConfig | None = None) -> None:
        super().__init__()
        self._config = config

    @classmethod
    def from_config(cls, config: AuthConfig, **context: Any) -> AuthProvider:
        return cls(config=config)

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        """Register auth services with the DI container."""
        if self._config is None:
            self._config = AuthConfig()
        container.singleton(AuthConfig, instance=self._config)

        container.singleton(
            KeyDerivationProtocol,
            factory=lambda _: Argon2idKeyDerivation(config=self._config.password),
        )

        if self._config.relay_verification:
            from oridecon.auth.authn.apikeys import APIKeyManager
            from oridecon.auth.authn.relay import RelayApiKeyVerifier
            from oridecon.contracts.ai.relay import RelayAuthVerifierProtocol
            from oridecon.contracts.auth import APIKeyRepositoryProtocol

            if not container.has(APIKeyRepositoryProtocol):
                logger.warning(
                    "relay_verifier_skipped",
                    reason="APIKeyRepositoryProtocol not bound",
                )
                return
            container.singleton(
                RelayAuthVerifierProtocol,
                factory=lambda c: RelayApiKeyVerifier(
                    manager=APIKeyManager(repo=c.resolve(APIKeyRepositoryProtocol))
                ),
            )

    async def boot(self, container: ContainerResolverProtocol) -> None:
        """Boot the auth provider."""

    async def shutdown(self) -> None:
        """Shutdown the auth provider."""

    async def health_check(self, timeout: float = 5.0) -> HealthCheckResult:
        """Return health status of the auth provider."""
        return HealthCheckResult(
            component=self.name,
            status=HealthStatus.HEALTHY,
            category=HealthCheckCategory.READINESS,
        )
