"""Overlay form inspection cannot turn plain component strings into markup."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import pytest

from oridecon.ui.core.base import Component, render_to_string
from oridecon.ui.molecules.modal import Modal
from oridecon.ui.organisms.slide_over import SlideOver

_PAYLOAD = '<img src=x onerror="overlayBypass()">'


class _PlainStringComponent(Component):
    def render(self) -> str:
        return _PAYLOAD


OverlayFactory = Callable[[Any], Component]


def _modal_child(child: Any) -> Modal:
    return Modal("Test", render_trigger=False, children=[child])


def _slide_over_child(child: Any) -> SlideOver:
    return SlideOver("Test", render_trigger=False, children=[child])


def _modal_footer(child: Any) -> Modal:
    return Modal("Test", render_trigger=False, footer=[child])


def _slide_over_footer(child: Any) -> SlideOver:
    return SlideOver("Test", render_trigger=False, footer=[child])


@pytest.mark.parametrize(
    "factory",
    [
        pytest.param(_modal_child, id="modal-child"),
        pytest.param(_slide_over_child, id="slide-over-child"),
        pytest.param(_modal_footer, id="modal-footer"),
        pytest.param(_slide_over_footer, id="slide-over-footer"),
    ],
)
def test_plain_component_output_is_escaped(factory: OverlayFactory) -> None:
    output = render_to_string(factory(_PlainStringComponent()))

    assert "<img " not in output
    assert "&lt;img src=x" in output


@pytest.mark.parametrize(
    "factory",
    [
        pytest.param(_modal_child, id="modal-child"),
        pytest.param(_slide_over_child, id="slide-over-child"),
        pytest.param(_modal_footer, id="modal-footer"),
        pytest.param(_slide_over_footer, id="slide-over-footer"),
    ],
)
def test_plain_html_strings_are_escaped(factory: OverlayFactory) -> None:
    output = render_to_string(factory(_PAYLOAD))

    assert "<img " not in output
    assert "&lt;img src=x" in output
