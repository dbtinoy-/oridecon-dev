"""Search engine module for dependency injection."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from oridecon.contracts.search import SearchEngineProtocol
from oridecon.di.module import DynamicModule, Module, module

if TYPE_CHECKING:
    from oridecon.search.config import SearchConfig


@module()
class SearchModule(Module):
    """Full-text and semantic search engine integration (Meilisearch, SQLite, Postgres).

    Registers :class:`~oridecon.contracts.search.SearchEngineProtocol` for
    constructor injection.

    Call :meth:`configure` to configure the search backend, or :meth:`stub`
    for an isolated in-memory setup with no external service dependencies.

    Usage::

        from oridecon.search.config import SearchConfig

        @module(
            imports=[SearchModule.configure(SearchConfig(backend="meilisearch"))]
        )
        class AppModule(Module):
            pass
    """

    @classmethod
    def configure(
        cls,
        config: SearchConfig | Any | None = None,
        enable_facets: bool = True,
    ) -> DynamicModule:
        """Create a SearchModule with explicit configuration.

        Args:
            config: :class:`~oridecon.search.config.SearchConfig`, a
                pre-built :class:`~oridecon.search.engine.SearchEngine`
                instance, or ``None`` to defer configuration to the yaml
                ``search`` section injected by the orchestrator before
                ``register()`` (framework defaults apply when no section
                exists).
            enable_facets: Enable faceted search / filterable attributes on
                the backing index.  Defaults to ``True``.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.search.di.provider import SearchProvider
        from oridecon.search.engine import SearchEngine

        if isinstance(config, SearchEngine):
            provider = SearchProvider(backend=config)
        elif config is not None:
            provider = SearchProvider.configure(config)
        else:
            # Zero-config construction: the provider composes its backend in
            # register() from the yaml-injected ``search`` section.
            provider = SearchProvider()

        return DynamicModule(
            module=cls,
            providers=[provider],
            exports=[SearchEngineProtocol],
        )

    @classmethod
    def stub(cls, config: SearchConfig | None = None) -> DynamicModule:
        """Create a SearchModule suitable for unit and integration testing.

        Uses an in-memory (null) backend with no external service dependencies.

        Args:
            config: Optional :class:`~oridecon.search.config.SearchConfig`
                override.  Uses an in-memory backend when ``None``.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.search.di.provider import SearchProvider

        if config is not None:
            provider = SearchProvider.configure(config)
        else:
            provider = SearchProvider.with_memory()

        return DynamicModule(
            module=cls,
            providers=[provider],
            exports=[SearchEngineProtocol],
        )


__all__ = ["SearchModule"]
