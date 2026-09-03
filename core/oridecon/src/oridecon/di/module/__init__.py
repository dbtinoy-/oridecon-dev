from __future__ import annotations

# file: di/module/__init__.py
"""Oridecon Module System.

Modules are ORGANIZERS only.  They group providers and define
import/export visibility boundaries.

Rule:
    Want to register a service?  → Write a Provider.
    Want to organize providers?  → Write a Module.

Static module::

    @module(
        providers=[DatabaseProvider, CacheProvider],
        imports=[ConfigModule],
        exports=[DatabaseSession, CacheBackendProtocol],
    )
    class InfraModule:
        pass

Dynamic module (configurable library package)::

    @module()
    class DatabaseModule(Module):

        @classmethod
        def configure(cls, url: str) -> DynamicModule:
            return DynamicModule(
                module=cls,
                providers=[DatabaseProvider(url=url)],
                exports=[DatabaseSession],
                is_global=True,
            )

Global module (exports visible everywhere)::

    @global_module
    class LoggingModule(Module):
        providers = [LoggingProvider]
        exports = [LoggerProtocol]
"""

from oridecon.contracts.exceptions.provider import (
    ModuleCycleError,
    ModuleDuplicateError,
    ModuleError,
    ModuleExportError,
    ModuleImportError,
    ModuleVisibilityError,
)
from oridecon.di.module.base import Module, ModuleBase
from oridecon.di.module.compiler import ModuleCompiler
from oridecon.di.module.constants import MODULE_METADATA_ATTR
from oridecon.di.module.decorator import create_module, global_module, module
from oridecon.di.module.dynamic import DynamicModule
from oridecon.di.module.graph import CompiledModuleGraph, ModuleNode, ProviderEntry
from oridecon.di.module.introspection import (
    get_module_class,
    get_module_metadata,
    get_module_name,
    is_dynamic_module,
    is_module,
    resolve_module_input,
)
from oridecon.di.module.metadata import ModuleMetadata
from oridecon.di.module.registry import ModuleRegistry

__all__ = [
    "MODULE_METADATA_ATTR",
    "CompiledModuleGraph",
    "DynamicModule",
    "Module",
    "ModuleBase",
    "ModuleCompiler",
    "ModuleCycleError",
    "ModuleDuplicateError",
    "ModuleError",
    "ModuleExportError",
    "ModuleImportError",
    "ModuleMetadata",
    "ModuleNode",
    "ModuleRegistry",
    "ModuleVisibilityError",
    "ProviderEntry",
    "create_module",
    "get_module_class",
    "get_module_metadata",
    "get_module_name",
    "global_module",
    "is_dynamic_module",
    "is_module",
    "module",
    "resolve_module_input",
]
