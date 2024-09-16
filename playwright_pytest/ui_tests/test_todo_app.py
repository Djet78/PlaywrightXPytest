import allure

from playwright.sync_api import Page, expect
from playwright_pytest.playwright_pytest.ui_comp import PlaywrightSearch


@allure.suite('UI')
@allure.feature('Docs search')
@allure.label('owner', 'Viacheslav')
class TestSearch:
    @allure.title('Test Simple Search')
    @allure.description('Search for Playwright docs.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_simple_search(self, page: Page):
        page.goto('https://playwright.dev/python/docs/input')

        s_bar = PlaywrightSearch(page)
        s_bar.search_for('Playwright')

        expect(s_bar.search_field).to_have_value('Playwright')

    @allure.title('Test Fail Example')
    @allure.description('Search for Bad Value.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_fail_example(self, page: Page):
        page.goto('https://playwright.dev/python/docs/input')

        s_bar = PlaywrightSearch(page)
        s_bar.search_for('Playwright')
        expect(s_bar.search_field).to_have_value('Bad Value')

    @allure.title('Test Add 1 TODO action')
    @allure.description('Simply add 1 TODO item.')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_1_action(self, page: Page) -> None:
        page.goto('https://demo.playwright.dev/todomvc/')
        page.get_by_placeholder('What needs to be done?').click()
        page.get_by_placeholder('What needs to be done?').fill('action 1')
        page.get_by_placeholder('What needs to be done?').press('Enter')
        expect(page.get_by_test_id('todo-title')).to_contain_text('action 1')
