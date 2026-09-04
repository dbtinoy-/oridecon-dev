"""Accessible, lifecycle-safe task progress dialog."""

from __future__ import annotations

import re
from typing import Any
from urllib.parse import quote

from oridecon.logging import get_logger
from oridecon.ui.atoms.icons import get_icon
from oridecon.ui.attributes import alpine
from oridecon.ui.core.base import Component, Element
from oridecon.ui.core.js import js_json, js_string
from oridecon.ui.core.render_context import get_render_scope
from oridecon.ui.core.trusted_html import trusted_html
from oridecon.ui.core.url import is_safe_navigation_url

logger = get_logger(__name__)


class TaskProgress(Component):
    """Display live progress from a task-specific Server-Sent Events stream.

    Alpine calls the generated controller's ``init`` hook exactly once. The
    controller owns and closes its EventSource, timers, and lifecycle listeners
    when the root leaves the DOM.
    """

    _CALLBACK_NAME = re.compile(r"^[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)*$")

    def __init__(
        self,
        task_id: str,
        title: str = "Processing…",
        auto_close: bool = False,
        on_complete: str | None = None,
        stream_url: str | None = None,
        task_progress_key: str | None = None,
        **props: Any,
    ) -> None:
        super().__init__(**props)
        self.task_id = task_id
        self.title = title
        self.auto_close = auto_close
        self.on_complete = on_complete
        encoded_task_id = quote(task_id, safe="")
        self.stream_url = stream_url or f"/admin/progress/{encoded_task_id}/stream"
        self.task_progress_key = task_progress_key

    def _completion_action(self) -> dict[str, str] | None:
        """Normalize the compatibility completion value into inert data."""
        target = self.on_complete
        if not target:
            return None

        if target.startswith("/"):
            if is_safe_navigation_url(target):
                return {"kind": "navigate", "target": target}
            logger.warning("task_progress_unsafe_redirect", on_complete=target)
            return None

        if self._CALLBACK_NAME.fullmatch(target):
            return {"kind": "callback", "target": target}

        logger.warning("task_progress_rejected_callback", on_complete=target)
        return None

    def _controller_script(self, controller_name: str) -> str:
        return f"""
(() => {{
    const controllerName = {js_string(controller_name)};
    const streamUrl = {js_string(self.stream_url)};
    const completionAction = {js_json(self._completion_action())};
    const autoClose = {js_json(self.auto_close)};
    const allowedStatuses = new Set(['pending', 'running', 'complete', 'failed']);

    const controller = () => ({{
        visible: true,
        status: 'pending',
        progress: 0,
        message: 'Initializing…',
        error: null,
        eventSource: null,
        closeTimer: null,
        cleanupHandler: null,
        pagehideHandler: null,
        previousFocus: null,
        destroyed: false,
        get isActive() {{
            return this.status === 'pending' || this.status === 'running';
        }},
        init() {{
            this.previousFocus = document.activeElement;
            this.cleanupHandler = event => {{
                const target = event.detail?.elt || event.target;
                if (target && (target === this.$el ||
                    (typeof target.contains === 'function' && target.contains(this.$el)))) {{
                    this.destroy();
                }}
            }};
            this.pagehideHandler = () => this.destroy();
            document.body.addEventListener(
                'htmx:beforeCleanupElement', this.cleanupHandler
            );
            window.addEventListener('pagehide', this.pagehideHandler, {{once: true}});
            this.$nextTick(() => this.$refs.dialog.focus());
            this.connect();
        }},
        connect() {{
            if (this.destroyed) return;
            this.closeStream();
            window.clearTimeout(this.closeTimer);
            this.closeTimer = null;
            this.status = 'pending';
            this.progress = 0;
            this.message = 'Connecting…';
            this.error = null;

            let source;
            try {{
                source = new EventSource(streamUrl);
            }} catch (_error) {{
                this.fail('Unable to connect to task progress.');
                return;
            }}
            this.eventSource = source;
            source.addEventListener('open', () => {{
                if (this.eventSource === source && this.status === 'pending') {{
                    this.message = 'Waiting for progress…';
                }}
            }});
            source.addEventListener('progress', event => {{
                if (this.eventSource === source) this.handleProgress(event);
            }});
            source.addEventListener('error', () => {{
                if (this.eventSource === source) {{
                    this.fail('Connection lost. Retry to reconnect.');
                }}
            }});
        }},
        handleProgress(event) {{
            let data;
            try {{
                data = JSON.parse(event.data);
            }} catch (_error) {{
                this.fail('The progress service sent an invalid update.');
                return;
            }}
            if (!data || typeof data !== 'object' || Array.isArray(data) ||
                !allowedStatuses.has(data.status) ||
                typeof data.progress !== 'number' ||
                !Number.isFinite(data.progress)) {{
                this.fail('The progress service sent an invalid update.');
                return;
            }}

            this.status = data.status;
            this.progress = Math.min(100, Math.max(0, data.progress));
            this.message = typeof data.message === 'string' && data.message
                ? data.message
                : (data.status === 'complete' ? 'Complete' : 'Processing…');

            if (data.status === 'failed') {{
                this.error = typeof data.error === 'string' && data.error
                    ? data.error : 'Task failed.';
                this.closeStream();
                return;
            }}
            if (data.status === 'complete') {{
                this.progress = 100;
                this.closeStream();
                this.runCompletionAction();
                if (autoClose) {{
                    this.closeTimer = window.setTimeout(() => this.close(), 700);
                }}
            }}
        }},
        runCompletionAction() {{
            if (!completionAction) return;
            if (completionAction.kind === 'navigate') {{
                try {{
                    const url = new URL(completionAction.target, window.location.href);
                    if (url.origin === window.location.origin &&
                        ['http:', 'https:'].includes(url.protocol)) {{
                        window.location.assign(url.pathname + url.search + url.hash);
                    }}
                }} catch (_error) {{}}
                return;
            }}
            if (completionAction.kind === 'callback') {{
                const parts = completionAction.target.split('.');
                const methodName = parts.pop();
                let owner = window;
                for (const part of parts) {{
                    owner = owner?.[part];
                    if (!owner) return;
                }}
                const callback = owner?.[methodName];
                if (typeof callback === 'function') callback.call(owner);
            }}
        }},
        fail(message) {{
            this.status = 'failed';
            this.error = message;
            this.closeStream();
        }},
        closeStream() {{
            const source = this.eventSource;
            this.eventSource = null;
            if (source) source.close();
        }},
        close() {{
            this.visible = false;
            this.closeStream();
            window.clearTimeout(this.closeTimer);
            this.closeTimer = null;
            this.$nextTick(() => this.previousFocus?.focus());
        }},
        destroy() {{
            if (this.destroyed) return;
            this.destroyed = true;
            this.closeStream();
            window.clearTimeout(this.closeTimer);
            if (this.cleanupHandler) {{
                document.body.removeEventListener(
                    'htmx:beforeCleanupElement', this.cleanupHandler
                );
            }}
            if (this.pagehideHandler) {{
                window.removeEventListener('pagehide', this.pagehideHandler);
            }}
        }}
    }});

    const register = () => window.Alpine.data(controllerName, controller);
    if (window.Alpine) register();
    else document.addEventListener('alpine:init', register, {{once: true}});
}})();
"""

    @staticmethod
    def _status_icons() -> Element:
        return Element(
            "div",
            get_icon(
                "refresh-cw",
                class_name=(
                    "h-12 w-12 animate-spin text-primary-600 dark:text-primary-400"
                ),
                **alpine.show(
                    alpine.expr("status === 'pending' || status === 'running'")
                ),
            ),
            get_icon(
                "check-circle",
                class_name="h-12 w-12 text-success",
                **alpine.show(alpine.expr("status === 'complete'")),
            ),
            get_icon(
                "alert-circle",
                class_name="h-12 w-12 text-destructive",
                **alpine.show(alpine.expr("status === 'failed'")),
            ),
            class_="mb-4 flex justify-center",
        )

    @staticmethod
    def _progress_bar(message_id: str) -> Element:
        return Element(
            "div",
            Element(
                "div",
                Element(
                    "div",
                    **alpine.bind("style", alpine.expr("'width: ' + progress + '%'")),
                    class_=(
                        "h-full rounded-full bg-primary-600 transition-all "
                        "duration-300 dark:bg-primary-400"
                    ),
                ),
                role="progressbar",
                aria_valuemin="0",
                aria_valuemax="100",
                aria_describedby=message_id,
                aria_label="Task progress",
                **alpine.bind("aria-valuenow", alpine.expr("progress")),
                **alpine.bind("aria-valuetext", alpine.expr("progress + '% complete'")),
                class_="h-2.5 w-full rounded-full bg-muted",
            ),
            Element(
                "span",
                **{"x-text": "progress + '%'"},
                class_="text-sm font-semibold text-foreground",
            ),
            **alpine.show(alpine.expr("status !== 'failed'")),
            class_="mb-4 space-y-2 text-right",
        )

    @staticmethod
    def _error_state() -> Element:
        return Element(
            "div",
            Element(
                "p",
                "An error occurred",
                class_="mb-2 font-semibold text-destructive",
            ),
            Element(
                "p",
                **{"x-text": "error"},
                class_="text-sm text-destructive",
            ),
            Element(
                "button",
                "Retry connection",
                type="button",
                **alpine.on("click", alpine.expr("connect()")),
                class_=(
                    "mt-4 inline-flex items-center justify-center rounded-md "
                    "bg-destructive px-4 py-2 text-sm font-medium text-white "
                    "hover:bg-destructive/90 focus-visible:outline-none "
                    "focus-visible:ring-2 focus-visible:ring-ring "
                    "focus-visible:ring-offset-2"
                ),
            ),
            **alpine.show(alpine.expr("error !== null")),
            role="alert",
            class_=("rounded-lg border border-destructive/30 bg-destructive/10 p-4"),
        )

    def render(self) -> Element:
        root_props = dict(self.props)
        explicit_id = root_props.pop("id", root_props.pop("id_", None))
        custom_class = root_props.pop("class_", root_props.pop("class", ""))
        for name in (
            "x-data",
            "x_data",
            "x-init",
            "x_init",
            "role",
            "aria-modal",
            "aria_modal",
        ):
            root_props.pop(name, None)

        scope = get_render_scope().child("task-progress")
        identity_key = self.task_progress_key or (
            str(explicit_id) if explicit_id is not None else self.task_id
        )
        root_scope_id = scope.id("dialog", key=identity_key)
        root_id = str(explicit_id) if explicit_id is not None else root_scope_id
        title_id = scope.id("title", key=identity_key)
        message_id = scope.id("message", key=identity_key)
        controller_name = root_scope_id.replace("-", "_")
        root_class = " ".join(
            value
            for value in (
                (
                    "fixed inset-0 z-50 bg-muted/75 p-4 backdrop-blur-sm "
                    "dark:bg-background/75"
                ),
                custom_class,
            )
            if value
        )

        return Element(
            "div",
            Element(
                "div",
                Element(
                    "h2",
                    self.title,
                    id=title_id,
                    class_=("mb-6 text-center text-lg font-semibold text-foreground"),
                ),
                self._status_icons(),
                self._progress_bar(message_id),
                Element(
                    "p",
                    id=message_id,
                    **{"x-text": "message"},
                    role="status",
                    aria_live="polite",
                    class_="mb-4 text-center text-sm text-muted-foreground",
                ),
                self._error_state(),
                class_="w-full max-w-md rounded-xl bg-card p-8 shadow-lg",
            ),
            Element(
                "script",
                trusted_html(
                    self._controller_script(controller_name),
                    source="generated TaskProgress Alpine controller",
                ),
            ),
            id=root_id,
            role="dialog",
            aria_modal="true",
            aria_labelledby=title_id,
            tabindex="-1",
            **{"x-ref": "dialog", "x-cloak": True},
            **alpine.data(alpine.expr(controller_name)),
            **alpine.show(alpine.expr("visible")),
            **alpine.bind("aria-busy", alpine.expr("isActive")),
            class_=root_class,
            **root_props,
        )
