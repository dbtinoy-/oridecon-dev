"""Tests for auth protocols."""

import pytest

from oridecon.contracts.auth import IdentityResolverProtocol
from oridecon.contracts.auth import IdentityResolverProtocol as BaseProtocol


class TestAuthProtocols:
    def test_identity_resolver_protocol_exists(self) -> None:
        assert IdentityResolverProtocol is not None

    def test_identity_resolver_protocol_is_base_protocol(self) -> None:
        assert IdentityResolverProtocol is BaseProtocol
