"""Data table component package with modular architecture."""

from __future__ import annotations

from oridecon.admin.config import TableConfiguration
from oridecon.admin.ui.organisms.data_table.actions import ActionManager
from oridecon.admin.ui.organisms.data_table.coordinator import DataTable
from oridecon.admin.ui.organisms.data_table.layout import LayoutComposer
from oridecon.admin.ui.organisms.data_table.permissions import PermissionManager
from oridecon.admin.ui.organisms.data_table.rendering import DataTableRenderer
from oridecon.admin.ui.organisms.data_table.states import StateRenderer
from oridecon.admin.ui.organisms.data_table.views import (
    ViewStrategy,
    ViewStrategyRegistry,
    view_strategy_registry,
)
from oridecon.ui import TableState

__all__ = [
    "ActionManager",
    "DataTable",
    "DataTableRenderer",
    "LayoutComposer",
    "PermissionManager",
    "StateRenderer",
    "TableConfiguration",
    "TableState",
    "ViewStrategy",
    "ViewStrategyRegistry",
    "view_strategy_registry",
]
