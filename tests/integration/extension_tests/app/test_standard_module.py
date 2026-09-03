from __future__ import annotations

from oridecon.app.base import Application
from oridecon.app.standard import StandardModule
from oridecon.config.main import OrideconConfig
from oridecon.contracts.core.serialization import JsonSerializerProtocol


def test_standard_module_re_exports_core_exports() -> None:
    """StandardModule should expose the core exports it extends."""
    dynamic_module = StandardModule.configure()

    assert Application in dynamic_module.exports
    assert OrideconConfig in dynamic_module.exports
    assert JsonSerializerProtocol in dynamic_module.exports
