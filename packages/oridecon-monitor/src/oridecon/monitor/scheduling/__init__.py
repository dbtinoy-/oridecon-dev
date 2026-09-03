"""Periodic scheduled-worker base for oridecon.monitor.

Implements the shared scheduled-worker pattern against the contracts
:class:`~oridecon.contracts.infra.tasks.TaskManagerProtocol` so monitor
never imports ``oridecon.tasks`` directly.
"""

from __future__ import annotations

from oridecon.monitor.scheduling.scheduled_worker import MonitorScheduledWorker

__all__ = ["MonitorScheduledWorker"]
