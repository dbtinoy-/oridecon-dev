import importlib

import pytest


def test_importing_oridecon_runtime_raises():
    # After removing the compatibility shim, importing `oridecon.runtime` should fail
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("oridecon.runtime")


def test_core_submodules_available_directly():
    # Core functionality should be available directly under `oridecon` (no shim required)
    import oridecon.resilience as core_res
    import oridecon.testing as core_testing

    assert hasattr(core_res, "RetryConfig")

    # Basic shared API keys exist in core testing
    shared = set(getattr(core_testing, "__all__", []))
    assert "TestEnvironment" in shared or hasattr(core_testing, "TestEnvironment")
