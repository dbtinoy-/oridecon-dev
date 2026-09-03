"""Conftest for oridecon-contracts tests.

This conftest does NOT depend on importing oridecon itself, allowing
contracts tests to run independently.
"""

from __future__ import annotations

import pytest


@pytest.fixture
def anyio_backend() -> str:
    """Configure anyio to use asyncio by default for all tests."""
    return "asyncio"
