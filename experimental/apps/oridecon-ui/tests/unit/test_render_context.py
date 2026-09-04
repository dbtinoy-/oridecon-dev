"""Deterministic, task-local rendering identity scopes."""

from __future__ import annotations

import asyncio
import re

import pytest

from oridecon.ui.core.base import Component, el, render_to_string
from oridecon.ui.core.render_context import (
    RenderContext,
    RenderScope,
    get_render_context,
    get_render_scope,
    render_context,
)
from oridecon.ui.molecules.modal import Modal
from oridecon.ui.organisms.slide_over import SlideOver

_VALID_ID = re.compile(r"^[a-z][a-z0-9-]*$")


class _ScopedComponent(Component):
    def render(self):
        identity = get_render_scope().child("item").id("node")
        return el("span", identity, id=identity)


class TestRenderScope:
    def test_unkeyed_ids_are_unique_and_reproducible(self) -> None:
        first = RenderScope("page").child("table")
        second = RenderScope("page").child("table")

        assert [first.id("row"), first.id("row")] == [
            "page-table-row-1",
            "page-table-row-2",
        ]
        assert [second.id("row"), second.id("row")] == [
            "page-table-row-1",
            "page-table-row-2",
        ]

    def test_stable_keys_reproduce_partial_target_ids(self) -> None:
        full_response = RenderScope("admin").child("users")
        partial_response = RenderScope("admin").child("users")

        assert full_response.id("table", key="active") == (
            partial_response.id("table", key="active")
        )

    def test_duplicate_explicit_key_fails_in_strict_mode(self) -> None:
        scope = RenderScope("page")
        assert scope.id("dialog", key="settings") == "page-dialog-settings"

        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            scope.id("dialog", key="settings")

    def test_duplicate_compatibility_mode_logs_and_suffixes(self) -> None:
        scope = RenderScope("page", strict=False)

        assert scope.id("dialog", key="settings") == "page-dialog-settings"
        assert scope.id("dialog", key="settings") == "page-dialog-settings-2"
        assert scope.id("dialog", key="settings") == "page-dialog-settings-3"

    def test_child_scopes_share_the_uniqueness_registry(self) -> None:
        root = RenderScope("page")
        root.child("panel").id("region", key="main")

        with pytest.raises(ValueError, match="Duplicate"):
            root.child("panel").id("region", key="main")

    @pytest.mark.parametrize(
        "value",
        ["User Settings", "123", "a/b", "Ünicode", "x" * 100],
    )
    def test_hostile_or_awkward_keys_become_valid_html_ids(self, value: str) -> None:
        identity = RenderScope("page").id("region", key=value)

        assert _VALID_ID.fullmatch(identity)
        assert " " not in identity
        assert "/" not in identity

    @pytest.mark.parametrize("value", ["", "   "])
    def test_blank_segments_are_rejected(self, value: str) -> None:
        with pytest.raises(ValueError, match="must not be blank"):
            RenderScope(value)

    def test_non_string_segments_are_rejected(self) -> None:
        with pytest.raises(TypeError, match="must be a string"):
            RenderScope("page").id("row", key=42)  # type: ignore[arg-type]


class TestRenderContext:
    def test_nested_context_restores_its_parent(self) -> None:
        outer = RenderContext(scope=RenderScope("outer"))
        inner = RenderContext(scope=RenderScope("inner"))

        assert get_render_context() is None
        with render_context(outer):
            assert get_render_context() is outer
            with render_context(inner):
                assert get_render_context() is inner
            assert get_render_context() is outer
        assert get_render_context() is None

    def test_context_is_restored_after_an_exception(self) -> None:
        context = RenderContext(scope=RenderScope("failure"))

        with pytest.raises(RuntimeError, match="boom"), render_context(context):
            raise RuntimeError("boom")

        assert get_render_context() is None

    @pytest.mark.asyncio
    async def test_interleaved_tasks_keep_independent_scopes(self) -> None:
        barrier = asyncio.Barrier(2)

        async def render(namespace: str) -> tuple[str, str]:
            context = RenderContext(scope=RenderScope(namespace))
            with render_context(context):
                first = get_render_scope().id("item")
                await barrier.wait()
                second = get_render_scope().id("item")
                return first, second

        alpha, beta = await asyncio.gather(render("alpha"), render("beta"))

        assert alpha == ("alpha-item-1", "alpha-item-2")
        assert beta == ("beta-item-1", "beta-item-2")
        assert get_render_context() is None


class TestRendererScopeIntegration:
    def test_one_render_tree_reuses_scope_for_siblings(self) -> None:
        output = render_to_string([_ScopedComponent(), _ScopedComponent()])

        assert 'id="oridecon-item-node-1"' in output
        assert 'id="oridecon-item-node-2"' in output

    def test_separate_renders_reproduce_default_scope_ids(self) -> None:
        first = str(_ScopedComponent())
        second = str(_ScopedComponent())

        assert first == second
        assert 'id="oridecon-item-node-1"' in first

    def test_caller_scope_controls_the_render_tree_namespace(self) -> None:
        context = RenderContext(scope=RenderScope("admin").child("dashboard"))

        with render_context(context):
            output = render_to_string(_ScopedComponent())

        assert 'id="admin-dashboard-item-node-1"' in output
        assert get_render_context() is None


class TestModalRenderScope:
    def test_sibling_modals_receive_unique_linked_ids(self) -> None:
        output = render_to_string(
            [
                Modal("First", render_trigger=False),
                Modal("Second", render_trigger=False),
            ]
        )

        assert 'id="oridecon-modal-dialog-1"' in output
        assert 'id="oridecon-modal-dialog-2"' in output
        assert 'aria-labelledby="oridecon-modal-title-1"' in output
        assert 'aria-labelledby="oridecon-modal-title-2"' in output

    def test_separate_modal_renders_are_stable(self) -> None:
        first = str(Modal("Settings", render_trigger=False))
        second = str(Modal("Settings", render_trigger=False))

        assert first == second
        assert 'id="oridecon-modal-dialog-1"' in first

    def test_explicit_modal_key_reproduces_partial_identity(self) -> None:
        full = str(Modal("Settings", modal_id="account-settings", render_trigger=False))
        partial = str(
            Modal("Settings", modal_id="account-settings", render_trigger=False)
        )

        assert 'id="oridecon-modal-dialog-account-settings"' in full
        assert full == partial

    def test_duplicate_explicit_modal_keys_fail_in_one_tree(self) -> None:
        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            render_to_string(
                [
                    Modal("First", modal_id="settings", render_trigger=False),
                    Modal("Second", modal_id="settings", render_trigger=False),
                ]
            )


class TestSlideOverRenderScope:
    def test_sibling_panels_receive_unique_linked_ids(self) -> None:
        output = render_to_string(
            [
                SlideOver("First", render_trigger=False),
                SlideOver("Second", render_trigger=False),
            ]
        )

        assert 'id="oridecon-slide-over-panel-1"' in output
        assert 'id="oridecon-slide-over-panel-2"' in output
        assert 'aria-labelledby="oridecon-slide-over-title-1"' in output
        assert 'aria-labelledby="oridecon-slide-over-title-2"' in output

    def test_separate_panel_renders_are_stable(self) -> None:
        first = str(SlideOver("Settings", render_trigger=False))
        second = str(SlideOver("Settings", render_trigger=False))

        assert first == second
        assert 'id="oridecon-slide-over-panel-1"' in first

    def test_explicit_panel_key_reproduces_partial_identity(self) -> None:
        full = str(
            SlideOver("Settings", slide_id="account-settings", render_trigger=False)
        )
        partial = str(
            SlideOver("Settings", slide_id="account-settings", render_trigger=False)
        )

        assert 'id="oridecon-slide-over-panel-account-settings"' in full
        assert full == partial

    def test_duplicate_explicit_panel_keys_fail_in_one_tree(self) -> None:
        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            render_to_string(
                [
                    SlideOver("First", slide_id="settings", render_trigger=False),
                    SlideOver("Second", slide_id="settings", render_trigger=False),
                ]
            )
