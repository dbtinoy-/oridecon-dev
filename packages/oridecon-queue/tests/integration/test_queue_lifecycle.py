"""Integration tests for oridecon-queue package."""

from __future__ import annotations

import pytest

from oridecon.queue.config import QueueConfig
from oridecon.queue.di.provider import QueueProvider


class TestQueueProviderIntegration:
    """Integration tests for QueueProvider basic functionality."""

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_provider_initialization_default(self):
        """Test QueueProvider initialization with default config."""
        provider = QueueProvider()
        assert provider.name == "queue"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_provider_initialization_with_config(self):
        """Test QueueProvider initialization with custom config."""
        config = QueueConfig()
        provider = QueueProvider(config=config)
        assert provider.name == "queue"

    @pytest.mark.integration
    def test_provider_has_required_attributes(self):
        """Test provider has required attributes."""
        provider = QueueProvider()
        assert hasattr(provider, "name")
        assert hasattr(provider, "config")

    @pytest.mark.integration
    def test_provider_priority(self):
        """Test provider has correct priority."""
        from oridecon.contracts.core.provider import ProviderPriority
        provider = QueueProvider()
        assert provider.priority == ProviderPriority.INFRASTRUCTURE


class TestQueueConfigIntegration:
    """Integration tests for QueueConfig."""

    @pytest.mark.integration
    def test_queue_config_creation(self):
        """Test QueueConfig can be created."""
        config = QueueConfig()
        assert config is not None

    @pytest.mark.integration
    def test_queue_config_model_dump(self):
        """Test QueueConfig model can be serialized."""
        config = QueueConfig()
        config_dict = config.model_dump()
        assert isinstance(config_dict, dict)


class TestQueueModuleIntegration:
    """Integration tests for QueueModule."""

    @pytest.mark.integration
    def test_queue_module_import(self):
        """Test QueueModule can be imported."""
        from oridecon.queue.module import QueueModule
        assert QueueModule is not None

    @pytest.mark.integration
    def test_queue_module_has_configure_method(self):
        """Test QueueModule has configure method."""
        from oridecon.queue.module import QueueModule
        assert hasattr(QueueModule, "configure")


class TestQueueProtocolsIntegration:
    """Integration tests for queue protocols."""

    @pytest.mark.integration
    def test_queue_protocol_import(self):
        """Test QueueProtocol can be imported."""
        from oridecon.contracts.queue import QueueProtocol
        assert QueueProtocol is not None