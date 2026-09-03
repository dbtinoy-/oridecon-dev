"""Backend module initialization."""

from __future__ import annotations

from oridecon.queue.backends.azure_servicebus import AzureServiceBusQueue
from oridecon.queue.backends.gcp_pubsub import GCPPubSubQueue
from oridecon.queue.backends.kafka import KafkaQueue
from oridecon.queue.backends.memory import InMemoryQueue
from oridecon.queue.backends.rabbitmq import RabbitMQQueue
from oridecon.queue.backends.redis import RedisQueue
from oridecon.queue.backends.sqs import SQSQueue

__all__ = [
    "AzureServiceBusQueue",
    "GCPPubSubQueue",
    "InMemoryQueue",
    "KafkaQueue",
    "RabbitMQQueue",
    "RedisQueue",
    "SQSQueue",
]
