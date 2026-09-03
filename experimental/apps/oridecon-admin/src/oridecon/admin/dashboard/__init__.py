"""Dashboard assembly — collects and composes dashboard surfaces from contributors."""

from __future__ import annotations

from oridecon.admin.dashboard.assembler import DashboardAssembler
from oridecon.admin.dashboard.chart_widget import ChartWidget
from oridecon.admin.dashboard.stats_widget import StatsOverviewWidget, StatTrend
from oridecon.admin.dashboard.widget_types import ConfigField
from oridecon.admin.dashboard.widgets import (
    DashboardConfig,
    InMemoryDashboardStore,
    WidgetConfig,
    WidgetRegistry,
    WidgetType,
)

__all__ = [
    "ChartWidget",
    "ConfigField",
    "DashboardAssembler",
    "DashboardConfig",
    "InMemoryDashboardStore",
    "StatTrend",
    "StatsOverviewWidget",
    "WidgetConfig",
    "WidgetRegistry",
    "WidgetType",
]
