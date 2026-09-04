"""Deterministic identity contracts for real-time feed components."""

from __future__ import annotations

import pytest

from oridecon.ui import RealTimeFeed, render_to_string


def test_feed_default_ids_are_deterministic_and_unique_for_siblings() -> None:
    html = render_to_string(
        [
            RealTimeFeed(url="/events/one"),
            RealTimeFeed(url="/events/two"),
        ]
    )

    assert 'id="oridecon-real-time-feed-1"' in html
    assert 'id="oridecon-real-time-feed-2"' in html


def test_explicit_feed_key_is_stable_across_partial_renders() -> None:
    first = render_to_string(RealTimeFeed(url="/events", feed_key="orders"))
    second = render_to_string(RealTimeFeed(url="/events", feed_key="orders"))

    assert 'id="oridecon-real-time-feed-orders"' in first
    assert first == second


def test_duplicate_explicit_feed_keys_fail_in_one_render_tree() -> None:
    with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
        render_to_string(
            [
                RealTimeFeed(url="/events/one", feed_key="orders"),
                RealTimeFeed(url="/events/two", feed_key="orders"),
            ]
        )


def test_explicit_dom_id_remains_supported() -> None:
    html = render_to_string(RealTimeFeed(url="/events", id="custom-feed"))

    assert 'id="custom-feed"' in html
