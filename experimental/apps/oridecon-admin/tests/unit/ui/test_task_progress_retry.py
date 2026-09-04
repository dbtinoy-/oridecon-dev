from oridecon.ui import TaskProgress
from oridecon.ui.core.base import render_to_string


def test_task_progress_retry_reconnects_without_reloading_the_page() -> None:
    html = render_to_string(TaskProgress(task_id="t-123", title="Working…"))

    assert "Retry connection" in html
    assert 'x-on:click="connect()"' in html
    assert "window.location.reload" not in html
