"""Events CLI generators."""

from oridecon.events.cli.generators.command_handler import CommandHandlerGenerator
from oridecon.events.cli.generators.event_generator import EventGenerator
from oridecon.events.cli.generators.event_handler import EventHandlerGenerator
from oridecon.events.cli.generators.projection import ProjectionGenerator
from oridecon.events.cli.generators.query_handler import QueryHandlerGenerator
from oridecon.events.cli.generators.saga import SagaGenerator

__all__ = [
    "CommandHandlerGenerator",
    "EventGenerator",
    "EventHandlerGenerator",
    "ProjectionGenerator",
    "QueryHandlerGenerator",
    "SagaGenerator",
]
