"""DI resolution engine — descriptors, registry, resolver, injector, and type hints."""

from __future__ import annotations

from oridecon.di.resolution.context import current_resolver_var, get_resolver
from oridecon.di.resolution.descriptor import ServiceDescriptor
from oridecon.di.resolution.injector import DependencyInjector
from oridecon.di.resolution.registry import ServiceRegistry
from oridecon.di.resolution.resolver import ServiceResolver
from oridecon.di.resolution.store import ServiceStore
from oridecon.di.resolution.type_hints import BoundedCache, TypeHintResolverImpl
from oridecon.di.resolution.validator import GraphValidator

__all__ = [
    "BoundedCache",
    "DependencyInjector",
    "GraphValidator",
    "ServiceDescriptor",
    "ServiceRegistry",
    "ServiceResolver",
    "ServiceStore",
    "TypeHintResolverImpl",
    "current_resolver_var",
    "get_resolver",
]
