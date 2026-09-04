from __future__ import annotations

import html as html_module

import pytest

from oridecon.ui.core.base import el
from oridecon.ui.molecules.tabs import TabPanel, Tabs


def _tabs(
    *,
    tabs_id: str = "account-tabs",
    active_tab: str = "profile",
) -> Tabs:
    return Tabs(
        [("Profile", "profile"), ("Security", "security")],
        active_tab=active_tab,
        tabs_id=tabs_id,
        children=[
            TabPanel("profile", "Profile panel"),
            TabPanel("security", "Security panel"),
        ],
    )


class TestTabsValidation:
    def test_stable_tabs_id_is_required(self) -> None:
        with pytest.raises(ValueError, match="stable tabs_id"):
            Tabs([("One", "one")])

    @pytest.mark.parametrize("tabs_id", ["1-tabs", "tabs id", "tabs<script>"])
    def test_tabs_id_must_be_valid_html_id(self, tabs_id: str) -> None:
        with pytest.raises(ValueError, match="valid HTML id"):
            Tabs([("One", "one")], tabs_id=tabs_id)

    def test_at_least_one_tab_is_required(self) -> None:
        with pytest.raises(ValueError, match="at least one"):
            Tabs([], tabs_id="empty-tabs")

    def test_tab_values_must_be_unique(self) -> None:
        with pytest.raises(ValueError, match="unique"):
            Tabs([("One", "same"), ("Two", "same")], tabs_id="duplicate-tabs")

    def test_active_tab_must_exist(self) -> None:
        with pytest.raises(ValueError, match="Unknown active_tab"):
            Tabs([("One", "one")], active_tab="missing", tabs_id="tabs")

    @pytest.mark.parametrize(
        "children",
        [
            [TabPanel("profile", "Profile")],
            [
                TabPanel("profile", "Profile"),
                TabPanel("security", "Security"),
                TabPanel("other", "Other"),
            ],
        ],
    )
    def test_panels_must_correspond_exactly(self, children: list[TabPanel]) -> None:
        tabs = Tabs(
            [("Profile", "profile"), ("Security", "security")],
            tabs_id="account-tabs",
            children=children,
        )

        with pytest.raises(ValueError, match="correspond exactly"):
            str(tabs)

    def test_duplicate_panels_fail(self) -> None:
        tabs = Tabs(
            [("Profile", "profile")],
            tabs_id="account-tabs",
            children=[TabPanel("profile"), TabPanel("profile")],
        )

        with pytest.raises(ValueError, match="Duplicate TabPanel"):
            str(tabs)

    def test_non_panel_child_fails(self) -> None:
        tabs = Tabs(
            [("Profile", "profile")],
            tabs_id="account-tabs",
            children=[el("div", "not a panel")],
        )

        with pytest.raises(TypeError, match="must all be TabPanel"):
            str(tabs)

    def test_panel_cannot_render_without_parent_identity(self) -> None:
        with pytest.raises(ValueError, match="child of Tabs"):
            str(TabPanel("profile", "Profile"))


class TestTabsSemantics:
    def test_ids_and_relationships_are_instance_scoped(self) -> None:
        rendered = str(_tabs())

        assert 'id="account-tabs"' in rendered
        assert 'id="account-tabs-select"' in rendered
        assert 'id="account-tabs-tab-0"' in rendered
        assert 'aria-controls="account-tabs-panel-0"' in rendered
        assert 'id="account-tabs-panel-0"' in rendered
        assert 'aria-labelledby="account-tabs-tab-0"' in rendered
        assert 'for="account-tabs-select"' in rendered

    def test_two_instances_do_not_share_ids(self) -> None:
        first = str(_tabs(tabs_id="profile-tabs"))
        second = str(_tabs(tabs_id="team-tabs"))

        assert "team-tabs" not in first
        assert "profile-tabs" not in second

    def test_roving_tabindex_and_selected_state_start_correctly(self) -> None:
        rendered = str(_tabs(active_tab="security"))

        assert (
            'id="account-tabs-tab-0" role="tab" tabindex="-1" '
            'aria-selected="false"' in rendered
        )
        assert (
            'id="account-tabs-tab-1" role="tab" tabindex="0" '
            'aria-selected="true"' in rendered
        )
        assert "x-bind:aria-selected" in rendered
        assert "x-bind:tabindex" in rendered

    @pytest.mark.parametrize("key", ["right", "left", "home", "end"])
    def test_keyboard_handler_moves_focus_and_activates(self, key: str) -> None:
        rendered = str(_tabs())

        assert f"x-on:keydown.{key}.prevent=" in rendered
        assert "target.focus(); target.click();" in html_module.unescape(rendered)

    def test_panels_are_bound_to_hidden_and_aria_state(self) -> None:
        rendered = str(_tabs())

        assert 'x-bind:hidden="activeTab !== &quot;profile&quot;"' in rendered
        assert "x-bind:aria-hidden" in rendered
        assert " hidden=" not in rendered
        assert "x-cloak" not in rendered

    def test_mobile_selector_has_an_accessible_label(self) -> None:
        rendered = str(_tabs())

        assert (
            '<label for="account-tabs-select" class="sr-only">Select a tab</label>'
            in rendered
        )
        assert 'x-model="activeTab"' in rendered

    def test_values_are_json_encoded_in_alpine_expressions(self) -> None:
        value = "profile'; window.compromised = true; //"
        tabs = Tabs(
            [("Unsafe-looking value", value)],
            tabs_id="safe-tabs",
            children=[TabPanel(value, "Panel")],
        )

        rendered = html_module.unescape(str(tabs))

        assert f'activeTab: "{value}"' in rendered
        assert f'activeTab = "{value}"' in rendered
        assert f"activeTab = '{value}'" not in rendered


class TestUrlTabs:
    def test_url_mode_uses_links_without_alpine_state(self) -> None:
        tabs = Tabs(
            [("Users", "/admin/users?status=active"), ("Docs", "https://example.test")],
            active_tab="/admin/users?status=active",
            client_side=False,
            tabs_id="resource-tabs",
        )

        rendered = str(tabs)

        assert 'href="/admin/users?status=active"' in rendered
        assert 'href="https://example.test"' in rendered
        assert 'aria-current="page"' in rendered
        assert "x-data" not in rendered
        assert "x-on:change" not in rendered
        assert rendered.count('href="/admin/users?status=active"') == 2
