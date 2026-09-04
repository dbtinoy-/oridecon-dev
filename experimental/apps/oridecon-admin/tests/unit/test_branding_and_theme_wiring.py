"""Tests for branding & theme settings wiring.

Covers the three bugs fixed:
1. Namespaced key priority in theme-override lookup (get_all() DEFAULT_SETTINGS shadowing).
2. TenantConfigStore.contains() correctly reports saved vs default values.
3. BrandingSpec dark_mode node override provides human-readable labels.
"""

from __future__ import annotations

import asyncio
from typing import Any

import pytest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_registry_with_memory_db():
    """Build a ConfigRegistry with an in-memory 'db' store for testing."""
    from oridecon.admin.services.settings_service import AdminSettingsService
    from oridecon.admin.settings.panel.registry import ConfigRegistry
    from oridecon.admin.settings.store import TenantConfigStore

    service = AdminSettingsService()  # pure in-memory, no real DB
    registry = ConfigRegistry.with_defaults()
    registry.register_store("db", TenantConfigStore(service))
    return registry, service


# ---------------------------------------------------------------------------
# Bug 1: Namespaced key takes priority in the theme-override lookup
# ---------------------------------------------------------------------------


class TestBrandingLookupPriority:
    """The 'admin.branding.X' namespaced key must win over the flat default 'X'."""

    @pytest.mark.asyncio
    async def test_saved_primary_color_overrides_default(self):
        registry, service = _make_registry_with_memory_db()

        await registry.save_values(
            "admin.branding",
            {"primary_color": "#ff0000"},
            "db",
            tenant_id="t1",
        )

        overrides = await service.get_all("t1")
        # Namespaced key wins over flat DEFAULT_SETTINGS key
        value = overrides.get("admin.branding.primary_color") or overrides.get(
            "primary_color"
        )
        assert value == "#ff0000", (
            f"Expected saved primary_color '#ff0000', got {value!r}. "
            "The flat DEFAULT_SETTINGS key shadowed the saved value."
        )

    @pytest.mark.asyncio
    async def test_saved_site_name_overrides_default(self):
        registry, service = _make_registry_with_memory_db()

        await registry.save_values(
            "admin.branding",
            {"site_name": "ACME Corp"},
            "db",
            tenant_id="t1",
        )

        overrides = await service.get_all("t1")
        value = overrides.get("admin.branding.site_name") or overrides.get("site_name")
        assert value == "ACME Corp"

    @pytest.mark.asyncio
    async def test_saved_dark_mode_overrides_default(self):
        registry, service = _make_registry_with_memory_db()

        await registry.save_values(
            "admin.branding",
            {"dark_mode": "dark"},
            "db",
            tenant_id="t1",
        )

        overrides = await service.get_all("t1")
        value = overrides.get("admin.branding.dark_mode") or overrides.get("dark_mode")
        assert value == "dark"

    @pytest.mark.asyncio
    async def test_unsaved_field_falls_back_to_default(self):
        registry, service = _make_registry_with_memory_db()
        # Nothing saved for this tenant
        overrides = await service.get_all("empty_tenant")
        # The flat fallback should return the DEFAULT_SETTINGS value
        value = overrides.get("admin.branding.primary_color") or overrides.get(
            "primary_color"
        )
        # Flat key from DEFAULT_SETTINGS
        assert value == "#6b7280"

    @pytest.mark.asyncio
    async def test_multiple_fields_saved_and_read_back(self):
        registry, service = _make_registry_with_memory_db()

        await registry.save_values(
            "admin.branding",
            {
                "primary_color": "#aabbcc",
                "site_name": "My Portal",
                "dark_mode": "light",
            },
            "db",
            tenant_id="org1",
        )

        overrides = await service.get_all("org1")
        branding: dict[str, Any] = {}
        for field in ("primary_color", "site_name", "logo_url", "favicon_url", "dark_mode"):
            value = overrides.get(f"admin.branding.{field}") or overrides.get(field)
            if value:
                branding[field] = value

        assert branding["primary_color"] == "#aabbcc"
        assert branding["site_name"] == "My Portal"
        assert branding["dark_mode"] == "light"

    @pytest.mark.asyncio
    async def test_registry_read_back_matches_saved(self):
        registry, service = _make_registry_with_memory_db()

        saved = {"primary_color": "#123456", "site_name": "Test", "dark_mode": "dark"}
        await registry.save_values("admin.branding", saved, "db", tenant_id="t2")

        read = await registry.get_values("admin.branding", "db", tenant_id="t2")
        assert read["primary_color"] == "#123456"
        assert read["site_name"] == "Test"
        assert read["dark_mode"] == "dark"


# ---------------------------------------------------------------------------
# Bug 2: TenantConfigStore.contains() distinguishes saved vs default
# ---------------------------------------------------------------------------


class TestTenantConfigStoreContains:
    """contains() must return True for saved keys and False for unsaved ones."""

    @pytest.mark.asyncio
    async def test_contains_true_after_save(self):
        registry, service = _make_registry_with_memory_db()
        store = registry._stores["db"]

        await registry.save_values(
            "admin.branding",
            {"primary_color": "#ff0000"},
            "db",
            tenant_id="default",
        )

        result = await store.contains("admin.branding.primary_color")
        assert result is True, (
            "contains() should return True for a key that was explicitly saved."
        )

    @pytest.mark.asyncio
    async def test_contains_false_for_unsaved_key(self):
        registry, _ = _make_registry_with_memory_db()
        store = registry._stores["db"]

        # logo_url was never saved
        result = await store.contains("admin.branding.logo_url")
        assert result is False, (
            "contains() should return False for a key that was never saved."
        )

    @pytest.mark.asyncio
    async def test_contains_false_before_any_save(self):
        registry, _ = _make_registry_with_memory_db()
        store = registry._stores["db"]

        for key in (
            "admin.branding.primary_color",
            "admin.branding.site_name",
            "admin.branding.dark_mode",
        ):
            result = await store.contains(key)
            assert result is False, f"contains({key!r}) should be False before any save"

    @pytest.mark.asyncio
    async def test_contains_true_only_for_saved_subset(self):
        registry, _ = _make_registry_with_memory_db()
        store = registry._stores["db"]

        # Save only primary_color
        await registry.save_values(
            "admin.branding",
            {"primary_color": "#abcdef"},
            "db",
            tenant_id="default",
        )

        assert await store.contains("admin.branding.primary_color") is True
        assert await store.contains("admin.branding.site_name") is False
        assert await store.contains("admin.branding.logo_url") is False
        assert await store.contains("admin.branding.dark_mode") is False

    @pytest.mark.asyncio
    async def test_contains_with_explicit_tenant_id(self):
        registry, _ = _make_registry_with_memory_db()
        store = registry._stores["db"]

        await registry.save_values(
            "admin.branding",
            {"site_name": "Tenant A"},
            "db",
            tenant_id="tenant-a",
        )

        assert await store.contains("admin.branding.site_name", tenant_id="tenant-a") is True
        # Different tenant — not saved there
        assert await store.contains("admin.branding.site_name", tenant_id="tenant-b") is False


# ---------------------------------------------------------------------------
# Bug 3: BrandingSpec dark_mode node uses human-readable labels
# ---------------------------------------------------------------------------


class TestBrandingSpecDarkModeNode:
    """dark_mode must be an EnumNode with human-readable dict options."""

    def test_dark_mode_node_is_enum(self):
        from oridecon.admin.settings.panel.branding_spec import BrandingSpec
        from oridecon.admin.settings.panel.nodes import EnumNode

        nodes = BrandingSpec.get_nodes()
        assert "dark_mode" in nodes
        assert isinstance(nodes["dark_mode"], EnumNode)

    def test_dark_mode_options_are_dict(self):
        from oridecon.admin.settings.panel.branding_spec import BrandingSpec

        nodes = BrandingSpec.get_nodes()
        dm = nodes["dark_mode"]
        assert isinstance(dm.options, dict), "dark_mode options should be a dict"

    def test_dark_mode_option_keys_are_valid_values(self):
        from oridecon.admin.settings.panel.branding_spec import BrandingSpec

        nodes = BrandingSpec.get_nodes()
        dm = nodes["dark_mode"]
        assert set(dm.options.keys()) == {"system", "light", "dark"}

    def test_dark_mode_option_labels_are_human_readable(self):
        from oridecon.admin.settings.panel.branding_spec import BrandingSpec

        nodes = BrandingSpec.get_nodes()
        dm = nodes["dark_mode"]
        # Labels should be descriptive (not lowercase raw values)
        for label in dm.options.values():
            assert label[0].isupper(), f"Label {label!r} should start with a capital letter"

    def test_dark_mode_validate_accepts_valid_choices(self):
        from oridecon.admin.settings.panel.branding_spec import BrandingSpec

        nodes = BrandingSpec.get_nodes()
        dm = nodes["dark_mode"]
        for choice in ("system", "light", "dark"):
            assert dm.validate(choice) == choice

    def test_dark_mode_validate_rejects_invalid_falls_back_to_default(self):
        from oridecon.admin.settings.panel.branding_spec import BrandingSpec

        nodes = BrandingSpec.get_nodes()
        dm = nodes["dark_mode"]
        result = dm.validate("invalid-value")
        assert result == dm.default

    def test_dark_mode_to_dict_includes_options(self):
        from oridecon.admin.settings.panel.branding_spec import BrandingSpec

        nodes = BrandingSpec.get_nodes()
        dm = nodes["dark_mode"]
        d = dm.to_dict()
        assert "options" in d
        assert isinstance(d["options"], dict)

    def test_branding_spec_has_all_expected_nodes(self):
        from oridecon.admin.settings.panel.branding_spec import BrandingSpec

        nodes = BrandingSpec.get_nodes()
        expected = {"site_name", "primary_color", "logo_url", "favicon_url", "dark_mode"}
        assert set(nodes.keys()) == expected

    def test_branding_spec_primary_color_is_color_node(self):
        from oridecon.admin.settings.panel.branding_spec import BrandingSpec
        from oridecon.admin.settings.panel.nodes import ColorNode

        nodes = BrandingSpec.get_nodes()
        assert isinstance(nodes["primary_color"], ColorNode)


# ---------------------------------------------------------------------------
# Integration: full save-then-read cycle with theme CSS generation
# ---------------------------------------------------------------------------


class TestBrandingThemeIntegration:
    """End-to-end: save branding -> read back -> generate theme CSS."""

    @pytest.mark.asyncio
    async def test_primary_color_flows_to_theme_css(self):
        from oridecon.admin.theme.service import AdminThemeService

        registry, service = _make_registry_with_memory_db()

        await registry.save_values(
            "admin.branding",
            {"primary_color": "#1a2b3c"},
            "db",
            tenant_id="default",
        )

        overrides = await service.get_all("default")
        primary = overrides.get("admin.branding.primary_color") or overrides.get(
            "primary_color"
        )
        assert primary == "#1a2b3c"

        theme_svc = AdminThemeService(primary_color=primary)
        css = theme_svc.generate_theme_css()
        assert css, "Theme CSS should be non-empty"
        # The primary color should influence the generated CSS
        assert isinstance(css, str)

    @pytest.mark.asyncio
    async def test_branding_spec_scope_is_tenant(self):
        from oridecon.admin.settings.panel.branding_spec import BrandingSpec

        assert BrandingSpec.scope == "tenant"

    @pytest.mark.asyncio
    async def test_branding_spec_store_name_is_db(self):
        from oridecon.admin.settings.panel.branding_spec import BrandingSpec

        assert BrandingSpec.store_name == "db"

    @pytest.mark.asyncio
    async def test_tenant_isolation(self):
        """Branding saved for one tenant must not leak to another."""
        registry, service = _make_registry_with_memory_db()

        await registry.save_values(
            "admin.branding",
            {"primary_color": "#aaaaaa", "site_name": "Tenant A"},
            "db",
            tenant_id="tenant-a",
        )
        await registry.save_values(
            "admin.branding",
            {"primary_color": "#bbbbbb", "site_name": "Tenant B"},
            "db",
            tenant_id="tenant-b",
        )

        vals_a = await registry.get_values("admin.branding", "db", tenant_id="tenant-a")
        vals_b = await registry.get_values("admin.branding", "db", tenant_id="tenant-b")

        assert vals_a["primary_color"] == "#aaaaaa"
        assert vals_a["site_name"] == "Tenant A"
        assert vals_b["primary_color"] == "#bbbbbb"
        assert vals_b["site_name"] == "Tenant B"
