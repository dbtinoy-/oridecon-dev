"""Oridecon UI — HTMX/htpy component library for oridecon web applications.

Provides general-purpose UI components, layouts, and utilities for building
server-rendered HTMX applications.
"""

from __future__ import annotations

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from typing import TYPE_CHECKING, Any

from oridecon.ui.constants import __version__ as __version__
from oridecon.ui.exports.lazy import LAZY_IMPORTS as _LAZY_IMPORTS
from oridecon.ui.exports.public import __all__

if TYPE_CHECKING:
    from oridecon.ui.accessibility import (
        AriaAttrs,
        AriaLive,
        AriaRole,
        SkipLink,
        announce,
        announce_action_complete,
        announce_selection_change,
        announce_table_update,
        button_aria,
        cell_aria,
        dialog_aria,
        header_aria,
        keyboard_navigation_script,
        live_region_aria,
        row_aria,
        search_aria,
        tab_aria,
        table_aria,
        tabpanel_aria,
    )
    from oridecon.ui.actions import (
        Action,
        ActionTarget,
        BulkAction,
        CreateAction,
        DeleteAction,
        DeleteBulkAction,
        EditAction,
        ExportAction,
        ExportBulkAction,
        ViewAction,
    )
    from oridecon.ui.charts import (
        AreaChart,
        BarChart,
        ChartConfig,
        ChartDataPoint,
        ChartType,
        LineChart,
        MiniBar,
        PieChart,
        Sparkline,
    )
    from oridecon.ui.columns import (
        BadgeColumn,
        BooleanColumn,
        Column,
        CurrencyColumn,
        DateColumn,
        ImageColumn,
        ListColumn,
        TextColumn,
    )
    from oridecon.ui.config import (
        BaseLayoutConfig,
        DebounceConfig,
        FooterConfig,
        HeadConfig,
        HTMLDocumentConfig,
        ToastConfig,
        UIConfig,
    )
    from oridecon.ui.core.base import (
        Component,
        Element,
        RawHTML,
        el,
        fragment,
        raw,
        render_to_string,
    )
    from oridecon.ui.core.context import (
        UIContext,
        get_ui_context,
        reset_ui_context,
        set_ui_context,
    )
    from oridecon.ui.core.js import js_json, js_string
    from oridecon.ui.core.render_context import (
        RenderContext,
        RenderScope,
        get_render_context,
        get_render_scope,
        render_context,
    )
    from oridecon.ui.core.trusted_html import (
        TrustedHTML,
        trusted_html,
        trusted_static_script,
        trusted_svg_icon,
        trusted_template_output,
    )
    from oridecon.ui.core.url import is_safe_navigation_url
    from oridecon.ui.core.zones import SwapMode, Zone, Zones
    from oridecon.ui.decorators import component
    from oridecon.ui.di.provider import UIProvider
    from oridecon.ui.exceptions import (
        ErrorCategory,
        ErrorResponse,
        FieldError,
        UIError,
        htmx_error_response,
        not_found_error,
        permission_error,
        render_validation_errors,
        server_error,
        timeout_error,
        validation_error,
    )
    from oridecon.ui.exports.atoms import *  # noqa: F403
    from oridecon.ui.exports.layouts import *  # noqa: F403
    from oridecon.ui.exports.molecules import *  # noqa: F403
    from oridecon.ui.htmx import HTMXAttrs, HTMXAttrsBuilder, helpers, htmx, sse
    from oridecon.ui.module import UIModule
    from oridecon.ui.organisms.activity_feed import ActivityFeed
    from oridecon.ui.organisms.filter_drawer import FilterDrawer
    from oridecon.ui.organisms.forms import Form
    from oridecon.ui.organisms.live_polling import AutoRefreshWidget, LiveDataTable
    from oridecon.ui.organisms.notification_bell import NotificationBell
    from oridecon.ui.organisms.repeater import Repeater
    from oridecon.ui.organisms.simple_pagination import SimplePagination
    from oridecon.ui.organisms.slide_over import SlideOver
    from oridecon.ui.organisms.sortable_list import SortableRecordList
    from oridecon.ui.organisms.systembox import SystemBox
    from oridecon.ui.organisms.task_progress import TaskProgress
    from oridecon.ui.organisms.userbox import UserBox
    from oridecon.ui.performance.observability import (
        MetricProtocol,
        MetricsCollector,
        MetricType,
    )
    from oridecon.ui.performance.performance import (
        RenderCache,
        RequestCoalescer,
        ResponseOptimizer,
        add_htmx_timing_header,
        cached_render,
        debounced_search_attrs,
        infinite_scroll_trigger,
        lazy_load_placeholder,
        measure_render_time,
        optimize_htmx_response,
    )
    from oridecon.ui.protocols import RenderableProtocol
    from oridecon.ui.state import TableState
    from oridecon.ui.styles.theme import shadcn_css


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib

        module = importlib.import_module(_LAZY_IMPORTS[name])
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))
