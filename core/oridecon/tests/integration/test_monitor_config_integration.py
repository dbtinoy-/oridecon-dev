"""Tests that OrideconConfig accepts monitor configuration when monitor package is available."""

import pytest

from oridecon.config import OrideconConfig

try:
    from oridecon.monitor.config import BackendType, MonitorProviderConfig

    HAS_MONITOR = True
except ImportError:
    HAS_MONITOR = False


@pytest.mark.integration
@pytest.mark.skipif(not HAS_MONITOR, reason="monitor package not available")
def test_oridecon_config_accepts_monitor():
    cfg = OrideconConfig(
        monitor=MonitorProviderConfig(backend_type=BackendType.PROMETHEUS),
    )
    assert cfg.monitor is not None
    assert cfg.monitor.backend_type == BackendType.PROMETHEUS
