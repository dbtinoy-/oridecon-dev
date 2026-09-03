"""Oridecon Web - Progressive Web Framework for Oridecon"""

from __future__ import annotations

import importlib.metadata
from typing import TYPE_CHECKING, Any

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from oridecon.web.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.web.config import WebConfig
    from oridecon.web.di.provider import WebProvider
    from oridecon.web.di.rate_limit import RateLimitProvider


# =============================================================================
# Lazy Loading to Avoid Circular Imports
# =============================================================================

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # Discovery
    "discover_controllers": ("oridecon.web.routing.discovery", "discover_controllers"),
    "discover_websocket_handlers": (
        "oridecon.web.routing.discovery",
        "discover_websocket_handlers",
    ),
    # Config & Provider
    "WebConfig": ("oridecon.web.config", "WebConfig"),
    "WebProvider": ("oridecon.web.di.provider", "WebProvider"),
    "RateLimitProvider": ("oridecon.web.di.rate_limit", "RateLimitProvider"),
    # Modules
    "WebModule": ("oridecon.web.module", "WebModule"),
    # Routing
    "Controller": ("oridecon.web.routing.controllers", "Controller"),
    "CQRSController": ("oridecon.web.routing.cqrs", "CQRSController"),
    "ControllerRegistry": (
        "oridecon.web.routing.controller_registry",
        "ControllerRegistry",
    ),
    "GenericController": ("oridecon.web.routing.controller", "GenericController"),
    "Router": ("oridecon.web.routing.router", "Router"),
    "RouteRegistry": ("oridecon.web.routing.registry", "RouteRegistry"),
    "VersionExtractor": ("oridecon.web.routing.versioning", "VersionExtractor"),
    "ApiVersionMetadata": ("oridecon.web.routing.versioning", "ApiVersionMetadata"),
    "api_version": ("oridecon.web.routing.versioning", "api_version"),
    # Parameters
    "body": ("oridecon.web.routing.parameters", "body"),
    "controller": ("oridecon.web.routing.controller_registry", "controller"),
    "controller_registry": (
        "oridecon.web.routing.controller_registry",
        "controller_registry",
    ),
    "cookie": ("oridecon.web.routing.parameters", "cookie"),
    "file": ("oridecon.web.routing.parameters", "file"),
    "form": ("oridecon.web.routing.parameters", "form"),
    "get_version": ("oridecon.web.routing.versioning", "get_version"),
    "header": ("oridecon.web.routing.parameters", "header"),
    "path": ("oridecon.web.routing.parameters", "path"),
    "query": ("oridecon.web.routing.parameters", "query"),
    "register_controller": ("oridecon.web.routing.registry", "register_controller"),
    "route_registry": ("oridecon.web.routing.registry", "route_registry"),
    "version": ("oridecon.web.routing.versioning", "version"),
    # HTTP Methods (from decorators)
    "delete": ("oridecon.web.routing.decorators", "delete"),
    "get": ("oridecon.web.routing.decorators", "get"),
    "head": ("oridecon.web.routing.decorators", "head"),
    "options": ("oridecon.web.routing.decorators", "options"),
    "patch": ("oridecon.web.routing.decorators", "patch"),
    "post": ("oridecon.web.routing.decorators", "post"),
    "put": ("oridecon.web.routing.decorators", "put"),
    "trace": ("oridecon.web.routing.decorators", "trace"),
    "websocket": ("oridecon.web.routing.decorators", "websocket"),
    "websocket_handler": ("oridecon.web.websocket.decorators", "websocket_handler"),
    # Transport
    "Response": ("oridecon.web.transport.responses", "Response"),
    "FastJSONResponse": ("oridecon.web.transport.responses", "FastJSONResponse"),
    "HTMXResponse": ("oridecon.web.transport.responses", "HTMXResponse"),
    "HTMLContent": ("oridecon.web.transport.responses", "HTMLContent"),
    "JSONResponse": ("oridecon.web.transport.responses", "JSONResponse"),
    "HTMLResponse": ("oridecon.web.transport.responses", "HTMLResponse"),
    "RedirectResponse": ("oridecon.web.transport.responses", "RedirectResponse"),
    "StreamingResponse": ("oridecon.web.transport.responses", "StreamingResponse"),
    "FileResponse": ("oridecon.web.transport.responses", "FileResponse"),
    "WebSocket": ("oridecon.web.transport.websockets", "WebSocket"),
    # Template rendering
    "render_template": ("oridecon.web.templates.core", "render_template"),
    # Response helpers
    "json_response": ("oridecon.web.transport.responses", "json_response"),
    "html_response": ("oridecon.web.transport.responses", "html_response"),
    "redirect_response": ("oridecon.web.transport.responses", "redirect_response"),
    "streaming_response": ("oridecon.web.transport.responses", "streaming_response"),
    "file_response": ("oridecon.web.transport.responses", "file_response"),
    # Middleware
    "DefaultMiddlewareStack": (
        "oridecon.web.middleware.stack",
        "DefaultMiddlewareStack",
    ),
    "InputSanitizationMiddleware": (
        "oridecon.web.middleware.sanitization",
        "InputSanitizationMiddleware",
    ),
    # Security
    "RoleGuard": ("oridecon.web.security.guards", "RoleGuard"),
    "guard": ("oridecon.web.security.shortcuts", "guard"),
    "roles": ("oridecon.web.security.shortcuts", "roles"),
    # Exceptions
    "HTTPError": ("oridecon.web.exceptions", "HTTPError"),
    "NotFoundError": ("oridecon.web.exceptions", "NotFoundError"),
    "ConflictError": ("oridecon.web.exceptions", "ConflictError"),
    "RateLimitError": ("oridecon.web.exceptions", "RateLimitError"),
    "TooManyConnectionsError": ("oridecon.web.exceptions", "TooManyConnectionsError"),
    "InternalServerError": ("oridecon.web.exceptions", "InternalServerError"),
    # Background tasks
    "background": ("oridecon.web.background.decorator", "background"),
    "BackgroundTasks": ("oridecon.web.background.tasks", "BackgroundTasks"),
    # Errors
    "ProblemDetail": ("oridecon.web.errors.problem_detail", "ProblemDetail"),
    # Request state helpers
    "get_request_id": ("oridecon.web.dependencies.functions", "get_request_id"),
    "get_current_user_optional": (
        "oridecon.web.dependencies.functions",
        "get_current_user_optional",
    ),
    "get_current_user_required": (
        "oridecon.web.dependencies.functions",
        "get_current_user_required",
    ),
    # Rate limiting sugar
    "throttle": ("oridecon.web.integrations.throttle", "throttle"),
    "RateLimitModule": ("oridecon.web.integrations.throttle", "RateLimitModule"),
    # Quickstart
    "app": ("oridecon.web.quickstart", "app"),
    # DI decorators — quickstart-aware versions that also register in the
    # quickstart service registry so classes defined in any scope are discovered.
    "singleton": ("oridecon.web.quickstart", "singleton"),
    "injectable": ("oridecon.web.quickstart", "injectable"),
    "transient": ("oridecon.di", "transient"),
    # Result bridge
    "ResultResponseMapper": (
        "oridecon.web.routing.result_bridge",
        "ResultResponseMapper",
    ),
    "error_status": ("oridecon.web.routing.result_bridge", "error_status"),
    # Protocols (web-layer pipe + interceptor)
    "ParamMetadata": ("oridecon.web.protocols", "ParamMetadata"),
    "PipeProtocol": ("oridecon.web.protocols", "PipeProtocol"),
    "ExecutionContextProtocol": ("oridecon.web.protocols", "ExecutionContextProtocol"),
    "CallHandlerProtocol": ("oridecon.web.protocols", "CallHandlerProtocol"),
    "WebInterceptorProtocol": ("oridecon.web.protocols", "WebInterceptorProtocol"),
    "WebInterceptorBase": ("oridecon.web.protocols", "WebInterceptorBase"),
    # Provider protocols (decoupling)
    "WebAppAccessorProtocol": ("oridecon.web.protocols", "WebAppAccessorProtocol"),
    "ControllerSourceProtocol": ("oridecon.web.protocols", "ControllerSourceProtocol"),
    "ConfigAccessorProtocol": ("oridecon.web.protocols", "ConfigAccessorProtocol"),
    "ProviderResourcesProtocol": (
        "oridecon.web.protocols",
        "ProviderResourcesProtocol",
    ),
    "WebProviderProtocol": ("oridecon.web.protocols", "WebProviderProtocol"),
    # Hooks
    "WebRequestReceivedHook": ("oridecon.web.hooks", "WebRequestReceivedHook"),
    "WebResponsePreparedHook": ("oridecon.web.hooks", "WebResponsePreparedHook"),
    "WebServerStartedHook": ("oridecon.web.hooks", "WebServerStartedHook"),
    "WebServerStoppedHook": ("oridecon.web.hooks", "WebServerStoppedHook"),
    # Core re-exports
    "Result": ("oridecon.result", "Result"),
    "Ok": ("oridecon.result", "Ok"),
    "Err": ("oridecon.result", "Err"),
}


def __getattr__(name: str) -> Any:
    """Lazy load attributes to avoid circular imports."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        # Cache in module globals so __getattr__ isn't called again for this name
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """List available attributes for IDE support (deduplicated, sorted).

    ``__all__`` already mirrors the lazy map, so the previous
    ``list(__all__) + list(_LAZY_IMPORTS.keys())`` listed every public name
    twice.
    """
    return sorted(set(globals()) | set(_LAZY_IMPORTS) | {"__version__"})


# Curated, sorted export list (kept in sync with _LAZY_IMPORTS) so tooling
# and docs see a stable ordering rather than the lazy map's insertion order.
__all__ = [
    "ApiVersionMetadata",
    "BackgroundTasks",
    "CQRSController",
    "CallHandlerProtocol",
    "ConfigAccessorProtocol",
    "ConflictError",
    "Controller",
    "ControllerRegistry",
    "ControllerSourceProtocol",
    "DefaultMiddlewareStack",
    "Err",
    "ExecutionContextProtocol",
    "FastJSONResponse",
    "FileResponse",
    "GenericController",
    "HTMLContent",
    "HTMLResponse",
    "HTMXResponse",
    "HTTPError",
    "InputSanitizationMiddleware",
    "InternalServerError",
    "JSONResponse",
    "NotFoundError",
    "Ok",
    "ParamMetadata",
    "PipeProtocol",
    "ProblemDetail",
    "ProviderResourcesProtocol",
    "RateLimitError",
    "RateLimitModule",
    "RateLimitProvider",
    "RedirectResponse",
    "Response",
    "Result",
    "ResultResponseMapper",
    "RoleGuard",
    "RouteRegistry",
    "Router",
    "StreamingResponse",
    "TooManyConnectionsError",
    "VersionExtractor",
    "WebAppAccessorProtocol",
    "WebConfig",
    "WebInterceptorBase",
    "WebInterceptorProtocol",
    "WebModule",
    "WebProvider",
    "WebProviderProtocol",
    "WebRequestReceivedHook",
    "WebResponsePreparedHook",
    "WebServerStartedHook",
    "WebServerStoppedHook",
    "WebSocket",
    "api_version",
    "app",
    "background",
    "body",
    "controller",
    "controller_registry",
    "cookie",
    "delete",
    "discover_controllers",
    "discover_websocket_handlers",
    "error_status",
    "file",
    "file_response",
    "form",
    "get",
    "get_current_user_optional",
    "get_current_user_required",
    "get_request_id",
    "get_version",
    "guard",
    "head",
    "header",
    "html_response",
    "injectable",
    "json_response",
    "options",
    "patch",
    "path",
    "post",
    "put",
    "query",
    "redirect_response",
    "register_controller",
    "render_template",
    "roles",
    "route_registry",
    "singleton",
    "streaming_response",
    "throttle",
    "trace",
    "transient",
    "version",
    "websocket",
    "websocket_handler",
]
