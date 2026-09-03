"""Vector store module for dependency injection."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from oridecon.contracts.data.vector.protocols import (
    VectorCollectionProtocol,
    VectorStoreProtocol,
)
from oridecon.di.module import DynamicModule, Module, module

if TYPE_CHECKING:
    from oridecon.vector.config import VectorConfig


@module()
class VectorModule(Module):
    """Vector storage module — registers VectorStoreProtocol and VectorCollectionProtocol.

    Registers :class:`~oridecon.contracts.data.vector.protocols.VectorStoreProtocol`
    and :class:`~oridecon.contracts.data.vector.protocols.VectorCollectionProtocol`
    for constructor injection.

    Call :meth:`configure` to configure the vector backend (Qdrant, ChromaDB,
    PGVector, or in-memory), or :meth:`stub` for an isolated setup with
    no external service dependencies.

    Usage::

        from oridecon.vector.config import VectorConfig

        @module(
            imports=[VectorModule.configure(VectorConfig(backend="qdrant"))]
        )
        class AppModule(Module):
            pass
    """

    @classmethod
    def configure(
        cls,
        config: VectorConfig | Any | None = None,
        enable_reranking: bool = False,
    ) -> DynamicModule:
        """Create a VectorModule with explicit configuration.

        Args:
            config: :class:`~oridecon.vector.config.VectorConfig`, a plain
                ``dict`` of config values, or ``None`` to use environment
                variable defaults.
            enable_reranking: Enable cross-encoder reranking of retrieval
                results to improve relevance scoring.  Defaults to ``False``.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.

        Raises:
            TypeError: If *config* is not a ``VectorConfig``, ``dict``, or
                ``None``.
        """
        from oridecon.vector.config import VectorConfig
        from oridecon.vector.di.provider import VectorProvider

        if config is not None:
            if isinstance(config, dict):
                provider = VectorProvider(config=VectorConfig(**config))
            elif isinstance(config, VectorConfig):
                provider = VectorProvider(config=config)
            else:
                raise TypeError(
                    f"config must be VectorConfig or dict, got {type(config).__name__}"
                )
        else:
            provider = VectorProvider()

        return DynamicModule(
            module=cls,
            providers=[provider],
            exports=[VectorStoreProtocol, VectorCollectionProtocol],
        )

    @classmethod
    def stub(cls, config: VectorConfig | None = None) -> DynamicModule:
        """Create a VectorModule suitable for unit and integration testing.

        Uses an in-memory backend with no external service dependencies.

        Args:
            config: Optional :class:`~oridecon.vector.config.VectorConfig`
                override.  Uses safe in-memory defaults when ``None``.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.vector.di.provider import VectorProvider

        return DynamicModule(
            module=cls,
            providers=[VectorProvider(config=config)],
            exports=[VectorStoreProtocol, VectorCollectionProtocol],
        )


__all__ = ["VectorModule"]
