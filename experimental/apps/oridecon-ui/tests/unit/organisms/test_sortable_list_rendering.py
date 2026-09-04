"""Composition and inline-script regressions for sortable record lists."""

from __future__ import annotations

from oridecon.ui import SortableRecordList, render_to_string


def _list(**kwargs: str) -> SortableRecordList:
    return SortableRecordList(
        rows=[{"id": "1", "title": "First"}],
        reorder_url=kwargs.get("reorder_url", "/posts/reorder"),
        hx_target=kwargs.get("hx_target", "this"),
        hx_swap=kwargs.get("hx_swap", "none"),
    )


def test_sibling_lists_do_not_emit_a_shared_fixed_id() -> None:
    html = render_to_string([_list(), _list()])

    assert 'id="sortable-list"' not in html
    assert html.count('x-ref="sortableList"') == 2


def test_generated_controller_remains_executable_script_text() -> None:
    html = render_to_string(_list())

    assert "onEnd: () =>" in html
    assert "=&gt;" not in html


def test_generated_controller_serializes_hostile_options_as_data() -> None:
    payload = "';</script><script>alert(1)</script>"
    html = render_to_string(
        _list(
            reorder_url=payload,
            hx_target=payload,
            hx_swap=payload,
        )
    )

    assert html.count("<script") == 1
    assert html.count("</script>") == 1
    assert payload not in html
    assert "\\u003c/script\\u003e" in html
