"""Dashboard controller."""

from __future__ import annotations

from collections import defaultdict
import contextvars
from datetime import datetime
from typing import Any

from starlette.requests import Request
from starlette.responses import HTMLResponse

from oridecon.admin.controllers.base import AdminController
from oridecon.admin.dashboard.assembler import DashboardAssembler
from oridecon.admin.dashboard.page_filters import (
    applied_from_query,
    read_page_filters,
    render_page_filter_form,
    save_page_filters,
)
from oridecon.admin.dashboard.widgets import WidgetRegistry
from oridecon.admin.engine.renderer import AdminRenderer
from oridecon.contracts.admin.types import PageFilterField, WidgetSize
from oridecon.contracts.web import get
from oridecon.di.decorators import inject
from oridecon.ui import RenderScope, el, get_render_scope, js_string, trusted_html

# Request-scoped in-memory dict, isolated per async context.
_request_cache_var: contextvars.ContextVar[dict[str, Any] | None] = (
    contextvars.ContextVar(
        "admin_request_cache",
        default=None,
    )
)


def _get_request_cache() -> dict[str, Any]:
    """Return the request-scoped cache dict for the current async context."""
    cache = _request_cache_var.get()
    return cache if cache is not None else {}


def _dashboard_dnd_nodes(
    *,
    scope: RenderScope,
    dashboard_key: str,
    grid_id: str,
    reorder_url: str,
    csrf_token: str,
) -> tuple[Any, Any]:
    """Build scoped layout controls and their generated client controller."""
    controls_id = scope.id("dnd-controls", key=dashboard_key)
    status_id = scope.id("layout-status", key=dashboard_key)
    save_id = scope.id("save-layout", key=dashboard_key)
    controls = el(
        "div",
        el(
            "span",
            id=status_id,
            role="status",
            aria_live="polite",
            class_="text-xs text-muted-foreground",
        ),
        el(
            "button",
            el("span", "✦", aria_hidden=True),
            " Save layout",
            id=save_id,
            type="button",
            class_=(
                "hidden inline-flex items-center gap-2 rounded-lg border "
                "border-primary/20 bg-primary/10 px-3 py-2 text-sm font-medium "
                "text-primary transition hover:bg-primary/15 "
                "focus-visible:outline-none focus-visible:ring-2 "
                "focus-visible:ring-ring focus-visible:ring-offset-2"
            ),
        ),
        id=controls_id,
        data_csrf_token=csrf_token,
        class_=("dashboard-dnd-controls mt-1 flex items-center justify-end gap-3"),
    )
    script = f"""
(function() {{
  var controllerKey = {js_string(controls_id)};
  var registry = window.__orideconDashboardControllers;
  if (!(registry instanceof Map)) {{
    registry = window.__orideconDashboardControllers = new Map();
  }}
  var previous = registry.get(controllerKey);
  if (previous) previous.destroy();

  var grid = null;
  var saveBtn = document.getElementById({js_string(save_id)});
  var status = document.getElementById({js_string(status_id)});
  var controls = document.getElementById({js_string(controls_id)});
  var sortableInstance = null;
  var saveRequest = null;
  var destroyed = false;
  var controller = {{destroy: destroy}};

  function setStatus(message) {{
    if (status && status.isConnected) status.textContent = message || '';
  }}

  function initSortable() {{
    if (destroyed) return;
    var nextGrid = document.getElementById({js_string(grid_id)});
    if (nextGrid !== grid) {{
      if (sortableInstance) sortableInstance.destroy();
      sortableInstance = null;
      grid = nextGrid;
    }}
    if (!grid || sortableInstance || typeof Sortable === 'undefined') return;
    sortableInstance = new Sortable(grid, {{
      animation: 150,
      handle: '.widget-card',
      onEnd: function() {{
        if (saveBtn) saveBtn.classList.remove('hidden');
        setStatus('Layout changed');
      }}
    }});
  }}

  async function saveLayout() {{
    initSortable();
    if (!sortableInstance || !grid || !saveBtn) return;
    var order = Array.from(grid.querySelectorAll('.widget-card')).map(function(card) {{
      return card.dataset.widgetName;
    }});
    if (saveRequest) saveRequest.abort();
    var request = new AbortController();
    saveRequest = request;
    saveBtn.disabled = true;
    setStatus('Saving layout…');
    try {{
      var csrf = controls ? controls.dataset.csrfToken || '' : '';
      var resp = await fetch({js_string(reorder_url)}, {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json', 'X-CSRF-Token': csrf}},
        body: JSON.stringify({{order: order}}),
        signal: request.signal
      }});
      if (!resp.ok) throw new Error('save_failed');
      if (saveRequest === request) {{
        saveBtn.classList.add('hidden');
        setStatus('Layout saved');
      }}
    }} catch (error) {{
      if (error.name !== 'AbortError' && saveRequest === request) {{
        setStatus('Could not save layout. Try again.');
      }}
    }} finally {{
      if (saveRequest === request) {{
        saveRequest = null;
        if (saveBtn.isConnected) saveBtn.disabled = false;
      }}
    }}
  }}

  function afterSwap() {{
    if (!controls || !controls.isConnected) {{
      destroy();
      return;
    }}
    initSortable();
  }}

  function beforeCleanup(event) {{
    var target = event.detail && event.detail.elt || event.target;
    if (target && controls && (target === controls ||
        (typeof target.contains === 'function' && target.contains(controls)))) destroy();
  }}

  function destroy() {{
    if (destroyed) return;
    destroyed = true;
    document.body.removeEventListener('htmx:afterSwap', afterSwap);
    document.body.removeEventListener('htmx:beforeCleanupElement', beforeCleanup);
    window.removeEventListener('pagehide', destroy);
    if (saveBtn) saveBtn.removeEventListener('click', saveLayout);
    if (saveRequest) saveRequest.abort();
    if (sortableInstance) sortableInstance.destroy();
    if (registry.get(controllerKey) === controller) registry.delete(controllerKey);
  }}

  registry.set(controllerKey, controller);
  document.body.addEventListener('htmx:afterSwap', afterSwap);
  document.body.addEventListener('htmx:beforeCleanupElement', beforeCleanup);
  window.addEventListener('pagehide', destroy, {{once: true}});
  if (saveBtn) saveBtn.addEventListener('click', saveLayout);
  initSortable();
}})();
"""
    script_node = el(
        "script",
        trusted_html(script, source="generated dashboard layout controller"),
    )
    return controls, script_node


@inject
class DashboardController(AdminController):
    """Controller for managing and viewing dashboards."""

    prefix = ""

    # Declared page-level dashboard filter schema.
    # Subclass to declare filters; the dashboard renders an apply/reset bar
    # and propagates the values to widget fetch URLs.
    page_filters: list[PageFilterField] = []

    def __init__(
        self,
        renderer: AdminRenderer,
        assembler: DashboardAssembler | None = None,
        widget_registry: WidgetRegistry | None = None,
    ):
        super().__init__(renderer)
        self.assembler = assembler
        self.widget_registry = widget_registry
        self._settings_service: Any = None

    def _size_to_grid_cols(self, size: WidgetSize) -> int:
        """Map WidgetSize to CSS grid column span."""
        mapping = {
            WidgetSize.SMALL: 1,
            WidgetSize.MEDIUM: 2,
            WidgetSize.LARGE: 3,
            WidgetSize.FULL: 4,
        }
        return mapping.get(size, 1)

    @get("/")
    async def index(self, request: Request) -> HTMLResponse:
        """Render the main dashboard overview."""
        from oridecon.admin.ui.organisms.dashboard.widgets import (
            ActivityFeed,
            ActivityItem,
            HealthEntry,
            Stat,
            StatCardGrid,
            SystemHealthWidget,
        )

        await self._ensure_csrf_token(request)
        dashboard_id = request.query_params.get("id", "default")
        from oridecon.admin.resources.urls import admin_prefix_from_request

        admin_prefix = admin_prefix_from_request(request)
        state_csrf_token = getattr(getattr(request, "state", None), "csrf_token", "")
        csrf_token = state_csrf_token if isinstance(state_csrf_token, str) else ""
        request_user = getattr(getattr(request, "state", None), "user", None)
        if isinstance(request_user, dict):
            display_name = (
                request_user.get("name")
                or request_user.get("username")
                or request_user.get("email")
                or "there"
            )
        else:
            display_name = (
                getattr(request_user, "name", None)
                or getattr(request_user, "username", None)
                or "there"
            )
        if not isinstance(display_name, str) or not display_name.strip():
            display_name = "there"
        dashboard_title = (
            "Overview"
            if dashboard_id == "default"
            else dashboard_id.replace("_", " ").replace("-", " ").title()
        )
        # With no resources registered the call to action had nowhere to go:
        # it linked to admin_prefix, the page already being viewed. Offer the
        # link only when it leads somewhere else.
        resource_names = self._get_resource_list(request)
        primary_resource_url = (
            f"{admin_prefix}/{resource_names[0]}" if resource_names else None
        )
        primary_resource_label = "Browse resources"

        # Page-level filter state: schema defaults → session → query params
        filter_state: dict[str, Any] = {}
        if self.page_filters:
            filter_state = read_page_filters(request, "dashboard", self.page_filters)
            if applied_from_query(request, self.page_filters):
                save_page_filters(request, "dashboard", filter_state)

        breadcrumbs = self.generate_breadcrumbs(
            ("Home", f"{admin_prefix}/"),
            current="Dashboard",
        )

        # Use assembler widgets when available; fall back to default overview
        if self.assembler:
            user = getattr(getattr(request, "state", None), "user", None)
            contributor_widgets = list(await self.assembler.get_all_widgets(user=user))
        else:
            contributor_widgets = []

        # Load user preferences for widget visibility and ordering
        widget_prefs = (
            await self._settings_service.get_widget_prefs("default", "default")
            if self._settings_service
            else {}
        )
        # Filter and sort widgets. No saved prefs means everything is on.
        if "enabled" in widget_prefs:
            enabled_set = set(widget_prefs["enabled"])
            contributor_widgets = [
                w for w in contributor_widgets if w.name in enabled_set
            ]
        custom_order = widget_prefs.get("order", {})
        if custom_order:
            contributor_widgets.sort(key=lambda w: custom_order.get(w.name, w.order))

        dashboard_scope = get_render_scope().child("dashboard")
        grid_id = dashboard_scope.id("grid", key=dashboard_id)

        if contributor_widgets and self.widget_registry is not None:
            # Render HTMX lazy-load widget cards via the registry, annotating
            # each fetch URL with the current page filter values
            contributor_markup = self.widget_registry.trusted_contributor_widgets(
                contributor_widgets,
                page_filters=filter_state,
                admin_prefix=admin_prefix,
            )
            widgets_section = el(
                "div",
                contributor_markup,
                id=grid_id,
                class_="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4",
            )
        elif contributor_widgets and self.widget_registry is None:
            # Fallback: basic title rendering when no registry is available
            fallback_widgets: list[Any] = []
            for w in contributor_widgets:
                fallback_widgets.append(
                    el(
                        "div",
                        el("h3", w.title, class_="font-semibold"),
                        class_="bg-card rounded-lg p-4 shadow",
                    )
                )
            widgets_section = el(
                "div",
                *fallback_widgets,
                id=grid_id,
                class_="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4",
            )
        else:
            # Provide a beautiful default overview dashboard
            default_stats = [
                Stat(
                    label="Resources",
                    value=str(len(resource_names)),
                    icon="layers",
                    color="blue",
                    description="Registered admin resources",
                ),
                Stat(
                    label="Active Now",
                    value="—",
                    icon="users",
                    color="green",
                    description="Live sessions",
                ),
                Stat(
                    label="Actions Today",
                    value="—",
                    icon="zap",
                    color="primary",
                    description="Admin operations today",
                ),
                Stat(
                    label="Errors (24h)",
                    value="—",
                    icon="alert-triangle",
                    color="red",
                    description="Last 24 hours",
                ),
            ]
            default_activity: list[ActivityItem] = []
            default_health = [
                HealthEntry(name="Admin API", status="ok"),
            ]

            from oridecon.admin.dashboard.chart_widget import ChartWidget
            from oridecon.ui import ChartType

            resources_chart = ChartWidget(
                title="Registered Resources",
                chart_type=ChartType.BAR,
                data_source=(f"{admin_prefix_from_request(request)}/widgets/resources"),
                description=("Every admin resource registered with this application."),
                col_span=3,
                refresh_interval=120,
            )
            chart_row = el(
                "div",
                resources_chart,
                class_="grid grid-cols-1 lg:grid-cols-3 gap-4",
            )

            bottom_row = el(
                "div",
                el(
                    "div",
                    ActivityFeed(default_activity, title="Recent Activity"),
                    class_="lg:col-span-2",
                ),
                SystemHealthWidget(default_health),
                class_="grid grid-cols-1 lg:grid-cols-3 gap-4",
            )
            widgets_section = el(
                "div",
                StatCardGrid(
                    default_stats,
                    cols=4,
                    data_source=(f"{admin_prefix_from_request(request)}/widgets/stats"),
                    refresh_interval=120,
                    aria_label="Overview statistics",
                ),
                chart_row,
                bottom_row,
                id=grid_id,
                class_="space-y-6",
            )

        # Drag-and-drop only applies to contributor cards, which are direct
        # grid children with stable ``data-widget-name`` identities.
        dnd_nodes: tuple[Any, ...] = ()
        if contributor_widgets and self.widget_registry is not None:
            dnd_nodes = _dashboard_dnd_nodes(
                scope=dashboard_scope,
                dashboard_key=dashboard_id,
                grid_id=grid_id,
                reorder_url=f"{admin_prefix}/core/widgets/reorder",
                csrf_token=csrf_token,
            )

        customize_btn = el(
            "button",
            "⚙ Customize Dashboard",
            **{
                "hx-get": f"{admin_prefix}/core/widgets/customize",
                "hx-target": "#slide-over-container",
                "hx-swap": "innerHTML",
                "hx-push-url": "false",
            },
            class_="text-sm bg-muted hover:bg-muted px-3 py-1.5 rounded border border-border cursor-pointer",
        )

        filter_form = (
            render_page_filter_form(self.page_filters, filter_state, f"{admin_prefix}/")
            if self.page_filters
            else None
        )

        dashboard_header = el(
            "section",
            el(
                "div",
                el(
                    "p",
                    "Workspace overview",
                    class_="text-xs font-semibold uppercase tracking-[0.18em] text-primary",
                ),
                el(
                    "h1",
                    f"Welcome back, {display_name}",
                    class_="mt-2 text-2xl font-semibold tracking-tight text-foreground sm:text-3xl",
                ),
                el(
                    "p",
                    f"A calm, current view of your {dashboard_title.lower()} operations.",
                    class_="mt-2 max-w-2xl text-sm leading-6 text-muted-foreground",
                ),
            ),
            el(
                "div",
                # Not a Badge: this chip carries a leading status dot, and
                # Badge renders text only. No role="status" either -- the
                # label is static, so announcing it would add noise without
                # reporting any change.
                el(
                    "span",
                    el("span", class_="h-2 w-2 rounded-full bg-success"),
                    "Live workspace",
                    class_="inline-flex items-center gap-2 rounded-full border border-success/20 bg-success/10 px-3 py-1.5 text-xs font-medium text-success",
                ),
                customize_btn,
                el(
                    "a",
                    primary_resource_label,
                    href=primary_resource_url,
                    class_="inline-flex items-center justify-center rounded-lg bg-primary px-3.5 py-2 text-sm font-medium text-primary-foreground shadow-sm transition hover:bg-primary/90 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2",
                )
                if primary_resource_url
                else None,
                class_="flex flex-wrap items-center gap-3 sm:justify-end",
            ),
            class_="dashboard-hero flex flex-col gap-5 rounded-2xl border border-border/70 bg-card/80 p-5 shadow-sm backdrop-blur sm:flex-row sm:items-end sm:justify-between sm:p-7",
        )

        content = el(
            "div",
            dashboard_header,
            filter_form,
            widgets_section,
            *dnd_nodes,
            class_="dashboard-view dashboard-page space-y-6",
        )

        return await self._render_with_flash(
            request, content, f"Dashboard: {dashboard_id}", breadcrumbs
        )

    @get("/widgets/resources")
    async def resources_chart(self, request: Request) -> HTMLResponse:
        """Render the registered-resources bar chart fragment.

        HTMX target for the default dashboard's ``ChartWidget``.  Returns an
        empty state when no resources are registered so the card body never
        renders a blank canvas.
        """
        from oridecon.admin.dashboard.content_renderer import render_chart_fragment
        from oridecon.contracts.admin.widget_content import ChartPoint
        from oridecon.ui import EmptyState, render_to_string

        resources = self._get_resource_list(request)
        if not resources:
            return HTMLResponse(
                render_to_string(
                    EmptyState(
                        title="No resources",
                        message="No admin resources are registered yet.",
                    )
                )
            )

        points = [ChartPoint(label=name, value=1) for name in resources]
        return HTMLResponse(render_chart_fragment("bar", points))

    @get("/widgets/stats")
    async def overview_stats(self, request: Request) -> HTMLResponse:
        """Render the default dashboard stat-grid fragment.

        HTMX target for ``StatsOverviewWidget(data_source=...)`` cards: the
        default overview's four headline stats, served through the shared
        content dispatcher so tone/delta rendering stays consistent with
        contributor-supplied stats.
        """
        from oridecon.admin.dashboard.content_renderer import render_stat_fragment
        from oridecon.contracts.admin.widget_content import Stat, Tone

        resources = self._get_resource_list(request)
        stats = [
            Stat(label="Resources", value=str(len(resources)), tone=Tone.PRIMARY),
            Stat(label="Active Now", value="—", tone=Tone.DEFAULT),
            Stat(label="Actions Today", value="—", tone=Tone.DEFAULT),
            Stat(label="Errors (24h)", value="—", tone=Tone.DEFAULT),
        ]
        return HTMLResponse(render_stat_fragment(stats))

    async def _render_with_flash(
        self,
        request: Request,
        content: Any,
        title: str,
        breadcrumbs: list[dict[str, Any]] | None,
    ) -> HTMLResponse:
        """Render the dashboard inside an admin context so flash messages
        (e.g. the sign-in toast) are consumed by the shell."""
        from oridecon.admin.state.context import AdminContextManager

        async with AdminContextManager(request):
            return await self.render_admin(
                request,
                content,
                title=title,
                breadcrumbs=breadcrumbs,
            )

    def _get_resource_list(self, request: Request) -> list[str]:
        """Return a list of registered resource names from app state."""
        try:
            app = request.app
            return sorted(getattr(app.state, "admin_resources", {}).keys())
        except Exception:  # noqa: BLE001
            return []

    # MetricProtocol aggregation helpers with caching

    def get_request_cache(self, request: Request) -> dict[str, Any]:
        """
        Get request-scoped cache.

        Returns the context-var-backed cache dict for the current request.
        The cache is isolated per async context — no shared state between
        concurrent requests.
        """
        return _get_request_cache()

    async def aggregate_metric(
        self,
        request: Request,
        metric_name: str,
        compute_func: Any,
        use_request_cache: bool = True,
    ) -> Any:
        """
        Aggregate metric with automatic caching.

        Args:
            request: Current request
            metric_name: Name of the metric
            compute_func: Async callable to compute metric value
            use_request_cache: Use request-scoped cache (default: True)

        Returns:
            Computed or cached metric value

        Example:
            ```python
            total_users = await self.aggregate_metric(
                request,
                "total_users",
                lambda: db.execute("SELECT COUNT(*) FROM users")
            )
            ```
        """
        if use_request_cache:
            cache = self.get_request_cache(request)
            key = f"metric:{metric_name}"
            if key not in cache:
                cache[key] = await compute_func()
            return cache[key]
        return await compute_func()

    # Time-series helpers

    def format_time_series(
        self,
        data: list[tuple[datetime, float]],
        interval: str = "hour",
    ) -> list[dict[str, Any]]:
        """
        Format time-series data for charting libraries.

        Args:
            data: List of (timestamp, value) tuples
            interval: Time interval ('hour', 'day', 'week', 'month')

        Returns:
            Formatted data for charting (Chart.js compatible)

        Example:
            ```python
            raw_data = [(datetime(2024, 1, 1, 10), 42.0), ...]
            chart_data = self.format_time_series(raw_data, interval='day')
            ```
        """
        return [
            {
                "timestamp": ts.isoformat(),
                "value": value,
                "label": self._format_timestamp_label(ts, interval),
            }
            for ts, value in data
        ]

    def _format_timestamp_label(self, ts: datetime, interval: str) -> str:
        """Format timestamp for display based on interval."""
        if interval == "hour":
            return ts.strftime("%H:%M")
        if interval == "day":
            return ts.strftime("%Y-%m-%d")
        if interval == "week":
            return f"Week {ts.isocalendar()[1]}, {ts.year}"
        if interval == "month":
            return ts.strftime("%b %Y")
        return ts.isoformat()

    def aggregate_time_series(
        self,
        data: list[tuple[datetime, float]],
        interval: str = "hour",
    ) -> list[tuple[datetime, float]]:
        """
        Aggregate time-series data into intervals.

        Groups data points by time interval and sums/averages values.

        Args:
            data: List of (timestamp, value) tuples
            interval: Aggregation interval ('hour', 'day', 'week', 'month')

        Returns:
            Aggregated time-series data
        """
        buckets: dict[str, list[float]] = defaultdict(list)

        for ts, value in data:
            bucket_key = self._get_bucket_key(ts, interval)
            buckets[bucket_key].append(value)

        # Compute average for each bucket
        result: list[tuple[datetime, float]] = []
        for key, values in sorted(buckets.items()):
            avg_value = sum(values) / len(values)
            # Parse bucket key back to datetime
            bucket_ts = self._parse_bucket_key(key, interval)
            result.append((bucket_ts, avg_value))

        return result

    def _get_bucket_key(self, ts: datetime, interval: str) -> str:
        """Generate bucket key for timestamp."""
        if interval == "hour":
            return ts.strftime("%Y-%m-%d %H:00")
        if interval == "day":
            return ts.strftime("%Y-%m-%d")
        if interval == "week":
            iso_year, iso_week, _ = ts.isocalendar()
            return f"{iso_year}-W{iso_week:02d}"
        if interval == "month":
            return ts.strftime("%Y-%m")
        return ts.isoformat()

    def _parse_bucket_key(self, key: str, interval: str) -> datetime:
        """Parse bucket key back to datetime."""
        if interval == "hour":
            return datetime.strptime(key, "%Y-%m-%d %H:00")
        if interval == "day":
            return datetime.strptime(key, "%Y-%m-%d")
        if interval == "week":
            year, week = key.split("-W")
            # ISO week to datetime
            return datetime.strptime(f"{year} {week} 1", "%Y %W %w")
        if interval == "month":
            return datetime.strptime(key, "%Y-%m")
        return datetime.fromisoformat(key)
