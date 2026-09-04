"""Verify monitoring/ duplicate shim directory has been deleted."""

from __future__ import annotations

import os


def test_monitoring_directory_deleted() -> None:
    monitoring_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "src",
        "oridecon",
        "ui",
        "monitoring",
    )
    assert not os.path.exists(os.path.normpath(monitoring_path)), (
        "oridecon/ui/monitoring/ still exists — delete it (it is a duplicate of performance/)"
    )


def test_performance_symbols_still_importable_after_deletion() -> None:
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
    from oridecon.ui.performance.observability import (
        MetricProtocol,
        MetricsCollector,
        MetricType,
    )
    assert RenderCache is not None
    assert MetricsCollector is not None
