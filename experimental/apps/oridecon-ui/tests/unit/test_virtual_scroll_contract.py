"""Virtual scrolling remains instance-safe and progressively enhanced."""

from __future__ import annotations

import pytest

from oridecon.ui.core.base import el, render_to_string
from oridecon.ui.molecules.virtual_scroll import (
    InfiniteScrollTrigger,
    VirtualScroll,
    render_infinite_row,
)


class TestVirtualScroll:
    def test_requires_a_stable_selector_safe_target_id(self) -> None:
        with pytest.raises(ValueError, match="stable target_id"):
            VirtualScroll("/items")
        with pytest.raises(ValueError, match="must start with a letter"):
            VirtualScroll("/items", target_id="shared results")

    def test_rejects_unsafe_urls_and_invalid_ranges(self) -> None:
        with pytest.raises(ValueError, match="safe HTTP"):
            VirtualScroll("javascript:alert(1)", target_id="results")
        with pytest.raises(ValueError, match="greater than zero"):
            VirtualScroll("/items", target_id="results", chunk_size=0)
        with pytest.raises(ValueError, match="cannot be negative"):
            VirtualScroll("/items", target_id="results", total_items=-1)

    def test_preserves_caller_identity_and_placeholder(self) -> None:
        first = render_to_string(
            VirtualScroll(
                "/items",
                target_id="orders-results",
                placeholder="No orders yet",
                class_="min-h-24",
            ).render()
        )
        second = render_to_string(
            VirtualScroll("/items", target_id="customers-results").render()
        )

        assert 'id="orders-results"' in first
        assert "virtual-scroll min-h-24" in first
        assert "No orders yet" in first
        assert 'id="customers-results"' in second
        assert "virtual-scroll-container" not in first + second

    def test_conflicting_id_alias_is_rejected(self) -> None:
        with pytest.raises(ValueError, match="conflicts"):
            VirtualScroll("/items", target_id="orders", id_="customers")

    def test_duplicate_targets_fail_in_one_render_tree(self) -> None:
        page = el(
            "main",
            VirtualScroll("/orders", target_id="shared-results"),
            VirtualScroll("/customers", target_id="shared-results"),
        )

        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            render_to_string(page)


class TestInfiniteRow:
    def test_decorating_an_element_does_not_mutate_the_caller(self) -> None:
        row = el("article", "Order one", class_="record")
        original_attrs = dict(row.attrs)
        original_children = list(row.children)

        decorated = render_infinite_row(row, "/items?cursor=next")

        assert decorated is not row
        assert row.attrs == original_attrs
        assert row.children == original_children
        assert decorated.attrs["hx-get"] == "/items?cursor=next"
        assert decorated.attrs["hx-trigger"] == "intersect once threshold:0.5"
        assert decorated.attrs["hx-swap"] == "afterend"

    def test_rejects_unsafe_urls_and_invalid_thresholds(self) -> None:
        with pytest.raises(ValueError, match="safe HTTP"):
            render_infinite_row("row", "javascript:alert(1)")
        with pytest.raises(ValueError, match="between zero and one"):
            render_infinite_row("row", "/items", threshold="2")

    def test_without_a_next_url_returns_the_original_content(self) -> None:
        row = el("article", "Last order")
        assert render_infinite_row(row) is row


class TestInfiniteScrollTrigger:
    def test_renders_one_progressively_enhanced_next_page_link(self) -> None:
        html = render_to_string(
            InfiniteScrollTrigger(
                "/items?cursor=next",
                target="#orders-results",
                swap="beforeend",
            ).render()
        )

        assert html.startswith("<a ")
        assert 'href="/items?cursor=next"' in html
        assert 'hx-get="/items?cursor=next"' in html
        assert 'hx-trigger="revealed once"' in html
        assert 'hx-target="#orders-results"' in html
        assert 'aria-label="Load more results"' in html
        assert "htmx-indicator" in html
        assert "<svg" in html
        assert "fa-spinner" not in html
        assert "Load more" in html
        assert "#table-content" not in html

    def test_explicit_scoped_fragment_selector_is_preserved(self) -> None:
        html = render_to_string(
            InfiniteScrollTrigger(
                "/items?page=2",
                target="#orders-results",
                select="#orders-results > .order",
            )
        )

        assert 'hx-select="#orders-results &gt; .order"' in html

    def test_custom_link_content_is_preserved(self) -> None:
        html = render_to_string(
            InfiniteScrollTrigger(
                "/items?page=2",
                children=["Next twenty orders"],
                class_="next-page",
            ).render()
        )

        assert "Next twenty orders" in html
        assert ">Load more<" not in html
        assert "next-page" in html

    def test_rejects_unsafe_or_ambiguously_overridden_navigation(self) -> None:
        with pytest.raises(ValueError, match="safe HTTP"):
            InfiniteScrollTrigger("javascript:alert(1)")
        with pytest.raises(ValueError, match="parameters instead"):
            InfiniteScrollTrigger("/items", hx_get="/other")
