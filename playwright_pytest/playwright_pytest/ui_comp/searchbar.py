from playwright.sync_api import Page


class PlaywrightSearch:
    def __init__(self, driver: Page):
        self.driver = driver

    @property
    def header_btn_locator(self):
        return self.driver.get_by_role('button').get_by_text('Search')

    @property
    def search_field(self):
        return self.driver.get_by_placeholder('Search docs')

    def search_for(self, term: str):
        self.header_btn_locator.click()
        self.search_field.fill(term)
        self.driver.keyboard.press('Enter')
