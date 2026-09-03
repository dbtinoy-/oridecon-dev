"""Beat-analysis module for dependency injection."""

from __future__ import annotations

from oridecon.contracts.multimedia.protocols import BeatAnalysisProvider
from oridecon.di.module import DynamicModule, Module, module
from oridecon.multimedia.beat.config import BeatAnalysisConfig


@module()
class BeatAnalysisModule(Module):
    """Librosa/madmom tempo-and-beat-detection integration."""

    @classmethod
    def configure(cls, config: BeatAnalysisConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.beat.di.provider import BeatAnalysisGenerationProvider

        return DynamicModule(
            module=cls,
            providers=[BeatAnalysisGenerationProvider(config=config)],
            exports=[BeatAnalysisProvider],
        )

    @classmethod
    def stub(cls, config: BeatAnalysisConfig | None = None) -> DynamicModule:
        from oridecon.multimedia.beat.di.provider import BeatAnalysisGenerationProvider

        return DynamicModule(
            module=cls,
            providers=[
                BeatAnalysisGenerationProvider(
                    config=config or BeatAnalysisConfig(backend="librosa")
                )
            ],
            exports=[BeatAnalysisProvider],
        )


__all__ = ["BeatAnalysisModule"]
