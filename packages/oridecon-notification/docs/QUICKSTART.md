---
title: oridecon-notification Quickstart
description: Install and send SMS, push, and email notifications in under 5 minutes.
---

:::note[Maturity]
`oridecon-notification` is **alpha (0.1.x)** and MIT-licensed. Public APIs may change before 1.0.
:::

## Install

```bash
uv add oridecon-notification
```

Optional extras for specific backends:

| Backend | Extras |
|---------|--------|
| Twilio SMS | `uv add oridecon-notification[twilio]` |
| SendGrid email | `uv add oridecon-notification[sendgrid]` |
| APNs push | `uv add oridecon-notification[apns]` |
| Web Push | `uv add oridecon-notification[web-push]` |

---

## Minimal Working Example (SMS)

```python
import asyncio
from oridecon import Application
from oridecon.contracts.notification.protocols import SMSChannelProtocol
from oridecon.contracts.notification.types import SMSMessage
from oridecon.notification.config import (
    NotificationConfig,
    NamedSMSConfig,
    TwilioDriverConfig,
)
from oridecon.notification.module import NotificationModule


async def main():
    config = NotificationConfig(
        sms_backends=[
            NamedSMSConfig(
                name="primary",
                primary=True,
                driver="twilio",
                twilio=TwilioDriverConfig(
                    account_sid="${TWILIO_ACCOUNT_SID}",
                    auth_token="${TWILIO_AUTH_TOKEN}",
                    from_number="+15551234567",
                ),
            ),
        ],
    )

    async with Application.boot(
        name="notify-app",
        modules=[NotificationModule.configure(config)],
    ) as app:
        sms = await app.container.resolve(SMSChannelProtocol)
        result = await sms.send(
            SMSMessage(to=["+15559876543"], body="Hello from Oridecon!")
        )

        if result.is_ok():
            print(f"Sent! Receipt: {result.unwrap()}")
        else:
            print(f"Failed: {result.unwrap_err()}")


asyncio.run(main())
```

---

## What Just Happened

| Step | What |
|------|------|
| `NotificationConfig(...)` | Declared a Twilio SMS backend named `"primary"` as the default |
| `NotificationModule.configure(config)` | Created a `DynamicModule` exporting `SMSChannelProtocol` + `PushChannelProtocol` |
| `app.container.resolve(SMSChannelProtocol)` | Resolved the primary Twilio backend via the protocol binding |
| `sms.send(SMSMessage(...))` | Sent the SMS through Twilio's API — returns `Result[MessageDeliveryReceipt, NotificationError]` |

---

## Next Steps

- [Guide](./GUIDE.md) — SMS, push, email, and inbox concepts
- [How-Tos](./HOWTOS.md) — push notifications, multi-backend, email via MailerProvider
- [Configuration](./CONFIGURATION.md) — all config keys with env vars
