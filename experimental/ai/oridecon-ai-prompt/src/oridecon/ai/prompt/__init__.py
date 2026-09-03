"""oridecon-ai-prompt — Prompt management for the Oridecon AI framework.

Public API
----------
Templates
~~~~~~~~~
.. autosummary::

    StringPromptTemplate
    ChatPromptTemplate
    FewShotPromptTemplate
    InMemoryExampleSelector
    PartialPromptTemplate
    AbstractPromptTemplate

Variables
~~~~~~~~~
.. autosummary::

    PromptVariable
    PromptContext

Rendering
~~~~~~~~~
.. autosummary::

    PromptRenderer
    RenderFormat
    InputSanitizer

Composition
~~~~~~~~~~~
.. autosummary::

    PromptPipeline
    ConditionalPrompt

Registry
~~~~~~~~
.. autosummary::

    PromptRegistry
    VersionedPromptStore

Configuration & DI
~~~~~~~~~~~~~~~~~~
.. autosummary::

    PromptConfig
    PromptModule
    PromptProvider

Exceptions
~~~~~~~~~~
.. autosummary::

    PromptError
    PromptRenderError
    PromptValidationError
    PromptNotFoundError
    PromptVersionError
    PromptConfigError
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oridecon.ai.prompt.composition.conditional import ConditionalPrompt
    from oridecon.ai.prompt.composition.pipeline import PromptPipeline
    from oridecon.ai.prompt.config import PromptConfig
    from oridecon.ai.prompt.decorators import prompt_template
    from oridecon.ai.prompt.di.provider import PromptProvider
    from oridecon.ai.prompt.exceptions import (
        PromptConfigError,
        PromptError,
        PromptNotFoundError,
        PromptRenderError,
        PromptValidationError,
        PromptVersionError,
    )
    from oridecon.ai.prompt.hooks import (
        PromptInputSanitizedHook,
        PromptRenderedHook,
        PromptTemplateResolvedHook,
    )
    from oridecon.ai.prompt.module import PromptModule
    from oridecon.ai.prompt.protocols import (
        PromptOptimizerProtocol,
        PromptRendererProtocol,
    )
    from oridecon.ai.prompt.registry.registry import PromptRegistry
    from oridecon.ai.prompt.registry.versioned import VersionedPromptStore
    from oridecon.ai.prompt.rendering.engine import PromptRenderer, RenderFormat
    from oridecon.ai.prompt.rendering.sanitizer import InputSanitizer
    from oridecon.ai.prompt.template.base import AbstractPromptTemplate
    from oridecon.ai.prompt.template.chat import ChatPromptTemplate
    from oridecon.ai.prompt.template.few_shot import (
        FewShotPromptTemplate,
        InMemoryExampleSelector,
    )
    from oridecon.ai.prompt.template.partial import PartialPromptTemplate
    from oridecon.ai.prompt.template.string import StringPromptTemplate
    from oridecon.ai.prompt.variables.types import PromptContext, PromptVariable

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "AbstractPromptTemplate": (
        "oridecon.ai.prompt.template.base",
        "AbstractPromptTemplate",
    ),
    "CacheAwarePromptAssembler": (
        "oridecon.ai.prompt.assembly",
        "CacheAwarePromptAssembler",
    ),
    "ChatPromptTemplate": ("oridecon.ai.prompt.template.chat", "ChatPromptTemplate"),
    "ConditionalPrompt": (
        "oridecon.ai.prompt.composition.conditional",
        "ConditionalPrompt",
    ),
    "FewShotPromptTemplate": (
        "oridecon.ai.prompt.template.few_shot",
        "FewShotPromptTemplate",
    ),
    "InMemoryExampleSelector": (
        "oridecon.ai.prompt.template.few_shot",
        "InMemoryExampleSelector",
    ),
    "InputSanitizer": ("oridecon.ai.prompt.rendering.sanitizer", "InputSanitizer"),
    "PartialPromptTemplate": (
        "oridecon.ai.prompt.template.partial",
        "PartialPromptTemplate",
    ),
    "PromptConfig": ("oridecon.ai.prompt.config", "PromptConfig"),
    "PromptConfigError": ("oridecon.ai.prompt.exceptions", "PromptConfigError"),
    "PromptContext": ("oridecon.ai.prompt.variables.types", "PromptContext"),
    "PromptError": ("oridecon.ai.prompt.exceptions", "PromptError"),
    "PromptInputSanitizedHook": (
        "oridecon.ai.prompt.hooks",
        "PromptInputSanitizedHook",
    ),
    "PromptModule": ("oridecon.ai.prompt.module", "PromptModule"),
    "PromptNotFoundError": ("oridecon.ai.prompt.exceptions", "PromptNotFoundError"),
    "PromptPipeline": ("oridecon.ai.prompt.composition.pipeline", "PromptPipeline"),
    "PromptProvider": ("oridecon.ai.prompt.di.provider", "PromptProvider"),
    "PromptRegistry": ("oridecon.ai.prompt.registry.registry", "PromptRegistry"),
    "PromptRenderError": ("oridecon.ai.prompt.exceptions", "PromptRenderError"),
    "PromptRenderedHook": ("oridecon.ai.prompt.hooks", "PromptRenderedHook"),
    "PromptRenderer": ("oridecon.ai.prompt.rendering.engine", "PromptRenderer"),
    "PromptTemplateResolvedHook": (
        "oridecon.ai.prompt.hooks",
        "PromptTemplateResolvedHook",
    ),
    "PromptValidationError": ("oridecon.ai.prompt.exceptions", "PromptValidationError"),
    "PromptVariable": ("oridecon.ai.prompt.variables.types", "PromptVariable"),
    "PromptVersionError": ("oridecon.ai.prompt.exceptions", "PromptVersionError"),
    "ProviderCacheStrategyRegistry": (
        "oridecon.ai.prompt.assembly",
        "ProviderCacheStrategyRegistry",
    ),
    "prompt_template": ("oridecon.ai.prompt.decorators", "prompt_template"),
    "RenderFormat": ("oridecon.ai.prompt.rendering.engine", "RenderFormat"),
    "StringPromptTemplate": (
        "oridecon.ai.prompt.template.string",
        "StringPromptTemplate",
    ),
    "VersionedPromptStore": (
        "oridecon.ai.prompt.registry.versioned",
        "VersionedPromptStore",
    ),
    # Internal protocols
    "PromptAssemblerProtocol": (
        "oridecon.ai.prompt.protocols",
        "PromptAssemblerProtocol",
    ),
    "PromptCompressorProtocol": (
        "oridecon.ai.prompt.protocols",
        "PromptCompressorProtocol",
    ),
    "PromptOptimizerProtocol": (
        "oridecon.ai.prompt.protocols",
        "PromptOptimizerProtocol",
    ),
    "PromptRegistryProtocol": (
        "oridecon.ai.prompt.protocols",
        "PromptRegistryProtocol",
    ),
    "PromptRendererProtocol": (
        "oridecon.ai.prompt.protocols",
        "PromptRendererProtocol",
    ),
    "PromptTemplateProtocol": (
        "oridecon.ai.prompt.protocols",
        "PromptTemplateProtocol",
    ),
    "PromptRenderedEvent": ("oridecon.ai.prompt.events", "PromptRenderedEvent"),
}

__all__ = list(_LAZY_IMPORTS)


def __getattr__(name: str) -> object:
    """Lazy-load public symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr = _LAZY_IMPORTS[name]
        mod = importlib.import_module(module_path)
        value = getattr(mod, attr)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """Expose lazy-loaded names for tab completion and dir()."""
    return list(_LAZY_IMPORTS)
