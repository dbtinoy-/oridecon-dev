"""oridecon-queue — message bus/queue with Named DI multi-backend support."""

from __future__ import annotations

from oridecon.contracts.queue.errors import QueueError
from oridecon.contracts.queue.protocols import QueueProtocol
from oridecon.contracts.queue.types import BusMessage
from oridecon.queue.consumers.consumer import MessageConsumer
from oridecon.queue.core.batch_publisher import BatchedPublisher
from oridecon.queue.core.dlq import DeadLetterQueue
from oridecon.queue.core.pipeline import MessagePipeline, MiddlewareBase
from oridecon.queue.events import (
    ConsumerRegisteredEvent,
    MessageConsumedEvent,
    MessageDeadLetteredEvent,
)
from oridecon.queue.exceptions import (
    AzureServiceBusQueueError,
    GCPPubSubQueueError,
    KafkaQueueError,
    RabbitMQQueueError,
    RedisQueueError,
    SQSQueueError,
)
from oridecon.queue.hooks import (
    MessageConsumedHook,
    MessagePublishedHook,
    QueueDrainedHook,
)
from oridecon.queue.module import QueueModule

__all__ = [
    "AzureServiceBusQueueError",
    "BatchedPublisher",
    "BusMessage",
    "ConsumerRegisteredEvent",
    "DeadLetterQueue",
    "GCPPubSubQueueError",
    "KafkaQueueError",
    "MessageConsumedEvent",
    "MessageConsumedHook",
    "MessageConsumer",
    "MessageDeadLetteredEvent",
    "MessagePipeline",
    "MessagePublishedHook",
    "MiddlewareBase",
    "QueueDrainedHook",
    "QueueError",
    "QueueModule",
    "QueueProtocol",
    "RabbitMQQueueError",
    "RedisQueueError",
    "SQSQueueError",
]
