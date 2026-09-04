"""Real-time, persisted notification menu."""

from __future__ import annotations

from typing import Any

from oridecon.ui.atoms.icons import get_icon
from oridecon.ui.attributes.alpine import alpine
from oridecon.ui.core.base import Component, Element
from oridecon.ui.core.js import js_string
from oridecon.ui.core.render_context import get_render_scope
from oridecon.ui.core.trusted_html import trusted_html


class NotificationBell(Component):
    """Render an accessible notification menu backed by SSE and inbox APIs.

    ``notification_key`` provides stable full/partial-render identity. Each
    instance registers a scoped Alpine controller, avoiding global controller
    collisions while still supporting HTMX insertion after Alpine has started.
    """

    def __init__(
        self,
        sse_url: str = "/admin/_sse/widgets",
        inbox_url: str | None = None,
        inbox_api_url: str = "/admin/notifications/inbox",
        mark_read_url: str = "/admin/notifications/read/{message_id}",
        mark_all_read_url: str = "/admin/notifications/read-all",
        csrf_token: str | None = None,
        max_display: int = 10,
        notification_key: str | None = None,
        **props: Any,
    ) -> None:
        super().__init__(**props)
        self.sse_url = sse_url
        self.inbox_url = inbox_url
        self.inbox_api_url = inbox_api_url
        self.mark_read_url = mark_read_url
        self.mark_all_read_url = mark_all_read_url
        self.csrf_token = csrf_token or ""
        self.max_display = max(1, int(max_display))
        self.notification_key = notification_key

    def _controller_script(self, controller_name: str) -> str:
        return f"""
(() => {{
    const controllerName = {js_string(controller_name)};
    const controller = () => ({{
        open: false,
        loading: true,
        loadError: '',
        mutationError: '',
        unreadCount: 0,
        notifications: [],
        eventSource: null,
        toggle() {{ this.open = !this.open; }},
        close() {{ this.open = false; }},
        parseEvent(event) {{
            try {{ return JSON.parse(event.data); }}
            catch (_error) {{ return null; }}
        }},
        init() {{
            this.loadInbox();
            if (this.eventSource) return;
            this.eventSource = new EventSource({js_string(self.sse_url)});
            const handleNotification = (event) => {{
                const envelope = this.parseEvent(event);
                if (!envelope) return;
                if (envelope.event && envelope.event !== 'notification') return;
                const data = envelope.data || envelope;
                this.notifications.unshift({{
                    id: envelope.id || data.id || Date.now() + Math.random(),
                    title: data.title || 'Notification',
                    message: data.message || '',
                    level: data.level || 'info',
                    read: false,
                    time: data.timestamp
                }});
                this.unreadCount += 1;
                if (this.notifications.length > {self.max_display}) {{
                    this.notifications.pop();
                }}
            }};
            this.eventSource.addEventListener('message', handleNotification);
            this.eventSource.addEventListener('notification', handleNotification);
            this.eventSource.addEventListener('toast', (event) => {{
                const data = this.parseEvent(event);
                if (data && typeof window.showToast === 'function') {{
                    window.showToast(data.message || data.title, data.variant || 'success');
                }}
            }});
            this.eventSource.addEventListener('error', () => {{}});
        }},
        async loadInbox() {{
            this.loading = true;
            this.loadError = '';
            try {{
                const response = await fetch({js_string(self.inbox_api_url)}, {{
                    headers: {{'X-Requested-With': 'fetch'}}
                }});
                if (!response.ok) throw new Error(`HTTP ${{response.status}}`);
                const data = await response.json();
                this.notifications = (data.notifications || []).map(notification => ({{
                    id: notification.id,
                    title: notification.title || 'Notification',
                    message: notification.message || '',
                    level: notification.level || 'info',
                    read: notification.read === true,
                    time: notification.timestamp
                }})).slice(0, {self.max_display});
                this.unreadCount = data.unread_count || 0;
            }} catch (_error) {{
                this.loadError = 'Notifications could not be loaded.';
            }} finally {{
                this.loading = false;
            }}
        }},
        destroy() {{
            if (this.eventSource) {{
                this.eventSource.close();
                this.eventSource = null;
            }}
        }},
        async markAsRead(id) {{
            const notification = this.notifications.find(item => item.id === id);
            const wasUnread = Boolean(notification && !notification.read);
            if (wasUnread) {{
                notification.read = true;
                this.unreadCount = Math.max(0, this.unreadCount - 1);
            }}
            this.mutationError = '';
            try {{
                const url = {js_string(self.mark_read_url)}.replace(
                    '{{message_id}}', encodeURIComponent(String(id))
                );
                const response = await fetch(url, {{
                    method: 'POST',
                    headers: {{
                        'X-Requested-With': 'fetch',
                        'X-CSRF-Token': this.$el.dataset.csrfToken || ''
                    }}
                }});
                if (!response.ok) throw new Error(`HTTP ${{response.status}}`);
            }} catch (_error) {{
                if (wasUnread) {{
                    notification.read = false;
                    this.unreadCount += 1;
                }}
                this.mutationError = 'The notification could not be marked as read.';
            }}
        }},
        async markAllRead() {{
            const previous = this.notifications.map(item => item.read);
            const previousUnreadCount = this.unreadCount;
            this.notifications.forEach(item => {{ item.read = true; }});
            this.unreadCount = 0;
            this.mutationError = '';
            try {{
                const response = await fetch({js_string(self.mark_all_read_url)}, {{
                    method: 'POST',
                    headers: {{
                        'X-Requested-With': 'fetch',
                        'X-CSRF-Token': this.$el.dataset.csrfToken || ''
                    }}
                }});
                if (!response.ok) throw new Error(`HTTP ${{response.status}}`);
            }} catch (_error) {{
                this.notifications.forEach((item, index) => {{
                    item.read = previous[index] ?? item.read;
                }});
                this.unreadCount = previousUnreadCount;
                this.mutationError = 'Notifications could not be marked as read.';
            }}
        }}
    }});

    const register = () => window.Alpine.data(controllerName, controller);
    if (window.Alpine) register();
    else document.addEventListener('alpine:init', register, {{ once: true }});
}})();
"""

    def _render_trigger(self, trigger_id: str, panel_id: str) -> Element:
        return Element(
            "button",
            get_icon("bell", class_name="w-5 h-5"),
            Element(
                "span",
                **alpine.show(alpine.expr("unreadCount > 0")),
                **{"x-text": "unreadCount > 99 ? '99+' : unreadCount"},
                class_=(
                    "absolute -top-0.5 -right-0.5 inline-flex items-center "
                    "justify-center px-1.5 py-0.5 text-[10px] font-bold leading-none "
                    "text-white bg-destructive rounded-full min-w-[16px]"
                ),
                aria_hidden=True,
            ),
            Element(
                "span",
                **{"x-text": "`${unreadCount} unread notifications`"},
                class_="sr-only",
                aria_live="polite",
            ),
            id=trigger_id,
            type="button",
            aria_label="Notifications",
            aria_haspopup="dialog",
            aria_controls=panel_id,
            aria_expanded="false",
            **{"x-ref": "trigger"},
            **alpine.on("click", alpine.expr("toggle()")),
            **alpine.on(
                "keydown",
                alpine.expr("open = false"),
                "escape",
                "prevent",
            ),
            **alpine.bind("aria-expanded", alpine.expr("open")),
            **alpine.bind(
                "aria-label",
                alpine.expr(
                    "unreadCount ? `Notifications, ${unreadCount} unread` : "
                    "'Notifications'"
                ),
            ),
            class_=(
                "relative p-2 rounded-lg hover:bg-muted dark:hover:bg-card "
                "transition-colors focus:outline-none focus:ring-2 focus:ring-primary-500"
            ),
        )

    def _render_notification_list(self) -> Element:
        return Element(
            "div",
            Element(
                "p",
                "Loading notifications…",
                **alpine.show(alpine.expr("loading")),
                class_="px-4 py-8 text-center text-sm text-muted-foreground",
                role="status",
            ),
            Element(
                "div",
                Element("p", **{"x-text": "loadError"}),
                Element(
                    "button",
                    "Retry",
                    type="button",
                    **alpine.on("click", alpine.expr("loadInbox()")),
                    class_=(
                        "mt-2 text-xs font-medium text-primary-600 hover:underline "
                        "focus:outline-none focus:ring-2 focus:ring-primary-500"
                    ),
                ),
                **alpine.show(alpine.expr("!loading && Boolean(loadError)")),
                class_="px-4 py-6 text-center text-sm text-destructive",
                role="alert",
            ),
            Element(
                "ul",
                Element(
                    "template",
                    Element(
                        "li",
                        Element(
                            "button",
                            Element(
                                "span",
                                **alpine.bind(
                                    "class",
                                    alpine.expr(
                                        "{'bg-info': notification.level === 'info', "
                                        "'bg-warning': notification.level === 'warning', "
                                        "'bg-destructive': notification.level === 'error', "
                                        "'bg-success': notification.level === 'success'}"
                                    ),
                                ),
                                class_="mt-1.5 w-2 h-2 rounded-full flex-shrink-0",
                                aria_hidden=True,
                            ),
                            Element(
                                "span",
                                Element(
                                    "span",
                                    **{"x-text": "notification.title"},
                                    class_="block text-sm font-medium text-foreground",
                                ),
                                Element(
                                    "span",
                                    **{"x-text": "notification.message"},
                                    class_=(
                                        "block text-xs text-muted-foreground mt-0.5 "
                                        "line-clamp-2"
                                    ),
                                ),
                                class_="flex-1 min-w-0 text-left",
                            ),
                            type="button",
                            **alpine.on(
                                "click",
                                alpine.expr("markAsRead(notification.id)"),
                            ),
                            **alpine.bind(
                                "class",
                                alpine.expr("notification.read ? 'opacity-60' : ''"),
                            ),
                            class_=(
                                "flex w-full items-start gap-3 px-4 py-3 "
                                "hover:bg-muted cursor-pointer transition-colors "
                                "focus:outline-none focus:bg-muted"
                            ),
                        ),
                    ),
                    **{"x-for": "notification in notifications"},
                    **alpine.bind("key", alpine.expr("notification.id")),
                ),
                **alpine.show(alpine.expr("!loading && !loadError")),
                class_="max-h-64 overflow-y-auto",
                aria_label="Recent notifications",
            ),
            Element(
                "p",
                "No new notifications",
                **alpine.show(
                    alpine.expr("!loading && !loadError && notifications.length === 0")
                ),
                class_="px-4 py-8 text-center text-sm text-muted-foreground",
            ),
        )

    def _render_panel(self, panel_id: str, title_id: str) -> Element:
        footer = (
            Element(
                "div",
                Element(
                    "a",
                    "View all notifications",
                    href=self.inbox_url,
                    class_=(
                        "block w-full text-center px-4 py-2 text-xs text-primary-600 "
                        "dark:text-primary-400 hover:bg-muted rounded-b-xl transition-colors"
                    ),
                ),
            )
            if self.inbox_url
            else None
        )
        return Element(
            "div",
            Element(
                "div",
                Element(
                    "h3",
                    "Notifications",
                    id=title_id,
                    class_="text-sm font-semibold text-foreground",
                ),
                Element(
                    "button",
                    "Mark all read",
                    type="button",
                    **alpine.on("click", alpine.expr("markAllRead()")),
                    **alpine.show(alpine.expr("unreadCount > 0")),
                    class_=(
                        "text-xs text-primary-600 dark:text-primary-400 "
                        "hover:underline focus:outline-none focus:ring-2 focus:ring-primary-500"
                    ),
                ),
                class_="flex items-center justify-between px-4 py-3",
            ),
            Element(
                "p",
                **{"x-text": "mutationError"},
                **alpine.show(alpine.expr("Boolean(mutationError)")),
                class_="px-4 py-2 text-xs text-destructive",
                role="alert",
            ),
            self._render_notification_list(),
            footer,
            id=panel_id,
            role="dialog",
            aria_labelledby=title_id,
            **{"x-cloak": True},
            **alpine.show(alpine.expr("open")),
            **alpine.on("click", alpine.expr("close()"), "outside"),
            **alpine.transition(
                "enter", alpine.expr("transition ease-out duration-200")
            ),
            **alpine.transition("enter-start", alpine.expr("opacity-0 translate-y-1")),
            **alpine.transition("enter-end", alpine.expr("opacity-100 translate-y-0")),
            **alpine.transition(
                "leave", alpine.expr("transition ease-in duration-150")
            ),
            **alpine.transition(
                "leave-start", alpine.expr("opacity-100 translate-y-0")
            ),
            **alpine.transition("leave-end", alpine.expr("opacity-0 translate-y-1")),
            class_=(
                "absolute right-0 mt-2 w-80 rounded-xl shadow-lg bg-card ring-1 "
                "ring-border divide-y divide-border z-50"
            ),
        )

    def render(self) -> Element:
        root_props = dict(self.props)
        explicit_id = root_props.pop("id", root_props.pop("id_", None))
        custom_class = root_props.pop("class_", root_props.pop("class", ""))
        for protected_name in (
            "x-data",
            "x_data",
            "x-init",
            "x_init",
            "data-csrf-token",
            "data_csrf_token",
        ):
            root_props.pop(protected_name, None)

        scope = get_render_scope().child("notification-bell")
        identity_key = self.notification_key or (
            str(explicit_id) if explicit_id is not None else None
        )
        root_scope_id = scope.id("root", key=identity_key)
        trigger_id = scope.id("trigger", key=root_scope_id)
        panel_id = scope.id("panel", key=root_scope_id)
        title_id = scope.id("title", key=root_scope_id)
        controller_name = root_scope_id.replace("-", "_")
        root_class = " ".join(value for value in ("relative", custom_class) if value)

        return Element(
            "div",
            self._render_trigger(trigger_id, panel_id),
            self._render_panel(panel_id, title_id),
            Element(
                "script",
                trusted_html(
                    self._controller_script(controller_name),
                    source="generated NotificationBell Alpine controller",
                ),
            ),
            id=explicit_id or root_scope_id,
            **alpine.data(alpine.expr(controller_name)),
            **{"x-init": "init()"},
            **alpine.on("beforeunload", alpine.expr("destroy()"), "window"),
            **alpine.on(
                "keydown",
                alpine.expr("if (open) { open = false; $refs.trigger.focus() }"),
                "escape",
                "window",
            ),
            data_inbox_url=self.inbox_url or "",
            data_inbox_api_url=self.inbox_api_url,
            data_sse_url=self.sse_url,
            data_csrf_token=self.csrf_token,
            class_=root_class,
            **root_props,
        )
