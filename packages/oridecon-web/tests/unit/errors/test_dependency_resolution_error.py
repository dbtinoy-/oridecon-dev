import asyncio
from starlette.testclient import TestClient

from oridecon.app.base import Application
from oridecon.web.config import WebConfig, RateLimitConfig
from oridecon.web.di.provider import WebProvider
from oridecon.web.routing.controllers import Controller
from oridecon.web import get


class UnregisteredService:
    pass


class DIErrorController(Controller):
    @get("/bad")
    async def bad(self, svc: UnregisteredService):
        return {"ok": True}


def test_dependency_resolution_error_returns_500():
    # Disable rate limiting to avoid requiring RateLimitProvider
    rate_limit_config = RateLimitConfig(enabled=False)
    web_config = WebConfig(rate_limit=rate_limit_config)
    
    app = Application(name="test-app")
    web = WebProvider(controllers=[DIErrorController], web_config=web_config)

    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(web.register(app.container))
        loop.run_until_complete(web.boot(app.container))

        client = TestClient(web.starlette)
        r = client.get("/bad")
        assert r.status_code == 500
        j = r.json()
        assert j["type"] == "urn:oridecon:internal-error"
        assert "svc" in j["detail"]

    finally:
        loop.run_until_complete(web.shutdown())
        loop.close()
