"""Tests for store module lazy loading."""

from __future__ import annotations

import pytest

from oridecon.audit.store import InMemoryAuditStore, SqlAuditStore


class TestStoreModuleLazyLoading:
    """Tests for store module __getattr__."""

    def test_inmemory_store_importable(self) -> None:
        assert InMemoryAuditStore is not None

    def test_sql_store_importable(self) -> None:
        assert SqlAuditStore is not None

    def test_sql_store_is_same_as_direct_import(self) -> None:
        from oridecon.audit.store.sql import SqlAuditStore as DirectImport
        assert SqlAuditStore is DirectImport

    def test_invalid_attribute_raises(self) -> None:
        from oridecon.audit import store
        with pytest.raises(AttributeError):
            store.NonExistentClass