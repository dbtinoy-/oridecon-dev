"""Clusters — first-class grouping of resources and pages."""

from __future__ import annotations

from oridecon.admin.clusters.base import Cluster
from oridecon.admin.clusters.registry import INFRASTRUCTURE_CLUSTER, ClusterRegistry

__all__ = [
    "INFRASTRUCTURE_CLUSTER",
    "Cluster",
    "ClusterRegistry",
]
