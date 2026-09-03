"""AI Evaluation framework for Oridecon.

Provides evaluators, a harness, and reproducible experiment tracking:
seed-stable run ids, metric/error streams, digest-verified checkpoints,
ablation comparisons, and error analysis for completed runs.
"""

from __future__ import annotations

from oridecon.ai.evaluation.ablation import AblationRunner
from oridecon.ai.evaluation.analysis import ErrorAnalysis
from oridecon.ai.evaluation.checkpoints import FileCheckpointStore
from oridecon.ai.evaluation.config import EvaluationConfig
from oridecon.ai.evaluation.constants import (
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_THRESHOLD,
    DEFAULT_TIMEOUT_SECONDS,
    MAX_RETRIES,
)
from oridecon.ai.evaluation.di.provider import EvaluationProvider
from oridecon.ai.evaluation.exceptions import (
    AblationError,
    AnalysisError,
    CheckpointError,
    DatasetError,
    EvaluationConfigError,
    EvaluatorNotFoundError,
    HarnessError,
    TrackingError,
)
from oridecon.ai.evaluation.module import EvaluationModule
from oridecon.ai.evaluation.tracking import LocalTracker, make_run_id
from oridecon.ai.evaluation.types import (
    BatchEvaluationResult,
    EvaluationDataset,
    EvaluationResult,
    EvaluationRunContext,
    EvaluationSample,
    RunReport,
)
from oridecon.contracts.ai.experiment import (
    AblationResult,
    AnalysisReport,
    Checkpoint,
    CheckpointStoreProtocol,
    ErrorRecord,
    ExperimentConfig,
    ExperimentRun,
    ExperimentTrackerProtocol,
    MetricRecord,
    RunStatus,
)

__all__ = [
    "DEFAULT_EMBEDDING_MODEL",
    "DEFAULT_THRESHOLD",
    "DEFAULT_TIMEOUT_SECONDS",
    "MAX_RETRIES",
    "AblationError",
    "AblationResult",
    "AblationRunner",
    "AnalysisError",
    "AnalysisReport",
    "BatchEvaluationResult",
    "Checkpoint",
    "CheckpointError",
    "CheckpointStoreProtocol",
    "DatasetError",
    "ErrorAnalysis",
    "ErrorRecord",
    "EvaluationConfig",
    "EvaluationConfigError",
    "EvaluationDataset",
    "EvaluationModule",
    "EvaluationProvider",
    "EvaluationResult",
    "EvaluationRunContext",
    "EvaluationSample",
    "EvaluatorNotFoundError",
    "ExperimentConfig",
    "ExperimentRun",
    "ExperimentTrackerProtocol",
    "FileCheckpointStore",
    "HarnessError",
    "LocalTracker",
    "MetricRecord",
    "RunReport",
    "RunStatus",
    "TrackingError",
    "make_run_id",
]
