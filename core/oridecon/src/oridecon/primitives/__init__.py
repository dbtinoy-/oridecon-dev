"""Oridecon Core — Core framework primitives: builders, contexts, registries.

This module uses lazy imports for all public symbols to keep
import overhead minimal.  Every name listed in _LAZY_IMPORTS
is available at package level:

    from oridecon.primitives import <Symbol>

or by accessing the attribute on the package:

    import oridecon.primitives as core
    core.<Symbol>
"""

from __future__ import annotations

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from oridecon.primitives.builder import (
        AbstractBuilder,
        buildable,
        builder_field,
    )
    from oridecon.primitives.context import (
        CAUSATION_ID,
        CORRELATION_ID,
        DEFAULT_KEYS,
        REQUEST_ID,
        REQUEST_METHOD,
        REQUEST_PATH,
        REQUEST_START_TIME,
        SPAN_ID,
        TENANT_ID,
        TRACE_FLAGS,
        TRACE_ID,
        USER_ID,
        Context,
        ContextKey,
        ContextVarRegistry,
        RequestContext,
        create_context_registry,
        create_default_context,
        get_request_context,
        propagate_context,
        request_scope,
        with_context,
    )
    from oridecon.primitives.pipeline import (
        PipelineContext,
        PipelineStep,
    )
    from oridecon.primitives.registry import (
        Registry,
        RegistryIntrospector,
        entry_point_catalog,
        on_register,
        on_unregister,
        registry_info,
    )

_LAZY_IMPORTS: dict[str, str] = {
    "AbstractBuilder": "oridecon.primitives.builder",
    "buildable": "oridecon.primitives.builder",
    "builder_field": "oridecon.primitives.builder",
    # context — keys
    "CAUSATION_ID": "oridecon.primitives.context",
    "CORRELATION_ID": "oridecon.primitives.context",
    "DEFAULT_KEYS": "oridecon.primitives.context",
    "REQUEST_ID": "oridecon.primitives.context",
    "REQUEST_METHOD": "oridecon.primitives.context",
    "REQUEST_PATH": "oridecon.primitives.context",
    "REQUEST_START_TIME": "oridecon.primitives.context",
    "SPAN_ID": "oridecon.primitives.context",
    "TENANT_ID": "oridecon.primitives.context",
    "TRACE_FLAGS": "oridecon.primitives.context",
    "TRACE_ID": "oridecon.primitives.context",
    "USER_ID": "oridecon.primitives.context",
    # clock
    "clock": "oridecon.primitives.clock",
    # context — classes
    "Context": "oridecon.primitives.context",
    "ContextKey": "oridecon.primitives.context",
    "ContextVarRegistry": "oridecon.primitives.context",
    "RequestContext": "oridecon.primitives.context",
    # context — factories & helpers
    "create_context_registry": "oridecon.primitives.context",
    "create_default_context": "oridecon.primitives.context",
    "get_request_context": "oridecon.primitives.context",
    "propagate_context": "oridecon.primitives.context",
    "request_scope": "oridecon.primitives.context",
    "with_context": "oridecon.primitives.context",
    # registry
    "Registry": "oridecon.primitives.registry",
    "on_register": "oridecon.primitives.registry",
    "on_unregister": "oridecon.primitives.registry",
    # registry introspection
    "RegistryIntrospector": "oridecon.primitives.registry.introspection",
    "entry_point_catalog": "oridecon.primitives.registry.introspection",
    "registry_info": "oridecon.primitives.registry.introspection",
    # exceptions
    "CoreError": "oridecon.primitives.exceptions",
    # constants
    "REQUEST_ID_KEY": "oridecon.primitives.constants",
    "TENANT_ID_KEY": "oridecon.primitives.constants",
    "TRACE_ID_KEY": "oridecon.primitives.constants",
    "SPAN_ID_KEY": "oridecon.primitives.constants",
    "USER_ID_KEY": "oridecon.primitives.constants",
    "REQUEST_PATH_KEY": "oridecon.primitives.constants",
    "REQUEST_METHOD_KEY": "oridecon.primitives.constants",
    "REQUEST_START_TIME_KEY": "oridecon.primitives.constants",
    # types
    "Priority": "oridecon.primitives.types",
    # protocols
    "Buildable": "oridecon.primitives.protocols",
    "Registrable": "oridecon.primitives.protocols",
    # pipeline
    "PipelineContext": "oridecon.primitives.pipeline",
    "PipelineStep": "oridecon.primitives.pipeline",
    "LazyImport": "oridecon.primitives.lazy",
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
__version__ = "0.1.0"
