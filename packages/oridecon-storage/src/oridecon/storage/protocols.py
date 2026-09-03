"""Public protocol surface for ``oridecon.storage``."""

from __future__ import annotations

from oridecon.contracts.infra.storage import BlobStoreProtocol, StorageBackendProtocol
from oridecon.storage.backends.protocols import StreamingBodyProtocol

__all__ = [
    "BlobStoreProtocol",
    "StorageBackendProtocol",
    "StreamingBodyProtocol",
]
