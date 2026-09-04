"""Protocol, trust, and identity contracts for SSE helpers."""

from __future__ import annotations

import re

import pytest

from oridecon.ui import Element
from oridecon.ui.core.trusted_html import TrustedHTML
from oridecon.ui.htmx.sse import SSE, SSEMessage


class TestSSEMessageProtocolSafety:
    @pytest.mark.parametrize("field", ["event", "event_id"])
    @pytest.mark.parametrize("boundary", ["\r", "\n", "\r\n", "\x00"])
    def test_control_fields_reject_protocol_boundaries(
        self,
        field: str,
        boundary: str,
    ) -> None:
        with pytest.raises(ValueError, match="SSE"):
            SSEMessage("payload", **{field: f"safe{boundary}data: injected"})

    def test_data_carriage_returns_are_prefixed_as_data_lines(self) -> None:
        output = str(SSEMessage("first\rdata: injected\r\nthird"))

        assert output == "data: first\ndata: data: injected\ndata: third\n\n"

    def test_zero_retry_is_emitted(self) -> None:
        assert "retry: 0\n" in str(SSEMessage("payload", retry=0))

    def test_negative_retry_is_rejected(self) -> None:
        with pytest.raises(ValueError, match="zero or greater"):
            SSEMessage("payload", retry=-1)


class TestSSEComponentTrustAndIdentity:
    def test_reconnect_script_has_specific_provenance(self) -> None:
        region = SSE(url="/events").render()
        script = region.children[-1]

        assert isinstance(script, Element)
        assert script.tag == "script"
        assert isinstance(script.children[0], TrustedHTML)
        assert script.children[0].source == "generated SSE reconnect controller"

    def test_generated_script_scopes_listeners_to_the_region(self) -> None:
        output = str(SSE(url="/events"))

        assert "element.addEventListener(&#x27;htmx:sseError&#x27;" not in output
        assert "element.addEventListener('htmx:sseError'" in output
        assert "document.addEventListener('htmx:sseError'" not in output
        assert "sseReconnectBound" in output

    def test_sibling_regions_receive_unique_deterministic_ids(self) -> None:
        page = Element("main", SSE(url="/events"), SSE(url="/events"))

        output = str(page)
        ids = re.findall(r'<div id="([^"]+)" hx-ext="sse"', output)

        assert ids == ["oridecon-sse-region-1", "oridecon-sse-region-2"]

    def test_explicit_key_is_stable_across_partial_renders(self) -> None:
        first = str(SSE(url="/events", sse_key="activity"))
        second = str(SSE(url="/events", sse_key="activity"))

        assert 'id="oridecon-sse-region-activity"' in first
        assert first == second

    def test_duplicate_keys_fail_in_one_render_tree(self) -> None:
        page = Element(
            "main",
            SSE(url="/first", sse_key="activity"),
            SSE(url="/second", sse_key="activity"),
        )

        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            str(page)

    def test_script_serializes_an_explicit_id(self) -> None:
        output = str(SSE(url="/events", id="region</script><script>pwned"))

        assert "<script>pwned" not in output
        assert "region\\u003c/script\\u003e\\u003cscript\\u003epwned" in output

    def test_root_props_are_preserved_without_overriding_sse_wiring(self) -> None:
        output = str(
            SSE(
                url="/events",
                class_="stream",
                data_testid="events",
                role="log",
                aria_live="assertive",
                hx_ext="untrusted",
                hx_target="#wrong",
            )
        )

        assert 'class="stream"' in output
        assert 'data-testid="events"' in output
        assert 'role="log"' in output
        assert 'aria-live="assertive"' in output
        assert output.count('hx-ext="sse"') == 1
        assert 'hx-ext="untrusted"' not in output
        assert 'hx-target="this"' in output
        assert 'hx-target="#wrong"' not in output
        assert " retry-ms=" not in output

    def test_children_remain_structured_inside_live_region(self) -> None:
        output = str(SSE(url="/events", children=[Element("strong", "Ready")]))

        assert "<strong>Ready</strong>" in output

    def test_event_type_rejects_line_boundaries(self) -> None:
        with pytest.raises(ValueError, match="event type"):
            SSE(url="/events", event_type="message\nsse-connect: /evil")
