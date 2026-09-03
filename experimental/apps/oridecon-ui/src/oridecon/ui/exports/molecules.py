"""Static molecule re-exports for the ``oridecon.ui`` public surface.

Type-checker only: the top-level package resolves names lazily via
``__getattr__`` at runtime, so these imports never execute eagerly.
"""

# File-level suppression: this module is an intentional lazy-re-export
# manifest — imports live under TYPE_CHECKING on purpose.
# ruff: noqa: TC004

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oridecon.ui.molecules.action_button import ActionButton
    from oridecon.ui.molecules.alert import Alert
    from oridecon.ui.molecules.breadcrumbs import Breadcrumbs
    from oridecon.ui.molecules.builder import Builder
    from oridecon.ui.molecules.card import Card
    from oridecon.ui.molecules.column_visibility_switcher import (
        ColumnVisibilitySwitcher,
    )
    from oridecon.ui.molecules.data_table_client_logic import DataTableScriptRenderer
    from oridecon.ui.molecules.date_hierarchy import DateHierarchyFilter
    from oridecon.ui.molecules.date_range_filter import DateRangeFilter
    from oridecon.ui.molecules.density_switcher import DensitySwitcher
    from oridecon.ui.molecules.dropdown import Dropdown
    from oridecon.ui.molecules.empty_state import EmptyState
    from oridecon.ui.molecules.error_state import ErrorState
    from oridecon.ui.molecules.filter_dropdown import FilterDropdown
    from oridecon.ui.molecules.form_actions import FormActions
    from oridecon.ui.molecules.form_field import FormField
    from oridecon.ui.molecules.infolist import (
        InfolistEntry,
        InfolistEntryType,
        InfolistWidget,
    )
    from oridecon.ui.molecules.inline_edit_cell import InlineEditCell
    from oridecon.ui.molecules.input_group import InputGroup
    from oridecon.ui.molecules.jump_to_page import JumpToPage
    from oridecon.ui.molecules.layout_switcher import LayoutSwitcher
    from oridecon.ui.molecules.loading_overlay import LoadingOverlay
    from oridecon.ui.molecules.metric_card import MetricCard
    from oridecon.ui.molecules.modal import Modal
    from oridecon.ui.molecules.page_size_selector import PageSizeSelector
    from oridecon.ui.molecules.pagination_links import PaginationLinks
    from oridecon.ui.molecules.popover import Popover
    from oridecon.ui.molecules.realtime import LiveCounter, RealTimeFeed
    from oridecon.ui.molecules.rich_select import RichSelect
    from oridecon.ui.molecules.section import Section
    from oridecon.ui.molecules.simple_alert import SimpleAlert
    from oridecon.ui.molecules.sort_switcher import SortSwitcher
    from oridecon.ui.molecules.stack import Stack
    from oridecon.ui.molecules.stat_card import StatCard
    from oridecon.ui.molecules.tab_group import Tab, TabGroup
    from oridecon.ui.molecules.table_pagination import TablePagination
    from oridecon.ui.molecules.tabs import TabPanel, Tabs
    from oridecon.ui.molecules.toast import (
        InlineToast,
        ServerToastChannel,
        ToastData,
        ToastType,
        flash_to_toast,
    )
    from oridecon.ui.molecules.toggle import ToggleIcon
    from oridecon.ui.molecules.virtual_scroll import (
        InfiniteScrollTrigger,
        VirtualScroll,
    )

    __all__ = (
        "ActionButton",
        "Alert",
        "Breadcrumbs",
        "Builder",
        "Card",
        "ColumnVisibilitySwitcher",
        "DataTableScriptRenderer",
        "DensitySwitcher",
        "DateHierarchyFilter",
        "DateRangeFilter",
        "Dropdown",
        "EmptyState",
        "ErrorState",
        "FilterDropdown",
        "FormActions",
        "FormField",
        "InfolistEntry",
        "InfolistEntryType",
        "InfolistWidget",
        "InlineEditCell",
        "InputGroup",
        "JumpToPage",
        "LayoutSwitcher",
        "LoadingOverlay",
        "MetricCard",
        "Modal",
        "PageSizeSelector",
        "PaginationLinks",
        "Popover",
        "LiveCounter",
        "RealTimeFeed",
        "RichSelect",
        "Section",
        "SimpleAlert",
        "SortSwitcher",
        "Stack",
        "StatCard",
        "Tab",
        "TabGroup",
        "TablePagination",
        "TabPanel",
        "Tabs",
        "InlineToast",
        "ServerToastChannel",
        "ToastData",
        "ToastType",
        "flash_to_toast",
        "ToggleIcon",
        "InfiniteScrollTrigger",
        "VirtualScroll",
    )
