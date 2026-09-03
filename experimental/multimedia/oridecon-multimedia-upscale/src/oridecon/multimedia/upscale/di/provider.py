"""DI provider for the upscale generation subsystem."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from oridecon.contracts.core.health import HealthCheckResult, HealthStatus
from oridecon.contracts.multimedia.protocols import UpscaleProvider
from oridecon.di.provider import Provider
from oridecon.di.provider_utils import resolve_optional
from oridecon.logging import get_logger
from oridecon.multimedia.upscale.backends.registry import UpscaleBackendRegistry
from oridecon.multimedia.upscale.config import UpscaleConfig
from oridecon.multimedia.upscale.tasks import UpscaleTask

if TYPE_CHECKING:
    from oridecon.contracts.core.di import (
        ContainerRegistrarProtocol,
        ContainerResolverProtocol,
    )
    from oridecon.contracts.infra.resilience.protocols import (
        CircuitBreakerProtocol,
        RetryPolicyProtocol,
    )
    from oridecon.multimedia.upscale.video_upscale_service import VideoUpscaleService

logger = get_logger(__name__)

__all__ = ["UpscaleGenerationProvider"]


class UpscaleGenerationProvider(Provider):
    """Provider that registers a configured UpscaleProvider backend."""

    name = "upscale"
    config_key: str | None = "multimedia_upscale"
    config_model: type | None = UpscaleConfig

    def __init__(
        self,
        config: UpscaleConfig | None = None,
        *,
        backend_registry: UpscaleBackendRegistry | None = None,
    ) -> None:
        super().__init__(name="upscale")
        self._requested_config = config
        self._config = config
        self._backend_registry = (
            backend_registry or UpscaleBackendRegistry.with_defaults()
        )
        self._backend: UpscaleProvider | None = None
        self._task_handler: UpscaleTask | None = None
        self._retry: RetryPolicyProtocol | None = None
        self._circuit_breaker: CircuitBreakerProtocol | None = None
        self._video_upscale_service: VideoUpscaleService | None = None

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        from oridecon.contracts.infra.resilience.protocols import (
            CircuitBreakerProtocol,
            RetryPolicyProtocol,
        )

        self._config = self._requested_config or self._config or UpscaleConfig()
        container.singleton(UpscaleConfig, self._config)

        self._retry = await resolve_optional(container, RetryPolicyProtocol)
        self._circuit_breaker = await resolve_optional(
            container, CircuitBreakerProtocol
        )

        self._backend = cast(
            "UpscaleProvider",
            await self._backend_registry.create_backend(
                self._config.backend,
                self._config,
                self._retry,
                self._circuit_breaker,
            ),
        )

        assert self._backend is not None  # noqa: S101
        container.singleton(UpscaleProvider, self._backend)

        self._task_handler = UpscaleTask(backend=self._backend)
        container.singleton(UpscaleTask, self._task_handler)

        from oridecon.contracts.multimedia.protocols import VideoProcessor

        video_processor = await resolve_optional(container, VideoProcessor)
        if video_processor is not None:
            from oridecon.multimedia.upscale.video_upscale_service import (
                VideoUpscaleService,
            )

            video_upscale_service = VideoUpscaleService(
                upscale_provider=self._backend, video_processor=video_processor
            )
            self._video_upscale_service = video_upscale_service
            container.singleton(VideoUpscaleService, video_upscale_service)

        logger.info("upscale_registered", backend=self._config.backend)

    async def boot(self, container: ContainerResolverProtocol) -> None:
        """No async I/O needed at boot beyond what register() already did."""

    async def health_check(self, timeout: float = 5.0) -> HealthCheckResult:
        if self._backend is None:
            return HealthCheckResult(component=self.name, status=HealthStatus.UNHEALTHY)

        base_url_map = {
            "real-esrgan": self._config.real_esrgan_base_url,
            "hat": self._config.hat_base_url,
        }
        base_url = base_url_map.get(self._config.backend)
        if base_url is None:
            return HealthCheckResult(component=self.name, status=HealthStatus.HEALTHY)

        import aiohttp

        try:
            async with (
                aiohttp.ClientSession(
                    timeout=aiohttp.ClientTimeout(total=timeout)
                ) as session,
                session.get(f"{base_url}/health") as resp,
            ):
                status = (
                    HealthStatus.HEALTHY
                    if resp.status == 200
                    else HealthStatus.DEGRADED
                )
        except (TimeoutError, OSError, aiohttp.ClientError):
            status = HealthStatus.DEGRADED
        return HealthCheckResult(component=self.name, status=status)
