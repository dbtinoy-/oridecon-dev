"""Tests for citation and source tracking."""

import pytest
pytest.importorskip("oridecon.ai.rag", reason="oridecon-ai-rag not installed")

from oridecon.ai.rag.citations.core import (
    Citation,
    CitationStyle,
    CitationTracker,
    CitedResponse,
    Source,
    SourceType,
)
