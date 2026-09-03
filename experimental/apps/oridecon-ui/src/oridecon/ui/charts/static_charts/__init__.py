"""Static SVG chart components."""

from __future__ import annotations

from oridecon.ui.charts.static_charts.bar import BarChart as BarChart
from oridecon.ui.charts.static_charts.line import (
    AreaChart as AreaChart,
)
from oridecon.ui.charts.static_charts.line import (
    LineChart as LineChart,
)
from oridecon.ui.charts.static_charts.pie import PieChart as PieChart
from oridecon.ui.charts.static_charts.sparkline import (
    MiniBar as MiniBar,
)
from oridecon.ui.charts.static_charts.sparkline import (
    Sparkline as Sparkline,
)

__all__ = [
    "AreaChart",
    "BarChart",
    "LineChart",
    "MiniBar",
    "PieChart",
    "Sparkline",
]
