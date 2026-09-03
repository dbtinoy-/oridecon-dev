"""P2 hook surface import verification for oridecon-nosql."""

from __future__ import annotations

from dataclasses import FrozenInstanceError, is_dataclass

import pytest


def test_nosql_hooks_root_module_exists() -> None:
    import oridecon.nosql
    from oridecon.nosql.hooks import (
        NoSQLConnectedHook,
        NoSQLDisconnectedHook,
    )

    assert NoSQLConnectedHook.__name__ == "NoSQLConnectedHook"
    assert NoSQLDisconnectedHook.__name__ == "NoSQLDisconnectedHook"
    assert oridecon.nosql.NoSQLConnectedHook is NoSQLConnectedHook
    assert oridecon.nosql.NoSQLDisconnectedHook is NoSQLDisconnectedHook


def test_nosql_hook_payloads_are_frozen_and_keyword_only() -> None:
    from oridecon.nosql.hooks import NoSQLConnectedHook

    hook = NoSQLConnectedHook(backend="mongodb")

    assert is_dataclass(hook)

    with pytest.raises(TypeError):
        NoSQLConnectedHook("mongodb")  # type: ignore[misc]

    with pytest.raises(FrozenInstanceError):
        hook.backend = "neo4j"  # type: ignore[misc]
