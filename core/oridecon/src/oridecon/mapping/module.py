"""Mapping module for dependency injection."""

from __future__ import annotations

from oridecon.di.module import Module, module
from oridecon.mapping.core.mapper import ObjectMapperImpl
from oridecon.mapping.di.provider import MappingProvider


@module(
    providers=[MappingProvider],
    exports=[ObjectMapperImpl],
)
class MappingModule(Module):
    """Object-to-object mapping registry and mapper.

    Static module — no factory required.  Registers a shared
    :class:`~oridecon.mapping.mapper.MappingRegistry` and
    :class:`~oridecon.mapping.mapper.ObjectMapperImpl` singleton.

    Usage::

        @module(imports=[MappingModule])
        class AppModule(Module):
            pass
    """


__all__ = ["MappingModule"]
