"""DI Provider for the AI Evaluation subsystem."""

from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.ai.evaluation.config import EvaluationConfig
from oridecon.contracts.ai.evaluation import EvaluatorProtocol
from oridecon.contracts.ai.experiment import (
    CheckpointStoreProtocol,
    ExperimentTrackerProtocol,
)
from oridecon.contracts.core.health import HealthCheckResult, HealthStatus
from oridecon.di.provider import Provider, ProviderPriority
from oridecon.logging import get_logger

if TYPE_CHECKING:
    from oridecon.contracts.core.di import (
        BootContainerProtocol,
        ContainerRegistrarProtocol,
    )

logger = get_logger(__name__)


class EvaluationProvider(Provider):
    """Registers evaluation services with the DI container."""

    name = "evaluation"
    priority = ProviderPriority.DOMAIN
    config_key: str | None = "ai_evaluation"
    config_model: type | None = EvaluationConfig

    def __init__(self, config: EvaluationConfig | None = None) -> None:
        super().__init__()
        self._requested_config = config
        self._config = config or EvaluationConfig()

    async def register(self, container: ContainerRegistrarProtocol) -> None:
        self._config = self._requested_config or self._config or EvaluationConfig()
        container.singleton(EvaluationConfig, instance=self._config)

        from oridecon.ai.evaluation.evaluators.criteria import CriteriaEvaluator
        from oridecon.ai.evaluation.evaluators.embedding_distance import (
            EmbeddingDistanceEvaluator,
        )
        from oridecon.ai.evaluation.evaluators.qa import QAEvaluator
        from oridecon.ai.evaluation.evaluators.string_distance import (
            StringDistanceEvaluator,
        )
        from oridecon.ai.evaluation.harness.runner import EvaluationHarness

        container.singleton(
            EvaluatorProtocol,
            CriteriaEvaluator(),
            name="criteria",
        )
        container.singleton(
            EvaluatorProtocol,
            QAEvaluator(),
            name="qa",
        )
        container.singleton(
            EvaluatorProtocol,
            StringDistanceEvaluator(),
            name="string_distance",
        )
        container.singleton(
            EvaluatorProtocol,
            EmbeddingDistanceEvaluator(),
            name="embedding_distance",
        )
        container.singleton(EvaluationHarness, EvaluationHarness())

        from oridecon.ai.evaluation.checkpoints import FileCheckpointStore
        from oridecon.ai.evaluation.tracking import LocalTracker

        experiment_root = self._config.experiment_dir or "runs"
        container.singleton(
            ExperimentTrackerProtocol,
            LocalTracker(root=experiment_root),
        )
        container.singleton(
            CheckpointStoreProtocol,
            FileCheckpointStore(root=experiment_root),
        )

        logger.info("evaluation_provider_registered")

    async def boot(self, container: BootContainerProtocol) -> None:
        logger.info("evaluation_provider_booted")

    async def shutdown(self) -> None:
        pass

    async def health_check(self, timeout: float = 5.0) -> HealthCheckResult:
        return HealthCheckResult(
            component="evaluation",
            status=HealthStatus.HEALTHY,
            details={"status": "ok"},
        )


__all__ = ["EvaluationProvider"]
