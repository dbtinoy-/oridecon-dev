"""Interpolation module for dependency injection."""

from __future__ import annotations

from oridecon.contracts.multimedia.protocols import InterpolationProvider
from oridecon.di.module import DynamicModule, Module, module
from oridecon.multimedia.interpolate.config import InterpolationConfig
from oridecon.multimedia.interpolate.tasks import InterpolationTask


@module()
class InterpolationModule(Module):
    """RIFE frame-interpolation integration."""

    @classmethod
    def configure(cls, config: InterpolationConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.interpolate.di.provider import (
            InterpolationGenerationProvider,
        )

        return DynamicModule(
            module=cls,
            providers=[InterpolationGenerationProvider(config=config)],
            exports=[InterpolationProvider, InterpolationTask],
        )

    @classmethod
    def stub(cls, config: InterpolationConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.interpolate.di.provider import (
            InterpolationGenerationProvider,
        )

        return DynamicModule(
            module=cls,
            providers=[
                InterpolationGenerationProvider(
                    config=config or InterpolationConfig(backend="rife")
                )
            ],
            exports=[InterpolationProvider, InterpolationTask],
        )


__all__ = ["InterpolationModule"]
