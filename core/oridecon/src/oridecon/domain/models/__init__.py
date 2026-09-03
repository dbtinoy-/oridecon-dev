"""Domain models for Oridecon.

This package provides the core domain modelling primitives:
- DomainModel: Base mixin for all domain objects
- Entity: Identity-based domain objects with unique IDs
- ValueObject: Immutable domain objects defined by attributes
"""

from __future__ import annotations

from oridecon.domain.models.base import DomainModel
from oridecon.domain.models.entity import Entity
from oridecon.domain.models.value_object import ValueObject

__all__ = [
    "DomainModel",
    "Entity",
    "ValueObject",
]
