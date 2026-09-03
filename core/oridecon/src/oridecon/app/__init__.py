"""Application runtime package for Oridecon Framework.

Entry-point for creating, starting, and stopping a Oridecon
:class:`Application`.  Lifecycle helper functions live in
:mod:`oridecon.app.runner`; the DI :class:`CoreProvider` lives in
:mod:`oridecon.app.di.provider`.

Exports:
    Application: The main application class.
    AppState: Application lifecycle state enum.
    run_application: Start, await OS signal, then stop.
    start_application: Start the application and its providers.
    stop_application: Gracefully stop the application.
"""

from __future__ import annotations

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from oridecon.app.base import Application, AppState
    from oridecon.app.factory import create_app
    from oridecon.app.module import CoreModule
    from oridecon.app.pipeline import MiddlewarePipeline
    from oridecon.app.runner import (
        run_application,
        start_application,
        stop_application,
    )
    from oridecon.app.standard import StandardModule

_LAZY_IMPORTS: dict[str, str] = {
    "Application": "oridecon.app.base",
    "CoreModule": "oridecon.app.module",
    "StandardModule": "oridecon.app.standard",
    "create_app": "oridecon.app.factory",
    "run_application": "oridecon.app.runner",
    "start_application": "oridecon.app.runner",
    "stop_application": "oridecon.app.runner",
    # types
    "AppState": "oridecon.app.types",
    "ApplicationStarted": "oridecon.app.types",
    "ApplicationStarting": "oridecon.app.types",
    "ApplicationStopped": "oridecon.app.types",
    "ApplicationStopping": "oridecon.app.types",
    "HealthCheckCompleted": "oridecon.app.types",
    "ProviderBooted": "oridecon.app.types",
    "ProviderRegistered": "oridecon.app.types",
    # constants
    "DEFAULT_APP_NAME": "oridecon.app.constants",
    "DEFAULT_HEALTH_CHECK_TIMEOUT": "oridecon.app.constants",
    "DEFAULT_SHUTDOWN_TIMEOUT": "oridecon.app.constants",
    # protocols
    "AppLifecycleProtocol": "oridecon.app.protocols",
    # --- added by migration script ---
    "AppConfig": "oridecon.app.config.models",
    "AppError": "oridecon.app.exceptions",
    "AppShutdownError": "oridecon.app.exceptions",
    "AppStartupError": "oridecon.app.exceptions",
    "CoreProvider": "oridecon.app.di.provider",
    "InjectableAutoProvider": "oridecon.app.injectable_provider",
    # pipeline
    "MiddlewarePipeline": "oridecon.app.pipeline",
}


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib

        module = importlib.import_module(_LAZY_IMPORTS[name])
        value = getattr(module, name)
        globals()[name] = value
        return value
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)


def __dir__() -> list[str]:
    return list(_LAZY_IMPORTS.keys())


__all__ = list(_LAZY_IMPORTS.keys())
