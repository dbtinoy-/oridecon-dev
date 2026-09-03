"""Oridecon Storage — Unified Storage Abstractions.

This package exposes **two distinct storage paradigms**.  Choose based on
your access patterns:

Blob / Object storage  (this package's primary API)
----------------------------------------------------
Designed for arbitrary binary objects (files, images, documents).
Operations: upload, download, delete, generate signed URLs, list objects.

Key classes:

* :class:`BlobStoreProtocol` — protocol for storage backend implementations.
* :class:`LocalDriver` — local filesystem driver (dev / CI).
* :class:`MemoryDriver` — ephemeral in-process driver (unit tests).
* :class:`S3Driver` — AWS S3 driver (requires ``boto3``).
* :class:`GCSDriver` — Google Cloud Storage driver (requires ``google-cloud-storage``).
* :class:`AzureDriver` — Azure Blob Storage driver (requires ``azure-storage-blob``).

Use blob storage when you need presigned download URLs, content-type
metadata, streaming uploads, or cloud-hosted durable file storage.

Key-Value (KV) storage  (:mod:`oridecon.storage.kv`)
------------------------------------------------------
Designed for small, string-keyed records (session data, feature flags,
ephemeral state) with optional TTL.  KV backends store values as JSON
and do **not** support binary blobs or presigned URLs.

Key classes (in :mod:`oridecon.storage.kv`):

* :class:`~oridecon.storage.kv.InMemoryKVStorage` — ephemeral dict-backed
  store (unit tests, single-node apps).
* :class:`~oridecon.storage.kv.LocalStorage` — JSON-file-backed persistent
  store (dev environments, low-volume single-node deployments).

Use KV storage when you need simple get / set / delete / TTL semantics
without the overhead of a full object storage system.

Exports (blob storage)
-----------------------
* :class:`StorageProvider` — DI provider for framework integration.
* :class:`StorageConfig` — root configuration model.
* :class:`BlobStoreProtocol` — protocol for storage backend implementations.
* :class:`FileInfo` — file metadata returned from storage operations.
* :class:`Uploadable` — type for file-like objects that can be uploaded.
* :class:`UploadOptions` — options for upload operations.
* :class:`LocalDriver`, :class:`MemoryDriver`, :class:`S3Driver`,
  :class:`GCSDriver`, :class:`AzureDriver` — concrete backend drivers.
"""

from __future__ import annotations

import importlib.metadata

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from typing import TYPE_CHECKING, Any

from oridecon.storage.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.contracts.infra.storage import (
        BlobStoreProtocol,
        FileInfo,
        Uploadable,
        UploadOptions,
    )
    from oridecon.storage.backends.azure import AzureDriver
    from oridecon.storage.backends.gcs import GCSDriver
    from oridecon.storage.backends.local import LocalDriver
    from oridecon.storage.backends.memory import MemoryDriver
    from oridecon.storage.backends.s3 import S3Driver
    from oridecon.storage.config import NamedStorageConfig, StorageConfig
    from oridecon.storage.di.provider import StorageProvider

_LAZY_IMPORTS = {
    # Module
    "StorageModule": "oridecon.storage.module",
    "BlobStoreProtocol": "oridecon.contracts.infra.storage",
    "FileInfo": "oridecon.contracts.infra.storage",
    "NamedStorageConfig": "oridecon.storage.config",
    "StorageConfig": "oridecon.storage.config",
    "StorageProvider": "oridecon.storage.di.provider",
    "UploadOptions": "oridecon.contracts.infra.storage",
    "Uploadable": "oridecon.contracts.infra.storage",
    "LocalDriver": "oridecon.storage.backends.local",
    "MemoryDriver": "oridecon.storage.backends.memory",
    "S3Driver": "oridecon.storage.backends.s3",
    "GCSDriver": "oridecon.storage.backends.gcs",
    "AzureDriver": "oridecon.storage.backends.azure",
    # Events
    "FileDeletedEvent": "oridecon.storage.events",
    "FileDownloadedEvent": "oridecon.storage.events",
    "FileUploadedEvent": "oridecon.storage.events",
    # Hooks
    "ObjectDeletedHook": "oridecon.storage.hooks",
    "ObjectStoredHook": "oridecon.storage.hooks",
}


def __getattr__(name: str) -> Any:
    if name == "__version__":
        return __version__
    if name in _LAZY_IMPORTS:
        import importlib

        module_path = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__} has no attribute {name}")


def __dir__() -> list[str]:
    return [*list(_LAZY_IMPORTS.keys()), "__version__"]


__all__ = [*list(_LAZY_IMPORTS.keys()), "__version__"]
