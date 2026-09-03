"""LLM module exports."""

from __future__ import annotations

import importlib.metadata
from typing import TYPE_CHECKING, Any

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from oridecon.ai.llm.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.ai.llm.caching.core import (
        CacheEntry,
        CacheStats,
        LLMCache,
        RedisLLMCache,
    )
    from oridecon.ai.llm.clients.anthropic import AnthropicClient
    from oridecon.ai.llm.clients.cohere import CohereClient
    from oridecon.ai.llm.clients.groq import GroqClient
    from oridecon.ai.llm.clients.mistral import MistralClient
    from oridecon.ai.llm.clients.ollama import OllamaClient
    from oridecon.ai.llm.clients.openai import OpenAIClient
    from oridecon.ai.llm.clients.openrouter import OpenRouterClient
    from oridecon.ai.llm.config import ClientConfig
    from oridecon.ai.llm.conversation.manager import (
        ConversationConfig,
        ConversationManager,
        ConversationStats,
    )
    from oridecon.ai.llm.events import LLMCompletionEvent
    from oridecon.ai.llm.extraction.extractor import InstructorExtractor
    from oridecon.ai.llm.hooks import (
        LLMProviderRegisteredHook,
        LLMRequestSentHook,
        LLMResponseReceivedHook,
    )
from oridecon.ai.llm.pricing import (
    AbstractPricingSource,
    JSONFilePricingSource,
    StaticPricingSource,
)
from oridecon.ai.llm.pricing.registry import TokenCounterRegistry
from oridecon.ai.llm.protocols import LLMCacheProtocol
from oridecon.ai.llm.rate_limiting.core import RateLimiter
from oridecon.ai.llm.registry.core import ProviderInfo, ProviderRegistry
from oridecon.ai.llm.routing.config import (
    GenerationDefaults,
    LLMConfig,
    LogConfig,
    ProviderConfig,
    QuotaConfig,
)
from oridecon.ai.llm.security.core import (
    OutputFilter,
    SecureLLMClient,
    SecurePromptTemplate,
    create_assistant_template,
    create_data_extraction_template,
)
from oridecon.ai.llm.selection.core import (
    ModelCapabilities,
    ModelSelector,
    SelectionCriteria,
    SelectionStrategy,
    create_balanced_selector,
    create_cost_optimized_selector,
    create_quality_optimized_selector,
)
from oridecon.ai.llm.structured.exceptions import (
    ParseError,
    SchemaValidationError,
    StructuredOutputError,
)
from oridecon.ai.llm.structured.extractor import JSONExtractor
from oridecon.ai.llm.structured.formatter import ResponseFormatter
from oridecon.ai.llm.structured.parser import StructuredOutputParser
from oridecon.ai.llm.structured.utils import (
    complete_with_json,
    complete_with_schema,
    create_json_mode_messages,
)
from oridecon.ai.llm.types import (
    ChatMessage,
    Completion,
    FunctionCall,
    LLMError,
    Role,
    StreamChunk,
    TokenUsage,
    ToolCall,
)
from oridecon.contracts.ai.multimodal import (
    ContentPart,
    ImageBase64Part,
    ImageUrlPart,
    MessageContent,
    TextPart,
)

_LAZY_IMPORTS: dict[str, str] = {
    "normalize_thinking_text": "oridecon.ai.llm.thinking",
    # Events
    "LLMCompletionEvent": "oridecon.ai.llm.events",
    # Hooks
    "LLMProviderRegisteredHook": "oridecon.ai.llm.hooks",
    "LLMRequestSentHook": "oridecon.ai.llm.hooks",
    "LLMResponseReceivedHook": "oridecon.ai.llm.hooks",
    # Types
    "AnthropicClient": "oridecon.ai.llm.clients.anthropic",
    "APIPricingSource": "oridecon.ai.llm.pricing",
    "CacheEntry": "oridecon.ai.llm.caching.core",
    "CacheStats": "oridecon.ai.llm.caching.core",
    "ChatMessage": "oridecon.ai.llm.types",
    "ContentPart": "oridecon.contracts.ai.multimodal",
    # Config
    "ClientConfig": "oridecon.ai.llm.config",
    "CohereClient": "oridecon.ai.llm.clients.cohere",
    "Completion": "oridecon.ai.llm.types",
    "ConversationConfig": "oridecon.ai.llm.conversation.manager",
    "ConversationManager": "oridecon.ai.llm.conversation.manager",
    "ConversationStats": "oridecon.ai.llm.conversation.manager",
    "CostEstimate": "oridecon.ai.llm.pricing.tokens",
    "FunctionCall": "oridecon.ai.llm.types",
    "GenerationDefaults": "oridecon.ai.llm.routing.config",
    "GroqClient": "oridecon.ai.llm.clients.groq",
    "ImageBase64Part": "oridecon.contracts.ai.multimodal",
    "ImageUrlPart": "oridecon.contracts.ai.multimodal",
    "InstructorExtractor": "oridecon.ai.llm.extraction.extractor",
    "JSONExtractor": "oridecon.ai.llm.structured.extractor",
    "JSONFilePricingSource": "oridecon.ai.llm.pricing",
    "LLMCache": "oridecon.ai.llm.caching.core",
    "LLMCacheProtocol": "oridecon.ai.llm.protocols",
    "LLMConfig": "oridecon.ai.llm.routing.config",
    "LogConfig": "oridecon.ai.llm.routing.config",
    "LLMError": "oridecon.ai.llm.types",
    "LLMAuthenticationError": "oridecon.ai.llm.exceptions",
    "LLMContentFilterError": "oridecon.ai.llm.exceptions",
    "LLMModelNotFoundError": "oridecon.ai.llm.exceptions",
    "ModelRevisionMismatchError": "oridecon.ai.llm.exceptions",
    "LLMQuotaExceededError": "oridecon.ai.llm.exceptions",
    "LLMRateLimitError": "oridecon.ai.llm.exceptions",
    "InvalidRequestError": "oridecon.ai.llm.exceptions",
    "ModelNotFoundError": "oridecon.ai.llm.exceptions",
    "ProviderConnectionError": "oridecon.ai.llm.exceptions",
    "StreamError": "oridecon.ai.llm.exceptions",
    "TokenLimitError": "oridecon.ai.llm.exceptions",
    "ExtractionError": "oridecon.ai.llm.exceptions",
    "ExtractionParseError": "oridecon.ai.llm.exceptions",
    "ExtractionValidationError": "oridecon.ai.llm.exceptions",
    "ExtractionMaxRetriesError": "oridecon.ai.llm.exceptions",
    "MessageContent": "oridecon.contracts.ai.multimodal",
    "MistralClient": "oridecon.ai.llm.clients.mistral",
    "ModelCapabilities": "oridecon.ai.llm.selection.core",
    "ModelPricing": "oridecon.ai.llm.pricing",
    "ModelSelector": "oridecon.ai.llm.selection.core",
    "OllamaClient": "oridecon.ai.llm.clients.ollama",
    "OpenAIClient": "oridecon.ai.llm.clients.openai",
    "OpenRouterClient": "oridecon.ai.llm.clients.openrouter",
    "OpenRouterPricingSource": "oridecon.ai.llm.pricing",
    "OutputFilter": "oridecon.ai.llm.security.core",
    "ParseError": "oridecon.ai.llm.structured.exceptions",
    "PricingConfig": "oridecon.ai.llm.config",
    "PricingCostEstimator": "oridecon.ai.llm.pricing.estimator",
    "PricingManager": "oridecon.ai.llm.pricing",
    "PricingManagerBuilder": "oridecon.ai.llm.pricing",
    "PricingSourceConfig": "oridecon.ai.llm.config",
    "AbstractPricingSource": "oridecon.ai.llm.pricing",
    "ProviderConfig": "oridecon.ai.llm.routing.config",
    # Pinning
    "ModelPinPolicy": "oridecon.ai.llm.pinning",
    "enforce_pin_policy": "oridecon.ai.llm.pinning",
    # Audit
    "LLMAuditBridge": "oridecon.ai.llm.audit_bridge",
    # Parsers
    "ParserRegistry": "oridecon.ai.llm.parsers.registry",
    "JSONOutputParser": "oridecon.ai.llm.parsers.json",
    "PydanticOutputParser": "oridecon.ai.llm.parsers.pydantic",
    "EnumOutputParser": "oridecon.ai.llm.parsers.enum",
    "CSVOutputParser": "oridecon.ai.llm.parsers.csv",
    "FormatFixingParser": "oridecon.ai.llm.parsers.fixing",
    "ProviderInfo": "oridecon.ai.llm.registry.core",
    "ProviderRegistry": "oridecon.ai.llm.registry.core",
    "QuotaConfig": "oridecon.ai.llm.routing.config",
    "RateLimiter": "oridecon.ai.llm.rate_limiting.core",
    "RedisLLMCache": "oridecon.ai.llm.caching.core",
    "ResponseFormatter": "oridecon.ai.llm.structured.formatter",
    "Role": "oridecon.ai.llm.types",
    "SchemaValidationError": "oridecon.ai.llm.structured.exceptions",
    "SecureLLMClient": "oridecon.ai.llm.security.core",
    "SecurePromptTemplate": "oridecon.ai.llm.security.core",
    "SelectionCriteria": "oridecon.ai.llm.selection.core",
    "SelectionStrategy": "oridecon.ai.llm.selection.core",
    "StaticPricingSource": "oridecon.ai.llm.pricing",
    "StreamChunk": "oridecon.ai.llm.types",
    "StructuredOutputError": "oridecon.ai.llm.structured.exceptions",
    "StructuredOutputParser": "oridecon.ai.llm.structured.parser",
    "TextPart": "oridecon.contracts.ai.multimodal",
    "TokenCount": "oridecon.ai.llm.pricing.tokens",
    "TiktokenCounter": "oridecon.ai.llm.pricing.tokens",
    "CharEstimateCounter": "oridecon.ai.llm.pricing.tokens",
    "HuggingFaceCounter": "oridecon.ai.llm.pricing.tokens",
    "MistralCounter": "oridecon.ai.llm.pricing.tokens",
    "TokenCounterRegistry": "oridecon.ai.llm.pricing.registry",
    "TokenUsage": "oridecon.ai.llm.types",
    "ToolCall": "oridecon.ai.llm.types",
    "complete_with_json": "oridecon.ai.llm.structured.utils",
    "complete_with_schema": "oridecon.ai.llm.structured.utils",
    "create_assistant_template": "oridecon.ai.llm.security.core",
    "create_balanced_selector": "oridecon.ai.llm.selection.core",
    "create_cost_optimized_selector": "oridecon.ai.llm.selection.core",
    "create_data_extraction_template": "oridecon.ai.llm.security.core",
    "create_json_mode_messages": "oridecon.ai.llm.structured.utils",
    "create_quality_optimized_selector": "oridecon.ai.llm.selection.core",
    "create_token_counter": "oridecon.ai.llm.pricing.tokens",
    # DI
    "LLMModule": "oridecon.ai.llm.module",
    "LLMProvider": "oridecon.ai.llm.di.provider",
    "LLMRoutingProvider": "oridecon.ai.llm.di.routing_provider",
    # Runnable composition
    "RunnableBranch": "oridecon.ai.llm.runnable",
    "RunnableLambda": "oridecon.ai.llm.runnable",
    "RunnableMixin": "oridecon.ai.llm.runnable",
    "RunnableParallel": "oridecon.ai.llm.runnable",
    "RunnablePassthrough": "oridecon.ai.llm.runnable",
    "RunnableSequence": "oridecon.ai.llm.runnable",
}


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        import importlib as _importlib

        module = _importlib.import_module(_LAZY_IMPORTS[name])
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = list(_LAZY_IMPORTS.keys())
