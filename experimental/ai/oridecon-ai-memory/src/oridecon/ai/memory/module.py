"""MemoryModule — DI module for oridecon-ai-memory."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.contracts.ai.memory import (
    EpisodicMemoryProtocol,
    MemoryConsolidatorProtocol,
    MemoryStoreProtocol,
    SemanticMemoryProtocol,
    WorkingMemoryProtocol,
)
from oridecon.di.module import DynamicModule, Module, module

if TYPE_CHECKING:
    from oridecon.ai.memory.config import MemoryConfig


@module
class MemoryModule(Module):
    """Three-tier AI memory: working, episodic, and semantic.

    Call :meth:`configure` to register :class:`~oridecon.ai.memory.di.provider.MemoryProvider`
    and expose all memory protocol contracts for injection.

    Usage::

        from oridecon.ai.memory.config import MemoryConfig
        from oridecon.ai.memory import MemoryModule

        @module(
            imports=[MemoryModule.configure(MemoryConfig(...))]
        )
        class AppModule(Module):
            pass
    """

    @classmethod
    def configure(
        cls,
        config: MemoryConfig | None = None,
        enable_consolidation: bool = True,
    ) -> DynamicModule:
        """Create a MemoryModule with explicit configuration.

        Args:
            config: :class:`~oridecon.ai.memory.config.MemoryConfig` or ``None``
                for defaults (in-memory backend, standard budget fractions).
            enable_consolidation: Register the
                :class:`~oridecon.ai.memory.consolidation.ConsolidationScheduler`
                which periodically promotes episodic memories into semantic
                storage. Defaults to ``True``.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.ai.memory.di.provider import MemoryProvider

        return DynamicModule(
            module=cls,
            providers=[
                MemoryProvider(config=config, enable_consolidation=enable_consolidation)
            ],
            exports=[
                MemoryStoreProtocol,
                EpisodicMemoryProtocol,
                SemanticMemoryProtocol,
                WorkingMemoryProtocol,
                MemoryConsolidatorProtocol,
            ],
        )

    @classmethod
    def stub(cls, config: MemoryConfig | None = None) -> DynamicModule:
        """Create a MemoryModule suitable for unit and integration testing.

        Uses in-memory backends with minimal side effects. Consolidation
        scheduling is disabled by default to avoid background timer tasks
        during tests.

        Args:
            config: Optional :class:`~oridecon.ai.memory.config.MemoryConfig`
                override. Uses safe test defaults when ``None``.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.ai.memory.di.provider import MemoryProvider

        return DynamicModule(
            module=cls,
            providers=[MemoryProvider(config=config, enable_consolidation=False)],
            exports=[
                MemoryStoreProtocol,
                EpisodicMemoryProtocol,
                SemanticMemoryProtocol,
                WorkingMemoryProtocol,
                MemoryConsolidatorProtocol,
            ],
        )


__all__ = ["MemoryModule"]
