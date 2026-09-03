"""Oridecon Domain — DDD domain primitives for the Oridecon Framework.

Groups the core DDD primitives — entities, value objects, and aggregate
roots — under a single cohesive package.  All types are sourced from the
``models`` subpackage and re-exported here for convenient access.

Domain primitives are pure Python with no infrastructure dependencies.
They integrate with the IoC container via :class:`DomainModule` for
graph completeness but require no provider registration.

Basic Usage::

    from oridecon.domain import Entity, ValueObject, AggregateRoot, DomainModel

    class UserId(ValueObject):
        value: str

    class User(Entity):
        name: str
        email: str

Module Structure:
    - config: Domain configuration (``DomainConfig``)
    - exceptions: Domain exception hierarchy (``DomainError``, ``DomainPolicyViolationError``)
    - models: Entity, ValueObject, AggregateRoot, DomainModel primitives
    - module: ``DomainModule`` IoC registration
    - types: Domain type aliases
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from oridecon.domain.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.contracts.data.exceptions import UnitOfWorkError
    from oridecon.contracts.exceptions.domain import (
        DomainError,
        FieldError,
        ValidationError,
    )
    from oridecon.domain.config import DomainConfig
    from oridecon.domain.exceptions import DomainPolicyViolationError
    from oridecon.domain.models.aggregate import AggregateRoot
    from oridecon.domain.models.base import DomainModel
    from oridecon.domain.models.entity import ID, Entity
    from oridecon.domain.models.factory import create_model
    from oridecon.domain.models.value_object import ValueObject
    from oridecon.domain.module import DomainModule

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # --- Module ---
    "DomainModule": ("oridecon.domain.module", "DomainModule"),
    # --- Config ---
    "DomainConfig": ("oridecon.domain.config", "DomainConfig"),
    # --- Models ---
    "DomainModel": ("oridecon.domain.models.base", "DomainModel"),
    "Entity": ("oridecon.domain.models.entity", "Entity"),
    "ID": ("oridecon.domain.models.entity", "ID"),
    "ValueObject": ("oridecon.domain.models.value_object", "ValueObject"),
    "AggregateRoot": ("oridecon.domain.models.aggregate", "AggregateRoot"),
    "create_model": ("oridecon.domain.models.factory", "create_model"),
    # --- Exceptions (sourced from contracts) ---
    "DomainError": ("oridecon.contracts.exceptions.domain", "DomainError"),
    "DomainPolicyViolationError": (
        "oridecon.domain.exceptions",
        "DomainPolicyViolationError",
    ),
    "FieldError": ("oridecon.contracts.exceptions.domain", "FieldError"),
    "ValidationError": ("oridecon.contracts.exceptions.domain", "ValidationError"),
    "UnitOfWorkError": ("oridecon.contracts.data.exceptions", "UnitOfWorkError"),
    # --- Protocols (sourced from contracts) ---
    "DomainEvent": ("oridecon.contracts.domain", "DomainEvent"),
    "EventBusProtocol": ("oridecon.contracts.events.protocols", "EventBusProtocol"),
    "RepositoryProtocol": ("oridecon.contracts.data.repository", "RepositoryProtocol"),
    "SpecificationProtocol": ("oridecon.contracts.domain", "SpecificationProtocol"),
    "UnitOfWorkProtocol": (
        "oridecon.contracts.data.sql.unit_of_work",
        "UnitOfWorkProtocol",
    ),
}


def __getattr__(name: str) -> Any:
    """Lazy-load symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__: list[str] = [
    "ID",
    "AggregateRoot",
    "DomainConfig",
    "DomainError",
    "DomainEvent",
    "DomainModel",
    "DomainModule",
    "DomainPolicyViolationError",
    "Entity",
    "EventBusProtocol",
    "FieldError",
    "RepositoryProtocol",
    "SpecificationProtocol",
    "UnitOfWorkError",
    "UnitOfWorkProtocol",
    "ValidationError",
    "ValueObject",
    "create_model",
]
