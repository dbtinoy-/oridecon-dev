from __future__ import annotations

import importlib

import pytest

EXPECTED_MODULE_EXPORTS: dict[str, list[str]] = {
    "oridecon.contracts.core.lifecycle": [
        "GracefulShutdownProtocol",
        "OnApplicationBootstrapProtocol",
        "OnApplicationShutdownProtocol",
        "OnBeforeShutdownProtocol",
        "OnConfigReloadProtocol",
        "OnModuleInitProtocol",
    ],
    "oridecon.contracts.domain.base": ["ID", "DomainModelProtocol"],
    "oridecon.contracts.domain.events": ["DomainEvent"],
    "oridecon.contracts.domain.pagination": [
        "CursorPage",
        "CursorPageProtocol",
        "OffsetPageProtocol",
        "T",
    ],
    "oridecon.contracts.domain.services": [
        "DomainServiceProtocol",
        "PolicyProtocol",
        "PolicyViolationProtocol",
        "T",
        "T_co",
    ],
    "oridecon.contracts.exceptions.components": [
        "ComponentConnectionError",
        "ComponentError",
        "DriverNotAvailableError",
        "KeyExistsError",
        "KeyNotFoundError",
        "LockAcquisitionError",
        "LockNotHeldError",
        "PubSubError",
        "SecretNotFoundError",
    ],
    "oridecon.contracts.exceptions.domain": [
        "AuthenticationError",
        "AuthorizationError",
        "ConflictError",
        "DomainError",
        "FieldError",
        "MappingError",
        "NotFoundError",
        "PermissionDeniedError",
        "RateLimitError",
        "SerializationError",
        "ValidationError",
        "WebError",
    ],
    "oridecon.contracts.exceptions.infra": [
        "ConstraintError",
        "DatabaseError",
        "DuplicateKeyError",
        "InfrastructureError",
        "IntegrityError",
        "LockConflictError",
        "LockError",
        "MigrationError",
        "NoPrimaryBackendError",
        "RegistryAlreadyExistsError",
        "RegistryError",
        "RegistryKeyError",
    ],
    "oridecon.contracts.lib.time": ["utcnow"],
}


@pytest.mark.parametrize(
    ("module_path", "expected_exports"),
    EXPECTED_MODULE_EXPORTS.items(),
)
def test_module_declares_explicit_all(
    module_path: str,
    expected_exports: list[str],
) -> None:
    module = importlib.import_module(module_path)
    exported = getattr(module, "__all__", None)

    assert isinstance(exported, list)
    assert exported == expected_exports
    for name in exported:
        assert not name.startswith("_")
        assert hasattr(module, name)
