"""TaskProgress protocol, lifecycle, identity, and accessibility contracts."""

from __future__ import annotations

import re

import pytest

from oridecon.ui import Element, TaskProgress, TrustedHTML


class TestTaskProgressProtocol:
    def test_uses_the_backend_complete_status(self) -> None:
        output = str(TaskProgress("task-1"))

        assert "data.status === 'complete'" in output
        assert "status === 'complete'" in output
        assert "data.status === 'completed'" not in output
        assert "status === 'completed'" not in output

    def test_validates_and_clamps_progress_updates(self) -> None:
        output = str(TaskProgress("task-1"))

        assert "allowedStatuses.has(data.status)" in output
        assert "typeof data.progress !== 'number'" in output
        assert "Number.isFinite(data.progress)" in output
        assert "Math.min(100, Math.max(0, data.progress))" in output
        assert "JSON.parse(event.data)" in output
        assert "invalid update" in output

    def test_completion_is_forced_to_one_hundred_percent(self) -> None:
        output = str(TaskProgress("task-1"))

        assert "this.progress = 100" in output
        assert (
            "this.closeStream();\n                this.runCompletionAction();" in output
        )

    def test_auto_close_is_serialized_as_a_boolean(self) -> None:
        enabled = str(TaskProgress("task-1", auto_close=True))
        disabled = str(TaskProgress("task-2", auto_close=False))

        assert "const autoClose = true;" in enabled
        assert "const autoClose = false;" in disabled
        assert "window.setTimeout(() => this.close(), 700)" in enabled


class TestTaskProgressLifecycle:
    def test_alpine_automatic_init_creates_only_one_event_source(self) -> None:
        output = str(TaskProgress("task-1"))

        assert output.count("new EventSource(") == 1
        assert "init()" in output
        assert " x-init=" not in output

    def test_retry_reconnects_instead_of_reloading(self) -> None:
        output = str(TaskProgress("task-1"))

        assert 'x-on:click="connect()"' in output
        assert "window.location.reload" not in output

    def test_resources_are_closed_for_terminal_and_dom_cleanup_paths(self) -> None:
        output = str(TaskProgress("task-1"))

        assert "htmx:beforeCleanupElement" in output
        assert "removeEventListener(" in output
        assert "window.addEventListener('pagehide'" in output
        assert "window.removeEventListener('pagehide'" in output
        assert "if (source) source.close()" in output
        assert "MutationObserver" not in output

    def test_generated_controller_has_specific_provenance(self) -> None:
        root = TaskProgress("task-1").render()
        script = root.children[-1]

        assert isinstance(script, Element)
        assert script.tag == "script"
        assert isinstance(script.children[0], TrustedHTML)
        assert script.children[0].source == ("generated TaskProgress Alpine controller")

    def test_controller_registers_before_and_after_alpine_startup(self) -> None:
        output = str(TaskProgress("task-1"))

        assert "if (window.Alpine) register();" in output
        assert (
            "document.addEventListener('alpine:init', register, {once: true})" in output
        )


class TestTaskProgressIdentityAndAccessibility:
    def test_two_tasks_have_unique_linked_ids(self) -> None:
        output = str(Element("main", TaskProgress("first"), TaskProgress("second")))
        ids = re.findall(r' id="([^"]+)"', output)
        dialogs = re.findall(r'<div id="([^"]+)" role="dialog"', output)

        assert len(ids) == len(set(ids)) == 6
        assert len(dialogs) == 2
        for dialog_id in dialogs:
            assert dialog_id.startswith("oridecon-task-progress-dialog-")

    def test_duplicate_task_identity_fails_in_one_tree(self) -> None:
        page = Element("main", TaskProgress("same"), TaskProgress("same"))

        with pytest.raises(ValueError, match="Duplicate RenderScope ID"):
            str(page)

    def test_explicit_key_is_stable_across_partial_renders(self) -> None:
        first = str(TaskProgress("runtime-a", task_progress_key="operation"))
        second = str(TaskProgress("runtime-b", task_progress_key="operation"))

        root_pattern = r'<div id="(oridecon-task-progress-dialog-operation)"'
        assert re.search(root_pattern, first)
        assert re.search(root_pattern, second)

    def test_dialog_label_and_progress_relationships_are_linked(self) -> None:
        output = str(TaskProgress("task-1", title="Import records"))
        title = re.search(r'<h2 id="([^"]+)"', output)
        message = re.search(r'<p id="([^"]+)" x-text="message"', output)

        assert title is not None
        assert message is not None
        assert f'aria-labelledby="{title.group(1)}"' in output
        assert f'aria-describedby="{message.group(1)}"' in output
        assert 'role="progressbar"' in output
        assert 'aria-valuemin="0"' in output
        assert 'aria-valuemax="100"' in output
        assert 'x-bind:aria-valuenow="progress"' in output
        assert 'role="status" aria-live="polite"' in output
        assert 'role="alert"' in output

    def test_root_props_are_preserved_but_controller_wiring_is_protected(self) -> None:
        output = str(
            TaskProgress(
                "task-1",
                id="progress-dialog",
                class_="custom-progress",
                data_testid="progress",
                x_data="untrusted",
                x_init="duplicate()",
                role="region",
            )
        )

        assert 'id="progress-dialog"' in output
        assert "custom-progress" in output
        assert 'data-testid="progress"' in output
        assert 'x-data="untrusted"' not in output
        assert "duplicate()" not in output
        assert 'role="dialog"' in output
        assert " task-id=" not in output
