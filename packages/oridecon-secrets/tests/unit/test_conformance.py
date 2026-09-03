from __future__ import annotations

import pytest

from oridecon.testing.compliance import StoreConformanceSuite
from oridecon.testing.fakes import FakeRotatableSecretStore


class TestFakeStoreConformance(StoreConformanceSuite):
    """Run the conformance suite against the fake store."""

    @pytest.fixture
    def make_store(  # type: ignore[override]
        self,
    ) -> type[FakeRotatableSecretStore]:
        return FakeRotatableSecretStore
