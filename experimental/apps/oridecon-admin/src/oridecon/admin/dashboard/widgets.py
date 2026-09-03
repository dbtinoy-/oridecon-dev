"""Admin dashboard widget types and infrastructure.

Facade module: widget type definitions live in
:mod:`oridecon.admin.dashboard.widget_defs`, contributor card rendering in
:mod:`oridecon.admin.dashboard.widget_cards`, and the config popup in
:mod:`oridecon.admin.dashboard.widget_config_popup`. Widget definitions
from oridecon-contracts are also re-exported here.
"""

from __future__ import annotations

from oridecon.admin.dashboard.widget_cards import (
    WidgetRegistry as WidgetRegistry,
)
from oridecon.admin.dashboard.widget_cards import (
    render_dashboard_widgets as render_dashboard_widgets,
)
from oridecon.admin.dashboard.widget_config_popup import (
    render_widget_config_popup as render_widget_config_popup,
)
from oridecon.admin.dashboard.widget_defs import (
    DashboardConfig as DashboardConfig,
)
from oridecon.admin.dashboard.widget_defs import (
    IDashboardStore as IDashboardStore,
)
from oridecon.admin.dashboard.widget_defs import (
    InMemoryDashboardStore as InMemoryDashboardStore,
)
from oridecon.admin.dashboard.widget_defs import IWidget as IWidget
from oridecon.admin.dashboard.widget_defs import (
    WidgetConfig as WidgetConfig,
)
from oridecon.admin.dashboard.widget_defs import WidgetType as WidgetType
from oridecon.admin.dashboard.widget_types import ConfigField as ConfigField
from oridecon.contracts.admin.types import (
    DashboardWidgetDefinition as DashboardWidgetDefinition,
)
from oridecon.contracts.admin.types import WidgetCategory as WidgetCategory
from oridecon.contracts.admin.types import WidgetSize as WidgetSize

__all__ = [
    "ConfigField",
    "DashboardConfig",
    "DashboardWidgetDefinition",
    "IDashboardStore",
    "IWidget",
    "InMemoryDashboardStore",
    "WidgetCategory",
    "WidgetConfig",
    "WidgetRegistry",
    "WidgetSize",
    "WidgetType",
    "render_dashboard_widgets",
    "render_widget_config_popup",
]
