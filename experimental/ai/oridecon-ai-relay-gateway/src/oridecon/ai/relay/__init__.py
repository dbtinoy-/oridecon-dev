"""Relay gateway package namespace for the Oridecon AI subsystem.

This package is split across oridecon-ai-relay (conversion engine) and
oridecon-ai-relay-gateway (gateway); see the respective submodules.
"""

from __future__ import annotations

from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)
