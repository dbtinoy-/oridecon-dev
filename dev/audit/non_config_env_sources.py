"""Intentional environment-variable reads that are outside package config models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NonConfigEnvSource:
    """Static metadata for env vars intentionally read outside config.py."""

    source_file: str
    env_var: str
    rationale: str


NON_CONFIG_ENV_SOURCES: tuple[NonConfigEnvSource, ...] = (
    NonConfigEnvSource(
        source_file="core/oridecon/src/oridecon/logging/debug.py",
        env_var="ORI_DEBUG",
        rationale="Early-boot logging toggle before typed config is available.",
    ),
    NonConfigEnvSource(
        source_file="core/oridecon/src/oridecon/app/base.py",
        env_var="ORI_QUIET",
        rationale="Controls startup banner suppression during process bootstrap.",
    ),
    NonConfigEnvSource(
        source_file="experimental/apps/oridecon-cli/src/oridecon/cli/lib/config_loader.py",
        env_var="ORI_CONFIG",
        rationale="CLI override for explicit configuration file path.",
    ),
)

