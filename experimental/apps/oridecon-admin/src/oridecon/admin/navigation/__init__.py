"""Navigation assembly — merges contributor and resource navigation."""

from __future__ import annotations

from oridecon.admin.navigation.assembler import NavigationAssembler
from oridecon.admin.navigation.builder import NavigationBuilder
from oridecon.admin.navigation.nav_item_builder import NavItemBuilder
from oridecon.admin.navigation.types import NavGroup, NavigationConfig, NavItem

from .assembler import contributions_to_flat_nav

__all__ = [
    "NavGroup",
    "NavItem",
    "NavItemBuilder",
    "NavigationAssembler",
    "NavigationBuilder",
    "NavigationConfig",
    "contributions_to_flat_nav",
]
