"""PipeProtocol system for parameter validation and transformation.

Pipes transform and validate input before it reaches the handler.
"""

from __future__ import annotations

from oridecon.web.pipes.builtin.file import (
    FileSizeValidationPipe,
    FileTypeValidationPipe,
)
from oridecon.web.pipes.builtin.parse import (
    ParseBoolPipe,
    ParseDatePipe,
    ParseIntPipe,
    ParseUUIDPipe,
)

# Built-in pipes
from oridecon.web.pipes.builtin.validation import ValidationPipe
from oridecon.web.pipes.decorators import use_pipes
from oridecon.web.pipes.pipeline import PipePipeline
from oridecon.web.protocols import (
    ParamMetadata,
    PipeProtocol,
)
from oridecon.web.types import PipeBase

__all__ = [
    "FileSizeValidationPipe",
    "FileTypeValidationPipe",
    # Protocols
    "ParamMetadata",
    "ParseBoolPipe",
    "ParseDatePipe",
    "ParseIntPipe",
    "ParseUUIDPipe",
    "PipeBase",
    # Pipeline
    "PipePipeline",
    "PipeProtocol",
    # Built-in pipes
    "ValidationPipe",
    "use_pipes",
]
