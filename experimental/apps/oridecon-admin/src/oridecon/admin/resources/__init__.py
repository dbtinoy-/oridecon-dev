"""Admin resources module.

Resources define the configuration for admin UI views including
columns, actions, filters, and permissions.
"""

from __future__ import annotations

from oridecon.admin.resources.base import Resource
from oridecon.admin.resources.config import (
    FormSection,
    ResourceConfig,
    TableConfiguration,
)
from oridecon.admin.resources.lenses import LensRegistry, ResourceLens
from oridecon.admin.resources.mixins import HasInfolist

__all__ = [
    "FormSection",
    "HasInfolist",
    "LensRegistry",
    "Resource",
    "ResourceConfig",
    "ResourceLens",
    "TableConfiguration",
]
