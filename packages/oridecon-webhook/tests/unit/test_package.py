"""Tests for oridecon-webhook module."""

import pytest

from oridecon import webhook as webhook_module


class TestWebhookModule:
    """Test basic webhook module structure."""

    def test_module_imports(self):
        """Test module can be imported."""
        assert webhook_module is not None

    def test_module_has_name(self):
        """Test module has __name__."""
        assert webhook_module.__name__ == "oridecon.webhook"

    def test_module_in_oridecon_packages(self):
        """Test webhook is in oridecon packages."""
        import oridecon
        assert hasattr(oridecon, "webhook")


class TestWebhookSubmodules:
    """Test webhook submodules exist."""

    def test_delivery_module(self):
        from oridecon.webhook import delivery
        assert delivery is not None

    def test_store_module(self):
        from oridecon.webhook import store
        assert store is not None

    def test_config_module(self):
        from oridecon.webhook import config
        assert config is not None

    def test_types_module(self):
        from oridecon.webhook import types
        assert types is not None