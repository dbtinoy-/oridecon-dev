"""P2 hook surface import verification for oridecon-admin."""

from __future__ import annotations

from dataclasses import FrozenInstanceError, is_dataclass

import pytest


def test_admin_hooks_root_module_exists() -> None:
    import oridecon.admin
    from oridecon.admin.hooks import (
        AdminPanelStartedHook,
        AdminPanelStoppedHook,
        AdminResourceAccessedHook,
    )

    assert AdminPanelStartedHook.__name__ == "AdminPanelStartedHook"
    assert AdminPanelStoppedHook.__name__ == "AdminPanelStoppedHook"
    assert AdminResourceAccessedHook.__name__ == "AdminResourceAccessedHook"
    assert oridecon.admin.AdminPanelStartedHook is AdminPanelStartedHook
    assert oridecon.admin.AdminPanelStoppedHook is AdminPanelStoppedHook
    assert oridecon.admin.AdminResourceAccessedHook is AdminResourceAccessedHook
    assert "AdminPanelStartedHook" in oridecon.admin.__all__
    assert "AdminPanelStoppedHook" in oridecon.admin.__all__
    assert "AdminResourceAccessedHook" in oridecon.admin.__all__


def test_admin_hook_payloads_are_frozen_and_keyword_only() -> None:
    from oridecon.admin.hooks import AdminPanelStartedHook, AdminResourceAccessedHook

    started = AdminPanelStartedHook()
    accessed = AdminResourceAccessedHook(
        resource_name="User", action="list", user_id="u1"
    )

    assert is_dataclass(started)
    assert is_dataclass(accessed)

    with pytest.raises(TypeError):
        AdminResourceAccessedHook("User", "list", "u1")  # type: ignore[misc]

    with pytest.raises(FrozenInstanceError):
        accessed.resource_name = "Order"  # type: ignore[misc]
