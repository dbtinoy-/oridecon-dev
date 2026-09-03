"""
Serialization module for Oridecon Cache.

This module provides various serialization implementations for cache backends,
allowing developers to choose the appropriate serialization strategy based on
their needs (interoperability vs. performance vs. compatibility).

The AsyncStringSerializerProtocol protocol is defined in oridecon.contracts.serialization
and implemented by cache-specific serializers in this module.
"""

from __future__ import annotations

from oridecon.cache.exceptions import CacheSerializationError
from oridecon.cache.serialization.compression import CompressingSerializer
from oridecon.cache.serialization.json import JSONSerializer
from oridecon.cache.serialization.msgpack import MsgPackSerializer
from oridecon.cache.serialization.type_registry import DEFAULT_REGISTRY, TypeRegistry
from oridecon.contracts.core.serialization import AsyncStringSerializerProtocol

__all__ = [
    "DEFAULT_REGISTRY",
    "AsyncStringSerializerProtocol",
    "CacheSerializationError",
    "CompressingSerializer",
    "JSONSerializer",
    "MsgPackSerializer",
    "TypeRegistry",
]
