from __future__ import annotations

from oridecon.contracts.cli.contributions import (
    CommandContribution,
    DoctorCheckContribution,
    HealthCheckContribution,
    HookContribution,
    ShellContextContribution,
)
from oridecon.contracts.cli.generators import (
    GenerationResult,
    GeneratorProtocol,
)
from oridecon.contracts.cli.naming import to_camel_case, to_snake_case
from oridecon.contracts.cli.parsers import FieldSpec, parse_fields
from oridecon.contracts.cli.protocols import CliContributorProtocol
from oridecon.contracts.cli.types import GeneratorDefinition, GeneratorOption

__all__ = [
    "CliContributorProtocol",
    "CommandContribution",
    "DoctorCheckContribution",
    "FieldSpec",
    "GenerationResult",
    "GeneratorDefinition",
    "GeneratorOption",
    "GeneratorProtocol",
    "HealthCheckContribution",
    "HookContribution",
    "ShellContextContribution",
    "parse_fields",
    "to_camel_case",
    "to_snake_case",
]
