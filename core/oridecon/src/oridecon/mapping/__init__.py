"""Object mapping module for transforming between domain models and DTOs.

Exports:
    MappingRegistry: Registry that stores mapper functions keyed by (source, target) type pairs.
    ObjectMapperImpl: Mapper that resolves and invokes registered mapper functions.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from oridecon.mapping.core.mapper import MappingRegistry, ObjectMapperImpl
    from oridecon.mapping.exceptions import (
        MappingError as MappingError,
    )
    from oridecon.mapping.exceptions import (
        MappingExecutionError as MappingExecutionError,
    )
    from oridecon.mapping.exceptions import (
        MappingNotFoundError as MappingNotFoundError,
    )
    from oridecon.mapping.protocols import (
        TypeConverterProtocol as TypeConverterProtocol,
    )
    from oridecon.mapping.types import MapperProtocol as MapperProtocol
    from oridecon.mapping.types import MappingFn as MappingFn

_LAZY_IMPORTS: dict[str, str] = {
    "MappingRegistry": "oridecon.mapping.core.mapper",
    "ObjectMapperImpl": "oridecon.mapping.core.mapper",
    # config
    "MappingConfig": "oridecon.mapping.config",
    # exceptions
    "MappingError": "oridecon.mapping.exceptions",
    "MappingExecutionError": "oridecon.mapping.exceptions",
    "MappingNotFoundError": "oridecon.mapping.exceptions",
    # protocols (now in types)
    "MapperProtocol": "oridecon.mapping.types",
    # types
    "MappingFn": "oridecon.mapping.types",
    # provider
    "MappingModule": "oridecon.mapping.module",
    "MappingProvider": "oridecon.mapping.di.provider",
    # Internal protocols
    "TypeConverterProtocol": "oridecon.mapping.protocols",
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
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = list(_LAZY_IMPORTS.keys())
