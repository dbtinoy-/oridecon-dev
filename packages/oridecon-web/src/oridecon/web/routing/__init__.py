from __future__ import annotations

from typing import Any

from oridecon.web.routing.controller import GenericController
from oridecon.web.routing.controller_registry import (
    ControllerRegistry,
    controller,
    controller_registry,
)
from oridecon.web.routing.controllers import Controller
from oridecon.web.routing.cqrs import CQRSController
from oridecon.web.routing.decorators import (
    delete,
    get,
    head,
    options,
    patch,
    post,
    put,
    trace,
    websocket,
)
from oridecon.web.routing.discovery import (
    discover_controllers,
    discover_websocket_handlers,
)


def __dir__() -> list[str]:
    return sorted(__all__)


from oridecon.web.routing.execution_context import WebExecutionContext
from oridecon.web.routing.parameter_binder import ParameterBinder
from oridecon.web.routing.parameters import (
    body,
    cookie,
    file,
    form,
    header,
    path,
    query,
)
from oridecon.web.routing.pipeline import RequestPipeline
from oridecon.web.routing.registry import (
    RouteRegistry,
    register_controller,
    route_registry,
)
from oridecon.web.routing.router import Router
from oridecon.web.routing.versioning import (
    ApiVersionMetadata,
    VersionExtractor,
    VersioningMiddleware,
    VersioningStrategy,
    api_version,
    get_version,
    version,
)


def __getattr__(name: str) -> Any:
    if name == "VersioningConfig":
        from oridecon.web.routing.versioning import VersioningConfig

        return VersioningConfig
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "ApiVersionMetadata",
    "CQRSController",
    "Controller",
    "ControllerRegistry",
    "GenericController",
    "ParameterBinder",
    "RequestPipeline",
    "RouteRegistry",
    "Router",
    "VersionExtractor",
    "VersioningConfig",
    "VersioningMiddleware",
    "VersioningStrategy",
    "WebExecutionContext",
    "api_version",
    "body",
    "controller",
    "controller_registry",
    "cookie",
    "delete",
    "discover_controllers",
    "discover_websocket_handlers",
    "file",
    "form",
    "get",
    "get_version",
    "head",
    "header",
    "options",
    "patch",
    "path",
    "post",
    "put",
    "query",
    "register_controller",
    "route_registry",
    "trace",
    "version",
    "websocket",
]
