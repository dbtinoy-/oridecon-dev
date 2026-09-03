"""HTTP client module for the Oridecon framework.

Provides a first-class async HTTP client, connection pooling, typed request/
response contexts, and a DI provider — available to every application without
pulling in a full web-server framework.

Quick start (standalone, outside DI):

    >>> from oridecon.http import HTTPClient
    >>> async with HTTPClient.session_context() as client:
    ...     response = await client.get("https://api.example.com/health")
    ...     assert response.ok

Quick start (via DI):

    >>> from oridecon.http import HTTPProvider, HTTPClientConfig
    >>> app.add_provider(HTTPProvider(HTTPClientConfig()))
    >>> # Later, resolve from container:
    >>> client = await container.resolve(HTTPClient)

Protocol exports:
    HTTPClientProtocol: Contract for HTTP clients.
    InterceptorProtocol: Contract for HTTP request/response interceptors.
    InterceptorChainProtocol: Contract for interceptor chains.
"""

from __future__ import annotations

from importlib import import_module
import importlib.metadata
from typing import TYPE_CHECKING, Any

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from oridecon.http.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.http.client import BaseURLHTTPClient, HTTPClient, StreamContext
    from oridecon.http.config import (
        ConnectionPoolConfig,
        HTTPClientConfig,
    )
    from oridecon.http.constants import (
        CONTENT_TYPE_FORM,
        CONTENT_TYPE_JSON,
        CONTENT_TYPE_TEXT,
        DEFAULT_ENCODING,
        DEFAULT_MAX_CONNECTIONS,
        DEFAULT_TIMEOUT,
        DELETE,
        GET,
        HEAD,
        OPTIONS,
        PATCH,
        POST,
        PUT,
    )
    from oridecon.http.di.provider import HTTPProvider
    from oridecon.http.exceptions import (
        HTTPCircuitOpenError,
        HTTPClientError,
        HTTPConnectionError,
        HTTPInterceptorError,
        HTTPRetryExhaustedError,
        HTTPTimeoutError,
    )
    from oridecon.http.lib import (
        build_url,
        extract_json_type,
        format_timeout,
        merge_headers,
        parse_headers,
        parse_url_parts,
    )
    from oridecon.http.pool import ConnectionPool
    from oridecon.http.protocols import (
        HTTPClientProtocol,
        InterceptorChainProtocol,
        InterceptorProtocol,
    )
    from oridecon.http.types import (
        RequestContext,
        ResponseContext,
    )
    from oridecon.http.validation import (
        validate_host,
        validate_port,
        validate_positive_int,
        validate_timeout,
        validate_url,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # Client
    "BaseURLHTTPClient": ("oridecon.http.client", "BaseURLHTTPClient"),
    "HTTPClient": ("oridecon.http.client", "HTTPClient"),
    "StreamContext": ("oridecon.http.client", "StreamContext"),
    # Config
    "ConnectionPoolConfig": ("oridecon.http.config", "ConnectionPoolConfig"),
    "HTTPClientConfig": ("oridecon.http.config", "HTTPClientConfig"),
    # Constants
    "CONTENT_TYPE_JSON": ("oridecon.http.constants", "CONTENT_TYPE_JSON"),
    "CONTENT_TYPE_TEXT": ("oridecon.http.constants", "CONTENT_TYPE_TEXT"),
    "CONTENT_TYPE_FORM": ("oridecon.http.constants", "CONTENT_TYPE_FORM"),
    "DEFAULT_ENCODING": ("oridecon.http.constants", "DEFAULT_ENCODING"),
    "DEFAULT_TIMEOUT": ("oridecon.http.constants", "DEFAULT_TIMEOUT"),
    "GET": ("oridecon.http.constants", "GET"),
    "POST": ("oridecon.http.constants", "POST"),
    "PUT": ("oridecon.http.constants", "PUT"),
    "DELETE": ("oridecon.http.constants", "DELETE"),
    "PATCH": ("oridecon.http.constants", "PATCH"),
    "OPTIONS": ("oridecon.http.constants", "OPTIONS"),
    "HEAD": ("oridecon.http.constants", "HEAD"),
    "DEFAULT_MAX_CONNECTIONS": ("oridecon.http.constants", "DEFAULT_MAX_CONNECTIONS"),
    # Events
    "RequestCompletedEvent": ("oridecon.http.events", "RequestCompletedEvent"),
    "RequestRetryExhaustedEvent": (
        "oridecon.http.events",
        "RequestRetryExhaustedEvent",
    ),
    "RequestTimeoutEvent": ("oridecon.http.events", "RequestTimeoutEvent"),
    # Exceptions
    "HTTPCircuitOpenError": ("oridecon.http.exceptions", "HTTPCircuitOpenError"),
    "HTTPConnectionError": ("oridecon.http.exceptions", "HTTPConnectionError"),
    "HTTPClientError": ("oridecon.http.exceptions", "HTTPClientError"),
    "HTTPInterceptorError": ("oridecon.http.exceptions", "HTTPInterceptorError"),
    "HTTPRetryExhaustedError": ("oridecon.http.exceptions", "HTTPRetryExhaustedError"),
    "HTTPTimeoutError": ("oridecon.http.exceptions", "HTTPTimeoutError"),
    # Protocols
    "HTTPClientProtocol": ("oridecon.http.protocols", "HTTPClientProtocol"),
    "InterceptorProtocol": ("oridecon.http.protocols", "InterceptorProtocol"),
    "InterceptorChainProtocol": ("oridecon.http.protocols", "InterceptorChainProtocol"),
    # Utils (URL, header, format helpers)
    "build_url": ("oridecon.http.lib", "build_url"),
    "extract_json_type": ("oridecon.http.lib", "extract_json_type"),
    "format_timeout": ("oridecon.http.lib", "format_timeout"),
    "merge_headers": ("oridecon.http.lib", "merge_headers"),
    "parse_headers": ("oridecon.http.lib", "parse_headers"),
    "parse_url_parts": ("oridecon.http.lib", "parse_url_parts"),
    # Pool
    "ConnectionPool": ("oridecon.http.pool", "ConnectionPool"),
    # Provider
    "HTTPModule": ("oridecon.http.module", "HTTPModule"),
    "HTTPProvider": ("oridecon.http.di.provider", "HTTPProvider"),
    # Types
    "RequestContext": ("oridecon.http.types", "RequestContext"),
    "ResponseContext": ("oridecon.http.types", "ResponseContext"),
    # Validation
    "validate_host": ("oridecon.http.validation", "validate_host"),
    "validate_port": ("oridecon.http.validation", "validate_port"),
    "validate_positive_int": ("oridecon.http.validation", "validate_positive_int"),
    "validate_timeout": ("oridecon.http.validation", "validate_timeout"),
    "validate_url": ("oridecon.http.validation", "validate_url"),
    # Hooks
    "HTTPRequestSentHook": ("oridecon.http.hooks", "HTTPRequestSentHook"),
    "HTTPResponseReceivedHook": ("oridecon.http.hooks", "HTTPResponseReceivedHook"),
}


def __getattr__(name: str) -> Any:
    """Lazy-load attributes to keep import time low."""
    if name in _LAZY_IMPORTS:
        module_path, attr_name = _LAZY_IMPORTS[name]
        module = import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """Expose lazy names for IDE completion."""
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = list(_LAZY_IMPORTS)
