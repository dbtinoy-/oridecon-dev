"""Instance-isolation contracts for the shared DataTable client methods."""

from __future__ import annotations

from pathlib import Path

from oridecon.admin.config import TableConfiguration
from oridecon.admin.ui.filters.types import SelectFilter
from oridecon.admin.ui.organisms.data_table import DataTable
from oridecon.ui import DataTableScriptRenderer, Element, TrustedHTML, render_to_string
from oridecon.ui.columns.types import TextColumn

ADMIN_ROOT = Path(__file__).resolve().parents[3]


def _source() -> str:
    script = DataTableScriptRenderer.render(["first-only-id"])
    assert isinstance(script, Element)
    assert isinstance(script.children[0], TrustedHTML)
    return script.children[0].value


def test_global_registry_contains_methods_not_first_table_state() -> None:
    source = _source()

    assert "window.LexigramTableLogic" in source
    assert "first-only-id" not in source
    assert "allIds:" not in source
    assert "hasActiveFiltersState:" not in source
    assert "const root = this.$root" in source


def test_root_local_ids_remain_encoded_in_the_alpine_attribute() -> None:
    hostile_id = '</div><script>alert("owned")</script>'
    html = render_to_string(
        DataTable(
            columns=[TextColumn("name")],
            data=[{"id": hostile_id, "name": "Safe label"}],
            table_key="safe-table",
        )
    )

    assert "<script>alert" not in html
    assert "allIds: [&quot;&lt;/div&gt;&lt;script&gt;" in html
    assert "window.LexigramTableLogic = {\n                allIds:" not in html


def test_search_filter_and_data_regions_expose_instance_markers() -> None:
    config = TableConfiguration(
        columns=[TextColumn("name")],
        resource_prefix="/admin/orders",
        filter_options=[SelectFilter("status", options=["open", "closed"])],
    )
    html = render_to_string(
        DataTable(config=config, data=[{"id": "one", "name": "Order"}])
    )

    assert " data-oridecon-table-root" in html
    assert " data-oridecon-table-data" in html
    assert " data-oridecon-table-search" in html
    assert " data-oridecon-table-filters" in html


def test_selection_reorder_group_and_search_queries_are_root_scoped() -> None:
    source = _source()

    assert "button.closest('[data-oridecon-table-root]')" in source
    assert "table.querySelectorAll('input[name=\"ids\"]:checked')" in source
    assert "serializeTableQuery(table)" in source
    assert "input[name], select[name], textarea[name]" in source
    assert "window.location.search" not in source
    assert "root.querySelectorAll('thead th[data-col-name]')" in source
    assert "root.querySelector('input[name=\"col_order\"]')" in source
    assert "root.querySelector('input[name=\"collapsed_groups\"]')" in source
    assert "'[data-oridecon-table-search] input'" in source
    assert "document.querySelector('input[name=\"col_order\"]')" not in source
    assert "document.querySelector('input[name=\"collapsed_groups\"]')" not in source


def test_data_refresh_reconciles_only_the_owning_table() -> None:
    source = _source()

    assert "refreshIdsFrom(target)" in source
    assert "!root.contains(target)" in source
    assert "target.matches('[data-oridecon-table-data]')" in source
    assert "target.querySelector('[data-oridecon-table-data]')" in source
    assert "dataRegion.dataset.orideconTableIds" in source
    assert "JSON.parse" in source
    assert "this.refreshAllIds" in source
    assert "table.dataset.orideconTableRefreshEvent" in source
    assert "refreshBulkTable(state.tableRoot)" in source
    assert "eventElement.closest('[data-oridecon-table-root]')" in source
    assert "if (!refreshTableRoot(table)) window.location.reload()" in source


def test_table_script_does_not_reprocess_htmx_swaps_or_bind_per_table_globals() -> None:
    source = _source()

    assert "htmx.process(target)" not in source
    assert "document.addEventListener('htmx:afterSwap'" not in source
    assert "document.addEventListener('htmx:beforeSwap'" not in source
    assert "LexigramTableInitialized" in source


def test_generated_script_has_specific_provenance() -> None:
    script = DataTableScriptRenderer.render([])

    assert isinstance(script, Element)
    assert isinstance(script.children[0], TrustedHTML)
    assert script.children[0].source == "generated DataTable client controller"


def test_static_download_fallback_is_scoped_to_the_initiating_table() -> None:
    source = (ADMIN_ROOT / "src/oridecon/admin/static/js/admin.js").read_text(
        encoding="utf-8"
    )

    assert "btn.closest('[data-oridecon-table-root]')" in source
    assert "table.querySelectorAll('input[name=\"ids\"]:checked')" in source
    assert "serializeTableQuery(table)" in source
    assert "input[name], select[name], textarea[name]" in source
    assert "table.querySelector('input[name=\"csrf_token\"]')" in source
    assert "document.querySelectorAll('input[name=\"ids\"]:checked')" not in source
