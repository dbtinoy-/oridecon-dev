"""Authentication token models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from oridecon.auth import constants as const
from oridecon.domain import DomainModel
from oridecon.validation import Field

if TYPE_CHECKING:
    from datetime import datetime


@dataclass(init=False)
class AuthToken(DomainModel):
    """Authentication token response."""

    token: str = Field(description="The primary authentication token string")
    expires_at: datetime = Field(description="Token expiration timestamp")
    refresh_token: str | None = Field(
        default=None, description="Optional refresh token"
    )
    refresh_expires_at: datetime | None = Field(
        default=None, description="Refresh token expiration timestamp"
    )
    token_type: str = Field(
        default=const.DEFAULT_TOKEN_TYPE, description="Token type (e.g. Bearer)"
    )


__all__ = [
    "AuthToken",
]
