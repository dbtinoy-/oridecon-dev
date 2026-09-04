"""Typed helper for building session cookie keyword arguments from AdminAuthConfig."""

from __future__ import annotations

from typing import Literal, TypedDict

from oridecon.admin.config import AdminAuthConfig


class SessionCookieKwargs(TypedDict):
    """Keyword arguments for Starlette SessionMiddleware."""

    secret_key: str
    https_only: bool
    same_site: Literal["lax", "strict", "none"]
    max_age: int | None


def build_session_cookie_kwargs(cfg: AdminAuthConfig) -> SessionCookieKwargs:
    """Build SessionMiddleware kwargs from AdminAuthConfig.

    In production the cookie is Secure, HttpOnly (implied by SessionMiddleware),
    and SameSite=strict. In development, https_only is relaxed so local dev
    without HTTPS still works.
    """
    is_prod = cfg.env == "production"
    https_only = cfg.cookie_secure if cfg.cookie_secure is not None else is_prod
    same_site = cfg.cookie_same_site or ("strict" if is_prod else "lax")
    if same_site == "none" and not https_only:
        # Browsers reject a SameSite=None cookie without Secure, so a
        # SameSite=None override implies the Secure flag.
        https_only = True
    return SessionCookieKwargs(
        secret_key=cfg.session_secret.get_secret_value(),
        https_only=https_only,
        same_site=same_site,
        max_age=cfg.session_lifetime,
    )


__all__ = [
    "SessionCookieKwargs",
    "build_session_cookie_kwargs",
]
