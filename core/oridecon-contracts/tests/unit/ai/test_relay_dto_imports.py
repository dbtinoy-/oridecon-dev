"""DTO package import compatibility tests for the relay contracts."""
from __future__ import annotations

import pytest


def test_every_public_dto_importable_from_package() -> None:
    """All previously public DTO names resolve from the stable package path."""
    from oridecon.contracts.ai.relay.dto import (  # noqa: F401
        ClaudeContent,
        ClaudeMessage,
        ClaudeRequest,
        GeminiContent,
        GeminiPart,
        GeminiRequest,
        OpenAIChatMessage,
        OpenAIChatRequest,
        ResponsesItem,
        ResponsesRequest,
        ResponsesResponse,
    )


@pytest.mark.parametrize(
    ("module", "names"),
    [
        (
            "oridecon.contracts.ai.relay.dto.openai_chat",
            ["OpenAIChatMessage", "OpenAIChatRequest"],
        ),
        (
            "oridecon.contracts.ai.relay.dto.openai_responses",
            ["ResponsesItem", "ResponsesRequest", "ResponsesResponse"],
        ),
        (
            "oridecon.contracts.ai.relay.dto.claude",
            ["ClaudeContent", "ClaudeMessage", "ClaudeRequest"],
        ),
        (
            "oridecon.contracts.ai.relay.dto.gemini",
            ["GeminiPart", "GeminiContent", "GeminiRequest"],
        ),
    ],
)
def test_protocol_names_importable_from_focused_module(
    module: str,
    names: list[str],
) -> None:
    """Each DTO family is importable from its focused submodule."""
    import importlib

    mod = importlib.import_module(module)
    for name in names:
        assert hasattr(mod, name)


def test_common_module_exports_helpers() -> None:
    """Shared helpers live in the common module."""
    from oridecon.contracts.ai.relay.dto.common import JsonDict

    sample: JsonDict = {"a": 1}
    assert isinstance(sample, dict)


def test_relay_dto_package_does_not_import_implementations() -> None:
    """Importing the DTO package must not load AI extension implementations."""
    import subprocess
    import sys
    from pathlib import Path

    contracts_root = Path(__file__).resolve().parents[4]
    src = contracts_root / "oridecon-contracts" / "src"
    script = (
        "import sys; "
        "sys.path.insert(0, {src!r}); "
        "import oridecon.contracts.ai.relay.dto; "
        "loaded = sorted(m for m in sys.modules if m.startswith(('oridecon.ai.relay', 'oridecon.ai.llm'))); "
        "assert not loaded, loaded"
    ).format(src=str(src))
    result = subprocess.run(
        [sys.executable, "-c", script],
        capture_output=True,
        text=True,
        cwd=str(contracts_root),
    )
    assert result.returncode == 0, result.stderr


def test_dto_imports_via_relay_module() -> None:
    """DTO families are also reachable through the relay package root."""
    from oridecon.contracts.ai.relay import (  # noqa: F401
        ClaudeRequest,
        GeminiRequest,
        OpenAIChatRequest,
        ResponsesRequest,
    )

    assert ClaudeRequest is not None