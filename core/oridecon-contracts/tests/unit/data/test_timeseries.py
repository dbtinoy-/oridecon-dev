"""Tests for timeseries protocols."""

from __future__ import annotations

from oridecon.contracts.data.timeseries import TimeSeriesStoreProtocol


class TestTimeseriesExports:
    """Tests for timeseries module exports."""

    def test_protocol_exported(self) -> None:
        """Verify protocol is exported."""
        from oridecon.contracts.data.timeseries import TimeSeriesStoreProtocol

        assert TimeSeriesStoreProtocol is not None
        assert hasattr(TimeSeriesStoreProtocol, "insert")
        assert hasattr(TimeSeriesStoreProtocol, "query")
        assert hasattr(TimeSeriesStoreProtocol, "connect")
        assert hasattr(TimeSeriesStoreProtocol, "disconnect")