"""Mailer submodule — email delivery backends, mailable base, and IoC module."""

from __future__ import annotations

from oridecon.notification.mailer.mailable import Mailable
from oridecon.notification.mailer.module import MailerModule
from oridecon.notification.mailer.retrying_mailer import RetryingMailer
from oridecon.notification.mailer.sendgrid_mailer import SendGridMailer
from oridecon.notification.mailer.smtp_mailer import SMTPMailer

__all__ = [
    "Mailable",
    "MailerModule",
    "RetryingMailer",
    "SMTPMailer",
    "SendGridMailer",
]
