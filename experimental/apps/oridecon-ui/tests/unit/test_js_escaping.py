"""Values crossing into inline JavaScript must not become code.

HTML escaping does not protect a JS context. A value interpolated into a JS
string literal is injectable by a bare quote, which needs no HTML
metacharacter, so ``html.escape`` neither prevents the attack nor survives
the round trip -- inside a script the JS parser sees ``&#x27;``, not a
quote. These tests cover the encoder and the components that were shipping
this bug.

The assertions deliberately parse the emitted literal rather than grepping
for a payload substring: an escaped payload still *contains* the attack
text, so a substring check passes for the wrong reason.
"""

from __future__ import annotations

import html
import json  # noqa: TID251 — JSONDecoder is needed to parse emitted JS literals

import pytest

from oridecon.ui import render_to_string
from oridecon.ui.core.js import js_json, js_string

#: Payloads that break out of a single-quoted JS string, a double-quoted
#: one, the enclosing <script> element, or a JS line.
BREAKOUT_PAYLOADS = [
    "');alert(document.cookie);('",
    '");alert(1);("',
    "</script><img src=x onerror=alert(1)>",
    "\u2028alert(1)",
    "\u2029alert(1)",
    "\\'); alert(1); //",
    "\\\\';alert(1);//",
]


def _decoder() -> json.JSONDecoder:
    return json.JSONDecoder()


def _literal_at(rendered: str, marker: str) -> str:
    """Return the JS literal that follows ``marker`` in ``rendered``.

    Uses ``raw_decode`` so the literal's own bounds are found by a real
    parser. Splitting on a delimiter would truncate any payload that
    contains that delimiter -- which is exactly what these payloads do.
    """
    start = rendered.index(marker) + len(marker)
    value, _ = _decoder().raw_decode(rendered[start:])
    return value


class TestJsString:
    def test_produces_its_own_quotes(self) -> None:
        """Callers must not add quotes; doing so reintroduces the bug."""
        assert js_string("x") == '"x"'

    @pytest.mark.parametrize("payload", BREAKOUT_PAYLOADS)
    def test_payload_round_trips_exactly(self, payload: str) -> None:
        """The literal must decode back to the input: no escape, no loss."""
        assert json.loads(js_string(payload)) == payload

    def test_script_close_cannot_end_the_block(self) -> None:
        """The HTML tokenizer ignores JS quoting, so a literal </script>
        inside a string still closes the element."""
        assert "</script>" not in js_string("</script>")
        assert "\\u003c/script\\u003e" in js_string("</script>")

    def test_html_breakout_characters_are_escaped(self) -> None:
        literal = js_string("<&>")

        assert "<" not in literal
        assert ">" not in literal
        assert "&" not in literal

    def test_js_line_terminators_are_escaped(self) -> None:
        """U+2028/9 are valid in JSON but terminate a line in JavaScript."""
        assert "\u2028" not in js_string("\u2028")
        assert "\u2029" not in js_string("\u2029")

    def test_none_becomes_empty_string_not_null(self) -> None:
        """Callers use this for text and URLs; a null would change type."""
        assert js_string(None) == '""'

    def test_non_strings_are_stringified(self) -> None:
        assert json.loads(js_string(42)) == "42"


class TestJsJson:
    def test_preserves_structure(self) -> None:
        assert json.loads(js_json({"a": [1, 2]})) == {"a": [1, 2]}

    def test_escapes_breakout_inside_values(self) -> None:
        literal = js_json({"k": "</script>"})

        assert "</script>" not in literal
        assert json.loads(literal.replace("\\u003c", "<").replace("\\u003e", ">")) == {
            "k": "</script>"
        }

    def test_raises_on_unserialisable(self) -> None:
        """Falling back to str() would emit a Python repr into a script."""
        with pytest.raises(TypeError):
            js_json(object())


class TestNotificationBell:
    """URLs reach this component from configuration and are placed in JS."""

    @pytest.mark.parametrize("payload", BREAKOUT_PAYLOADS)
    def test_sse_url_cannot_escape_its_literal(self, payload: str) -> None:
        from oridecon.ui.organisms.notification_bell import NotificationBell

        rendered = render_to_string(NotificationBell(sse_url=payload))

        assert _literal_at(rendered, "new EventSource(") == payload

    def test_script_block_is_not_closed_early(self) -> None:
        from oridecon.ui.organisms.notification_bell import NotificationBell

        rendered = render_to_string(
            NotificationBell(sse_url="</script><img src=x onerror=alert(1)>")
        )
        body = rendered.split("<script>")[1].split("</script>")[0]

        assert "<img" not in body

    def test_normal_url_is_unchanged(self) -> None:
        from oridecon.ui.organisms.notification_bell import NotificationBell

        rendered = render_to_string(NotificationBell(sse_url="/admin/_sse/widgets"))

        assert _literal_at(rendered, "new EventSource(") == "/admin/_sse/widgets"

    def test_max_display_is_numeric(self) -> None:
        """It is emitted bare, outside any quotes, so it must be an int."""
        from oridecon.ui.organisms.notification_bell import NotificationBell

        rendered = render_to_string(NotificationBell(max_display=7))

        assert "notifications.length > 7" in rendered


class TestTaskProgress:
    """``on_complete`` was concatenated in as executable code."""

    def _script(self, **kwargs: object) -> str:
        from oridecon.ui.organisms.task_progress import TaskProgress

        return html.unescape(render_to_string(TaskProgress(**kwargs)))  # type: ignore[arg-type]

    def _stream_url(self, rendered: str) -> str:
        return _literal_at(rendered, "const streamUrl = ")

    def _completion_action(self, rendered: str) -> object:
        return _literal_at(rendered, "const completionAction = ")

    @pytest.mark.parametrize("payload", BREAKOUT_PAYLOADS)
    def test_stream_url_cannot_escape_its_literal(self, payload: str) -> None:
        rendered = self._script(task_id="t", stream_url=payload)

        assert self._stream_url(rendered) == payload

    def test_task_id_cannot_escape_the_derived_url(self) -> None:
        rendered = self._script(task_id="');alert(1);//")

        assert self._stream_url(rendered) == (
            "/admin/progress/%27%29%3Balert%281%29%3B%2F%2F/stream"
        )

    @pytest.mark.parametrize(
        "callback",
        [
            "alert(document.cookie)",
            "x;alert(1)",
            "javascript:alert(1)",
            "a()||b()",
            "'-alert(1)-'",
        ],
    )
    def test_arbitrary_code_is_rejected(self, callback: str) -> None:
        """There is no encoding that makes attacker code safe to execute, so
        anything that is not a plain identifier path is dropped."""
        rendered = self._script(task_id="t", on_complete=callback)

        assert callback not in rendered

    @pytest.mark.parametrize("target", ["//evil.test", "https://evil.test"])
    def test_offsite_redirects_are_rejected(self, target: str) -> None:
        rendered = self._script(task_id="t", on_complete=target)

        assert "evil.test" not in rendered

    def test_identifier_callback_becomes_inert_action_data(self) -> None:
        rendered = self._script(task_id="t", on_complete="app.onDone")

        assert self._completion_action(rendered) == {
            "kind": "callback",
            "target": "app.onDone",
        }
        assert "app.onDone();" not in rendered

    def test_local_redirect_becomes_inert_action_data(self) -> None:
        rendered = self._script(task_id="t", on_complete="/admin/done")

        assert self._completion_action(rendered) == {
            "kind": "navigate",
            "target": "/admin/done",
        }
        assert "window.location.href =" not in rendered

    def test_redirect_target_is_an_encoded_literal(self) -> None:
        target = '/admin/"+alert(1)+"'
        rendered = self._script(task_id="t", on_complete=target)

        assert self._completion_action(rendered) == {
            "kind": "navigate",
            "target": target,
        }


class TestInfolistIcon:
    """``icon`` was rendered as raw markup."""

    def _render(self, icon: str) -> str:
        from oridecon.ui.molecules.infolist import InfolistEntry, InfolistWidget

        entry = InfolistEntry(name="n", label="L", value="v", icon=icon)
        return render_to_string(InfolistWidget(entries=[entry]).render())

    def test_markup_is_not_injected(self) -> None:
        rendered = self._render("<img src=x onerror=alert(1)>")

        assert "<img" not in rendered
        assert "onerror" not in rendered

    def test_script_is_not_injected(self) -> None:
        rendered = self._render("<script>alert(1)</script>")

        assert "<script>" not in rendered

    def test_known_icon_still_renders(self) -> None:
        """The fix must not silently blank out legitimate icons."""
        assert "<svg" in self._render("users")

    def test_unknown_icon_renders_nothing_dangerous(self) -> None:
        rendered = self._render("definitely-not-an-icon")

        assert "<img" not in rendered
        assert "<script" not in rendered


class TestChartRenderers:
    """Chart labels, titles and ids are caller data placed in a script."""

    def _renderers(self) -> list[object]:
        from oridecon.admin.services.charts import ChartJSRenderer, PlotlyRenderer

        return [ChartJSRenderer(), PlotlyRenderer()]

    def _render(self, renderer: object, **options: object) -> str:
        from oridecon.admin.services.charts import ChartData, ChartType

        data = ChartData(
            labels=options.pop("labels", ["Jan"]),  # type: ignore[arg-type]
            datasets=[{"label": options.pop("series", "Sales"), "data": [1]}],
            title=options.pop("title", "T"),  # type: ignore[arg-type]
        )
        return renderer.render(ChartType.BAR, data, **options)  # type: ignore[attr-defined]

    @pytest.mark.parametrize("field", ["labels", "series", "title"])
    def test_data_cannot_close_the_script_block(self, field: str) -> None:
        payload = "</script><img src=x onerror=alert(1)>"
        value = [payload] if field == "labels" else payload

        for renderer in self._renderers():
            rendered = self._render(renderer, **{field: value})

            assert "<img" not in rendered
            assert rendered.count("</script>") == rendered.count("<script")

    def test_chart_id_cannot_break_out_of_the_attribute(self) -> None:
        for renderer in self._renderers():
            rendered = self._render(renderer, id='c"><img src=x onerror=alert(1)>')

            assert "<img" not in rendered

    @pytest.mark.parametrize("payload", BREAKOUT_PAYLOADS)
    def test_chart_id_cannot_break_out_of_the_js_literal(self, payload: str) -> None:
        """A quote in the id must stay data. Asserting the payload text is
        absent would be wrong -- it may legitimately appear verbatim inside
        a double-quoted literal -- so decode the literal and compare."""
        for renderer, marker in (
            (self._renderers()[0], "getElementById("),
            (self._renderers()[1], "Plotly.newPlot("),
        ):
            rendered = self._render(renderer, id=payload)

            assert _literal_at(rendered, marker) == payload

    def test_dimensions_cannot_break_out_of_the_style_attribute(self) -> None:
        for renderer in self._renderers():
            rendered = self._render(renderer, width='"><img src=x onerror=alert(1)>')

            assert "<img" not in rendered

    def test_legitimate_chart_still_renders(self) -> None:
        """Encoding must not break the normal path."""
        from oridecon.admin.services.charts import ChartJSRenderer, PlotlyRenderer

        chartjs = self._render(ChartJSRenderer(), labels=["Jan", "Feb"], id="sales")
        assert 'id="sales"' in chartjs
        assert "new Chart(ctx," in chartjs
        assert "Jan" in chartjs

        plotly = self._render(PlotlyRenderer(), id="sales")
        assert 'id="sales"' in plotly
        assert 'Plotly.newPlot("sales"' in plotly


class TestHtmxOptimisticHelpers:
    """Both helpers build JS by interpolating a selector and a snippet."""

    @pytest.mark.parametrize("payload", BREAKOUT_PAYLOADS)
    def test_optimistic_update_encodes_both_arguments(self, payload: str) -> None:
        from oridecon.ui.htmx.helpers import optimistic_update

        expression = optimistic_update(payload, payload)["hx-on::before-request"]
        selector = _literal_at(expression, "document.querySelector(")
        content = json.loads(expression.split(".innerHTML = ", 1)[1])

        assert selector == payload
        assert content == payload

    @pytest.mark.parametrize("payload", BREAKOUT_PAYLOADS)
    def test_optimistic_swap_encodes_both_arguments(self, payload: str) -> None:
        from oridecon.ui.htmx.helpers import hx_optimistic_swap

        expression = hx_optimistic_swap(payload, payload)["hx-on-click"]
        selector = _literal_at(expression, "document.querySelector(")
        content = json.loads(expression.split(".innerHTML = ", 1)[1])

        assert selector == payload
        assert content == payload

    def test_backslash_defeated_the_previous_escaping(self) -> None:
        """The old code did html_snippet.replace("'", "\\'"), so a leading
        backslash escaped the backslash instead of the quote and the
        remainder ran as code."""
        from oridecon.ui.htmx.helpers import hx_optimistic_swap

        expression = hx_optimistic_swap("#t", "\\';alert(1);//")["hx-on-click"]

        assert json.loads(expression.split(".innerHTML = ", 1)[1]) == (
            "\\';alert(1);//"
        )


class TestDataTableAllIds:
    """Per-table row IDs must never seed process-global client state."""

    def _render(self, all_ids: list[str]) -> str:
        from oridecon.ui import render_to_string
        from oridecon.ui.molecules.data_table_client_logic import (
            DataTableScriptRenderer,
        )

        return str(render_to_string(DataTableScriptRenderer.render(all_ids)))

    def test_row_id_cannot_close_the_script_block(self) -> None:
        rendered = self._render(["a", "</script><img src=x onerror=alert(1)>"])

        assert "</script><img" not in rendered
        assert "<img" not in rendered

    def test_ids_are_not_stored_in_the_global_method_registry(self) -> None:
        rendered = self._render(["r1", "r2"])

        assert "r1" not in rendered
        assert "r2" not in rendered
        assert "allIds:" not in rendered
        assert "window.LexigramTableLogic" in rendered

    def test_bulk_progress_listener_is_idempotent_and_accessible(self) -> None:
        rendered = self._render([])

        assert "LexigramBulkProgressInitialized" in rendered
        assert "bulk-progress-start" in rendered
        assert "new EventSource" in rendered
        assert "sameOriginUrl" in rendered
        assert "root.setAttribute('role', 'status')" in rendered
        assert "root.setAttribute('aria-live', 'polite')" in rendered
        assert "refreshTable" in rendered


class TestAdminLayoutCsrf:
    """The CSRF token is emitted into script content, not into markup."""

    def test_token_is_a_js_literal_not_an_html_entity(self) -> None:
        """html.escape would send JavaScript the text &#39; rather than a
        quote, corrupting the token instead of protecting it."""
        from oridecon.ui.core.js import js_string

        literal = js_string("tok'en")

        assert "&#39;" not in literal
        assert json.loads(literal) == "tok'en"
