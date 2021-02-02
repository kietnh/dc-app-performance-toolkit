import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']
        project_key = datasets['custom_project_key']

    @print_timing("selenium_app_bulkmove_subtasks")
    def measure():

        @print_timing("selenium_app_bulkmove_subtasks:view_menu_item_move_all")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/browse/{issue_key}")
            page.wait_until_visible((By.ID, "summary-val"))  # Wait for summary field visible
            page.element_exists((By.ID,"move-all-subtasks-link")) # menu item
        sub_measure()

        @print_timing("selenium_app_bulkmove_subtasks:view_pave_bulk_move_subtasks")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/BulkMoveSubtasks.jspa?render=true&parentIssueId={issue_key}&projectKey={project_key}")
            page.element_exists((By.ID,"move-subtasks-submit")) # btn submit
        sub_measure()
    measure()
