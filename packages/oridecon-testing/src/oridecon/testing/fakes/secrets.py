"""In-memory rotatable secret store — provided as a test fake.

The implementation is the production ``memory`` backend owned by
``oridecon.secrets``; this module re-exports it so test code can keep
importing the fake from ``oridecon.testing``.
"""

from __future__ import annotations

from oridecon.secrets.backends.memory import InMemoryRotatableSecretStore

__all__ = ["FakeRotatableSecretStore"]

FakeRotatableSecretStore = InMemoryRotatableSecretStore
