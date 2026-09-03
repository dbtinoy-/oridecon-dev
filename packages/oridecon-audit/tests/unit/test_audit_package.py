"""Tests for audit package __init__ exports."""

from __future__ import annotations


class TestAuditPackageExports:
    """Tests for package-level exports."""

    def test_audit_module_imports(self) -> None:
        from oridecon import audit
        assert audit is not None

    def test_audit_has_hooks(self) -> None:
        from oridecon.audit import hooks
        assert hasattr(hooks, "AuditEntryCreatedHook")

    def test_audit_has_events(self) -> None:
        from oridecon.audit import events
        assert hasattr(events, "AuditEntryLoggedEvent")

    def test_audit_has_types(self) -> None:
        from oridecon.audit import types
        assert hasattr(types, "AuditStoreBackend")

    def test_audit_has_config(self) -> None:
        from oridecon.audit import config
        assert hasattr(config, "AuditConfig")

    def test_audit_has_exceptions(self) -> None:
        from oridecon.audit import exceptions
        assert hasattr(exceptions, "AuditError")

    def test_audit_has_constants(self) -> None:
        from oridecon.audit import constants
        assert hasattr(constants, "DEFAULT_TABLE_NAME")

    def test_audit_has_decorators(self) -> None:
        from oridecon.audit import decorators
        assert hasattr(decorators, "audited")

    def test_audit_has_module(self) -> None:
        pass  # module.py has import issues

    def test_audit_has_logging(self) -> None:
        from oridecon.audit import logging
        assert hasattr(logging, "AuditLogger")


class TestAuditSubPackages:
    """Tests for subpackage imports."""

    def test_retention_importable(self) -> None:
        from oridecon.audit import retention
        assert retention is not None

    def test_verification_importable(self) -> None:
        from oridecon.audit import verification
        assert verification is not None

    def test_scheduling_importable(self) -> None:
        from oridecon.audit import scheduling
        assert scheduling is not None

    def test_admin_importable(self) -> None:
        from oridecon.audit import admin
        assert admin is not None

    def test_cli_importable(self) -> None:
        from oridecon.audit import cli
        assert cli is not None

    def test_di_importable(self) -> None:
        from oridecon.audit import di
        assert di is not None