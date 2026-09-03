"""Oridecon Concurrency — async task management and synchronization primitives.

Provides task management, parallel execution, dispatchers, bounded
channels, and synchronization primitives built on asyncio.  All
components are registered through the DI container via
:class:`ConcurrencyModule`.

The dispatcher runs CPU-bound and I/O-bound work in dedicated thread
pools; ``BoundedChannel`` brings Go-style backpressure to async
producer-consumer pipelines; ``AsyncRWLock`` provides fair read-write
locking without starvation.

Basic Usage::

    from oridecon.concurrency import ConcurrencyModule, ConcurrencyConfig

    @module(imports=[ConcurrencyModule.configure(ConcurrencyConfig())])
    class AppModule(Module):
        pass

Module Structure:
    - bridges: Sync/async bridge utilities (``SyncBridge``)
    - channels: Bounded async channels (``BoundedChannel``)
    - config: Configuration models (``ConcurrencyConfig``, ``DispatcherConfig``)
    - di: Dependency injection provider (``ConcurrencyProvider``)
    - exceptions: Concurrency exception hierarchy (``ConcurrencyError``, …)
    - executors: Task dispatcher, parallel executor, task manager
    - locks: Async read-write locks (``AsyncRWLock``)
    - module: ``ConcurrencyModule`` IoC registration
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from oridecon.concurrency.constants import __version__ as __version__

if TYPE_CHECKING:
    from oridecon.concurrency.bridges.sync_bridge import SyncBridge
    from oridecon.concurrency.channels.channel import BoundedChannel
    from oridecon.concurrency.config import (
        ConcurrencyConfig,
        DispatcherConfig,
        PoolConfig,
        ThreadPoolConfig,
    )
    from oridecon.concurrency.di.provider import ConcurrencyProvider
    from oridecon.concurrency.exceptions import (
        AsyncError,
        CancellationScopeError,
        ChannelClosedError,
        ChannelFullError,
        ConcurrencyError,
        DispatcherError,
        StructuredParallelismError,
        TaskGroupError,
    )
    from oridecon.concurrency.executors.dispatcher import (
        DispatcherImpl,
        dispatch,
        run_sync,
        shutdown_dispatcher,
    )
    from oridecon.concurrency.executors.parallel import Parallel
    from oridecon.concurrency.executors.task_manager import TaskManager
    from oridecon.concurrency.locks.rwlock import AsyncRWLock
    from oridecon.concurrency.module import ConcurrencyModule
    from oridecon.concurrency.task_utils import create_tracked_task
    from oridecon.contracts.core import (
        ExecutionStrategy,
        ParallelProtocol,
        TaskManagerProtocol,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # --- Task Utilities ---
    "create_tracked_task": (
        "oridecon.concurrency.task_utils",
        "create_tracked_task",
    ),
    # --- Module ---
    "ConcurrencyModule": ("oridecon.concurrency.module", "ConcurrencyModule"),
    # --- Config ---
    "ConcurrencyConfig": ("oridecon.concurrency.config", "ConcurrencyConfig"),
    "DispatcherConfig": ("oridecon.concurrency.config", "DispatcherConfig"),
    "PoolConfig": ("oridecon.concurrency.config", "PoolConfig"),
    "ThreadPoolConfig": ("oridecon.concurrency.config", "ThreadPoolConfig"),
    # --- Channels ---
    "BoundedChannel": ("oridecon.concurrency.channels.channel", "BoundedChannel"),
    # --- Locks ---
    "AsyncRWLock": ("oridecon.concurrency.locks.rwlock", "AsyncRWLock"),
    # --- Executors ---
    "DispatcherImpl": ("oridecon.concurrency.executors.dispatcher", "DispatcherImpl"),
    "dispatch": ("oridecon.concurrency.executors.dispatcher", "dispatch"),
    "run_sync": ("oridecon.concurrency.executors.dispatcher", "run_sync"),
    "shutdown_dispatcher": (
        "oridecon.concurrency.executors.dispatcher",
        "shutdown_dispatcher",
    ),
    "Parallel": ("oridecon.concurrency.executors.parallel", "Parallel"),
    "TaskManager": ("oridecon.concurrency.executors.task_manager", "TaskManager"),
    # --- Bridges ---
    "SyncBridge": ("oridecon.concurrency.bridges.sync_bridge", "SyncBridge"),
    # --- Exceptions ---
    "AsyncError": ("oridecon.concurrency.exceptions", "AsyncError"),
    "CancellationScopeError": (
        "oridecon.concurrency.exceptions",
        "CancellationScopeError",
    ),
    "ChannelClosedError": ("oridecon.concurrency.exceptions", "ChannelClosedError"),
    "ChannelFullError": ("oridecon.concurrency.exceptions", "ChannelFullError"),
    "ConcurrencyError": ("oridecon.concurrency.exceptions", "ConcurrencyError"),
    "DispatcherError": ("oridecon.concurrency.exceptions", "DispatcherError"),
    "StructuredParallelismError": (
        "oridecon.concurrency.exceptions",
        "StructuredParallelismError",
    ),
    "TaskGroupError": ("oridecon.concurrency.exceptions", "TaskGroupError"),
    # --- Contracts (re-exported for convenience) ---
    "ExecutionStrategy": ("oridecon.contracts.core", "ExecutionStrategy"),
    "ParallelProtocol": ("oridecon.contracts.core", "ParallelProtocol"),
    "TaskManagerProtocol": ("oridecon.contracts.core", "TaskManagerProtocol"),
    # --- Provider ---
    "ConcurrencyProvider": ("oridecon.concurrency.di.provider", "ConcurrencyProvider"),
}


def __getattr__(name: str) -> Any:
    """Lazy-load symbols on first access."""
    if name in _LAZY_IMPORTS:
        import importlib

        module_path, attr_name = _LAZY_IMPORTS[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(set(__all__) | set(_LAZY_IMPORTS.keys()))


__all__ = [
    "AsyncError",
    "AsyncRWLock",
    "BoundedChannel",
    "CancellationScopeError",
    "ChannelClosedError",
    "ChannelFullError",
    "ConcurrencyConfig",
    "ConcurrencyError",
    "ConcurrencyModule",
    "ConcurrencyProvider",
    "DispatcherConfig",
    "DispatcherError",
    "DispatcherImpl",
    "ExecutionStrategy",
    "Parallel",
    "ParallelProtocol",
    "PoolConfig",
    "StructuredParallelismError",
    "SyncBridge",
    "TaskGroupError",
    "TaskManager",
    "TaskManagerProtocol",
    "ThreadPoolConfig",
    "create_tracked_task",
    "dispatch",
    "run_sync",
    "shutdown_dispatcher",
]
