"""Response synthesizers package.

This package provides various strategies for synthesizing responses from
retrieved context chunks.
"""

from __future__ import annotations

from oridecon.ai.rag.synthesis.synthesizers.abstractive import (
    AbstractiveSynthesizer,
)
from oridecon.ai.rag.synthesis.synthesizers.base import (
    AbstractSynthesizer,
    ResponseSynthesizerProtocol,
)
from oridecon.ai.rag.synthesis.synthesizers.direct import DirectSynthesizer
from oridecon.ai.rag.synthesis.synthesizers.extractive import (
    ExtractiveSynthesizer,
)
from oridecon.ai.rag.synthesis.synthesizers.hybrid import HybridSynthesizer

__all__ = [
    "AbstractSynthesizer",
    "AbstractiveSynthesizer",
    "DirectSynthesizer",
    "ExtractiveSynthesizer",
    "HybridSynthesizer",
    "ResponseSynthesizerProtocol",
]
