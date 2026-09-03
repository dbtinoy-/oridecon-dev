"""Image generation module for dependency injection."""

from __future__ import annotations

from oridecon.contracts.multimedia.protocols import ImageProvider
from oridecon.di.module import DynamicModule, Module, module
from oridecon.multimedia.image.config import ImageConfig
from oridecon.multimedia.image.tasks import ImageGenerationTask


@module()
class ImageModule(Module):
    """Image generation integration."""

    @classmethod
    def configure(cls, config: ImageConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.image.di.provider import ImageGenerationProvider

        return DynamicModule(
            module=cls,
            providers=[ImageGenerationProvider(config=config)],
            exports=[ImageProvider, ImageGenerationTask],
        )

    @classmethod
    def stub(cls, config: ImageConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.image.di.provider import ImageGenerationProvider

        return DynamicModule(
            module=cls,
            providers=[
                ImageGenerationProvider(
                    config=config or ImageConfig(backend="local-http")
                )
            ],
            exports=[ImageProvider, ImageGenerationTask],
        )


__all__ = ["ImageModule"]
