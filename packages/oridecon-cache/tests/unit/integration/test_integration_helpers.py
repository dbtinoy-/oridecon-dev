import pytest

from oridecon.cache.config import CacheBackendConfig
from oridecon.cache.backends.factory import create_backend
from oridecon.cache.serialization.factory import create_serializers
from oridecon.cache.service.factory import create_service
from oridecon.cache.types import BackendType
from oridecon.testing.clock import FixedClock


@pytest.fixture
def clock():
    return FixedClock()


@pytest.mark.integration
def test_create_serializers_returns_json_by_default():
    serializers = create_serializers()
    assert "json" in serializers


def test_create_service_and_backend(clock):
    cfg = CacheBackendConfig.model_validate({"name": "mem", "type": BackendType.MEMORY})
    backend = create_backend(
        cfg,
    )
    service = create_service(None, "mem", backend, None)
    assert service is not None
