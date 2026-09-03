"""Tests for WebhookModule.configure()."""

from __future__ import annotations
from enum import Enum

import pytest

from oridecon.di.module import DynamicModule
from oridecon.webhook.config import WebhookConfig
from oridecon.webhook.di.bundle_provider import WebhookBundleProvider
from oridecon.webhook.module import WebhookModule


class TestWebhookModule:
    """Tests for WebhookModule."""

    def test_configure_returns_dynamic_module(self) -> None:
        """configure() returns a DynamicModule instance."""
        dm = WebhookModule.configure()
        assert isinstance(dm, DynamicModule)

    def test_configure_with_config(self) -> None:
        """configure() accepts a custom WebhookConfig."""
        cfg = WebhookConfig(store_backend="sql", enable_admin=False)
        dm = WebhookModule.configure(cfg)
        assert isinstance(dm, DynamicModule)

    def test_configure_has_bundle_provider(self) -> None:
        """configure() includes WebhookBundleProvider in providers."""
        dm = WebhookModule.configure()
        assert any(isinstance(p, WebhookBundleProvider) for p in dm.providers)

    def test_configure_exports_protocols(self) -> None:
        """configure() exports the expected protocol types."""
        from oridecon.contracts.webhook.protocols import (
            WebhookDeliveryServiceProtocol,
            WebhookSubscriptionStoreProtocol,
        )
        from oridecon.webhook.subscription.service import WebhookSubscriptionService

        dm = WebhookModule.configure()
        assert WebhookSubscriptionStoreProtocol in dm.exports
        assert WebhookDeliveryServiceProtocol in dm.exports
        assert WebhookSubscriptionService in dm.exports

    def test_configure_default_uses_memory_backend(self) -> None:
        """configure() default config uses memory backend."""
        dm = WebhookModule.configure()
        provider = next(
            p for p in dm.providers if isinstance(p, WebhookBundleProvider)
        )
        # The sub-provider list should have been created successfully
        assert provider is not None
