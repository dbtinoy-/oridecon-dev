"""Admin authentication service protocols.

All protocols remain in oridecon-admin (not oridecon-contracts) because they
are admin-specific and not consumed by other extension packages.

``AdminAuditLogServiceProtocol`` extends the framework-wide
``AuditLoggerProtocol`` from ``oridecon.contracts.audit`` so that admin audit
implementations satisfy the cross-package contract.
"""

from __future__ import annotations

from oridecon.admin.auth.protocols.attempt_service import (
    AdminLoginAttemptServiceProtocol as AdminLoginAttemptServiceProtocol,
)
from oridecon.admin.auth.protocols.audit import (
    AdminAuditLogServiceProtocol as AdminAuditLogServiceProtocol,
)
from oridecon.admin.auth.protocols.audit import (
    AdminAuditLogStoreProtocol as AdminAuditLogStoreProtocol,
)
from oridecon.admin.auth.protocols.csrf import (
    AdminCsrfServiceProtocol as AdminCsrfServiceProtocol,
)
from oridecon.admin.auth.protocols.email_otp import (
    AdminEmailOtpServiceProtocol as AdminEmailOtpServiceProtocol,
)
from oridecon.admin.auth.protocols.email_otp import (
    AdminEmailOtpStoreProtocol as AdminEmailOtpStoreProtocol,
)
from oridecon.admin.auth.protocols.email_verification import (
    AdminEmailVerificationServiceProtocol as AdminEmailVerificationServiceProtocol,
)
from oridecon.admin.auth.protocols.email_verification import (
    AdminEmailVerificationStoreProtocol as AdminEmailVerificationStoreProtocol,
)
from oridecon.admin.auth.protocols.mfa import (
    AdminMfaServiceProtocol as AdminMfaServiceProtocol,
)
from oridecon.admin.auth.protocols.mfa import (
    AdminMfaStoreProtocol as AdminMfaStoreProtocol,
)
from oridecon.admin.auth.protocols.password_reset import (
    AdminPasswordResetServiceProtocol as AdminPasswordResetServiceProtocol,
)
from oridecon.admin.auth.protocols.password_reset import (
    AdminPasswordResetTokenStoreProtocol as AdminPasswordResetTokenStoreProtocol,
)
from oridecon.admin.auth.protocols.policy import (
    AdminPasswordPolicyServiceProtocol as AdminPasswordPolicyServiceProtocol,
)
from oridecon.admin.auth.protocols.service import (
    AdminAuthServiceProtocol as AdminAuthServiceProtocol,
)
from oridecon.admin.auth.protocols.session import (
    AdminSessionServiceProtocol as AdminSessionServiceProtocol,
)
from oridecon.admin.auth.protocols.user_store import (
    AdminAccountLockoutStoreProtocol as AdminAccountLockoutStoreProtocol,
)
from oridecon.admin.auth.protocols.user_store import (
    AdminLoginAttemptStoreProtocol as AdminLoginAttemptStoreProtocol,
)

__all__ = [
    "AdminAccountLockoutStoreProtocol",
    "AdminAuditLogServiceProtocol",
    "AdminAuditLogStoreProtocol",
    "AdminAuthServiceProtocol",
    "AdminCsrfServiceProtocol",
    "AdminEmailOtpServiceProtocol",
    "AdminEmailOtpStoreProtocol",
    "AdminEmailVerificationServiceProtocol",
    "AdminEmailVerificationStoreProtocol",
    "AdminLoginAttemptServiceProtocol",
    "AdminLoginAttemptStoreProtocol",
    "AdminMfaServiceProtocol",
    "AdminMfaStoreProtocol",
    "AdminPasswordPolicyServiceProtocol",
    "AdminPasswordResetServiceProtocol",
    "AdminPasswordResetTokenStoreProtocol",
    "AdminSessionServiceProtocol",
]
