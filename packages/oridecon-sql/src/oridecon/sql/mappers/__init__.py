"""Entity mapping system for Oridecon DB"""

from __future__ import annotations

from oridecon.sql.mappers.base import DataMapper, MappingError
from oridecon.sql.mappers.domain_mapper import DomainDataMapper

__all__ = [
    "DataMapper",
    "DomainDataMapper",
    "MappingError",
]
