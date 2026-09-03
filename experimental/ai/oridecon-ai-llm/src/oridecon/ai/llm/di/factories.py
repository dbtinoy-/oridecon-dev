"""Factory functions for creating LLM service instances from configuration.

These factories are used by LLMProvider to construct concrete client
implementations from typed config objects without hardcoding dependencies.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.contracts.ai import LLMClientProtocol
from oridecon.contracts.ai.providers import ProviderRegistryProtocol
from oridecon.logging import (
    get_logger,
)

if TYPE_CHECKING:
    from oridecon.ai.llm.config import ClientConfig
    from oridecon.ai.llm.protocols import LLMCacheProtocol
    from oridecon.contracts.infra.cache import CacheBackendProtocol

logger = get_logger(__name__)


async def create_llm_client(
    config: ClientConfig,
    registry: ProviderRegistryProtocol,
) -> LLMClientProtocol:
    """Instantiate an LLM client from provider configuration via the registry.

    Delegates to :class:`~oridecon.ai.llm.registry.ProviderRegistry` so that
    all built-in **and** custom providers registered at runtime are supported
    without requiring changes to this factory.

    Args:
        config: LLM-specific configuration block.

    Returns:
        A concrete LLMClientProtocol for the configured provider.

    Raises:
        ValueError: When ``config.provider`` is not registered.
    """
    try:
        provider_info = registry.get_provider(config.provider)  # type: ignore[attr-defined]
    except KeyError as exc:
        msg = f"Unsupported LLM provider: {config.provider!r}"
        raise ValueError(msg) from exc

    client = provider_info.client_class(config)
    if not isinstance(client, LLMClientProtocol):
        msg = (
            f"LLM client for provider {config.provider!r} does not satisfy "
            "the LLMClientProtocol protocol. Ensure the client implements complete(), "
            "stream_chat(), health_check(), and close()."
        )
        raise TypeError(msg)
    return client


async def create_llm_cache(
    config: ClientConfig,
    cache: CacheBackendProtocol | None,
) -> LLMCacheProtocol:
    """Create an LLM response cache instance from configuration.

    Args:
        config: LLM configuration carrying cache settings.
        cache: Platform cache backend (required when enable_cache=True).

    Returns:
        A configured LLMCacheProtocol instance.

    Raises:
        ValueError: When enable_cache is True but no CacheBackendProtocol is provided.
    """
    from oridecon.ai.llm.caching.core import LLMCache, RedisLLMCache

    if cache is not None:
        return RedisLLMCache(cache_backend=cache, ttl=config.cache_ttl)  # type: ignore[return-value]

    if config.enable_cache and cache is None:
        msg = "CacheBackendProtocol required for LLM caching but not found in container"
        raise ValueError(msg)

    return LLMCache(ttl=config.cache_ttl)  # type: ignore[return-value]
