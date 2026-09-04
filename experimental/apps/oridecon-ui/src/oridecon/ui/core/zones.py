"""
Zone-Based UI Architecture for Oridecon Admin.

A Zone is a DOM subtree with:
- A unique ID
- A defined responsibility
- Clear rules about what can swap it
- A contract for what it contains

This module provides the central registry of all UI zones, replacing
the scattered IDs in consts.py with a structured, type-safe system.
"""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar

from oridecon.ui.core.render_context import RenderScope, get_render_context, get_render_scope


class SwapMode(str, Enum):
    """Valid HTMX swap modes."""

    OUTER_HTML = "outerHTML"
    INNER_HTML = "innerHTML"
    BEFORE_END = "beforeend"
    AFTER_BEGIN = "afterbegin"
    NONE = "none"


@dataclass(slots=True)
class _ZoneResolution:
    scope: RenderScope
    table_key: str
    ids: dict[str, str]


_active_zone_resolution: ContextVar[_ZoneResolution | None] = ContextVar(
    "oridecon_ui_zone_resolution",
    default=None,
)


@dataclass(frozen=True, init=False)
class Zone:
    """Semantic UI region whose DOM ID can be resolved for one render scope.

    ``id`` remains the compatibility ID outside a scoped component render. A
    table render activates response-local IDs for its table roles, so existing
    controls resolve the same target without process-global DOM identities.
    """

    _default_id: str
    role: str
    description: str
    swappable: bool
    swap_mode: SwapMode
    preserve_alpine: bool
    oob_only: bool

    def __init__(
        self,
        id: str,
        description: str,
        swappable: bool,
        swap_mode: SwapMode,
        preserve_alpine: bool = False,
        oob_only: bool = False,
        *,
        role: str | None = None,
    ) -> None:
        object.__setattr__(self, "_default_id", id)
        object.__setattr__(self, "role", role or id)
        object.__setattr__(self, "description", description)
        object.__setattr__(self, "swappable", swappable)
        object.__setattr__(self, "swap_mode", swap_mode)
        object.__setattr__(self, "preserve_alpine", preserve_alpine)
        object.__setattr__(self, "oob_only", oob_only)

    @property
    def id(self) -> str:
        """Return the active response-local ID or the compatibility default."""
        resolution = _active_zone_resolution.get()
        if resolution is None:
            return self._default_id
        return resolution.ids.get(self.role, self._default_id)

    @property
    def default_id(self) -> str:
        """Return the process-stable compatibility ID used outside a scope."""
        return self._default_id

    @property
    def selector(self) -> str:
        """Return the CSS selector for this zone."""
        return f"#{self.id}"

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return f"Zone({self.id!r})"


class Zones:
    """
    Central registry of all UI zones.

    This class provides a single source of truth for all targetable
    regions in the admin UI. Components should reference these zones
    rather than hardcoding IDs.

    Zone Hierarchy:

        TABLE (root scope)
        ├── TOOLBAR (switchers, header actions) - OOB only
        ├── SEARCH (search input) - never swap
        ├── FILTERS (filter bar) - OOB only
        └── DATA (rows + pagination) - most common target

        DASHBOARD (dashboard page)
        └── WIDGET_CONTAINER (per-widget lazy-load target)

        MODAL (global, outside table)
        SLIDE_OVER (global, outside table)
        FLASH (toast notifications)

    Usage:
        from oridecon.ui.core.zones import Zones

        attrs = {
            "hx-target": Zones.DATA.selector,
            "hx-swap": Zones.DATA.swap_mode.value,
        }
    """

    # === Primary Zones ===

    TABLE: ClassVar[Zone] = Zone(
        id="oridecon-table",
        role="table",
        description="Root table scope with Alpine.js state. Target for full refresh only.",
        swappable=True,
        swap_mode=SwapMode.OUTER_HTML,
        preserve_alpine=False,  # Full refresh reinitializes Alpine
    )

    DATA: ClassVar[Zone] = Zone(
        id="table-data",
        description="Data content + pagination. Most common target for data updates.",
        swappable=True,
        swap_mode=SwapMode.INNER_HTML,
        preserve_alpine=True,  # Parent Alpine scope preserved
    )

    # === Secondary Zones (typically OOB) ===

    TOOLBAR: ClassVar[Zone] = Zone(
        id="table-toolbar",
        description="Switchers and header actions. Update via OOB only.",
        swappable=True,
        swap_mode=SwapMode.OUTER_HTML,
        oob_only=True,
    )

    FILTERS: ClassVar[Zone] = Zone(
        id="table-filters",
        description="Filter controls. Update via OOB when filter options change.",
        swappable=True,
        swap_mode=SwapMode.OUTER_HTML,
        oob_only=True,
    )

    SCOPE_TABS: ClassVar[Zone] = Zone(
        id="table-scope-tabs",
        description="Active/trash table scope controls. Updated via OOB swaps.",
        swappable=True,
        swap_mode=SwapMode.OUTER_HTML,
        oob_only=True,
    )

    PAGINATION: ClassVar[Zone] = Zone(
        id="table-pagination",
        description="Pagination controls owned by one table instance.",
        swappable=False,
        swap_mode=SwapMode.NONE,
    )

    SELECT_ALL: ClassVar[Zone] = Zone(
        id="table-select-all",
        description="Select-all control owned by one table instance.",
        swappable=False,
        swap_mode=SwapMode.NONE,
    )

    # === Non-Swappable Zones ===

    SEARCH: ClassVar[Zone] = Zone(
        id="table-search",
        description="Search input. Never swap to preserve focus and input state.",
        swappable=False,
        swap_mode=SwapMode.NONE,
    )

    # === Global Zones (outside table scope) ===

    MODAL: ClassVar[Zone] = Zone(
        id="modal-container",
        description="Modal dialogs. Target for modal actions.",
        swappable=True,
        swap_mode=SwapMode.INNER_HTML,
    )

    SLIDE_OVER: ClassVar[Zone] = Zone(
        id="slide-over-container",
        description="Side panel forms. Target for edit/create actions.",
        swappable=True,
        swap_mode=SwapMode.INNER_HTML,
    )

    FLASH: ClassVar[Zone] = Zone(
        id="flash-container",
        description="Toast/flash notifications.",
        swappable=True,
        swap_mode=SwapMode.INNER_HTML,
    )

    # === Dashboard Zones ===

    DASHBOARD_GRID: ClassVar[Zone] = Zone(
        id="dashboard-grid",
        description="Main dashboard widget grid container. Swappable for full dashboard refresh.",
        swappable=True,
        swap_mode=SwapMode.INNER_HTML,
    )

    WIDGET_CONTAINER: ClassVar[Zone] = Zone(
        id="widget-container",
        description="Individual widget card. Used for per-widget HTMX lazy-load and refresh.",
        swappable=True,
        swap_mode=SwapMode.INNER_HTML,
        preserve_alpine=True,
    )

    # === Bulk Action Zone ===

    BULK_BAR: ClassVar[Zone] = Zone(
        id="table-bulk-bar",
        description="Bulk action buttons shown when items selected. Controlled by Alpine.",
        swappable=False,  # Visibility controlled by Alpine x-show
        swap_mode=SwapMode.NONE,
    )

    _TABLE_SCOPED: ClassVar[tuple[Zone, ...]] = (
        TABLE,
        DATA,
        TOOLBAR,
        FILTERS,
        SCOPE_TABS,
        PAGINATION,
        SELECT_ALL,
        SEARCH,
        BULK_BAR,
    )

    @classmethod
    def _table_ids(cls, scope: RenderScope, table_key: str) -> dict[str, str]:
        """Claim all table-role IDs from one response-local render scope."""
        return {
            zone.role: scope.id(zone.role, key=table_key) for zone in cls._TABLE_SCOPED
        }

    @classmethod
    @contextmanager
    def table_scope(
        cls,
        scope: RenderScope,
        table_key: str,
    ) -> Iterator[dict[str, str]]:
        """Resolve table roles for ``table_key`` during one component render."""
        resolved = cls._table_ids(scope, table_key)
        resolution = _ZoneResolution(
            scope=scope,
            table_key=table_key,
            ids=resolved,
        )
        token = _active_zone_resolution.set(resolution)
        try:
            yield resolved
        finally:
            _active_zone_resolution.reset(token)

    @classmethod
    def claim_table_id(cls, role: str, *, key: str | None = None) -> str:
        """Claim a deterministic child ID inside the active table scope."""
        resolution = _active_zone_resolution.get()
        if resolution is None:
            raise RuntimeError(
                "A table child ID requires an active Zones.table_scope()"
            )
        stable_key = resolution.table_key
        if key is not None:
            stable_key = f"{stable_key}-{key}"
        return resolution.scope.id(role, key=stable_key)

    @classmethod
    def table_zone_id(cls, zone: Zone, *, table_key: str) -> str:
        """Resolve one stable table ID for request/fragment routing code.

        Inside an active response render scope this returns exactly the ID
        the table will render, so HTMX ``HX-Target`` values computed at
        routing time match the emitted DOM. Outside a request (standalone
        helpers/tests) a deterministic fallback scope is used.
        """
        if zone not in cls._TABLE_SCOPED:
            raise ValueError(f"{zone!r} is not scoped to a data table")
        return cls._table_ids(get_render_scope(), table_key)[zone.role]

    @classmethod
    def data_refresh_oob_select(cls) -> str:
        """Selectors an ``hx-select`` data swap must additionally preserve.

        ``hx-select`` rebuilds the swap from ``querySelectorAll(select)``
        alone, so any ``hx-swap-oob`` element sitting outside the selected
        subtree is silently dropped. A data-zone refresh returns exactly
        that shape -- ``#table-data`` plus sibling OOB fragments for the
        toolbar switchers and the Active/Trash tabs -- so without pairing
        ``hx-select`` with ``hx-select-oob`` the rows update while every
        control around them keeps rendering the previous state.

        Returns:
            Comma-separated selector list for ``hx-select-oob``.
        """
        return f"#{cls.TOOLBAR.id}-switchers,{cls.SCOPE_TABS.selector}"

    @classmethod
    def all_zones(cls) -> list[Zone]:
        """Return all registered zones."""
        return [
            cls.TABLE,
            cls.DATA,
            cls.TOOLBAR,
            cls.FILTERS,
            cls.SCOPE_TABS,
            cls.PAGINATION,
            cls.SELECT_ALL,
            cls.SEARCH,
            cls.MODAL,
            cls.SLIDE_OVER,
            cls.FLASH,
            cls.DASHBOARD_GRID,
            cls.WIDGET_CONTAINER,
            cls.BULK_BAR,
        ]

    @classmethod
    def swappable(cls) -> list[Zone]:
        """Return all zones that can be targeted by HTMX swaps."""
        return list(filter(lambda z: z.swappable, cls.all_zones()))

    @classmethod
    def get_by_id(cls, zone_id: str) -> Zone | None:
        """
        Look up a zone by its ID.

        Returns None if no zone with that ID exists.
        """
        for zone in cls.all_zones():
            if zone_id in (zone.id, zone.default_id):
                return zone
        return None

    @classmethod
    def get_by_selector(cls, selector: str) -> Zone | None:
        """
        Look up a zone by its CSS selector.

        Handles both "#zone-id" and "zone-id" formats.
        """
        # Normalize selector
        zone_id = selector[1:] if selector.startswith("#") else selector
        return cls.get_by_id(zone_id)
