"""Component gallery: renders every oridecon-ui component as HTML pages.

The gallery is the substrate for axe-core accessibility scans (Phase 1 of
the professional-grade plan). Each component is rendered through
``render_to_string`` and wrapped in a full document with the real design
tokens injected via ``shadcn_css`` so axe can measure computed contrast,
focus styles, and semantic structure.
"""

from __future__ import annotations

from oridecon.ui.atoms.badge import Badge
from oridecon.ui.atoms.button import Button
from oridecon.ui.atoms.divider import Divider
from oridecon.ui.atoms.fieldset import Fieldset
from oridecon.ui.atoms.icon import Icon
from oridecon.ui.atoms.inputs import (
    Checkbox,
    NumberInput,
    PasswordInput,
    Radio,
    Select,
    TextArea,
    TextInput,
)
from oridecon.ui.atoms.label import Label
from oridecon.ui.atoms.layout import Col, Row
from oridecon.ui.atoms.link import Link
from oridecon.ui.atoms.progress_bar import ProgressBar
from oridecon.ui.atoms.skeleton import Skeleton
from oridecon.ui.atoms.spinner import Spinner
from oridecon.ui.atoms.switch import Switch
from oridecon.ui.atoms.tooltip import Tooltip
from oridecon.ui.charts import BarChart, LineChart, PieChart, Sparkline
from oridecon.ui.charts.types import ChartDataPoint
from oridecon.ui.core.base import el
from oridecon.ui.molecules.alert import Alert
from oridecon.ui.molecules.card import Card
from oridecon.ui.molecules.dropdown import Dropdown
from oridecon.ui.molecules.modal import Modal
from oridecon.ui.molecules.pagination import Pagination
from oridecon.ui.molecules.tabs import TabPanel, Tabs
from oridecon.ui.molecules.toast import InlineToast
from oridecon.ui.organisms.forms import Form
from oridecon.ui.organisms.slide_over import SlideOver
from oridecon.ui.styles.theme import shadcn_css


def build_gallery() -> dict[str, str]:
    """Return {component_name: full HTML page} for every component."""
    panels: list[tuple[str, object]] = [
        ("Alert", Alert("Operation complete")),
        ("Badge", Badge("New")),
        (
            "BarChart",
            BarChart(
                [
                    ChartDataPoint("Jan", 42, "chart-1"),
                    ChartDataPoint("Feb", 68, "chart-2"),
                    ChartDataPoint("Mar", 33, "chart-3"),
                ]
            ),
        ),
        ("Button", Button("Save")),
        ("Card", Card(title="Card title", content="Card body content")),
        ("Checkbox", Checkbox(name="agree", label="Agree")),
        ("Divider", Divider()),
        ("Dropdown", Dropdown("Menu", items=["Item 1", "Item 2"])),
        (
            "Fieldset",
            Fieldset(TextInput(name="username", label="Username"), legend="Account"),
        ),
        (
            "Form",
            Form(children=[TextInput(name="field", label="Field")], action_url="/save"),
        ),
        ("Icon", Icon(name="check")),
        ("InlineToast", InlineToast("Saved successfully")),
        ("Label", Label("Name")),
        ("Layout", Row(Col("Cell A"), Col("Cell B"))),
        (
            "LineChart",
            LineChart(
                [
                    ChartDataPoint("Jan", 42, "chart-1"),
                    ChartDataPoint("Feb", 68, "chart-2"),
                    ChartDataPoint("Mar", 33, "chart-3"),
                ]
            ),
        ),
        ("Link", Link("Home", href="/")),
        (
            "Modal",
            Modal(
                title="Dialog",
                trigger="Open",
                is_open=True,
                footer=[Button("Close", size="sm")],
            ),
        ),
        ("NumberInput", NumberInput(name="count", label="Count")),
        ("Pagination", Pagination(page=1, total=45, per_page=20)),
        ("PasswordInput", PasswordInput(name="pw", label="Password")),
        (
            "PieChart",
            PieChart(
                [
                    ChartDataPoint("Alpha", 30, "chart-1"),
                    ChartDataPoint("Beta", 50, "chart-2"),
                    ChartDataPoint("Gamma", 20, "chart-3"),
                ]
            ),
        ),
        ("ProgressBar", ProgressBar(value=60)),
        ("Radio", Radio(name="r", choices=[("a", "Alpha"), ("b", "Beta")])),
        (
            "Select",
            Select(
                name="s", label="Choose one", choices=[("a", "Alpha"), ("b", "Beta")]
            ),
        ),
        ("Skeleton", Skeleton()),
        ("SlideOver", SlideOver(title="Panel", trigger="Open", is_open=True)),
        (
            "Sparkline",
            Sparkline(
                [
                    ChartDataPoint("P1", 10, "chart-1"),
                    ChartDataPoint("P2", 25, "chart-2"),
                    ChartDataPoint("P3", 18, "chart-3"),
                ]
            ),
        ),
        ("Spinner", Spinner()),
        ("Switch", Switch("Toggle setting", name="toggle")),
        (
            "Tabs",
            Tabs(
                [("Overview", "overview"), ("Details", "details")],
                active_tab="overview",
                tabs_id="gallery-tabs",
                children=[
                    TabPanel("overview", "Overview content"),
                    TabPanel("details", "Details content"),
                ],
            ),
        ),
        ("TextArea", TextArea(name="notes", label="Notes")),
        ("TextInput", TextInput(name="name", label="Name")),
        (
            "Tooltip",
            Tooltip(
                "More info here",
                el("button", "More information", id="gallery-tooltip-trigger"),
            ),
        ),
    ]

    pages: dict[str, str] = {}
    for name, component in panels:
        pages[name] = render_page(component)
    return pages


def render_page(component: object) -> str:
    """Wrap a rendered component in a full HTML document with design tokens."""
    from oridecon.ui.core.base import render_to_string

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Component: {type(component).__name__}</title>
<script src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.4/dist/htmx.min.js"></script>
<script src="https://cdn.tailwindcss.com"></script>
<script>tailwind.config = {{ darkMode: 'class' }}</script>
<script defer src="https://cdn.jsdelivr.net/npm/@alpinejs/focus@3.14.0/dist/cdn.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.14.0/dist/cdn.min.js"></script>
<style>
{shadcn_css()}
:root {{ color-scheme: light; }}
.dark {{ color-scheme: dark; }}
[x-cloak] {{ display: none !important; }}
body {{ font-family: var(--font-sans); margin: 2rem; background: var(--background); color: var(--foreground); }}
</style>
</head>
<body>
{render_to_string(component)}
</body>
</html>"""
