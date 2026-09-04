"""Accessible global command palette."""

from __future__ import annotations

from typing import Any

from oridecon.ui import (
    Component,
    Element,
    get_icon,
    get_render_scope,
    js_json,
    js_string,
    trusted_html,
)
from oridecon.ui.atoms.icons import ICONS
from oridecon.ui.attributes.alpine import alpine


class CommandPalette(Component):
    """Render permission-aware command search and keyboard navigation."""

    def __init__(
        self,
        commands: list[dict[str, str]] | None = None,
        admin_prefix: str = "/admin",
        command_palette_key: str | None = None,
        **props: Any,
    ) -> None:
        super().__init__(**props)
        self.admin_prefix = admin_prefix.rstrip("/") or "/admin"
        # Defaults must be safe without a request-bound permission decision.
        self.commands = (
            [
                {
                    "label": "Go to Dashboard",
                    "href": f"{self.admin_prefix}/",
                    "icon": "home",
                    "shortcut": "G D",
                },
                {
                    "label": "Toggle Dark Mode",
                    "action": "darkMode = !darkMode",
                    "icon": "moon",
                    "shortcut": "T D",
                },
            ]
            if commands is None
            else commands
        )
        self.command_palette_key = command_palette_key

    def _safe_icon_markup(self) -> dict[str, str]:
        names = {"home", "moon", "search", "settings", "users"}
        names.update(command.get("icon", "") for command in self.commands)
        return {
            name: str(
                get_icon(
                    name,
                    class_name=(
                        "w-6 h-6 text-muted-foreground group-hover:text-foreground "
                        "transition-colors"
                    ),
                )
            )
            for name in sorted(names)
            if name in ICONS
        }

    def _controller_script(
        self,
        *,
        controller_name: str,
        command_palette_url: str,
        option_id_prefix: str,
    ) -> str:
        return f"""
(() => {{
    const controllerName = {js_string(controller_name)};
    const initialCommands = {js_json(self.commands)};
    const iconMarkup = {js_json(self._safe_icon_markup())};
    const endpoint = {js_string(command_palette_url)};

    const controller = () => ({{
        open: false,
        search: '',
        selectedIndex: 0,
        searchTimeout: null,
        requestController: null,
        previousFocus: null,
        loading: false,
        error: '',
        icons: iconMarkup,
        commands: [],
        staticCommands: [],
        get filteredCommands() {{ return this.commands; }},
        get activeOptionId() {{
            return this.filteredCommands.length
                ? {js_string(option_id_prefix)} + this.selectedIndex
                : '';
        }},
        normalizeCommands(value) {{
            if (!Array.isArray(value)) return [];
            return value
                .filter(command => command && typeof command.label === 'string')
                .map((command, index) => ({{
                    ...command,
                    icon_html: this.icons[command.icon] || '',
                    _key: [command.href || '', command.action || '', command.label, index].join(':')
                }}));
        }},
        init() {{
            this.staticCommands = this.normalizeCommands(initialCommands);
            this.commands = this.staticCommands;
            this.$watch('search', value => {{
                window.clearTimeout(this.searchTimeout);
                this.selectedIndex = 0;
                this.searchTimeout = window.setTimeout(() => this.fetchResults(value), 200);
            }});
        }},
        destroy() {{
            window.clearTimeout(this.searchTimeout);
            this.requestController?.abort();
        }},
        async fetchResults(query) {{
            const normalizedQuery = query.trim();
            this.requestController?.abort();
            if (normalizedQuery.length < 2) {{
                this.commands = this.staticCommands;
                this.loading = false;
                this.error = '';
                return;
            }}

            const request = new AbortController();
            this.requestController = request;
            this.loading = true;
            this.error = '';
            try {{
                const url = new URL(endpoint, window.location.href);
                url.searchParams.set('q', normalizedQuery);
                const response = await fetch(url, {{
                    headers: {{'X-Requested-With': 'fetch'}},
                    signal: request.signal
                }});
                if (!response.ok) throw new Error(`HTTP ${{response.status}}`);
                const data = await response.json();
                if (this.requestController === request) {{
                    this.commands = this.normalizeCommands(data);
                    this.selectedIndex = 0;
                }}
            }} catch (error) {{
                if (error.name !== 'AbortError' && this.requestController === request) {{
                    this.commands = [];
                    this.error = 'Commands could not be loaded.';
                }}
            }} finally {{
                if (this.requestController === request) {{
                    this.loading = false;
                    this.requestController = null;
                }}
            }}
        }},
        openPalette() {{
            if (this.open) return;
            this.previousFocus = document.activeElement;
            this.open = true;
            this.search = '';
            this.commands = this.staticCommands;
            this.selectedIndex = 0;
            this.$nextTick(() => this.$refs.search.focus());
        }},
        toggle() {{ this.open ? this.close() : this.openPalette(); }},
        close() {{
            if (!this.open) return;
            this.open = false;
            this.$nextTick(() => this.previousFocus?.focus());
        }},
        next() {{
            if (!this.filteredCommands.length) return;
            this.selectedIndex = (this.selectedIndex + 1) % this.filteredCommands.length;
        }},
        prev() {{
            if (!this.filteredCommands.length) return;
            this.selectedIndex = (
                this.selectedIndex - 1 + this.filteredCommands.length
            ) % this.filteredCommands.length;
        }},
        safeNavigationUrl(href) {{
            try {{
                const url = new URL(href, window.location.href);
                return url.origin === window.location.origin &&
                    ['http:', 'https:'].includes(url.protocol) ? url : null;
            }} catch (_error) {{
                return null;
            }}
        }},
        execute(requestedIndex = null) {{
            const index = requestedIndex === null ? this.selectedIndex : requestedIndex;
            const command = this.filteredCommands[index];
            if (!command) return;

            if (command.href) {{
                const url = this.safeNavigationUrl(command.href);
                if (!url) {{
                    this.error = 'That command points to an unsafe destination.';
                    return;
                }}
                const destination = url.href;
                this.close();
                // Single navigation owner: the shell navigator handles the
                // swap target, title, scroll/focus lifecycle, auth expiry
                // and history entries. Fall back to a direct assignment in
                // environments where the admin shell script is absent.
                if (window.OrideconNavigator) {{
                    window.OrideconNavigator.navigate(destination);
                }} else if (window.htmx) {{
                    window.htmx.ajax('GET', destination, {{
                        target: '#main-content', swap: 'innerHTML',
                        headers: {{ 'HX-Target': '#main-content' }}
                    }});
                }} else {{
                    window.location.assign(destination);
                }}
                return;
            }}

            if (command.action === 'darkMode = !darkMode') {{
                const shell = document.querySelector('[x-data*="darkMode"]');
                if (shell) {{
                    const data = window.Alpine.$data(shell);
                    data.darkMode = !data.darkMode;
                }}
                this.close();
            }}
        }}
    }});

    const register = () => window.Alpine.data(controllerName, controller);
    if (window.Alpine) register();
    else document.addEventListener('alpine:init', register, {{ once: true }});
}})();
"""

    @staticmethod
    def _transitions(prefix: str) -> dict[str, str]:
        if prefix == "backdrop":
            return {
                **alpine.transition(
                    "enter", alpine.expr("transition-opacity ease-out duration-300")
                ),
                **alpine.transition("enter-start", alpine.expr("opacity-0")),
                **alpine.transition("enter-end", alpine.expr("opacity-100")),
                **alpine.transition(
                    "leave", alpine.expr("transition-opacity ease-in duration-200")
                ),
                **alpine.transition("leave-start", alpine.expr("opacity-100")),
                **alpine.transition("leave-end", alpine.expr("opacity-0")),
            }
        return {
            **alpine.transition(
                "enter", alpine.expr("transition-all ease-out duration-300")
            ),
            **alpine.transition("enter-start", alpine.expr("opacity-0 scale-95")),
            **alpine.transition("enter-end", alpine.expr("opacity-100 scale-100")),
            **alpine.transition(
                "leave", alpine.expr("transition-all ease-in duration-200")
            ),
            **alpine.transition("leave-start", alpine.expr("opacity-100 scale-100")),
            **alpine.transition("leave-end", alpine.expr("opacity-0 scale-95")),
        }

    def _search_input(self, options_id: str) -> Element:
        return Element(
            "div",
            Element(
                "div",
                get_icon("search", class_name="h-5 w-5 text-muted-foreground"),
                class_="pointer-events-none absolute left-4 top-3.5 h-5 w-5",
            ),
            Element(
                "input",
                type="search",
                placeholder="Search commands or navigation…",
                role="combobox",
                aria_expanded="true",
                aria_controls=options_id,
                aria_autocomplete="list",
                aria_label="Search commands and navigation",
                **{"x-ref": "search"},
                **alpine.model(alpine.expr("search")),
                **alpine.bind("aria-expanded", alpine.expr("open")),
                **alpine.bind("aria-activedescendant", alpine.expr("activeOptionId")),
                **alpine.on("keydown", alpine.expr("next()"), "down", "prevent"),
                **alpine.on("keydown", alpine.expr("prev()"), "up", "prevent"),
                **alpine.on("keydown", alpine.expr("execute()"), "enter", "prevent"),
                class_=(
                    "h-12 w-full border-0 bg-transparent pl-11 pr-4 text-foreground "
                    "placeholder:text-muted-foreground focus:ring-0 sm:text-sm"
                ),
            ),
            class_="relative",
        )

    def _results(self, options_id: str, option_id_prefix: str) -> Element:
        return Element(
            "div",
            Element(
                "p",
                "Loading commands…",
                **alpine.show(alpine.expr("loading")),
                class_="p-10 text-center text-sm text-muted-foreground",
                role="status",
            ),
            Element(
                "div",
                Element("p", **{"x-text": "error"}),
                Element(
                    "button",
                    "Retry",
                    type="button",
                    **alpine.on("click", alpine.expr("fetchResults(search)")),
                    class_=(
                        "mt-2 text-xs font-medium text-primary-600 hover:underline "
                        "focus:outline-none focus:ring-2 focus:ring-primary-500"
                    ),
                ),
                **alpine.show(alpine.expr("!loading && Boolean(error)")),
                class_="p-8 text-center text-sm text-destructive",
                role="alert",
            ),
            Element(
                "ul",
                Element(
                    "template",
                    Element(
                        "li",
                        Element(
                            "span",
                            **{"x-html": "command.icon_html"},
                            class_=(
                                "flex h-10 w-10 flex-none items-center justify-center "
                                "rounded-lg"
                            ),
                            **alpine.bind(
                                "class",
                                alpine.expr(
                                    "selectedIndex === index ? 'bg-primary-500' : "
                                    "'bg-muted dark:bg-card'"
                                ),
                            ),
                        ),
                        Element(
                            "span",
                            Element(
                                "span",
                                **{"x-text": "command.label"},
                                class_="block font-semibold",
                            ),
                            Element(
                                "span",
                                **{"x-text": "command.subtitle || ''"},
                                **alpine.show(alpine.expr("Boolean(command.subtitle)")),
                                class_="block text-xs opacity-75",
                            ),
                            class_="ml-4 flex-auto",
                        ),
                        Element(
                            "span",
                            **{"x-text": "command.shortcut"},
                            **alpine.show(alpine.expr("Boolean(command.shortcut)")),
                            **alpine.bind(
                                "class",
                                alpine.expr(
                                    "selectedIndex === index ? 'text-primary-100' : "
                                    "'text-muted-foreground'"
                                ),
                            ),
                            class_="ml-3 flex-none text-xs font-semibold",
                        ),
                        role="option",
                        tabindex="-1",
                        aria_selected="false",
                        **alpine.bind(
                            "id",
                            alpine.expr(f"{js_string(option_id_prefix)} + index"),
                        ),
                        **alpine.bind(
                            "aria-selected",
                            alpine.expr("selectedIndex === index"),
                        ),
                        **alpine.bind(
                            "class",
                            alpine.expr(
                                "selectedIndex === index ? 'bg-primary-600 text-white' : "
                                "'text-foreground hover:bg-muted dark:hover:bg-card'"
                            ),
                        ),
                        **alpine.on("click", alpine.expr("execute(index)")),
                        **alpine.on("mouseenter", alpine.expr("selectedIndex = index")),
                        class_=(
                            "group flex cursor-pointer select-none items-center "
                            "rounded-xl p-3 focus:outline-none"
                        ),
                    ),
                    **{"x-for": "(command, index) in filteredCommands"},
                    **alpine.bind("key", alpine.expr("command._key")),
                ),
                id=options_id,
                role="listbox",
                aria_label="Commands",
                **alpine.show(alpine.expr("!loading && !error")),
                class_="max-h-96 scroll-py-3 overflow-y-auto p-3",
            ),
            Element(
                "p",
                "No results found for that search.",
                **alpine.show(
                    alpine.expr(
                        "!loading && !error && search !== '' && "
                        "filteredCommands.length === 0"
                    )
                ),
                class_="p-10 text-center text-sm text-muted-foreground",
            ),
        )

    @staticmethod
    def _help_footer() -> Element:
        return Element(
            "div",
            Element(
                "span",
                Element(
                    "kbd",
                    "esc",
                    class_=(
                        "rounded-md border border-border px-1.5 py-0.5 "
                        "text-xs font-semibold text-muted-foreground"
                    ),
                ),
                " to close",
                class_="text-xs text-muted-foreground",
            ),
            Element(
                "span",
                Element(
                    "kbd",
                    "enter",
                    class_=(
                        "rounded-md border border-border px-1.5 py-0.5 "
                        "text-xs font-semibold text-muted-foreground"
                    ),
                ),
                " to select",
                class_="ml-4 text-xs text-muted-foreground",
            ),
            class_="flex flex-none items-center justify-end bg-muted px-4 py-2.5",
        )

    def render(self) -> Element:
        root_props = dict(self.props)
        explicit_id = root_props.pop("id", root_props.pop("id_", None))
        custom_class = root_props.pop("class_", root_props.pop("class", ""))
        for protected_name in (
            "x-data",
            "x_data",
            "role",
            "aria-modal",
            "aria_modal",
        ):
            root_props.pop(protected_name, None)

        scope = get_render_scope().child("command-palette")
        identity_key = self.command_palette_key or (
            str(explicit_id) if explicit_id is not None else None
        )
        root_scope_id = scope.id("dialog", key=identity_key)
        options_id = scope.id("options", key=root_scope_id)
        option_id_prefix = f"{scope.id('option', key=root_scope_id)}-"
        controller_name = root_scope_id.replace("-", "_")
        command_palette_url = f"{self.admin_prefix}/command-palette"
        root_class = " ".join(
            value
            for value in (
                "fixed inset-0 z-50 overflow-y-auto p-4 sm:p-6 md:p-20",
                custom_class,
            )
            if value
        )

        return Element(
            "div",
            Element(
                "div",
                **alpine.show(alpine.expr("open")),
                **self._transitions("backdrop"),
                **alpine.on("click", alpine.expr("close()")),
                class_=(
                    "fixed inset-0 bg-muted/60 backdrop-blur-sm transition-opacity"
                ),
                aria_hidden=True,
            ),
            Element(
                "div",
                self._search_input(options_id),
                self._results(options_id, option_id_prefix),
                self._help_footer(),
                **alpine.show(alpine.expr("open")),
                **self._transitions("panel"),
                class_=(
                    "mx-auto max-w-2xl transform divide-y divide-border "
                    "overflow-hidden rounded-2xl bg-background shadow-2xl "
                    "ring-1 ring-border transition-all"
                ),
            ),
            Element(
                "script",
                trusted_html(
                    self._controller_script(
                        controller_name=controller_name,
                        command_palette_url=command_palette_url,
                        option_id_prefix=option_id_prefix,
                    ),
                    source="generated CommandPalette Alpine controller",
                ),
            ),
            id=explicit_id or root_scope_id,
            role="dialog",
            aria_modal="true",
            aria_label="Command palette",
            **{"x-cloak": True, "x-trap.noscroll": "open"},
            **alpine.data(alpine.expr(controller_name)),
            **alpine.show(alpine.expr("open")),
            **alpine.on("open-command-palette", alpine.expr("openPalette()"), "window"),
            **alpine.on(
                "keydown", alpine.expr("toggle()"), "window", "cmd", "k", "prevent"
            ),
            **alpine.on(
                "keydown", alpine.expr("toggle()"), "window", "ctrl", "k", "prevent"
            ),
            **alpine.on(
                "keydown", alpine.expr("close()"), "window", "escape", "prevent"
            ),
            class_=root_class,
            **root_props,
        )
