"""Pytest plugin for Oridecon Framework.

This plugin is automatically loaded by pytest via entry points when oridecon-testing
is installed in the environment.
"""

from __future__ import annotations

# Export core fixtures so they are automatically available in all tests
pytest_plugins = [
    "oridecon.testing.fixtures.core",
    "oridecon.testing.fixtures.ai",
    "oridecon.testing.fixtures.db",
    "oridecon.testing.fixtures.messaging",
    "oridecon.testing.fixtures.web",
    "oridecon.testing.fixtures.tasks",
    "oridecon.testing.integration.fixtures",
]
