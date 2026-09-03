"""Dependency injection system for Oridecon Framework.

Provides the IoC container, builder, scoping, module system, provider
orchestrator, and DI decorators for constructor injection.

Exports:
    Container, Scope: Core DI container and scope.
    ContainerBuilder: Fluent API for building a configured container.
    ContainerRegistrarProtocol: Write-only container interface for Provider.register().
    ContainerResolverProtocol: Read-only container interface for Provider.boot().
    Module, module: DI module descriptor and decorator.
    Provider: Base class for all framework providers.
    ProviderOrchestrator: Coordinates provider lifecycle in priority order.
    ProviderPriority: Enum for provider registration priority.
    ResolutionStrategy: Extension hook for custom resolution logic.
    ServiceScope: Enum for singleton/scoped/transient lifetimes.
    Injectable, inject, injectable, scoped, singleton, transient: DI decorators.
"""

from __future__ import annotations

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from oridecon.contracts.core.di import (
        ContainerRegistrarProtocol,
        ContainerResolverProtocol,
    )
    from oridecon.contracts.core.provider import ProviderPriority
    from oridecon.contracts.core.scopes import ServiceScope
    from oridecon.di.builder import ContainerBuilder
    from oridecon.di.container import Container, Scope
    from oridecon.di.context import (
        ModuleContextTokens,
        check_visibility,
        clear_module_context,
        get_current_module,
        set_module_context,
    )
    from oridecon.di.decorators import (
        Injectable,
        inject,
        injectable,
        scoped,
        singleton,
        transient,
    )
    from oridecon.di.extensions.strategies import ResolutionStrategy
    from oridecon.di.function_provider import FunctionProvider, provide
    from oridecon.di.markers import named
    from oridecon.di.module import Module, module
    from oridecon.di.orchestrator import ProviderOrchestrator
    from oridecon.di.provider import Provider

_LAZY_IMPORTS: dict[str, str] = {
    "ContainerRegistrarProtocol": "oridecon.contracts.core.di",
    "ContainerResolverProtocol": "oridecon.contracts.core.di",
    "ProviderPriority": "oridecon.contracts.core.provider",
    "Injectable": "oridecon.di.decorators",
    "inject": "oridecon.di.decorators",
    "injectable": "oridecon.di.decorators",
    "scoped": "oridecon.di.decorators",
    "singleton": "oridecon.di.decorators",
    "transient": "oridecon.di.decorators",
    "ContainerBuilder": "oridecon.di.builder",
    "Container": "oridecon.di.container",
    "Scope": "oridecon.di.container",
    "ResolutionStrategy": "oridecon.di.extensions.strategies",
    "FunctionProvider": "oridecon.di.function_provider",
    "provide": "oridecon.di.function_provider",
    "named": "oridecon.di.markers",
    "Module": "oridecon.di.module",
    "module": "oridecon.di.module",
    "ProviderOrchestrator": "oridecon.di.orchestrator",
    "Provider": "oridecon.di.provider",
    "ServiceScope": "oridecon.types",
    # types
    "ProviderState": "oridecon.di.types",
    # constants
    "DEFAULT_MAX_RESOLUTION_DEPTH": "oridecon.di.constants",
    "DEFAULT_SCOPE_NAME": "oridecon.di.constants",
    # --- added by migration script ---
    "DiConfig": "oridecon.di.config.models",
    "CircularDependencyError": "oridecon.di.exceptions",
    "ContainerBuildError": "oridecon.di.exceptions",
    "ContainerError": "oridecon.di.exceptions",
    "DependencyError": "oridecon.di.exceptions",
    "ModuleError": "oridecon.di.exceptions",
    "ProviderError": "oridecon.di.exceptions",
    "RegistrationError": "oridecon.di.exceptions",
    "UnresolvableDependencyError": "oridecon.di.exceptions",
    "DiProvider": "oridecon.di.integration.provider",
    # context
    "ModuleContextTokens": "oridecon.di.context",
    "check_visibility": "oridecon.di.context",
    "clear_module_context": "oridecon.di.context",
    "get_current_module": "oridecon.di.context",
    "set_module_context": "oridecon.di.context",
}


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib

        mod = importlib.import_module(_LAZY_IMPORTS[name])
        return getattr(mod, name)
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)


def __dir__() -> list[str]:
    return list(_LAZY_IMPORTS.keys())


__all__ = list(_LAZY_IMPORTS.keys())
