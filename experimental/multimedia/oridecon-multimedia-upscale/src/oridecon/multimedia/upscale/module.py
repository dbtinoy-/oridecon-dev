"""Upscale generation module for dependency injection."""

from __future__ import annotations

from oridecon.contracts.multimedia.protocols import UpscaleProvider
from oridecon.di.module import DynamicModule, Module, module
from oridecon.multimedia.upscale.config import UpscaleConfig
from oridecon.multimedia.upscale.tasks import UpscaleTask


@module()
class UpscaleModule(Module):
    """Image/video upscale integration."""

    @classmethod
    def configure(cls, config: UpscaleConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.upscale.di.provider import UpscaleGenerationProvider

        return DynamicModule(
            module=cls,
            providers=[UpscaleGenerationProvider(config=config)],
            exports=[UpscaleProvider, UpscaleTask],
        )

    @classmethod
    def stub(cls, config: UpscaleConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.upscale.di.provider import UpscaleGenerationProvider

        return DynamicModule(
            module=cls,
            providers=[
                UpscaleGenerationProvider(
                    config=config or UpscaleConfig(backend="real-esrgan")
                )
            ],
            exports=[UpscaleProvider, UpscaleTask],
        )


__all__ = ["UpscaleModule"]
