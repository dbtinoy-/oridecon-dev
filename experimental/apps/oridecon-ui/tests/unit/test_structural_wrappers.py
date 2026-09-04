"""Framework wrappers preserve typed children instead of laundering HTML trust."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import pytest

from oridecon.ui.atoms.fieldset import Fieldset
from oridecon.ui.atoms.layout import Aside, Col, Container, Grid, Row
from oridecon.ui.core.base import Component, render_to_string
from oridecon.ui.core.trusted_html import trusted_html
from oridecon.ui.molecules.card import Card
from oridecon.ui.molecules.popover import Popover
from oridecon.ui.molecules.section import Section
from oridecon.ui.organisms.admin import AdminCard, PageLayout

_PAYLOAD = "<script>nestedRenderBypass()</script>"


class _PlainStringComponent(Component):
    """Return HTML-looking text without an explicit trust capability."""

    def render(self) -> str:
        return _PAYLOAD


def _popover(child: Any) -> Popover:
    popover = Popover(trigger="Open")
    popover.children = [child]
    return popover


def _card_action(child: Any) -> Card:
    card = Card(content="Body")
    card.props["actions"] = [child]
    return card


WrapperFactory = Callable[[Any], Any]


@pytest.mark.parametrize(
    ("factory"),
    [
        pytest.param(Row, id="row"),
        pytest.param(Col, id="column"),
        pytest.param(Aside, id="aside"),
        pytest.param(Grid, id="grid"),
        pytest.param(Container, id="container"),
        pytest.param(lambda child: Fieldset(child, legend="Details"), id="fieldset"),
        pytest.param(lambda child: Section(child, title="Details"), id="section"),
        pytest.param(_popover, id="popover"),
        pytest.param(lambda child: Card(content=child), id="card-content"),
        pytest.param(lambda child: Card(footer=child), id="card-footer"),
        pytest.param(_card_action, id="card-action"),
        pytest.param(lambda child: AdminCard(content=child), id="admin-card-content"),
        pytest.param(
            lambda child: PageLayout(children=child), id="page-layout-content"
        ),
        pytest.param(
            lambda child: PageLayout(actions=[child]), id="page-layout-action"
        ),
    ],
)
def test_plain_component_strings_remain_text(factory: WrapperFactory) -> None:
    output = render_to_string(factory(_PlainStringComponent()))

    assert "<script>" not in output
    assert "&lt;script&gt;nestedRenderBypass()&lt;/script&gt;" in output


@pytest.mark.parametrize(
    "wrapper",
    [
        pytest.param(Card(content=_PAYLOAD), id="card-content"),
        pytest.param(Card(footer=_PAYLOAD), id="card-footer"),
        pytest.param(AdminCard(content=_PAYLOAD), id="admin-card-content"),
    ],
)
def test_plain_html_strings_are_escaped(wrapper: Any) -> None:
    output = render_to_string(wrapper)

    assert "<script>" not in output
    assert "&lt;script&gt;nestedRenderBypass()&lt;/script&gt;" in output


def test_explicit_trusted_html_remains_verbatim() -> None:
    markup = trusted_html("<strong>owned markup</strong>", source="test fixture")

    assert "<strong>owned markup</strong>" in render_to_string(Card(content=markup))
