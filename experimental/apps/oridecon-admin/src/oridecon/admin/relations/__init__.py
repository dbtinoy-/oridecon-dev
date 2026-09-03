"""Relations module for oridecon-admin.

Provides relation managers for managing entity relationships
in admin views, including many-to-many with pivot data,
polymorphic relations, and inline CRUD.
"""

from __future__ import annotations

from oridecon.admin.relations.belongs_to_many import BelongsToManyRelationManager
from oridecon.admin.relations.manager import AbstractRelationManager
from oridecon.admin.relations.manager_ext import RelationManager
from oridecon.admin.relations.morph_many import MorphManyRelationManager
from oridecon.admin.relations.morph_to import MorphToRelationManager
from oridecon.admin.relations.routes import register_relation_routes

__all__ = [
    "AbstractRelationManager",
    "BelongsToManyRelationManager",
    "MorphManyRelationManager",
    "MorphToRelationManager",
    "RelationManager",
    "register_relation_routes",
]
