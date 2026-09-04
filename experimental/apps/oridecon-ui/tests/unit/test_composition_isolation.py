"""Implicit composition compatibility state stays task-local and recoverable."""

from __future__ import annotations

import asyncio

import pytest

from oridecon.ui.core.base import Component, NoContext, el


class _Container(Component):
    def render(self):
        return el("div", *self.children)


@pytest.mark.asyncio
async def test_interleaved_component_contexts_keep_their_own_children() -> None:
    """Two tasks may compose concurrently without crossing parent trees."""
    both_entered = asyncio.Event()
    entered = 0

    async def build(marker: str) -> _Container:
        nonlocal entered
        parent = _Container()
        with parent:
            entered += 1
            if entered == 2:
                both_entered.set()
            await both_entered.wait()
            el("span", marker)
        return parent

    first, second = await asyncio.gather(build("first"), build("second"))

    assert len(first.children) == 1
    assert first.children[0].children == ["first"]
    assert len(second.children) == 1
    assert second.children[0].children == ["second"]


@pytest.mark.asyncio
async def test_no_context_only_suppresses_registration_in_its_own_task() -> None:
    """One task's explicit suppression must not disable another task's tree."""
    suppression_active = asyncio.Event()
    second_finished = asyncio.Event()
    first = _Container()
    second = _Container()

    async def build_first() -> None:
        with first:
            with NoContext():
                suppression_active.set()
                await second_finished.wait()
                el("span", "suppressed")
            el("span", "first")

    async def build_second() -> None:
        await suppression_active.wait()
        with second:
            el("span", "second")
        second_finished.set()

    await asyncio.gather(build_first(), build_second())

    assert [child.children for child in first.children] == [["first"]]
    assert [child.children for child in second.children] == [["second"]]


def test_nested_contexts_restore_the_parent_after_inner_exit() -> None:
    outer = _Container()
    with outer:
        with _Container() as inner:
            el("span", "inner")
        el("span", "outer")

    assert outer.children[0] is inner
    assert inner.children[0].children == ["inner"]
    assert outer.children[1].children == ["outer"]


def test_context_tokens_restore_state_after_exceptions() -> None:
    parent = _Container()

    with pytest.raises(ValueError, match="stop"):
        with parent:
            raise ValueError("stop")

    el("span", "orphan")
    assert parent.children == []

    with parent:
        with pytest.raises(ValueError, match="suppressed block"):
            with NoContext():
                raise ValueError("suppressed block")
        el("span", "attached")

    assert parent.children[0].children == ["attached"]


def test_mismatched_exit_fails_and_clears_poisoned_descendants() -> None:
    outer = _Container()
    outer.__enter__()
    inner = _Container()
    inner.__enter__()

    with pytest.raises(RuntimeError, match="LIFO"):
        outer.__exit__(None, None, None)

    orphan = el("span", "orphan")
    assert orphan not in outer.children
    assert orphan not in inner.children
