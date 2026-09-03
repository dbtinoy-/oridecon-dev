"""LLM client and prompt protocols."""

from __future__ import annotations

from oridecon.contracts.ai.exceptions import ExtractionError as ExtractionError
from oridecon.contracts.ai.exceptions import LLMError as LLMError
from oridecon.contracts.ai.llm.protocols import (
    ChatMessageProtocol as ChatMessageProtocol,
)
from oridecon.contracts.ai.llm.protocols import CompletionProtocol as CompletionProtocol
from oridecon.contracts.ai.llm.protocols import (
    CostEstimatorProtocol as CostEstimatorProtocol,
)
from oridecon.contracts.ai.llm.protocols import (
    EmbeddingClientProtocol as EmbeddingClientProtocol,
)
from oridecon.contracts.ai.llm.protocols import LLMClientProtocol as LLMClientProtocol
from oridecon.contracts.ai.llm.protocols import (
    PromptAssemblerProtocol as PromptAssemblerProtocol,
)
from oridecon.contracts.ai.llm.protocols import (
    PromptOptimizerProtocol as PromptOptimizerProtocol,
)
from oridecon.contracts.ai.llm.protocols import (
    PromptRegistryProtocol as PromptRegistryProtocol,
)
from oridecon.contracts.ai.llm.protocols import (
    PromptRendererProtocol as PromptRendererProtocol,
)
from oridecon.contracts.ai.llm.protocols import (
    PromptTemplateProtocol as PromptTemplateProtocol,
)
from oridecon.contracts.ai.llm.protocols import (
    SemanticCacheProtocol as SemanticCacheProtocol,
)
from oridecon.contracts.ai.llm.protocols import (
    StructuredExtractorProtocol as StructuredExtractorProtocol,
)
from oridecon.contracts.ai.llm.protocols import (
    TokenCounterProtocol as TokenCounterProtocol,
)
from oridecon.contracts.ai.llm.types import ChatMessage as ChatMessage
from oridecon.contracts.ai.llm.types import Completion as Completion
from oridecon.contracts.ai.llm.types import FunctionCall as FunctionCall
from oridecon.contracts.ai.llm.types import Role as Role
from oridecon.contracts.ai.llm.types import StreamChunk as StreamChunk
from oridecon.contracts.ai.llm.types import StreamEvent as StreamEvent
from oridecon.contracts.ai.llm.types import TokenBudget as TokenBudget
from oridecon.contracts.ai.llm.types import TokenUsage as TokenUsage
from oridecon.contracts.ai.llm.types import ToolCall as ToolCall
from oridecon.contracts.ai.thinking import ThinkingConfig as ThinkingConfig
from oridecon.contracts.ai.thinking import ThinkingResult as ThinkingResult
from oridecon.contracts.infra import AsyncStream as AsyncStream

__all__ = [
    "AsyncStream",
    "ChatMessage",
    "ChatMessageProtocol",
    "Completion",
    "CompletionProtocol",
    "CostEstimatorProtocol",
    "EmbeddingClientProtocol",
    "ExtractionError",
    "FunctionCall",
    "LLMClientProtocol",
    "LLMError",
    "PromptAssemblerProtocol",
    "PromptOptimizerProtocol",
    "PromptRegistryProtocol",
    "PromptRendererProtocol",
    "PromptTemplateProtocol",
    "Role",
    "SemanticCacheProtocol",
    "StreamChunk",
    "StreamEvent",
    "StructuredExtractorProtocol",
    "ThinkingConfig",
    "ThinkingResult",
    "TokenBudget",
    "TokenCounterProtocol",
    "TokenUsage",
    "ToolCall",
]
