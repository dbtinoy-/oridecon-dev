"""Test fixtures for oridecon-testing."""
import pytest

from oridecon.testing import TestEnvironment


@pytest.fixture
def test_env():
    """Create a clean test environment."""
    return TestEnvironment()