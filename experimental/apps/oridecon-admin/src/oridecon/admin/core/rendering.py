from __future__ import annotations

from typing import TYPE_CHECKING

from oridecon.admin.config import AdminConfig
from oridecon.di.decorators import inject

if TYPE_CHECKING:
    from starlette.requests import Request
    from starlette.responses import HTMLResponse
    from starlette.templating import Jinja2Templates


@inject
class AdminRenderer:
    """Renderer for admin templates."""

    def __init__(self, config: AdminConfig, templates: Jinja2Templates | None = None):
        self._config = config
        self._templates = templates

    def render_template(
        self,
        request: Request,
        name: str,
        context: dict,
    ) -> HTMLResponse:
        if self._templates is None:
            raise ValueError("No Jinja2Templates configured for AdminRenderer")
        context.update(
            {
                "title": self._config.title,
                "admin": None,
            },
        )
        return self._templates.TemplateResponse(request, name, context=context)

    def render_html_shell(
        self,
        request: Request,
        content_html: str,
        title: str = "",
    ) -> HTMLResponse:
        """Render pre-built HTML inside the admin shell.

        Args:
            request: Starlette request.
            content_html: Fully-rendered, framework-composed HTML.
            title: Page title.
        """
        from oridecon.ui import trusted_template_output

        return self.render_template(
            request,
            "admin_shell.html",
            {
                # admin_shell.html renders {{ content }} under autoescaping
                # and has no `| safe` filter, so already-rendered HTML must
                # be granted trust here, at the template output boundary.
                "content": trusted_template_output(
                    content_html,
                    template="admin_shell.html (autoescape on, no |safe)",
                ),
                "title": f"{title} - {self._config.title}"
                if title
                else self._config.title,
            },
        )
