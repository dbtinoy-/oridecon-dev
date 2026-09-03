"""NoSQL-specific exceptions."""

from __future__ import annotations

from oridecon.contracts.exceptions import OrideconError


class NoSQLError(OrideconError):
    """Base exception for all NoSQL operations."""

    _code: str = "ORI_ERR_NOSQL_001"


class NoSQLConnectionError(NoSQLError):
    """Failed to connect to the document store."""

    _code: str = "ORI_ERR_NOSQL_002"


class DocumentNotFoundError(NoSQLError):
    """Requested document does not exist."""

    _code: str = "ORI_ERR_NOSQL_003"


class DuplicateKeyError(NoSQLError):
    """Insert/update violated a unique constraint."""

    _code: str = "ORI_ERR_NOSQL_004"


class DocumentValidationError(NoSQLError):
    """Document failed schema validation."""

    _code: str = "ORI_ERR_NOSQL_005"


class TransactionError(NoSQLError):
    """Multi-document transaction failed."""

    _code: str = "ORI_ERR_NOSQL_006"


class NoSQLFilterError(NoSQLError):
    """Filter rejected by the operator/identifier validation guard."""

    _code: str = "ORI_ERR_NOSQL_007"


__all__ = [
    "DocumentNotFoundError",
    "DocumentValidationError",
    "DuplicateKeyError",
    "NoSQLConnectionError",
    "NoSQLError",
    "NoSQLFilterError",
    "TransactionError",
]
