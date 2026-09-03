"""Composition root for the single-niche Artifact Vault demo."""

from __future__ import annotations

from artifact_vault.controllers.api import ArtifactVaultApiController
from artifact_vault.di.provider import ArtifactVaultProvider
from artifact_vault.ui.pages import ArtifactVaultPageController
from oridecon.app.base import Application
from oridecon.config.main import OrideconConfig
from oridecon.di.provider import Provider
from oridecon.storage.module import StorageModule
from oridecon.web.module import WebModule


def build_modules() -> list[object]:
    """Build the Oridecon modules required by the artifact vault demo."""
    return [
        StorageModule.configure(),
        WebModule.configure(
            controllers=[ArtifactVaultApiController, ArtifactVaultPageController],
        ),
    ]


def build_providers() -> list[Provider]:
    """Build the DI providers for the artifact vault demo."""
    return [ArtifactVaultProvider()]


def create_app(config: OrideconConfig | None = None) -> Application:
    """Create and configure the artifact vault application."""
    app = Application(name="artifact-vault", config=config)
    app.add_modules(build_modules())
    app.add_providers(build_providers())
    return app


__all__ = ["build_modules", "build_providers", "create_app"]
