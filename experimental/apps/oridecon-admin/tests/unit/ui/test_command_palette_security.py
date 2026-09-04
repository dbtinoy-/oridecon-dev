"""Trust, identity, and resilience contracts for CommandPalette.

Since the CSP v2 migration the palette controller ships in the generated
asset ``static/js/admin-shell.js`` (source of truth:
``dev/generators/admin_shell_assets.py``); the component markup carries only
a non-executable ``application/json`` config island, so the security
contracts are asserted against the asset plus the structured markup.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from oridecon.admin.ui.organisms.command_palette import CommandPalette
from oridecon.ui import Element, TrustedHTML

_SHELL_JS = (
    Path(__file__).parents[3]
    / "src"
    / "oridecon"
    / "admin"
    / "static"
    / "js"
    / "admin-shell.js"
)


def _shell_js() -> str:
    return _SHELL_JS.read_text(encoding="utf-8")


class TestCommandPaletteTrust:
    def test_generated_config_island_has_specific_provenance(self) -> None:
        root = CommandPalette().render()
        island = root.children[-1]

        assert isinstance(island, Element)
        assert island.tag == "script"
        assert island.attrs["type_"] == "application/json"
        assert isinstance(island.children[0], TrustedHTML)
        assert island.children[0].source == (
            "generated CommandPalette config island (non-executable)"
        )

    def test_command_data_cannot_close_the_island(self) -> None:
        payload = "</script><script>window.pwned=true</script>"
        palette = CommandPalette(
            commands=[
                {
                    "label": payload,
                    "href": payload,
                    "icon": payload,
                    "icon_html": payload,
                }
            ]
        )

        output = str(palette)
        script_body = output.split(
            '<script type="application/json"', 1
        )[1].split("</script>", 1)[0]

        assert "<script>window.pwned" not in script_body
        assert "\\u003c/script\\u003e\\u003cscript\\u003e" in script_body

    def test_remote_icon_html_is_overridden_by_the_builtin_icon_map(self) -> None:
        output = str(CommandPalette())
        controller = _shell_js()

        assert "...command," in controller
        assert "icon_html: this.icons[command.icon] || ''" in controller
        assert 'x-html="command.icon_html"' in output

    def test_navigation_rejects_cross_origin_and_non_http_destinations(self) -> None:
        controller = _shell_js()

        assert "url.origin === window.location.origin" in controller
        assert "['http:', 'https:'].includes(url.protocol)" in controller
        assert "unsafe destination" in controller
        assert "window.location.href = command.href" not in controller

    def test_admin_prefix_is_serialized_for_the_search_endpoint(self) -> None:
        payload = "/admin</script><script>window.pwned=true"

        output = str(CommandPalette(admin_prefix=payload))
        script_body = output.split(
            '<script type="application/json"', 1
        )[1].split("</script>", 1)[0]

        assert "<script>window.pwned" not in script_body
        assert "\\u003c/script\\u003e\\u003cscript\\u003e" in script_body


class TestCommandPaletteIdentity:
    def test_sibling_palettes_receive_unique_ids_and_config_islands(self) -> None:
        page = Element("main", CommandPalette(), CommandPalette())

        output = str(page)
        roots = re.findall(
            r'<div id="(oridecon-command-palette-dialog-[^"]+)" role="dialog"',
            output,
        )
        controllers = re.findall(r'x-data="([^"]+)"', output)
        config_ids = re.findall(r'type="application/json" id="([^"]+)"', output)

        assert roots == [
            "oridecon-command-palette-dialog-1",
            "oridecon-command-palette-dialog-2",
        ]
        # The Alpine name is a single fixed registration (static asset); the
        # per-instance data islands remain uniquely scoped.
        assert controllers == ["commandPalette", "commandPalette"]
        assert len(config_ids) == len(set(config_ids)) == 2

    def test_explicit_key_is_stable_across_partial_renders(self) -> None:
        first = str(CommandPalette(command_palette_key="global"))
        second = str(CommandPalette(command_palette_key="global"))

        assert 'id="oridecon-command-palette-dialog-global"' in first
        assert first == second

    def test_duplicate_keys_fail_in_one_render_tree(self) -> None:
        page = Element(
            "main",
            CommandPalette(command_palette_key="global"),
            CommandPalette(command_palette_key="global"),
        )

        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            str(page)

    def test_combobox_and_options_share_the_scoped_listbox_id(self) -> None:
        output = str(CommandPalette())
        options_id = re.search(r'<ul id="([^"]+)" role="listbox"', output)

        assert options_id is not None
        assert f'aria-controls="{options_id.group(1)}"' in output
        assert "activeOptionId" in _shell_js()
        assert 'x-bind:aria-activedescendant="activeOptionId"' in output


class TestCommandPaletteExperience:
    def test_search_requests_are_abortable_and_ignore_stale_results(self) -> None:
        output = str(CommandPalette())
        controller = _shell_js()

        assert "new AbortController()" in controller
        assert "this.requestController && this.requestController.abort()" in controller
        assert "this.requestController === request" in controller
        assert "if (!response.ok)" in controller
        assert "Loading commands…" in output

    def test_loading_error_empty_and_retry_states_are_rendered(self) -> None:
        output = str(CommandPalette())
        controller = _shell_js()

        assert "Loading commands…" in output
        assert "Commands could not be loaded." in controller
        assert ">Retry</button>" in output
        assert "No results found for that search." in output

    def test_focus_is_restored_after_the_palette_closes(self) -> None:
        output = str(CommandPalette())
        controller = _shell_js()

        assert "this.previousFocus = document.activeElement" in controller
        assert "this.previousFocus && this.previousFocus.focus()" in controller
        assert 'x-ref="search"' in output

    def test_controller_supports_initial_and_htmx_inserted_rendering(self) -> None:
        controller = _shell_js()

        assert "if (window.Alpine) register();" in controller
        assert "{ once: true }" in controller
        assert "destroy()" in controller

    def test_result_keys_are_stable_within_each_response(self) -> None:
        output = str(CommandPalette())
        controller = _shell_js()

        assert "_key: [command.href || ''" in controller
        assert 'x-bind:key="command._key"' in output
        assert 'x-bind:key="command.label"' not in output

    def test_root_props_are_preserved_while_dialog_wiring_is_protected(self) -> None:
        output = str(
            CommandPalette(
                id="global-palette",
                class_="custom-palette",
                data_testid="palette",
                x_data="untrusted",
                role="region",
            )
        )

        assert 'id="global-palette"' in output
        assert "custom-palette" in output
        assert 'data-testid="palette"' in output
        assert 'x-data="untrusted"' not in output
        assert 'role="dialog"' in output
        assert " command-palette-key=" not in output
