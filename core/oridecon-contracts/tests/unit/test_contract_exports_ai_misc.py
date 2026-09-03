from __future__ import annotations

import importlib

import pytest

EXPECTED_MODULE_EXPORTS: dict[str, list[str]] = {
    "oridecon.contracts.ai.memory": [
        "ConsolidationError",
        "ConsolidationResult",
        "ConversationMemory",
        "EpisodicMemoryProtocol",
        "MemoryConsolidatorProtocol",
        "MemoryEntry",
        "MemoryProtocol",
        "MemoryQuery",
        "MemorySearchResult",
        "MemoryStoreProtocol",
        "SemanticMemoryProtocol",
        "StorageError",
        "WindowMemory",
        "WorkingMemoryProtocol",
    ],
    "oridecon.contracts.ai.models": ["ModelRequest", "ModelResponse"],
    "oridecon.contracts.ai.multimodal": [
        "ContentPart",
        "ImageBase64Part",
        "ImageUrlPart",
        "MessageContent",
        "TextPart",
    ],
    "oridecon.contracts.ai.providers": [
        "FallbackChainProtocol",
        "ModelInfo",
        "ModelSelectorProtocol",
        "ProviderHealth",
        "ProviderRegistryProtocol",
        "SelectionStrategy",
    ],
    "oridecon.contracts.ai.skills": [
        "SkillDefinition",
        "SkillError",
        "SkillExecutorProtocol",
        "SkillParameter",
        "SkillProtocol",
        "SkillRegistryProtocol",
        "SkillResult",
        "ToolkitProtocol",
    ],
    "oridecon.contracts.auth.guard": [
        "AuthenticatorProtocol",
        "AuthorizerProtocol",
    ],
    "oridecon.contracts.auth.store": [
        "UserReaderProtocol",
        "UserStoreProtocol",
        "UserWriterProtocol",
    ],
    "oridecon.contracts.cli.protocols": ["CliContributorProtocol"],
    "oridecon.contracts.cli.types": ["GeneratorDefinition", "GeneratorOption"],
    "oridecon.contracts.feature_flags.protocols": [
        "FlagManagerProtocol",
        "FlagProviderProtocol",
        "MutableFlagProviderProtocol",
    ],
    "oridecon.contracts.mcp.exceptions": [
        "MCPError",
        "MCPInitializationError",
        "MCPMethodNotFoundError",
        "MCPPromptError",
        "MCPProtocolError",
        "MCPResourceError",
        "MCPToolCallError",
        "MCPTransportError",
    ],
    "oridecon.contracts.mcp.protocols": [
        "MCPAuthorizerProtocol",
        "MCPPromptHandlerProtocol",
        "MCPPromptProviderProtocol",
        "MCPResourceHandlerProtocol",
        "MCPResourceProviderProtocol",
        "MCPServerProtocol",
        "MCPToolHandlerProtocol",
        "MCPToolProviderProtocol",
        "MCPTransportProtocol",
    ],
    "oridecon.contracts.search.models": [
        "DocumentData",
        "IndexSettings",
        "SearchFilters",
    ],
    "oridecon.contracts.search.types": [
        "DocumentData",
        "IndexSettings",
        "SearchFilters",
        "SearchIndexResult",
        "SearchableSpec",
    ],
}


@pytest.mark.parametrize(
    ("module_path", "expected_exports"),
    EXPECTED_MODULE_EXPORTS.items(),
)
def test_module_declares_explicit_all(
    module_path: str,
    expected_exports: list[str],
) -> None:
    module = importlib.import_module(module_path)
    exported = getattr(module, "__all__", None)

    assert isinstance(exported, list)
    assert exported == expected_exports
    for name in exported:
        assert not name.startswith("_")
        assert hasattr(module, name)
