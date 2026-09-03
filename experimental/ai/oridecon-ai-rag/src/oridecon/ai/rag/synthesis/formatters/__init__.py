"""Response formatters package.

This package provides various formatters for synthesis results, including
plain text, Markdown, and JSON output.
"""

from __future__ import annotations

from oridecon.ai.rag.synthesis.formatters.base import ResponseFormatterProtocol
from oridecon.ai.rag.synthesis.formatters.json import JSONFormatter
from oridecon.ai.rag.synthesis.formatters.markdown import MarkdownFormatter
from oridecon.ai.rag.synthesis.formatters.text import PlainTextFormatter

__all__ = [
    "JSONFormatter",
    "MarkdownFormatter",
    "PlainTextFormatter",
    "ResponseFormatterProtocol",
]
