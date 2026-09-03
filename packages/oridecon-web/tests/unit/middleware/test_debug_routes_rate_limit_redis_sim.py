import asyncio
import time

from starlette.testclient import TestClient

from oridecon.app.base import Application
from oridecon.web.config import WebProviderConfig
from oridecon.web.di.provider import WebProvider
from oridecon.web.routing.controllers import Controller
from oridecon.web import get


class FakeRedis:
    def __init__(self):
        self._data = {}

    async def incr(self, key: str) -> int:
        now = int(time.time())
        entry = self._data.get(key)
        if entry is None or entry[1] <= now:
            # reset
            self._data[key] = [1, now + 60]
            return 1
        else:
            self._data[key][0] += 1
            return self._data[key][0]

    async def expire(self, key: str, seconds: int) -> None:
        now = int(time.time())
        entry = self._data.get(key)
        if entry is None:
            self._data[key] = [0, now + seconds]
        else:
            entry[1] = now + seconds

    async def close(self):
        self._data.clear()


class RateController(Controller):
    @get("/x")
    def x(self):
        return {"ok": True}


def test_debug_routes_rate_limit_with_redis_simulation():
    app = Application(name="test-app")
    web = WebProvider(
        controllers=[RateController],
        provider_config=WebProviderConfig(
            debug_routes=True,
            debug_routes_rate_limit=1,
            debug_routes_rate_window_seconds=1,
        ),
    )

    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(web.register(app.container))
        loop.run_until_complete(web.boot(app.container))

        # Inject fake redis client
        web._debug_redis_client = FakeRedis()

        client = TestClient(web.starlette)
        r1 = client.get("/debug/routes")
        assert r1.status_code == 200
        r2 = client.get("/debug/routes")
        assert r2.status_code == 429

    finally:
        loop.run_until_complete(web.shutdown())
        loop.close()
