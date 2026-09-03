"""Tests for monitor module."""

import pytest
from oridecon.monitor import MonitorModule
from oridecon.di.module import DynamicModule


class TestMonitorModule:
    def test_monitor_module_exists(self) -> None:
        assert MonitorModule is not None

    def test_configure_defaults_to_noop_backend(self) -> None:
        """configure() with no backend defaults to NoOpMetricsBackend."""
        from oridecon.observability.core import NoOpMetricsBackend

        result = MonitorModule.configure(None)
        assert isinstance(result, DynamicModule)
        provider = result.providers[0]
        assert isinstance(provider.backend, NoOpMetricsBackend)
