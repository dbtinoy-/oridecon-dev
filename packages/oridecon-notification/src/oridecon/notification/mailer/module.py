"""MailerModule — IoC module for email delivery."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from oridecon.contracts.mailer.protocols import MailerProtocol
from oridecon.di.module import DynamicModule, Module, module

if TYPE_CHECKING:
    from oridecon.notification.config import MailerConfig


@module(is_global=True)
class MailerModule(Module):
    """Email delivery integration with Named DI multi-backend support.

    Registers :class:`~oridecon.contracts.mailer.protocols.MailerProtocol` for
    constructor injection, supporting SMTP and SendGrid backends.

    Usage::

        from oridecon.notification.config import MailerConfig, NamedMailerConfig
        from oridecon.notification.mailer.module import MailerModule

        @module(
            imports=[
                MailerModule.configure(
                    MailerConfig(
                        backends=[
                            NamedMailerConfig(
                                name="transactional",
                                primary=True,
                                driver="sendgrid",
                            )
                        ]
                    )
                )
            ]
        )
        class AppModule(Module):
            pass

    Named injection::

        class MyService:
            def __init__(
                self,
                mailer: MailerProtocol,                                          # primary
                bulk: Annotated[MailerProtocol, Named("bulk")],                  # named
            ) -> None: ...
    """

    @classmethod
    def configure(cls, config: MailerConfig | Any | None = None) -> DynamicModule:
        """Create a MailerModule with explicit configuration.

        Args:
            config: :class:`~oridecon.notification.config.MailerConfig` or ``None``
                to use defaults (no backends).

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.notification.di.mailer_provider import MailerProvider

        return DynamicModule(
            module=cls,
            providers=[MailerProvider(config=config)],
            exports=[MailerProtocol],
        )

    @classmethod
    def stub(cls, config: MailerConfig | Any | None = None) -> DynamicModule:
        """Return a MailerModule for unit tests — no emails sent.

        Uses an empty config (no backends configured) so all mail operations
        are dropped and no external services are contacted.

        Args:
            config: Optional :class:`~oridecon.notification.config.MailerConfig`
                for test scenarios that need specific stubs.

        Returns:
            A :class:`~oridecon.di.module.DynamicModule` descriptor.
        """
        from oridecon.notification.config import MailerConfig as _MailerConfig
        from oridecon.notification.di.mailer_provider import MailerProvider

        stub_config = config or _MailerConfig()
        if not stub_config.backends:
            stub_config.console_fallback = False
        return DynamicModule(
            module=cls,
            providers=[MailerProvider(config=stub_config)],
            exports=[MailerProtocol],
        )


__all__ = ["MailerModule"]
