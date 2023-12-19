from playwright.sync_api import Page, expect
from playwright_pytest.playwright_pytest.ui_comp import PlaywrightSearch


def test_simple_search(page: Page):
    page.goto('https://playwright.dev/python/docs/input')

    s_bar = PlaywrightSearch(page)
    s_bar.search_for('Playwright')

    expect(s_bar.search_field).to_have_value('Playwright')
